# 原頁簡報畫面縮圖表（每頁最後一步），標上新鍵名
import re,json,base64,io,sys
from PIL import Image, ImageDraw
t=open(sys.argv[1],encoding='utf8').read()
img=json.loads(re.search(r'const IMG\s*=\s*(\{.*?\});\s*\n',t,re.S).group(1))
last={}
for k,v in img.items():
    m=re.fullmatch(r'[A-Za-z]*0*(\d+)\D+0*(\d+)',k)
    if not m: continue
    a,b=int(m.group(1)),int(m.group(2))
    if a not in last or b>last[a][0]: last[a]=(b,k)
W,H=320,180; ks=sorted(last); cols=5; rows=(len(ks)+cols-1)//cols
sh=Image.new('RGB',(W*cols,H*rows),'white'); d=ImageDraw.Draw(sh)
for i,a in enumerate(ks):
    b,k=last[a]; im=Image.open(io.BytesIO(base64.b64decode(img[k].split(',',1)[1])))
    if abs(im.width/im.height-16/9)>0.05: continue
    im=im.convert('RGB').resize((W,H)); x,y=(i%cols)*W,(i//cols)*H; sh.paste(im,(x,y))
    d.rectangle([x,y+H-16,x+70,y+H],fill='black'); d.text((x+3,y+H-14),'s%02d_%02d'%(a,b),fill='yellow')
sh.save(sys.argv[2]); print(len(ks))
