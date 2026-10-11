import sys,glob; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.Gen('book.pdf')
G.crop('fl',1,(80,170,505,300)); G.crop('tb',1,(92,376,484,488)); G.crop('cyl',1,(92,540,484,738))
G.crop('s4',2,(160,186,555,478)); G.crop('s5',2,(350,495,552,700)); G.crop('s6',3,(92,208,484,350)); G.crop('hero',3,(299,210,482,348))
G.label('L1',1,(78,170,505,300),[
 {'id':'foil','m':(197,183,224,192)},{'id':'r1','m':(137,274,213,296)},{'id':'r2','m':(250,274,326,296)},{'id':'r3','m':(364,274,440,296)}],pad=1.5,minw=40,minh=14)
G.label('L2',2,(350,495,552,700),[
 {'id':'foil','m':(366,516,393,524)},{'id':'paper','m':(375,575,393,584)},{'id':'leaf','m':(375,644,393,652)},{'id':'sol','m':(366,669,393,677)}],pad=2,minw=34,minh=13)
G.done()
CFG=dict(old=glob.glob('/home/user/hanlin-elective-biology-2-web/探討活動3-1*/教學網頁/*質感新版.html')[0],old_assets=[],
 out='/home/user/hanlin-elective-biology-2-web/探討活動3-1-光合色素之層析分離/教學網頁/光合色素探索站_質感新版_優化版.html',
 text=dict(CODE='探討活動 3-1',CH='3',CHNAME='植物體內物質的吸收、合成及運輸',NAME='光合色素之層析分離',BRAND='光合色素探索站',BRAND_EN='Pigment Chromatography',
  DESC='選修生物Ⅱ 探討活動 3-1 光合色素之層析分離：從課本實驗步驟圖認識展開液配製、濾紙點樣與展開，並用貼標籤、排序與分類練習判讀色素條帶與討論題。',
  LEDE='菠菜的綠色裡藏著不只一種色素。濾紙層析法利用色素與濾紙吸附力的差異，讓混合色素隨展開液移動時分開。跟著課本實驗步驟圖，從配製展開液到判讀條帶，一步一步完成。',
  HERO_ALT='課本實驗：濾紙上分離出的光合色素條帶',HERO_CAP='課本實驗：濾紙上的色素條帶',
  TIPS='<li>濾紙層析原理</li><li>展開液配製</li><li>點樣與展開</li><li>色素條帶判讀</li>',
  PAGES='P92–P95',VIDEO='1few0bCQAFhgYs8aql5Jm2iuWMw-Wgtnj',PATH='原理 → 配製展開液 → 點樣 → 展開 → 判讀色素'))
if len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
