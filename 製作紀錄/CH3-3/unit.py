import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.ImgGen()
G.crop('eng','engelmann',(0,0,1240,712)); G.crop('hist','history'); G.crop('ov','overview',(0,0,1840,1320))
G.crop('spec','spectra'); G.crop('ps','photosystem',(0,0,2427,950)); G.crop('ll','lightleft',(0,0,2219,1290)); G.crop('lr','lightright',(0,120,2427,1700))
G.crop('cyc','cyclic'); G.crop('pho','phospho'); G.crop('cal','calvin',(0,0,1536,1150)); G.crop('hero','overview',(560,0,1700,1300))
G.label('L1','overview',r=(0,60,1840,1320),items=[
 {'id':'om','m':(21,547,101,587)},{'id':'im','m':(23,613,100,653)},{'id':'tm','m':(336,613,487,647)},{'id':'th','m':(373,847,493,891)},
 {'id':'lr','m':(606,719,729,764)},{'id':'cf','m':(1276,728,1425,762)},{'id':'st','m':(1490,878,1581,920)},{'id':'atp','m':(963,792,1023,817)},{'id':'nadph','m':(937,882,1055,912)}],minw=90,minh=40)
G.label('L2','photosystem',r=(220,0,1620,950),items=[
 {'id':'lhc','m':(874,128,1059,163)},{'id':'lhc2','m':(1299,129,1482,163),'nos':1},{'id':'rc','m':(1104,115,1252,191)},{'id':'acc','m':(1138,275,1220,357)},
 {'id':'chla','m':(1104,667,1252,748)},{'id':'ant','m':(1389,843,1538,877)},{'id':'tm','m':(264,513,411,544)},{'id':'lu','m':(264,837,414,871)}],minw=150,minh=56)
G.label('L3','calvin',r=(0,0,1536,1150),items=[
 {'id':'rubp','m':(434,216,550,252)},{'id':'fix','m':(680,212,859,253)},{'id':'pga','m':(906,332,1088,366)},{'id':'red','m':(820,470,1000,524)},
 {'id':'reg','m':(406,588,587,628)},{'id':'g3p','m':(851,799,968,840)}],minw=110,minh=44)
G.label('L4','lightleft',r=(0,100,2219,1220),items=[
 {'id':'psii','m':(1107,158,1372,192)},{'id':'cplx','m':(1743,200,1961,230)},{'id':'str','m':(764,259,862,296)},{'id':'mem','m':(737,522,888,556)},
 {'id':'p680','m':(1187,627,1256,660)},{'id':'lu','m':(738,904,889,941)},{'id':'h2o','m':(982,905,1059,949)}],minw=110,minh=48)
G.label('L5','lightright',r=(0,120,2427,1360),items=[
 {'id':'psi','m':(543,432,794,465)},{'id':'p700','m':(631,901,695,933)},{'id':'nr','m':(1078,705,1315,744)},{'id':'atps','m':(1778,962,1979,998)},
 {'id':'nadph','m':(1390,415,1497,443)},{'id':'adp','m':(1493,148,1633,181)}],minw=130,minh=50)
G.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/CH3-3*/教學網頁/*質感新版.html')[0],
 old_assets=['originalLight'],
 out='/home/user/hanlin-elective-biology-2-web/CH3-3-光合作用/教學網頁/光合作用探索站_質感新版_優化版.html',
 text=dict(CODE='3-3',CH='3',CHNAME='植物體內物質的吸收、合成及運輸',NAME='光合作用',BRAND='光合作用探索站',BRAND_EN='Photosynthesis',
  DESC='選修生物Ⅱ 3-3 光合作用：從英格曼與 ¹⁸O 示蹤實驗、光合色素與光系統、非循環式與循環式電子傳遞，到卡爾文循環，用課本圖解、貼標籤與排序練習看懂光能如何變成醣類。',
  LEDE='植物如何把陽光變成醣類？從英格曼用好氧菌找出最有效的色光、¹⁸O 示蹤證明氧氣來自水，到類囊體膜上兩個光系統接力傳遞電子、合成 ATP 與 NADPH，再到基質中的卡爾文循環固定二氧化碳——跟著課本圖解一步步拆解光合作用。',
  HERO_ALT='課本圖 3-7：光合作用的示意圖（葉綠體）',HERO_CAP='課本圖 3-7：光反應與固碳反應',
  TIPS='<li>光合作用的發現史</li><li>光合色素與光系統</li><li>光反應與電子傳遞</li><li>卡爾文循環</li>',
  PAGES='P78–P88',VIDEO='12St3aSOE9k_h5AQESvvIerD2pdgZV4Lx',PATH='發現史 → 光反應 → 固碳反應'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
