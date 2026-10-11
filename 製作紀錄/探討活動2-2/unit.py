import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.Gen('book.pdf')
def T(x0,y0,x1,y1): return (x0-10,y0-6,x1+10,y1+6)
G.crop('p62',0,(40,430,580,720)); G.crop('p63',1,(0,0,607,500)); G.crop('sect',3,(42,118,500,668)); G.crop('hero',1,(0,0,607,500))
G.label('L1',0,(40,430,580,720),[{'id':'al','m':T(238,461,257,470)},{'id':'ec','m':T(389,461,407,470)}],pad=2,minw=56,minh=22)
G.label('L2',1,(0,0,607,500),[{'id':'li','m':T(154,137,172,146)},{'id':'su','m':T(527,239,555,248)},{'id':'wa','m':T(267,420,285,429)},{'id':'el','m':T(528,420,556,429)}],pad=2,minw=56,minh=22,wipe=[(55,203,305,368)])
G.label('L3',3,(42,118,500,668),[{'id':'al','m':T(65,202,83,210)},{'id':'li','m':T(65,340,83,348)},{'id':'wa','m':T(65,478,83,486)}],pad=2,minw=50,minh=22)
G.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/探討活動2-2*/教學網頁/*質感新版.html')[0],old_assets=[],
 out='/home/user/hanlin-elective-biology-2-web/探討活動2-2-營養構造的形態適應與特化/教學網頁/植物特化探索站_質感新版_優化版.html',
 text=dict(CODE='探討活動 2-2',CH='2',CHNAME='植物體的構造與功能',NAME='營養構造的形態適應與特化',BRAND='植物特化探索站',BRAND_EN='Plant Adaptations',
  DESC='選修生物Ⅱ 探討活動 2-2 營養構造的形態適應與特化：認識旱生、中生與水生植物的代表植物，比較莖與葉的構造，並用課本照片貼標籤與分類練習歸納構造與環境適應的關係。',
  LEDE='蘆薈肥厚多汁、睡蓮的葉柄中空、水蘊草的維管束退化——植物的營養器官為什麼長成不同的樣子？跟著課本照片，從旱生、中生到水生，把構造與環境中的水和空氣連起來。',
  HERO_ALT='課本照片：旱生、中生與水生植物',HERO_CAP='課本：中生與水生植物',
  TIPS='<li>旱生・中生・水生植物</li><li>肉質儲水</li><li>空腔通氣</li><li>葉橫切面比較</li>',
  PAGES='P62–P65',VIDEO='1QW17Yi8IUm24ZDxIQBvC2UrO4XSIdSxq',PATH='分類 → 特化構造 → 莖葉觀察 → 適應功能'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
