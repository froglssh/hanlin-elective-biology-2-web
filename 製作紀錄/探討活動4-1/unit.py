import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.Gen('book.pdf')
def T(x0,y0,x1,y1,p=8): return (x0-p,y0-2,x1+p,y1+2)
G.crop('sym',1,(75,388,255,504)); G.crop('tweez',1,(304,310,513,454)); G.crop('flA',2,(200,167,525,330)); G.crop('flB',2,(196,458,492,604))
G.crop('fruit',4,(92,240,520,712)); G.crop('p5',5,(70,135,590,715)); W=[(185,262,225,269)]; G.crop('pine',6,(185,262,525,492),wipe=W); G.crop('hero',6,(185,262,525,492),wipe=W)
G.label('L1',1,(75,388,255,504),[{'id':'ra','m':T(98,482,134,491)},{'id':'bi','m':T(191,482,228,491)}],pad=2,minw=50,minh=18)
G.label('L2',4,(375,445,540,545),[{'id':'in','m':T(490,490,518,499,3)},{'id':'mi','m':T(490,508,518,516,3)},{'id':'ou','m':T(490,524,518,533,3)}],pad=0.5,minw=40,minh=10)
G.label('L3',5,(78,490,235,612),[{'id':'ca','m':T(83,526,111,534,3)},{'id':'ov','m':T(83,549,111,558,3)},{'id':'se','m':T(93,573,111,581,3)}],pad=2,minw=40,minh=14)
G.label('L4',5,(295,278,495,395),[{'id':'ca','m':T(301,301,329,309,3)},{'id':'se','m':T(311,327,329,335,3)}],pad=2,minw=40,minh=14,wipe=[(300,277,342,282)])
G.label('L5',6,(185,262,525,492),[{'id':'fl','m':(186,410,222,432)},{'id':'fr','m':T(444,396,518,404,3)},{'id':'ax','m':T(444,413,472,422,3)},{'id':'br','m':T(444,440,463,448,3)}],pad=0.5,minw=44,minh=10,wipe=W)
G.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/探討活動4-1*/教學網頁/*質感新版.html')[0],old_assets=[],
 out='/home/user/hanlin-elective-biology-2-web/探討活動4-1-花與果實的形態與構造/教學網頁/花果構造探索站_質感新版_優化版.html',
 text=dict(CODE='探討活動 4-1',CH='4',CHNAME='植物的生殖',NAME='花與果實的形態與構造',BRAND='花果構造探索站',BRAND_EN='Flowers and Fruits',
  DESC='選修生物Ⅱ 探討活動 4-1 花與果實的形態與構造：從花的解剖、對稱性到果實的縱橫切，用課本圖貼標籤、分類與排序練習分辨單花果與多花果，並連結花長成果實的過程。',
  LEDE='花凋謝之後，哪些構造會長成果實？蘋果的肉質部分是子房嗎？鳳梨又是一朵花還是很多朵花？跟著課本的解剖步驟與圖解，把花的構造與果實的來源一一對起來。',
  HERO_ALT='課本圖：鳳梨外觀與縱切面構造',HERO_CAP='課本圖：多花果（鳳梨）',
  TIPS='<li>花的對稱與解剖</li><li>果實縱切與橫切</li><li>單花果與多花果</li><li>花構造的殘跡</li>',
  PAGES='P126–P132',VIDEO='1f8TZ-5htN3YX00ZNBtJHtQeduo6KNt36',PATH='花的觀察 → 果實解剖 → 單花果 → 多花果'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
