import sys; sys.path.insert(0,'../../fw'); import gen_lib, build_lib
G=gen_lib.Gen('book.pdf')
G.crop('f13',1,(56,494,535,650)); G.crop('hero',1,(58,496,425,648))
G.crop('f14',2,(58,400,562,724),wipe=[(212,400,562,583)])
G.crop('f15',3,(58,62,540,572))
G.pair('bs2',2,(82,120,243,392),250,300)
G.crop('bs1',1,(395,145,532,238))
G.label('L1',2,(58,400,562,724),wipe=[(212,400,562,583)],items=[
 {'id':'pro','t':'原核細胞'},{'id':'fold','t':'細胞膜內陷並摺疊'},{'id':'mem','t':'形成細胞內的膜'},
 {'id':'erne','t':'形成內質網及核膜'},{'id':'ern','m':(382,630,412,650),'s':(376,627,418,653)},{'id':'euk','t':'真核細胞'}],pad=2,minw=34,minh=14)
G.label('L2',3,(58,62,540,572),[
 {'id':'aero','t':'好氧菌'},{'id':'endo','t':['粒線體內','共生體']},{'id':'endomem','t':'內膜系統'},{'id':'mito','t':'粒線體'},
 {'id':'cyano','t':'藍綠菌'},{'id':'chl','t':'葉綠體'},{'id':'het','t':'異營真核細胞始祖'},{'id':'aut','t':'自營真核細胞始祖'}],pad=2,minw=36,minh=14)
G.label('L3',3,(58,62,540,420),[
 {'id':'p1','t':['粒線體內共生事件','未出現的早期階段']},{'id':'p2','t':['內共生發生在','內膜形成後']},{'id':'p3','t':['細胞核與內膜系統形','後演化出真核細胞']}],pad=2)
G.done()
# 需裁掉 L1 上方右側課文
CFG=dict(old=__import__('glob').glob('/home/user/hanlin-elective-biology-2-web/CH1-3*/教學網頁/*質感新版.html')[0],
 out='/home/user/hanlin-elective-biology-2-web/CH1-3-生命形式的多樣化/教學網頁/生命多樣化探索站_質感新版_優化版.html',
 text=dict(CODE='1-3',CH='1',CHNAME='生物的起源與演化',NAME='生命形式的多樣化',BRAND='生命多樣化探索站',BRAND_EN='Diversification of Life Forms',
  DESC='選修生物Ⅱ 1-3 生命形式的多樣化：由異營到自營、由無氧到有氧、由原核到真核、由單細胞到多細胞，用課本圖解、貼標籤與排序練習，看懂生命演化的四條主線。',
  LEDE='第一個細胞出現之後，生命如何一步步變得多樣？從攝取現成有機物的異營、到自行合成的自營；從無氧產能、經歷「氧氣大災難」到有氧呼吸；從細胞膜內陷、內共生到真核細胞，再到分工合作的多細胞生物——跟著課本圖解走過這四條演化主線。',
  HERO_ALT='課本圖 1-13：澳洲西部的疊層石與其層狀構造',HERO_CAP='課本圖 1-13：疊層石保存了 35 億年前類似藍綠菌的化石',
  TIPS='<li>異營 → 自營</li><li>無氧 → 有氧</li><li>原核 → 真核（內共生）</li><li>單細胞 → 多細胞</li>',
  PAGES='P22–P25',VIDEO='1yQxcRxkJwWsJvvqNa9NNIUS3fmMlSANR',PATH='營養與產能 → 原核到真核 → 多細胞'))
if __name__=='__main__' and len(sys.argv)>1 and sys.argv[1]=='build': build_lib.build(CFG)
