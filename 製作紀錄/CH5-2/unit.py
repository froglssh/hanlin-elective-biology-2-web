import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.ImgGen()
G.crop('touch','touch'); G.crop('mim','mimosa',(0,0,1268,490)); G.crop('day','dayGraph'); G.crop('spec','spectrum',(0,0,832,880))
G.crop('sw','switch',(0,0,996,895)); G.crop('lt','lettuceTable'); G.crop('nt','nightTreatments'); G.crop('flo','florigen')
G.crop('nar','narcissus'); G.crop('pap','papaya'); G.crop('lp','lettucePhoto'); G.crop('ani','animals'); G.crop('def','defense',(0,0,2424,2010))
G.crop('hero','touch',(0,0,636,620))
G.label('L1','switch',r=(0,0,996,895),items=[
 {'id':'pr','m':(452,5,563,89)},{'id':'pfr','m':(450,345,564,431)},{'id':'fr','m':(313,206,428,241)},{'id':'dk','m':(115,205,268,241)},{'id':'r','m':(583,205,664,241)},
 {'id':'dec','m':(194,683,395,725)},{'id':'inc','m':(601,682,803,724)},{'id':'sdp','m':(170,834,429,866)},{'id':'ldp','m':(541,836,872,865)}],minw=100,minh=40)
G.label('L2','mimosa',r=(0,0,1268,490),items=[
 {'id':'rach','m':(165,193,242,228)},{'id':'leaf','m':(162,293,243,332)},
 {'id':'uh','m':(367,31,549,108)},{'id':'ll','m':(180,382,362,459)},{'id':'ul','m':(914,33,1094,108)},{'id':'lh','m':(1065,382,1247,459)},{'id':'rev','m':(628,319,883,397)}],minw=90,minh=40)
G.label('L3','defense',r=(0,0,2424,2010),items=[
 {'id':'imm','m':(333,133,581,177)},{'id':'loc','m':(331,388,581,432)},{'id':'sys1','m':(330,877,582,920)},{'id':'sys2','m':(1324,687,1575,730),'nos':1},
 {'id':'hurt','m':(715,1923,965,1967)},{'id':'heal','m':(1854,1922,2057,1969)}],minw=260,minh=60)
G.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/CH5-2*/教學網頁/*質感新版.html')[0],
 old_assets=['nightQuestion'],
 out='/home/user/hanlin-elective-biology-2-web/CH5-2-植物體對環境刺激的反應/教學網頁/環境刺激探索站_質感新版_優化版.html',
 text=dict(CODE='5-2',CH='5',CHNAME='植物的生長發育',NAME='植物體對環境刺激的反應',BRAND='環境刺激探索站',BRAND_EN='Plant Responses to Environment',
  DESC='選修生物Ⅱ 5-2 植物體對環境刺激的反應：向性與傾性運動、光週期與光敏素、春化作用、種子萌發的環境因子，以及逆境與植物的防禦，用課本圖解、貼標籤與分類練習理解植物如何回應環境。',
  LEDE='植物行固著生活，卻能感應光、重力、接觸、日長與溫度。含羞草為什麼一碰就合起？菊花為什麼秋天才開？光敏素如何決定開花與萌發？面對乾旱、淹水與蟲害，植物又如何自保？跟著課本圖解一探究竟。',
  HERO_ALT='課本圖 5-14：牽牛花的嫩莖彼此纏繞以利蔓延',HERO_CAP='課本圖 5-14：牽牛花的向觸性',
  TIPS='<li>向性與傾性</li><li>光週期與光敏素</li><li>春化作用</li><li>萌發條件・逆境・防禦</li>',
  PAGES='P148–P157',VIDEO='1Rc0myKjmdddZKaYq-SR2s-e58IcEnBiu',PATH='植物運動 → 開花 → 萌發 → 逆境與防禦'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
