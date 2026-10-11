# 列出原頁題目（摘要），PPT 原題完整列出
import re,json,sys
t=open(sys.argv[1],encoding='utf8').read()
s=re.sub(r'data:[^"\')]{200,}','DATA',t)
m=re.search(r'const CONTENT\s*=\s*(\{.*?\});\s*\n',s,re.S)
C=json.loads(m.group(1))
print('lessons',len(C['lessons']),[l.get('t') for l in C['lessons']])
for q in C['questions']:
    ppt='PPT' in json.dumps(q,ensure_ascii=False)[:400] or q.get('sourceSlide')
    if ppt and q.get('opts'):
        print('★',q.get('t'),'|',q.get('q'),'|',[(o['t'],o.get('ok')) for o in q['opts']],'|',q.get('why','')[:300])
    else:
        print('-',q.get('kind'),q.get('t'),'|',q.get('q','')[:80])
