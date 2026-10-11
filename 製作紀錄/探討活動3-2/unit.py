import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.Gen('book.pdf')
G.crop('eq',0,(120,420,548,466)); G.crop('blend',1,(138,490,447,720)); G.crop('filt',2,(160,159,550,323)); G.crop('cent',2,(160,380,550,543)); G.crop('resus',2,(360,563,550,727))
G.crop('des1',3,(100,200,480,360)); G.crop('des2',3,(100,433,480,595)); G.crop('lt',4,(160,170,548,328)); G.crop('rd',4,(160,411,548,569)); G.crop('tbl',5,(73,187,484,300)); G.crop('hero',4,(160,170,548,328))
G.label('L1',0,(120,420,548,466),[
 {'id':'ox','m':(153,453,232,462)},{'id':'re','m':(424,453,503,462)}],pad=2,minw=95,minh=15)
G.label('L2',3,(100,200,480,600),[
 {'id':'a','m':(109,254,186,264)},{'id':'b','m':(317,254,401,264)},{'id':'c','m':(167,466,227,487)},{'id':'d','m':(326,466,380,498),'minw':88,'minh':34}],pad=2,minw=64,minh=28,wipe=[(103,396,478,414)])
G.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/探討活動3-2*/教學網頁/*質感新版.html')[0],old_assets=[],
 out='/home/user/hanlin-elective-biology-2-web/探討活動3-2-光反應的還原作用/教學網頁/光反應探索站_質感新版_優化版.html',
 text=dict(CODE='探討活動 3-2',CH='3',CHNAME='植物體內物質的吸收、合成及運輸',NAME='光反應的還原作用',BRAND='光反應探索站',BRAND_EN='Hill Reaction',
  DESC='選修生物Ⅱ 探討活動 3-2 光反應的還原作用：用 DCPIP 的顏色變化檢測葉綠體照光後釋放電子，並以課本實驗步驟圖、貼標籤與分類練習分析四支離心管的實驗設計。',
  LEDE='氧氣是從水裂解來的，不是從二氧化碳。1937 年希爾用分離的葉綠體與氧化劑 DCPIP 做了什麼實驗？跟著課本步驟圖，看懂實驗組與對照組的設計，並解釋四支離心管為什麼結果不同。',
  HERO_ALT='課本實驗：離心管置於檯燈前照光',HERO_CAP='課本實驗：四支離心管照光與遮光',
  TIPS='<li>希爾反應</li><li>DCPIP 氧化態與還原態</li><li>葉綠體懸浮液製備</li><li>實驗組與對照組</li>',
  PAGES='P96–P101',VIDEO='1o4FqsI5q-QbuHMXm-ehSo6qggODb0Iiu',PATH='原理 → 葉綠體製備 → 四管設計 → 照光 → 判讀'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
