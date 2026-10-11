# 從課本PDF以288dpi重裁圖，並產生貼標籤遮罩圖
import pymupdf as fitz, json, io, base64
from PIL import Image, ImageDraw
d=fitz.open('book.pdf')
Z=4
def crop(pi,r,mask=None):
    p=d[pi]; r=fitz.Rect(*r)
    pix=p.get_pixmap(matrix=fitz.Matrix(Z,Z),clip=r,alpha=False)
    im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
    if mask:
        dr=ImageDraw.Draw(im)
        for m in mask:
            x0,y0,x1,y1=[(v-(r.x0 if i%2==0 else r.y0))*Z for i,v in enumerate(m)]
            dr.rounded_rectangle([x0-6,y0-6,x1+6,y1+6],radius=14,fill=(226,224,214),outline=(150,146,130),width=2)
    return im
def save(im,name,maxw=1800,q=82):
    if im.width>maxw: im=im.resize((maxw,round(im.height*maxw/im.width)),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'WEBP',quality=q,method=6)
    open('out/'+name+'.webp','wb').write(b.getvalue())
    return [im.width,im.height]
R={ # 圖解用完整圖
 'f1':(1,(44,270,560,728)),
 'f2a':(3,(66,425,531,560)),'f2b':(3,(66,570,531,706)),
 'f3a':(4,(232,486,555,728)),'f3b':(5,(50,487,345,736)),'f3c':(5,(350,487,545,718)),
 'f4':(6,(112,190,528,758)),
 'ks':(2,(77,403,548,722)),'spore':(2,(377,452,533,676)),
 'hero':(5,(353,558,536,681)),
}
info={}
for k,(pi,r) in R.items(): info[k]=save(crop(pi,r),k)
# 貼標籤題：mask=遮罩框(pt)；slot=答題格(pt，不小於遮罩)
def slot(m,minw=58,minh=17):
    cx=(m[0]+m[2])/2; cy=(m[1]+m[3])/2; w=max(m[2]-m[0]+6,minw); h=max(m[3]-m[1]+4,minh)
    return (cx-w/2,cy-h/2,cx+w/2,cy+h/2)
Q={}
def mk(name,pi,r,items,minw=58,minh=17):
    ms=[it['m'] for it in items]
    im=crop(pi,r,ms); wh=save(im,name)
    out=[]
    for it in items:
        s=it.get('s') or slot(it['m'],minw,minh)
        out.append({'id':it['id'],'label':it['label'],
          'x':round((s[0]-r[0])/(r[2]-r[0])*100,3),'y':round((s[1]-r[1])/(r[3]-r[1])*100,3),
          'w':round((s[2]-s[0])/(r[2]-r[0])*100,3),'h':round((s[3]-s[1])/(r[3]-r[1])*100,3)})
    Q[name]={'wh':wh,'slots':out}
# 圖1-1：三張紙條（整塊說明）
mk('L1',1,(44,270,560,728),[
 {'id':'a','label':'瓶口敞開，數日後肉塊腐敗且出現蛆蟲','m':(57,320,136,353),'s':(52,316,142,358)},
 {'id':'b','label':'瓶口蓋緊蓋子，數日後肉塊腐敗，沒有出現蛆蟲','m':(57,461,136,495),'s':(52,457,142,500)},
 {'id':'c','label':'瓶口覆蓋紗布，數日後肉塊腐敗，沒有出現蛆蟲','m':(57,616,136,650),'s':(52,612,142,655)}])
# 圖1-2
mk('L2',3,(66,425,531,706),[
 {'id':'n1','label':'瓶口保持開放，置於室溫下冷卻','m':(285,527,352,549),'s':(281,521,356,553)},
 {'id':'n2','label':'以軟木塞封口','m':(367,533,424,543),'s':(361,527,430,549)},
 {'id':'n3','label':'數日後，肉汁變混濁，長出微生物','m':(445,515,493,548),'s':(441,511,497,552)},
 {'id':'s1','label':'立刻燒融封口','m':(325,681,382,691),'s':(319,675,388,697)},
 {'id':'s2','label':'數日後，肉汁保持澄清，不會長出微生物','m':(444,660,502,693),'s':(440,656,506,697)}])
# 圖1-3(b)
mk('L3',5,(50,487,345,736),[
 {'id':'neck','label':'鵝頸瓶','m':(90,560,119,569),'s':(80,553,129,576)},
 {'id':'cut','label':'切斷','m':(161,559,181,569),'s':(150,552,192,576)},
 {'id':'nocut','label':'不切斷','m':(156,687,186,697),'s':(144,680,198,704)},
 {'id':'grow','label':'長出微生物','m':(271,492,319,502),'s':(262,486,328,508)},
 {'id':'nogrow','label':'不長微生物','m':(271,612,319,622),'s':(262,606,328,628)},
 {'id':'dust','label':'塵埃','m':(288,693,308,703),'s':(276,686,320,710)}])
# 圖1-4 歷程（遮人名）
mk('L4',6,(112,190,528,758),[
 {'id':'ari','label':'亞里斯多德','m':(188,651,247,665),'s':(186,648,262,668)},
 {'id':'hel','label':'凡赫芒','m':(188,561,224,575),'s':(186,558,250,578)},
 {'id':'nee','label':'尼丹','m':(188,463,221,477),'s':(186,460,246,480)},
 {'id':'pou','label':'蒲歇與其他學者','m':(188,336,270,349),'s':(186,333,278,352)},
 {'id':'job','label':'約伯勒','m':(349,485,385,498),'s':(347,482,402,502)},
 {'id':'spa','label':'司巴蘭贊尼','m':(349,388,408,401),'s':(347,385,418,405)},
 {'id':'red','label':'雷迪','m':(349,549,382,562),'s':(347,546,402,566)},
 {'id':'pas','label':'巴斯德','m':(349,310,385,323),'s':(347,307,402,327)}])
# 內孢子電顯照片
mk('L5',2,(377,452,533,676),[
 {'id':'wall','label':'孢子壁','m':(482,511,508,519),'s':(480,506,531,524)},
 {'id':'esp','label':'內孢子','m':(398,526,424,535),'s':(380,521,432,540)},
 {'id':'edna','label':'內孢子DNA','m':(482,524,508,544),'s':(480,521,531,547)},
 {'id':'dna','label':'DNA','m':(482,577,500,587),'s':(480,572,524,592)}])
json.dump({'info':info,'Q':Q},open('out/meta.json','w'),ensure_ascii=False,indent=1)
print(info); 
import os; print(sum(os.path.getsize('out/'+f) for f in os.listdir('out'))/1e6)
