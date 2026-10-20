"""Run live-model checks. No mocks; synthetic fixtures are explicitly labeled."""
import hashlib
import json
from pathlib import Path
from scout import Scout

ROOT=Path(__file__).resolve().parent/'eval_workspace'
papers=ROOT/'papers';papers.mkdir(parents=True,exist_ok=True)
fixtures={
 'standard.md':'''# Synthetic MARL evaluation fixture
This is an ML research test fixture, not a published paper.
Architecture: Multi-Agent Reinforcement Learning with PPO policies.
Dataset: 100 simulated vehicle-routing episodes.
Reported experiment: median route distance was 42 km versus a 50 km greedy baseline.
These figures are synthetic values used only to test extraction.''',
 'missing.md':'''# ML opinion fixture: what makes a useful study assistant?
This opinion discusses machine learning and neural networks for study support.
No experiment was performed. No dataset was collected. No baseline metrics are reported.
A user should compare explanations with source notes and ask for clarification.''',
 'unknown.md':'''# Synthetic algorithm research fixture
Architecture: a neural-network method called Zorvex-Temporal Routing.
This new named method has no definition in this text; external research is needed.
Dataset: simulated routing trajectories. No baseline metrics are reported.
This is a synthetic ML evaluation fixture, not evidence of a real algorithm.''',
 'menu.md':'''# Restaurant menu
Soup: 5 dollars. Salad: 7 dollars. Grilled fish: 15 dollars.
Open daily from noon. Ask the waiter about ingredients.'''}
for name,text in fixtures.items():(papers/name).write_text(text,encoding='utf-8')

checks=[]
def case(name,source,predicate):
    s=Scout(ROOT,backend='codex',cloud_approved=True) # These fixtures are generated synthetic text, not user documents.
    try:
        result=s.run(source)
        note=(ROOT/result['note']).read_text(encoding='utf-8') if result['note'] else ''
        ok=predicate(result,note)
        checks.append({'case':name,'pass':bool(ok),'status':result['status'],'note':result['note']})
    except Exception as exc:checks.append({'case':name,'pass':False,'error':type(exc).__name__+': '+str(exc)})
    (ROOT/'eval_results.json').write_text(json.dumps({'fixture_scope':'Synthetic Markdown live-model checks; PDF integration is a separate run','checks':checks},indent=2))
    print('EVAL',checks[-1],flush=True)

case('standard extraction','standard.md',lambda r,n:r['status']=='saved' and '42' in n and '50' in n)
case('missing baseline','missing.md',lambda r,n:r['status']=='saved' and 'No baseline metrics provided in text.' in n)
case('unrelated refusal','menu.md',lambda r,n:r['status']=='refused' and r['note'] is None)
case('unknown algorithm triggers real lookup','unknown.md',lambda r,n:any(e['tool']=='web_search' for e in r['events']))
before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'notes').glob('*.md')}
case('repeat input uses new filename','standard.md',lambda r,n:r['status']=='saved' and Path(r['note']).name not in before)
checks.append({'case':'previous notes unchanged','pass':all((ROOT/'notes'/name).exists() and hashlib.sha256((ROOT/'notes'/name).read_bytes()).hexdigest()==digest for name,digest in before.items())})
(ROOT/'eval_results.json').write_text(json.dumps({'fixture_scope':'Synthetic Markdown live-model checks; PDF integration is a separate run','checks':checks},indent=2))
print(json.dumps(checks,indent=2))
