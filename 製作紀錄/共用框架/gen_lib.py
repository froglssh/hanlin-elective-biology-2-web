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
