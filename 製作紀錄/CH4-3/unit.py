import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.Gen('book.pdf')
G.crop('f12',1,(115,110,625,800-40)); G.crop('seedlings',0,(80,505,560,712))
G.crop('f13',2,(88,465,635,695)); G.crop('f14',3,(60,465,600,695)); G.crop('hero',1,(380,180,620,440))
G.label('L1',1,(128,195,316,352),[
 {'id':'sc','t':'種皮','i':0},{'id':'en','t':'胚乳','i':0},{'id':'co','t':'子葉','i':0},{'id':'pl','t':'胚芽','i':0},{'id':'ax','t':'胚軸','i':0},{'id':'ra','t':'胚根','i':0}],pad=1,minw=24,minh=10,maskpad=1)
G.label('L2',1,(380,205,500,352),[
 {'id':'sc','m':(443,235,489,254)},{'id':'en','m':(443,269,462,277)},{'id':'co','m':(443,284,462,292)},{'id':'pl','m':(443,299,462,307)},
 {'id':'ax','m':(443,315,462,323)},{'id':'ra','m':(443,330,462,338)},{'id':'em','m':(484,306,493,315)}],pad=1.5,minw=24,minh=12)
G.label('L3',3,(62,465,326,695),[
 {'id':'lf','m':(118,586,137,594)},{'id':'hy','m':(188,595,216,604)},{'id':'pr','m':(95,641,104,667)},{'id':'mr','m':(195,629,204,646)},{'id':'lr','m':(191,653,201,670)},{'id':'co','m':(271,572,289,580)},{'id':'co2','m':(152,560,170,568),'nos':1},{'id':'co3','m':(79,617,98,625),'nos':1}],pad=1.5,minw=22,minh=11)
G.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/CH4-3*/教學網頁/*質感新版.html')[0],
 out='/home/user/hanlin-elective-biology-2-web/CH4-3-種子的構造與萌發/教學網頁/種子萌發探索站_質感新版_優化版.html',
 text=dict(CODE='4-3',CH='4',CHNAME='植物的生殖',NAME='種子的構造與萌發',BRAND='種子萌發探索站',BRAND_EN='Seed Structure & Germination',
  DESC='選修生物Ⅱ 4-3 種子的構造與萌發：種皮、胚與胚乳，蓖麻、黃豆、玉米、洋蔥四種種子的比較，以及胚根突出、胚軸延伸、胚芽生長三階段，用課本圖解與貼標籤練習追蹤一粒種子長成幼苗。',
  LEDE='一粒種子裡藏著什麼？種皮保護、胚是幼小的植物、胚乳或子葉貯藏養分。蓖麻、黃豆、玉米、洋蔥的種子各有不同；萌發時，有的子葉留在土中，有的被下胚軸推出地面。跟著課本圖解，看種子如何長成幼苗。',
  HERO_ALT='課本圖 4-12(c)：玉米種子的縱切面',HERO_CAP='課本圖 4-12(c)：玉米種子的構造',
  TIPS='<li>種皮・胚・胚乳</li><li>單子葉與雙子葉種子</li><li>萌發三階段</li><li>上胚軸與下胚軸</li>',
  PAGES='P122–P125',VIDEO='1qxiBYgFXm_ytzPCJDHR7vWCfe5JV3Bpa',PATH='種子的構造 → 萌發三階段 → 四種幼苗'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
