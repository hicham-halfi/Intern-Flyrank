"""Execute plain Python notebook cells sequentially and persist real stream outputs.
No IPython magics are supported; errors fail immediately and are saved.
"""
import contextlib
import io
import json
import os
import sys
import traceback
from pathlib import Path

path = Path(sys.argv[1]).resolve()
root = path.parents[2]
os.chdir(root)
nb = json.loads(path.read_text(encoding='utf-8'))
scope = {'__name__':'__main__'}
count = 0
for cell in nb['cells']:
    if cell['cell_type'] != 'code': continue
    count += 1
    out, err = io.StringIO(), io.StringIO()
    cell['execution_count'] = count
    cell['outputs'] = []
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            exec(compile(''.join(cell['source']),str(path)+f':cell{count}','exec'),scope)
    except Exception as exc:
        cell['outputs'].append({'output_type':'error','ename':type(exc).__name__,'evalue':str(exc),'traceback':traceback.format_exc().splitlines()})
        path.write_text(json.dumps(nb,indent=1),encoding='utf-8')
        raise
    for name,stream in [('stdout',out),('stderr',err)]:
        if stream.getvalue():cell['outputs'].append({'output_type':'stream','name':name,'text':stream.getvalue().splitlines(True)})
    print(f'Executed cell {count}:\n{out.getvalue()[:7000]}',flush=True)
nb['metadata']['execution']={'method':'sequential Python exec; real stdout/stderr','python':sys.version.split()[0]}
path.write_text(json.dumps(nb,indent=1),encoding='utf-8')
print('PASS: all code cells executed top to bottom')
