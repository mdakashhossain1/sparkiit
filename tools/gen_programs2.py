import json, os, re, glob, warnings
warnings.filterwarnings('ignore')
import pymupdf
from pdfparse import parse_doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, 'pdf')

SW, DA, CL, CY, DE, EN, BM, HL = 'Software Development', 'Data and AI', 'Cloud and DevOps', 'Cyber Security', 'Design', 'Engineering', 'Business and Management', 'Healthcare and Life Sciences'

M = {
 'AI(Generative + Agentic) September October': ('AI (Generative and Agentic)', DA, 'layers', [['python']], '1485827404703-89b55fcc595e'),
 'Android App Development October': ('Android App Development', SW, 'phone-dev', [['android'], ['kotlin']], '1553877522-43269d4ea984'),
 'Artificial Intelligence September October': ('Artificial Intelligence', DA, 'layers', [['python'], ['tensorflow'], ['jupyter']], '1485827404703-89b55fcc595e'),
 'AutoCad September October': ('AutoCAD', EN, 'layout', [], '1581092160562-40aa08e78837'),
 'AWS September October': ('AWS', CL, 'cloud', [['amazonwebservices', 'plain-wordmark']], '1558494949-ef010cbdcc31'),
 'Business Analytics September October': ('Business Analytics', DA, 'trend', [], '1460925895917-afdab827c52f'),
 'CAR DESIGN September October': ('Car Design', EN, 'layers', [], '1503376780353-7e6692767b70'),
 'Clinical Trial & Research September October': ('Clinical Trial and Research', HL, 'shield', [], '1579684385127-1ef15d508118'),
 'Cloud Computing September October': ('Cloud Computing', CL, 'cloud', [['azure'], ['googlecloud'], ['amazonwebservices', 'plain-wordmark']], '1573164713988-8665fc963095'),
 'Cyber Security & Ethical Hacking September October': ('Cyber Security and Ethical Hacking', CY, 'shield', [['linux'], ['bash'], ['python']], '1531297484001-80022131f5a1'),
 'Data Analytics October': ('Data Analytics', DA, 'chart', [['python'], ['mysql']], '1551288049-bebda4e38f71'),
 'Data Science October': ('Data Science', DA, 'chart', [['python'], ['pandas'], ['jupyter']], '1460925895917-afdab827c52f'),
 'DeVops September October': ('DevOps', CL, 'server', [['docker'], ['kubernetes'], ['git']], '1558494949-ef010cbdcc31'),
 'Digital Marketing September October': ('Digital Marketing', BM, 'trend', [['google'], ['facebook']], '1533750349088-cd871a92f312'),
 'DSA with Python September October': ('DSA with Python', SW, 'code', [['python']], '1555066931-4365d14bab8c'),
 'Embedded Systems September October': ('Embedded Systems', EN, 'server', [['c'], ['cplusplus'], ['arduino']], '1518770660439-4636190af475'),
 'Finance September October': ('Finance', BM, 'briefcase', [], '1554224155-6726b3ff858f'),
 'Full-Stack Web Development October': ('Full-Stack Web Development', SW, 'layout', [['html5'], ['css3'], ['javascript']], '1498050108023-c5249f4df085'),
 'Graphic Designing September October': ('Graphic Designing', DE, 'palette', [['photoshop', 'plain'], ['illustrator', 'plain']], '1561070791-2526d30994b5'),
 'HEV September October': ('Hybrid Electric Vehicle', EN, 'layers', [['matlab']], '1473341304170-971dccb5ac1e'),
 'HRM September October': ('Human Resource Management', BM, 'users', [], '1521791136064-7986c2920216'),
 'IoT & Robotics September October': ('IoT and Robotics', EN, 'server', [['arduino'], ['raspberrypi']], '1485827404703-89b55fcc595e'),
 'Machine Learning August October': ('Machine Learning', DA, 'layers', [['python'], ['scikitlearn'], ['numpy']], '1460925895917-afdab827c52f'),
 'MEDICAL CODING September October': ('Medical Coding', HL, 'file', [], '1576091160399-112ba8d25d1d'),
 'Nanotechnology August October': ('Nanotechnology', EN, 'layers', [], '1532094349884-543bc11b234d'),
 'Programming in Java August October': ('Programming in Java', SW, 'coffee', [['java']], '1555066931-4365d14bab8c'),
 'Programming in Python October': ('Programming in Python', SW, 'code', [['python']], '1517694712202-14dd9538aa97'),
 'Project & Product Management October': ('Project and Product Management', BM, 'target', [['jira']], '1454165804606-c3d57bc86b40'),
 'Psychology October': ('Psychology', HL, 'users', [], '1573497019940-1c28c88b4f3e'),
 'Startup & Entrepreneurship September October': ('Startup and Entrepreneurship', BM, 'briefcase', [], '1533750349088-cd871a92f312'),
 'Stock Markting September September October': ('Stock Market', BM, 'trend', [], '1611974789855-9c2a0a7236a3'),
 'Supply Chain Management October': ('Supply Chain Management', BM, 'layers', [], '1586528116311-ad8dd3c8310d'),
 'UI_UX September October': ('UI UX Design', DE, 'palette', [['figma'], ['illustrator', 'plain']], '1522202176988-66273c2fd55f'),
 'VLSI September October': ('VLSI', EN, 'layers', [], '1518770660439-4636190af475'),
}

CONNECT = (' and', ' of', ' using', ' in', ' to', ' for', ' &', ',', '-', ' with', ' the', ' a', ' w.r.t.', ' on', ' or', ' vs', ' between')

def clean(s):
    return re.sub(r'\s+', ' ', (s or '').replace('\u200b', ' ')).strip()

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

def slugify(n):
    return re.sub(r'[^a-z0-9]+', '-', n.lower().replace('&', 'and')).strip('-')

progs = []
missing = []
for f in sorted(glob.glob(os.path.join(PDF, '*.pdf'))):
    stem = os.path.splitext(os.path.basename(f))[0]
    if stem not in M:
        missing.append(stem)
        continue
    name, cat, icon, tools, img = M[stem]
    doc = pymupdf.open(f)
    mods = parse_doc(doc)
    merged = []
    for m in mods:
        if merged and merged[-1]['t'].lower() == m['t'].lower():
            merged[-1]['items'] += m['items']
        else:
            merged.append(m)
    for m in merged:  # nano_fix
        if re.match(r'^Module \d+$', m['t']) and m['items']:
            m['t'] = m['t'] + ': ' + m['items'][0]
            m['items'] = m['items'][1:]
    top = []
    for m in merged:
        t = m['t']
        if any(t.lower() in x.lower() or x.lower() in t.lower() for x in top):
            continue
        top.append(t)
        if len(top) == 3:
            break
    if top:
        desc = 'Covers ' + (', '.join(top[:-1]) + ' and ' if len(top) > 1 else '') + top[-1] + ' and more.'
    else:
        desc = 'See the brochure for the full syllabus.'
    progs.append({'slug': slugify(name), 'name': name, 'cat': cat, 'icon': icon, 'tools': tools, 'img': img, 'd': desc,
                  'pdf': os.path.basename(f), 'mods': merged})

order = [SW, DA, CL, CY, DE, EN, BM, HL]
progs.sort(key=lambda p: (order.index(p['cat']), p['name']))
js = '/* generated from the brochure PDFs in /pdf */\nwindow.PROGRAMS = ' + json.dumps(progs, ensure_ascii=False, indent=1) + ';\nwindow.PROGRAM_CATS = ' + json.dumps(order) + ';\n'
open(os.path.join(ROOT, 'assets', 'programs-data.js'), 'w', encoding='utf-8').write(js)
print('programs', len(progs), 'missing', missing)
for p in progs:
    print(p['slug'], '|', len(p['mods']), 'mods', sum(len(m['items']) for m in p['mods']), 'items |', [m['t'][:30] for m in p['mods'][:2]])
