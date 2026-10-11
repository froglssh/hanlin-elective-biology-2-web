import json,base64,re,io,os
from PIL import Image
def b64(path,mime='image/webp'): return 'data:%s;base64,%s'%(mime,base64.b64encode(open(path,'rb').read()).decode())
meta=json.load(open('out/meta.json'))
assets={}
for k in ['f1','f2a','f2b','f3a','f3b','f3c','hero','f4','ks','L1','L2','L3','L4','L5']:
    assets[k]=b64(f'out/{k}.webp')
slides={}
for f in sorted(os.listdir('slides')):
    if not re.fullmatch(r'k\d+_\d+\.webp',f): continue
    im=Image.open('slides/'+f).convert('RGB').resize((1024,576),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'WEBP',quality=74,method=6)
    slides[f[:-5]]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
old=open('/home/user/hanlin-elective-biology-2-web/CH1-1-生源說與無生源說/教學網頁/生源論戰法庭_質感新版.html',encoding='utf8').read()
i=old.index('const CAP={'); j=old.index('};',i)
scap=dict(re.findall(r"(k\d+_\d+):'([^']*)'",old[i:j]))
data='const ASSETS=%s;\nconst SLIDES=%s;\nObject.keys(SLIDES).forEach(k=>{ASSETS[k]=SLIDES[k]});\nconst SCAP=%s;\nconst Q_SLOTS=%s;\n'%(
 json.dumps(assets),json.dumps(slides),json.dumps(scap,ensure_ascii=False),json.dumps(meta['Q'],ensure_ascii=False))
t=open('tpl.html',encoding='utf8').read().replace('/*DATA*/',data)
out='/home/user/hanlin-elective-biology-2-web/CH1-1-生源說與無生源說/教學網頁/生源論戰法庭_質感新版_優化版.html'
open(out,'w',encoding='utf8').write(t)
print(len(t)/1e6,'MB',len(slides),'slides')
