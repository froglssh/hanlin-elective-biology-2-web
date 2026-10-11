# 共用：從課本 PDF（288dpi）裁圖、切半並排、以文字層自動定位貼標籤遮罩
import pymupdf as fitz, json, io, os, numpy as np
from PIL import Image, ImageDraw
Z=4
class Gen:
    def __init__(s,pdf,out='out'):
        s.d=fitz.open(pdf); s.out=out; os.makedirs(out,exist_ok=True); s.info={}; s.Q={}
    def render(s,pi,r):
        p=s.d[pi]; pix=p.get_pixmap(matrix=fitz.Matrix(Z,Z),clip=fitz.Rect(*r),alpha=False)
        return Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
    def save(s,im,name,maxw=1800,q=82):
        if im.width>maxw: im=im.resize((maxw,round(im.height*maxw/im.width)),Image.LANCZOS)
        b=io.BytesIO(); im.save(b,'WEBP',quality=q,method=6); open(f'{s.out}/{name}.webp','wb').write(b.getvalue())
        s.info[name]=[im.width,im.height]; return [im.width,im.height]
    def crop(s,name,pi,r,maxw=1800,wipe=()):
        im=s.render(pi,r)
        if wipe:
            dr=ImageDraw.Draw(im)
            for w in wipe:
                x0,y0,x1,y1=[(v-(r[0] if i%2==0 else r[1]))*Z for i,v in enumerate(w)]
                bg=im.getpixel((max(0,int(x0)-2) if x0>2 else int(x1)+2, min(im.height-1,int(y1)+2)))
                dr.rectangle([x0,y0,x1,y1],fill=bg)
        return s.save(im,name,maxw)
    def cutrow(s,pi,r,lo,hi):
        im=s.render(pi,(r[0],lo,r[2],hi)); a=np.asarray(im.convert('L'),dtype=float)
        dark=(a<150).sum(1); return lo+int(np.argmin(dark))/Z
    def pair(s,name,pi,r,lo,hi):
        y=s.cutrow(pi,r,lo,hi); a=s.render(pi,(r[0],r[1],r[2],y)); b=s.render(pi,(r[0],y,r[2],r[3]))
        H=max(a.height,b.height); bg=a.getpixel((8,a.height//2))
        for k,im in (('a',a),('b',b)):
            c=Image.new('RGB',(im.width,H),bg); c.paste(im,(0,0)); s.save(c,name+k)
        return y
    def find(s,pi,r,text,idx=0):
        clip=fitz.Rect(*r); parts=text if isinstance(text,list) else [text]; rect=None
        for t in parts:
            hits=s.d[pi].search_for(t,clip=clip)
            if not hits: raise SystemExit(f'找不到文字 p{pi} {t!r}')
            h=hits[min(idx,len(hits)-1)]
            rect=h if rect is None else rect|h
        return (rect.x0,rect.y0,rect.x1,rect.y1)
    def label(s,name,pi,r,items,pad=3,minw=30,minh=14,maskpad=1.5,maxw=1800,wipe=()):
        ms=[]
        for it in items:
            m=it.get('m') or s.find(pi,r,it['t'],it.get('i',0))
            m=(m[0]-maskpad,m[1]-maskpad,m[2]+maskpad,m[3]+maskpad); it['_m']=m; ms.append(m)
        im=s.render(pi,r); dr=ImageDraw.Draw(im)
        for w in wipe:
            x0,y0,x1,y1=[(v-(r[0] if i%2==0 else r[1]))*Z for i,v in enumerate(w)]
            bg=im.getpixel((max(0,int(x0)-2) if x0>2 else int(x1)+2, min(im.height-1,int(y1)+2))); dr.rectangle([x0,y0,x1,y1],fill=bg)
        for m in ms:
            x0,y0,x1,y1=[(v-(r[0] if i%2==0 else r[1]))*Z for i,v in enumerate(m)]
            dr.rounded_rectangle([x0-3,y0-3,x1+3,y1+3],radius=10,fill=(226,224,214),outline=(150,146,130),width=2)
        wh=s.save(im,name,maxw); out=[]
        for it in items:
            if it.get('nos'): continue
            m=it['_m']
            if it.get('s'): sx0,sy0,sx1,sy1=it['s']
            else:
                cx=(m[0]+m[2])/2; cy=(m[1]+m[3])/2; w=max(m[2]-m[0]+2*pad,it.get('minw',minw)); h=max(m[3]-m[1]+2*pad,it.get('minh',minh))
                sx0,sy0,sx1,sy1=cx-w/2,cy-h/2,cx+w/2,cy+h/2
            out.append({'id':it['id'],'x':round((sx0-r[0])/(r[2]-r[0])*100,3),'y':round((sy0-r[1])/(r[3]-r[1])*100,3),
                        'w':round((sx1-sx0)/(r[2]-r[0])*100,3),'h':round((sy1-sy0)/(r[3]-r[1])*100,3)})
        for i,a in enumerate(out):
            for b in out[i+1:]:
                if a['x']<b['x']+b['w'] and b['x']<a['x']+a['w'] and a['y']<b['y']+b['h'] and b['y']<a['y']+a['h']: print('OVERLAP',name,a['id'],b['id'])
        s.Q[name]={'wh':wh,'slots':out}
        # 檢查圖
        im2=Image.open(f'{s.out}/{name}.webp').convert('RGB'); d=ImageDraw.Draw(im2)
        for o in out:
            x,y,w,h=[o[k]/100 for k in 'xywh']; d.rectangle([x*im2.width,y*im2.height,(x+w)*im2.width,(y+h)*im2.height],outline=(220,0,0),width=4)
        im2.thumbnail((800,800)); os.makedirs('chk',exist_ok=True); im2.save(f'chk/{name}.png')
    def done(s):
        json.dump({'info':s.info,'Q':s.Q},open(f'{s.out}/meta.json','w'),ensure_ascii=False,indent=1); print(s.info)

def inspect(pdf,dpi_scale=1.2):
    d=fitz.open(pdf); os.makedirs('pg',exist_ok=True); lines=[]
    for i,p in enumerate(d):
        p.get_pixmap(matrix=fitz.Matrix(dpi_scale,dpi_scale)).save(f'pg/p{i}.png')
        imgs=[[round(x) for x in im['bbox']] for im in p.get_image_info() if (im['bbox'][2]-im['bbox'][0])>60 and (im['bbox'][3]-im['bbox'][1])>40]
        lines.append(f'=== PAGE {i} imgs {imgs}')
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines',[]):
                t=''.join(sp['text'] for sp in l['spans']).strip()
                if t: lines.append(f"{[round(v) for v in l['bbox']]} {t}")
    open('text.txt','w').write('\n'.join(lines)); print(len(d),'pages')

# ---------- 以既有高解析圖（原頁內嵌、原自 PDF 裁出）＋ OCR 定位 ----------
_OCR=None
def _ocr():
    global _OCR
    if _OCR is None:
        from rapidocr_onnxruntime import RapidOCR; _OCR=RapidOCR()
    return _OCR
class ImgGen(Gen):
    def __init__(s,src='old',out='out'):
        s.src=src; s.out=out; os.makedirs(out,exist_ok=True); s.info={}; s.Q={}; s._cache={}
    def img(s,k):
        return Image.open(f'{s.src}/{k}.png').convert('RGB')
    def boxes(s,k):
        if k not in s._cache:
            res,_=_ocr()(f'{s.src}/{k}.png'); s._cache[k]=[(min(p[0] for p in b),min(p[1] for p in b),max(p[0] for p in b),max(p[1] for p in b),t) for b,t,_ in (res or [])]
        return s._cache[k]
    def dump(s,k):
        for b in s.boxes(k): print([int(v) for v in b[:4]],b[4])
    def findpx(s,k,text,idx=0):
        import difflib
        cands=[]
        for b in s.boxes(k):
            t=b[4]
            if text in t:   # 子字串：依字元比例截取
                i=t.index(text); n=len(t); w=b[2]-b[0]; h=b[3]-b[1]
                if h>w*1.6:  # 直排
                    cands.append((1.0,(b[0],b[1]+h*i/n,b[2],b[1]+h*(i+len(text))/n)))
                else: cands.append((1.0,(b[0]+w*i/n,b[1],b[0]+w*(i+len(text))/n,b[3])))
            else:
                r=difflib.SequenceMatcher(None,text,t).ratio()
                if r>=0.6: cands.append((r,b[:4]))
        if not cands: raise SystemExit(f'OCR 找不到 {k} {text!r}')
        cands.sort(key=lambda c:(-c[0],c[1][1],c[1][0])); return cands[min(idx,len(cands)-1)][1]
    def crop(s,name,k,r=None,maxw=1800,wipe=()):
        im=s.img(k)
        if r: im=im.crop(r)
        if wipe:
            dr=ImageDraw.Draw(im)
            for w in wipe: dr.rectangle(w,fill=im.getpixel((max(0,w[0]-3),min(im.height-1,w[3]+3))))
        return s.save(im,name,maxw)
    def label(s,name,k,items,pad=6,minw=70,minh=34,maskpad=4,r=None,wipe=(),maxw=1800):
        im=s.img(k); ox,oy=(r[0],r[1]) if r else (0,0)
        if r: im=im.crop(r)
        dr=ImageDraw.Draw(im)
        for w in wipe: dr.rectangle(w,fill=im.getpixel((max(0,w[0]-3),min(im.height-1,w[3]+3))))
        ms=[]
        for it in items:
            if it.get('m'): m=it['m']; m=(m[0]-ox,m[1]-oy,m[2]-ox,m[3]-oy)
            else:
                parts=it['t'] if isinstance(it['t'],list) else [it['t']]; m=None
                for t in parts:
                    b=s.findpx(k,t,it.get('i',0)); b=(b[0]-ox,b[1]-oy,b[2]-ox,b[3]-oy)
                    m=b if m is None else (min(m[0],b[0]),min(m[1],b[1]),max(m[2],b[2]),max(m[3],b[3]))
            m=(m[0]-maskpad,m[1]-maskpad,m[2]+maskpad,m[3]+maskpad); it['_m']=m; ms.append(m)
        for m in ms: dr.rounded_rectangle(m,radius=10,fill=(226,224,214),outline=(150,146,130),width=2)
        W,H=im.size; wh=s.save(im,name,maxw); out=[]
        for it in items:
            if it.get('nos'): continue
            m=it['_m']
            if it.get('s'): x0,y0,x1,y1=it['s']; x0,x1,y0,y1=x0-ox,x1-ox,y0-oy,y1-oy
            else:
                cx=(m[0]+m[2])/2; cy=(m[1]+m[3])/2; w=max(m[2]-m[0]+2*pad,it.get('minw',minw)); h=max(m[3]-m[1]+2*pad,it.get('minh',minh))
                x0,y0,x1,y1=cx-w/2,cy-h/2,cx+w/2,cy+h/2
            out.append({'id':it['id'],'x':round(x0/W*100,3),'y':round(y0/H*100,3),'w':round((x1-x0)/W*100,3),'h':round((y1-y0)/H*100,3)})
        for i,a in enumerate(out):
            for b in out[i+1:]:
                if a['x']<b['x']+b['w'] and b['x']<a['x']+a['w'] and a['y']<b['y']+b['h'] and b['y']<a['y']+a['h']: print('OVERLAP',name,a['id'],b['id'])
        s.Q[name]={'wh':wh,'slots':out}
        im2=Image.open(f'{s.out}/{name}.webp').convert('RGB'); d=ImageDraw.Draw(im2)
        for o in out:
            x,y,w,h=[o[k2]/100 for k2 in 'xywh']; d.rectangle([x*im2.width,y*im2.height,(x+w)*im2.width,(y+h)*im2.height],outline=(220,0,0),width=4)
        im2.thumbnail((800,800)); os.makedirs('chk',exist_ok=True); im2.save(f'chk/{name}.png')

def extract_old(html,dst='old'):
    import re,base64
    os.makedirs(dst,exist_ok=True)
    t=open(html,encoding='utf8').read()
    img=json.loads(re.search(r'const IMG\s*=\s*(\{.*?\});\s*\n',t,re.S).group(1)); keys=[]
    for k,v in img.items():
        try: im=Image.open(io.BytesIO(__import__('base64').b64decode(v.split(',',1)[1])))
        except Exception: continue
        if abs(im.width/im.height-16/9)>0.05: im.convert('RGB').save(f'{dst}/{k}.png'); keys.append((k,im.size))
    print(keys)
def contact(src='old',out='contact.png',skip=('BOOK','page','pdf')):
    import glob
    fs=[f for f in sorted(glob.glob(f'{src}/*.png')) if not os.path.basename(f).startswith(skip)]
    W=300; cols=4; ims=[]
    for f in fs:
        im=Image.open(f).convert('RGB'); im.thumbnail((W,W)); ims.append((os.path.basename(f)[:-4],im))
    rows=(len(ims)+cols-1)//cols; sh=Image.new('RGB',(W*cols,(W+16)*rows),'white'); d=ImageDraw.Draw(sh)
    for i,(k,im) in enumerate(ims):
        x,y=(i%cols)*W,(i//cols)*(W+16); sh.paste(im,(x,y+16)); d.text((x+2,y+2),k,fill='red')
    sh.save(out)
