import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.ImgGen()
G.crop('rz','rootzones',(0,0,1485,925)); G.crop('rc','rootcompare',(0,0,1473,1150))
G.crop('lat','lateral'); G.crop('rmods','rootmods'); G.crop('adv','adventitious'); G.crop('rsec','rootsecondary')
G.crop('sext','stemexternal',(0,0,471,870)); G.crop('trees','treeforms'); G.crop('smods','stemmods'); G.crop('potato','potato')
G.crop('sc','stemcompare',(0,0,1491,1140)); G.crop('peri','periderm'); G.crop('wood','wood',(0,200,1515,1475))
G.crop('rings','rings',(0,0,1494,1225),wipe=[(0,0,840,300)])
G.crop('lext','leafexternal',(0,50,1467,1040)); G.crop('lsec','leafsections',(0,0,1479,1110)); G.crop('lmods','leafmods'); G.crop('bracts','bracts')
G.crop('hero','rootmods',(0,0,723,436))
G.label('L1','rootzones',r=(0,0,1485,925),items=[
 {'id':'mat','m':(1249,52,1371,92)},{'id':'elo','m':(1250,463,1370,497)},{'id':'mer','m':(1249,721,1371,759)},{'id':'cap','m':(285,534,376,574)},
 {'id':'hair','m':(633,400,696,432)},{'id':'stele','m':(637,345,697,375)}])
G.label('L2','rootcompare',r=(0,0,1473,1150),items=[
 {'id':'ph','m':(672,199,763,229)},{'id':'per','m':(687,284,748,313)},{'id':'xy','m':(673,386,762,414)},{'id':'en','m':(685,445,750,476)},
 {'id':'co','m':(686,865,747,894)},{'id':'ep','m':(688,950,749,979)}])
G.label('L3','stemcompare',r=(0,0,1491,1140),items=[
 {'id':'ep','m':(712,249,776,278)},{'id':'co','m':(713,329,773,358)},{'id':'vb','m':(700,455,788,483)},{'id':'pf','m':(687,507,801,534)},
 {'id':'ph','m':(699,567,787,595)},{'id':'vc','m':(699,608,787,664)},{'id':'xy','m':(700,769,788,795)},{'id':'gt','m':(688,823,801,850)}],pad=2,minh=26)
G.label('L4','periderm',r=(0,0,880,600),items=[
 {'id':'old','m':(201,49,394,75)},{'id':'cork','m':(308,174,394,202)},{'id':'cc','m':(226,282,394,332),'s':(222,280,398,335)},{'id':'pd','m':(308,341,395,369),'s':(304,338,399,372)},
 {'id':'co','m':(337,510,396,539)},{'id':'peri','m':(64,208,98,262)}],minw=60,pad=2,minh=24)
G.label('L5','rings',r=(0,0,1494,1225),wipe=[(0,0,840,300)],items=[
 {'id':'early','m':(1207,30,1358,57)},{'id':'late','m':(1258,571,1409,598)},{'id':'heart','m':(834,769,898,801)},{'id':'ring','m':(833,869,898,903)},
 {'id':'vc','m':(700,974,866,1000)},{'id':'ph','m':(699,1026,786,1054)},{'id':'co','m':(695,1069,758,1101)},{'id':'peri','m':(696,1117,760,1146)},{'id':'bark','m':(834,1090,900,1122)}],pad=1,minh=24,minw=60)
G.label('L6','leafsections',r=(0,0,1479,725),items=[
 {'id':'ue','m':(1202,165,1300,193)},{'id':'pal','m':(1212,215,1383,244)},{'id':'spo','m':(1212,308,1382,335)},{'id':'le','m':(1165,369,1303,413)},
 {'id':'st','m':(1072,454,1131,484)},{'id':'gc','m':(900,602,956,661)},{'id':'ch','m':(171,381,231,411)},{'id':'xy','m':(582,44,667,72)},{'id':'ph','m':(589,646,676,674)}])
G.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/CH2-2*/教學網頁/*質感新版.html')[0],
 old_assets=['original-ring','original-bark'],
 out='/home/user/hanlin-elective-biology-2-web/CH2-2-植物體的營養器官/教學網頁/營養器官探索站_質感新版_優化版.html',
 text=dict(CODE='2-2',CH='2',CHNAME='植物體的構造與功能',NAME='植物體的營養器官',BRAND='營養器官探索站',BRAND_EN='Roots · Stems · Leaves',
  DESC='選修生物Ⅱ 2-2 植物體的營養器官：根的四區與橫切面、特化根、莖的外形與內部構造、周皮與年輪、葉的構造與特化，用課本圖解、貼標籤與分類練習讀懂根莖葉。',
  LEDE='根、莖、葉是植物的營養器官。根尖如何一邊保護、一邊伸長吸收？雙子葉與單子葉植物的根莖葉橫切面有何不同？樹皮、年輪、心材與邊材怎麼形成？馬鈴薯為什麼是莖不是根？跟著課本圖解一一拆解。',
  HERO_ALT='課本圖 2-11(a)：玉米的支持根',HERO_CAP='課本圖 2-11(a)：玉米的支持根',
  TIPS='<li>根：四區與橫切面</li><li>莖：周皮、年輪、心材與邊材</li><li>葉：葉肉與氣孔</li><li>特化的根、莖、葉</li>',
  PAGES='P42–P57',VIDEO='11G1TJsSHEegGsTIRHUrVr-NMxULTbIBR',PATH='根 → 莖 → 葉'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
