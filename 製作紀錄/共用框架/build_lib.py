import json,base64,re,io,os,glob,sys
from PIL import Image
def b64(p): return 'data:image/webp;base64,'+base64.b64encode(open(p,'rb').read()).decode()
def build(cfg):
    meta=json.load(open('out/meta.json'))
    assets={os.path.basename(f)[:-5]:b64(f) for f in glob.glob('out/*.webp')}
    old=open(cfg['old'],encoding='utf8').read()
    img=json.loads(re.search(r'const IMG\s*=\s*(\{.*?\});\s*\n',old,re.S).group(1))
    for k in cfg.get('old_assets',[]):  # 沿用原頁素材
        im=Image.open(io.BytesIO(base64.b64decode(img[k].split(',',1)[1]))).convert('RGB'); b=io.BytesIO(); im.save(b,'WEBP',quality=85)
        assets[k]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
    slides={}; mp={}
    nsl=sum(1 for k in img if re.fullmatch(r'[A-Za-z]*0*(\d+)\D+0*(\d+)',k))
    SW,SH,SQ=(1024,576,74) if nsl<=100 else (960,540,62)
    for k,v in img.items():
        m=re.fullmatch(r'[A-Za-z]*0*(\d+)\D+0*(\d+)',k)
        if not m: continue
        im=Image.open(io.BytesIO(base64.b64decode(v.split(',',1)[1])))
        if abs(im.width/im.height-16/9)>0.05: continue
        nk='s%02d_%02d'%(int(m.group(1)),int(m.group(2))); mp[k]=nk
        im=im.convert('RGB').resize((SW,SH),Image.LANCZOS); b=io.BytesIO(); im.save(b,'WEBP',quality=SQ,method=6)
        slides[nk]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
    scap={}
    dm=re.search(r'const DECK\s*=\s*(\[.*?\]);\s*\n',old,re.S)
    if dm:
        try:
            for row in json.loads(dm.group(1)):
                if isinstance(row,list) and row[0] in mp and len(row)>2 and isinstance(row[2],str): scap[mp[row[0]]]=row[2]
        except Exception: pass
    for nk in slides:
        if nk not in scap: a,b=nk[1:].split('_'); scap[nk]=f'原PPT第{int(a)}頁・第{int(b)}步'
    data='const ASSETS=%s;\nconst SLIDES=%s;\nObject.keys(SLIDES).forEach(k=>{ASSETS[k]=SLIDES[k]});\nconst SCAP=%s;\nconst Q_SLOTS=%s;\n'%(
        json.dumps(assets),json.dumps(slides),json.dumps(scap,ensure_ascii=False),json.dumps(meta['Q'],ensure_ascii=False))
    t=open(os.path.dirname(__file__)+'/base.html',encoding='utf8').read()
    t=t.replace('/*UNITJS*/',open('content.js',encoding='utf8').read())
    for k,v in cfg['text'].items(): t=t.replace('{{%s}}'%k,v)
    left=re.findall(r'\{\{[A-Z_]+\}\}',t)
    if left: raise SystemExit('未填：'+str(set(left)))
    t=t.replace('/*DATA*/',data)
    os.makedirs(os.path.dirname(cfg['out']),exist_ok=True)
    open(cfg['out'],'w',encoding='utf8').write(t)
    # 語法檢查
    for i,s in enumerate(re.findall(r'<script>([\s\S]*?)</script>',t)):
        open(f'_s{i}.js','w').write(s)
        if os.system(f'node --check _s{i}.js'): raise SystemExit('JS 語法錯誤')
    print(round(len(t)/1e6,2),'MB',len(slides),'slides',len(assets),'assets')
