import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.Gen('book.pdf')
G.crop('f1',0,(240,480,550,722)); G.crop('willow',0,(0,398,222,662))
G.crop('f2',1,(41,405,607,705)); G.crop('f3',2,(50,280,565,560)); G.crop('ks',2,(80,592,548,722))
G.crop('hero',2,(450,285,565,520))
G.label('L1',2,(50,280,565,540),[
 {'id':'s1','m':(80,358,126,389)},{'id':'s2','m':(149,430,195,450)},{'id':'s3','m':(221,467,285,497)},{'id':'s4','m':(318,486,374,505)},
 {'id':'s5','m':(415,486,452,505)},{'id':'s6','m':(492,486,548,527)}],pad=2,minw=50,minh=22)
G.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/CH4-1*/教學網頁/*質感新版.html')[0],
 out='/home/user/hanlin-elective-biology-2-web/CH4-1-被子植物的無性生殖/教學網頁/無性生殖探索站_質感新版_優化版.html',
 text=dict(CODE='4-1',CH='4',CHNAME='植物的生殖',NAME='被子植物的無性生殖',BRAND='無性生殖探索站',BRAND_EN='Asexual Reproduction in Plants',
  DESC='選修生物Ⅱ 4-1 被子植物的無性生殖：營養繁殖、植物細胞的全潛能性與組織培養，用課本圖解、貼標籤與排序練習理解一小段組織如何長成一棵新植株。',
  LEDE='「無心插柳，柳成蔭」——一根柳條為什麼能長成一棵柳樹？植物可藉根、莖、葉的片段再生出與親代遺傳特性相同的新植株，關鍵在於細胞的全潛能性。組織培養更把這項能力發揮到極致，能大量複製優良品種。',
  HERO_ALT='課本圖 4-3：組織培養後移出培養基的蝴蝶蘭複製個體',HERO_CAP='課本圖 4-3：組織培養產生的蘭花複製個體',
  TIPS='<li>營養繁殖</li><li>全潛能性</li><li>組織培養六步驟</li><li>無性與有性生殖的比較</li>',
  PAGES='P108–P110',VIDEO='1Fp5OOtb6TaTZjT0mOqb2m6ZqBIio0cGo',PATH='營養繁殖 → 全潛能性 → 組織培養'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
