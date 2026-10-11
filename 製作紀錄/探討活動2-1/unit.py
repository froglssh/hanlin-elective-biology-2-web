import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
P=gen_lib.Gen('book.pdf'); G=gen_lib.ImgGen()
P.crop('micro',1,(108,423,500,517)); P.crop('cut',2,(269,323,435,435)); P.crop('dish',2,(367,533,483,613)); P.crop('mount',3,(73,215,500,310)); P.crop('hero',1,(250,423,500,517))
G.crop('sunT','PPT15S3',(95,190,1245,570)); G.crop('celT','PPT19S3',(80,190,1250,570))
G.label('L1','PPT15S3',r=(95,190,1245,570),items=[
 {'id':'sk','m':(460,316,690,350)},{'id':'cw','m':(480,370,695,404)},{'id':'cc','m':(745,370,972,404)},
 {'id':'vw','m':(452,445,712,480)},{'id':'vs','m':(995,422,1235,505)},{'id':'pw','m':(460,523,690,557)}],minw=190,minh=34,pad=3,maskpad=3)
G.label('L2','PPT19S3',r=(80,190,1250,570),items=[
 {'id':'sk','m':(480,316,707,350)},{'id':'cw','m':(495,370,710,404)},{'id':'cc','m':(760,370,985,404)},
 {'id':'vw','m':(475,445,715,480)},{'id':'vs','m':(1005,422,1235,505)},{'id':'bw','m':(480,523,707,557)}],minw=190,minh=34,pad=3,maskpad=3)
P.Q.update(G.Q); P.info.update(G.info); P.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/探討活動2-1*/教學網頁/*質感新版.html')[0],old_assets=[],
 out='/home/user/hanlin-elective-biology-2-web/探討活動2-1-植物的細胞與組織/教學網頁/植物組織觀察站_質感新版_優化版.html',
 text=dict(CODE='探討活動 2-1',CH='2',CHNAME='植物體的構造與功能',NAME='植物的細胞與組織',BRAND='植物組織觀察站',BRAND_EN='Plant Cells and Tissues',
  DESC='選修生物Ⅱ 探討活動 2-1 植物的細胞與組織：觀察向日葵莖永久切片與西洋芹徒手切片，分辨表皮、皮層、維管束與髓的組成細胞，並用課本步驟圖、PPT 答案表貼標籤與分類練習歸納三類細胞的比例與功能。',
  LEDE='一片莖橫切面裡，薄壁、厚角、厚壁三類細胞各占多少？它們分布在哪裡、做什麼？從永久切片到徒手切片，跟著課本步驟與 PPT 的比例表，把組織位置、細胞類型與功能連起來。',
  HERO_ALT='課本步驟：在顯微鏡下觀察永久切片標本',HERO_CAP='課本步驟：用顯微鏡觀察永久切片',
  TIPS='<li>永久切片與徒手切片</li><li>薄壁・厚角・厚壁細胞</li><li>向日葵與西洋芹比例表</li><li>組織位置與功能</li>',
  PAGES='P58–P61',VIDEO='1DDge5EBqNlULu5Cc8kdrJW_KOAEcIKGI',PATH='原理 → 永久切片 → 徒手切片 → 比例與功能'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
