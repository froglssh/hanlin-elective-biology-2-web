import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.ImgGen()
G.crop('ov','overview',(0,0,1908,1130)); G.crop('ft','fruitTypes',(0,0,2032,1790)); G.crop('sb','strawberry'); G.crop('pa','pineapple')
G.crop('alt','alternation',(0,0,2004,1340)); G.crop('gam','gametophytes'); G.crop('pol','pollen',(0,0,1256,1050)); G.crop('orc','orchid')
G.crop('dbl','double',(0,0,708,1720)); G.crop('brd','breeding'); G.crop('hero','overview',(560,150,1500,1130))
G.label('L1','overview',r=(0,0,1908,1130),items=[
 {'id':'pet','m':(82,74,163,114)},{'id':'cor','m':(353,371,433,410)},{'id':'cal','m':(306,831,387,871)},{'id':'sep','m':(83,971,163,1011)},{'id':'rec','m':(82,1033,164,1073)},
 {'id':'sta','m':(1653,111,1750,160)},{'id':'sac','m':(1661,190,1777,228)},{'id':'grn','m':(1659,246,1777,286)},{'id':'fil','m':(1659,445,1743,489)},
 {'id':'pis','m':(1653,664,1751,715)},{'id':'stg','m':(1661,747,1743,788)},{'id':'sty','m':(1660,854,1742,894)},{'id':'ova','m':(1662,958,1741,998)},{'id':'ovu','m':(1662,1017,1741,1057)}],minw=110,minh=36,pad=3,maskpad=2)
G.label('L2','alternation',r=(0,200,2004,1340),items=[
 {'id':'spo','m':(1103,268,1244,347)},{'id':'mit1','m':(616,361,766,398)},{'id':'zyg','m':(542,500,685,581)},{'id':'fer','m':(527,665,674,702)},
 {'id':'mei','m':(1302,667,1451,701)},{'id':'spr','m':(1252,769,1482,802)},{'id':'gam','m':(919,1238,1061,1319)}],minw=140,minh=46)
G.label('L3','double',r=(0,0,708,500),items=[
 {'id':'pt','m':(72,93,183,127)},{'id':'int','m':(509,99,591,141)},{'id':'pn','m':(512,255,592,294)},{'id':'cc','m':(514,302,663,338)},{'id':'egg','m':(513,355,627,391)},
 {'id':'tn','m':(512,403,593,442)},{'id':'sp','m':(45,429,158,463)}],minw=90,minh=34,pad=2,maskpad=2)
G.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/CH4-2*/教學網頁/*質感新版.html')[0],
 old_assets=['original48','original49'],
 out='/home/user/hanlin-elective-biology-2-web/CH4-2-被子植物的有性生殖/教學網頁/有性生殖探索站_質感新版_優化版.html',
 text=dict(CODE='4-2',CH='4',CHNAME='植物的生殖',NAME='被子植物的有性生殖',BRAND='有性生殖探索站',BRAND_EN='Sexual Reproduction in Angiosperms',
  DESC='選修生物Ⅱ 4-2 被子植物的有性生殖：花與果實的構造、世代交替、花粉粒與胚囊的形成、授粉與雙重受精，用課本圖解、貼標籤與分類練習追蹤從花到種子的歷程。',
  LEDE='被子植物以花進行有性生殖，再以果實孕育與散播種子。花由哪些構造組成？果實怎麼分類？孢子體與配子體如何交替？花粉與胚囊如何形成？雙重受精又產生了什麼？跟著課本圖解，從一朵花追到一顆種子。',
  HERO_ALT='課本圖 4-4：花的基本組成構造',HERO_CAP='課本圖 4-4：花的基本組成構造',
  TIPS='<li>花與果實的構造</li><li>世代交替</li><li>花粉粒與胚囊</li><li>雙重受精</li>',
  PAGES='P111–P121',VIDEO='1d1UfsuVs1yvVY3ksKiCraev6e5xTY1K9',PATH='花與果實 → 世代交替 → 雙重受精'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
