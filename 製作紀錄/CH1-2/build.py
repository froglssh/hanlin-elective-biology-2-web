import json,base64,re,io,os,glob
from PIL import Image
def b64(path,mime='image/webp'): return 'data:%s;base64,%s'%(mime,base64.b64encode(open(path,'rb').read()).decode())
meta=json.load(open('out/meta.json'))
assets={}
for k in ['f5','f6','f7','hero','f8','f9','f10','ch4','f11','f12','bubblea','bubbleb','riboa','ribob','L1','L2','L3','L4']:
    assets[k]=b64(f'out/{k}.webp')
# PPT 原題二的參考圖沿用原頁
im=Image.open(glob.glob('old/exam_apparatus.*')[0]).convert('RGB'); b=io.BytesIO(); im.save(b,'WEBP',quality=85); assets['exam_apparatus']='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
slides={}
for f in sorted(glob.glob('old/s*_*.*')):
    k=os.path.basename(f).split('.')[0]
    if not re.fullmatch(r's\d+_\d+',k): continue
    im=Image.open(f).convert('RGB').resize((1024,576),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'WEBP',quality=74,method=6)
    slides[k]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
old=open('old_stripped.html',encoding='utf8').read()
D=json.loads(re.search(r'const DECK=(\[.*?\]);\n',old,re.S).group(1))
scap={k:c for k,n,c in D}
data='const ASSETS=%s;\nconst SLIDES=%s;\nObject.keys(SLIDES).forEach(k=>{ASSETS[k]=SLIDES[k]});\nconst SCAP=%s;\nconst Q_SLOTS=%s;\n'%(
 json.dumps(assets),json.dumps(slides),json.dumps(scap,ensure_ascii=False),json.dumps(meta['Q'],ensure_ascii=False))
t=open('tpl.html',encoding='utf8').read().replace('/*DATA*/',data)
out='/home/user/hanlin-elective-biology-2-web/CH1-2-生命的起源與化學演化/教學網頁/生命起源探索站_質感新版_優化版.html'
open(out,'w',encoding='utf8').write(t)
print(round(len(t)/1e6,2),'MB',len(slides),'slides')
