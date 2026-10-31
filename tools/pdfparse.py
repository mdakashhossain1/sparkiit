import re

CONNECT = (' and', ' of', ' using', ' in', ' to', ' for', ' &', ',', '-', ' with', ' the', ' a', ' w.r.t.', ' on', ' or', ' vs', ' between')
HDR = ('topic', 'tropic', 'topics', 'curriculum', 'subtopics', 'sub topics', 'subtropic', 'sub tropic', 's. no.', 's.no', 'sl.no', 'sl. no', 'sno', 'duration', 'date', 'date & time', 'date and time', 'subtopic')
BUL = re.compile('^\\s*(?:[●•▪\\-\\*]|\\d{1,2}[\\.\\)])\\s*')
ROCKET = '\U0001F539'


def clean(s):
    return re.sub(r'\s+', ' ', (s or '').replace('​', ' ')).strip()


def merge_lines(text):
    lines = [clean(x) for x in (text or '').split('\n')]
    lines = [x for x in lines if x]
    out = []
    for ln in lines:
        if out and (ln[0].islower() or out[-1].lower().endswith(CONNECT)):
            out[-1] = out[-1] + ' ' + ln
        else:
            out.append(ln)
    return out


def tidy(x):
    return BUL.sub('', x).strip()


HDR_RE = re.compile(r'^(s\.? ?no\.?|sl\.? ?no\.?|sno|topics?|tropic|curriculum|sub ?-?(topics?|tropic)|key focus|dates?.*|duration)$')


def hnorm(c):
    return re.sub(r'[\s_]+', ' ', clean(c).lower()).strip()


def is_header(row):
    cells = [hnorm(c) for c in row if c is not None]
    cells = [c for c in cells if c]
    return bool(cells) and all(HDR_RE.match(c) for c in cells)


def parse_tables(doc):
    rows = []
    for pg in doc:
        for tb in pg.find_tables().tables:
            rows += tb.extract()
    if not rows:
        return []
    hdr = None
    for r in rows:
        if is_header(r):
            hdr = [hnorm(c) for c in r]
            break
    if hdr is None:
        topic_i, sub_i, ncol = 0, 1, max(len(r) for r in rows)
        body = rows[1:]
    else:
        ncol = len(hdr)
        topic_i = next((i for i, c in enumerate(hdr) if c in ('topic', 'tropic', 'topics', 'curriculum')), None)
        sub_i = next((i for i, c in enumerate(hdr) if (c.startswith('sub') or c == 'key focus') and i != topic_i), None)
        k = next(i for i, r in enumerate(rows) if is_header(r))
        body = rows[k + 1:]
    mods = []
    for r in body:
        if not r or is_header(r):
            continue
        r = list(r) + [None] * (ncol - len(r))
        if topic_i is None:
            lines = [tidy(x) for x in merge_lines(r[sub_i if sub_i is not None else 0])]
            lines = [x for x in lines if x]
            if lines:
                mods.append({'t': lines[0], 'items': lines[1:]})
            continue
        topic = clean(r[topic_i])
        items = [tidy(x) for x in merge_lines(r[sub_i])] if sub_i is not None else []
        items = [x for x in items if x]
        if topic:
            mods.append({'t': tidy(topic).rstrip(':'), 'items': items})
        elif mods and items:
            mods[-1]['items'] += items
    return mods


def parse_text(doc):
    lines = []
    for pg in doc:
        lines += [clean(x) for x in pg.get_text().split('\n')]
    mods = []
    for ln in lines:
        if not ln or ln in ('●', '•'):
            continue
        if ln.startswith(ROCKET):
            t = ln.replace(ROCKET, '', 1).strip()
            t = re.sub(r'\d{1,2}(st|nd|rd|th)\s+\w+.*$', '', t).strip()
            t = re.sub(r'^Lecture\s*\d+\s*:\s*', '', t).strip(' .:')
            mods.append({'t': t, 'items': []})
        elif mods:
            mods[-1]['items'].append(tidy(ln))
    return [m for m in mods if m['t']]


def parse_doc(doc):
    mods = parse_tables(doc)
    if not mods:
        mods = parse_text(doc)
    return mods
