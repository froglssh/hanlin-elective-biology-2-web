# 從原網頁內嵌的課本整頁圖（288dpi，1pt=4px）裁圖並產生貼標籤遮罩圖
from PIL import Image, ImageDraw
import glob, json, io, numpy as np
P=[Image.open(glob.glob(f'old/page{i}.*')[0]).convert('RGB') for i in range(7)]
Z=4
def crop(pi,r,mask=None):
    im=P[pi].crop(tuple(int(round(v*Z)) for v in r))
    if mask:
        dr=ImageDraw.Draw(im)
        for m in mask:
            x0,y0,x1,y1=[(v-(r[0] if i%2==0 else r[1]))*Z for i,v in enumerate(m)]
            dr.rounded_rectangle([x0-4,y0-4,x1+4,y1+4],radius=12,fill=(226,224,214),outline=(150,146,130),width=2)
    return im
def save(im,name,maxw=1800,q=82):
    if im.width>maxw: im=im.resize((maxw,round(im.height*maxw/im.width)),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'WEBP',quality=q,method=6); open('out/'+name+'.webp','wb').write(b.getvalue()); return [im.width,im.height]
def cutrow(pi,r,lo,hi):
    # 在 lo..hi(pt) 之間找最空白的列作為切點
    a=np.asarray(P[pi].crop((int(r[0]*Z),int(lo*Z),int(r[2]*Z),int(hi*Z))).convert('L'),dtype=float)
    dark=(a<150).sum(1); i=int(np.argmin(dark)); return lo+i/Z
def pair(pi,r,lo,hi,name):
    y=cutrow(pi,r,lo,hi)
    a=crop(pi,(r[0],r[1],r[2],y)); b=crop(pi,(r[0],y,r[2],r[3]))
    H=max(a.height,b.height); bg=a.getpixel((8,a.height//2))
    out=[]
    for k,im in (('a',a),('b',b)):
        c=Image.new('RGB',(im.width,H),bg); c.paste(im,(0,0)); out.append(save(c,name+k))
    return y
R={
 'f5':(1,(255,455,385,620)),'f6':(1,(395,455,525,620)),
 'f7':(2,(0,60,607,740)),'hero':(2,(0,60,607,300)),
 'f8':(3,(70,390,552,725)),'f9':(3,(70,238,195,385)),
 'f10':(4,(400,228,535,398)),'ch4':(4,(68,412,558,715)),
 'f11':(5,(170,465,530,680)),'f12':(6,(392,92,522,290)),
}
info={k:save(crop(pi,r),k) for k,(pi,r) in R.items()}
info['bubble_cut']=pair(1,(72,118,220,577),335,365,'bubble')
info['ribo_cut']=pair(6,(386,302,536,681),478,505,'ribo')
Q={}
def mk(name,pi,r,items,pad=3,minw=30,minh=14):
    im=crop(pi,r,[it['m'] for it in items]); wh=save(im,name); out=[]
    for it in items:
        m=it['m']; cx=(m[0]+m[2])/2; cy=(m[1]+m[3])/2
        w=max(m[2]-m[0]+2*pad,minw); h=max(m[3]-m[1]+2*pad,minh); s=(cx-w/2,cy-h/2,cx+w/2,cy+h/2)
        out.append({'id':it['id'],'x':round((s[0]-r[0])/(r[2]-r[0])*100,3),'y':round((s[1]-r[1])/(r[3]-r[1])*100,3),
          'w':round(w/(r[2]-r[0])*100,3),'h':round(h/(r[3]-r[1])*100,3)})
    # 檢查槽位重疊
    for i,a in enumerate(out):
        for b in out[i+1:]:
            if a['x']<b['x']+b['w'] and b['x']<a['x']+a['w'] and a['y']<b['y']+b['h'] and b['y']<a['y']+a['h']: print('OVERLAP',name,a['id'],b['id'])
    Q[name]={'wh':wh,'slots':out}
mk('L1',2,(0,60,607,740),[
 {'id':'s1','m':(229,212,370,249)},{'id':'s2','m':(345,341,489,367)},{'id':'s3','m':(408,454,543,479)},{'id':'s4','m':(444,587,533,613)}],pad=4,minw=120,minh=30)
mk('L2',3,(302,420,552,702),[
 {'id':'elec','m':(489,438,512,451)},{'id':'gas','m':(484,467,532,498)},{'id':'vap','m':(315,493,347,505)},
 {'id':'cond','m':(469,502,500,513)},{'id':'valve','m':(437,611,468,623)},{'id':'amino','m':(382,673,460,685)}],pad=2)
mk('L3',5,(170,465,530,680),[
 {'id':'bil','m':(226,488,304,502)},{'id':'org','m':(301,544,342,567)},{'id':'soup','m':(249,622,281,636)}])
mk('L4',4,(305,450,535,710),[
 {'id':'poop','m':(323,543,379,559)},{'id':'land','m':(381,543,433,559)},{'id':'fuel','m':(467,568,512,584)},
 {'id':'anae','m':(378,616,444,630)},{'id':'marsh','m':(447,633,504,648)}],pad=1)
json.dump({'info':info,'Q':Q},open('out/meta.json','w'),ensure_ascii=False,indent=1)
print(info)
