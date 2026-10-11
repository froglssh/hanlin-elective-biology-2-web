const {chromium}=require('/opt/node-tools/node_modules/playwright');
const url='file:///home/user/hanlin-elective-biology-2-web/CH1-2-生命的起源與化學演化/教學網頁/生命起源探索站_質感新版_優化版.html';
const VP=[[1440,900],[1366,768],[1280,720],[1024,768],[1280,640],[390,844],[360,640]];
(async()=>{
 const b=await chromium.launch();const out=[];
 for(const [w,h] of VP){
  const p=await b.newPage({viewport:{width:w,height:h}});const errs=[];
  p.on('pageerror',e=>errs.push(e.message));
  await p.goto(url);await p.waitForTimeout(300);
  const desk=w>900;
  const ov=()=>p.evaluate(()=>{const s=document.scrollingElement;return {x:s.scrollWidth>innerWidth+1,y:s.scrollHeight>innerHeight+1,sh:s.scrollHeight}});
  const rec=(tag,o)=>{if(o.x||(desk&&o.y&&tag.startsWith('Q'))||(desk&&o.y&&tag==='home')||o.bad)out.push(`${w}x${h} ${tag} ${JSON.stringify(o)}`)};
  rec('home',await ov());
  // learn
  for(let i=0;i<12;i++){await p.evaluate(i=>navigate("learn",i),i);await p.waitForTimeout(80);
    const o=await p.evaluate(()=>{const s=document.scrollingElement;const pn=document.getElementById('pane');const lf=document.getElementById('l-fig');return {x:s.scrollWidth>innerWidth+1,y:s.scrollHeight>innerHeight+1,paneOv:pn.scrollHeight>pn.clientHeight+1,figH:Math.round(lf.clientHeight),figW:Math.round(lf.clientWidth),imgs:[...lf.querySelectorAll('img')].map(i=>[Math.round(i.getBoundingClientRect().width),Math.round(i.getBoundingClientRect().height),i.naturalWidth>0])}});
    if(o.x||(desk&&(o.y||o.paneOv))||o.imgs.some(a=>!a[2]))out.push(`${w}x${h} L${i+1} ${JSON.stringify(o)}`)}
  // play
  const n=await p.evaluate(()=>STAGES.length);
  for(let i=0;i<n;i++){await p.evaluate(i=>navigate('play',i),i);await p.waitForTimeout(120);
    const o=await p.evaluate(()=>{const s=document.scrollingElement,bd=document.getElementById('board'),bar=document.getElementById('bar').getBoundingClientRect();
      const q=STAGES[QI];const exp=q.kind==='mc'?q.opts.length:(q.kind==='label'?q.cards.length:q.items.length);
      const vis=[...document.querySelectorAll('[data-card],[data-opt]')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0});
      const pre=q.pre?Object.keys(q.pre).length:0;
      const over=vis.filter(e=>e.getBoundingClientRect().bottom>bar.top+1).length;
      const fi=document.getElementById('figwrap');const fr=fi&&fi.getBoundingClientRect();
      const slots=[...document.querySelectorAll('[data-slot]')].map(e=>e.getBoundingClientRect());
      const sOut=slots.filter(r=>r.bottom>bar.top+1).length;
      return {x:s.scrollWidth>innerWidth+1,y:s.scrollHeight>innerHeight+1,sh:s.scrollHeight,boardOv:bd.scrollHeight>bd.clientHeight+1,vis:vis.length,exp:exp-pre,over,sOut,fig:fr?[Math.round(fr.width),Math.round(fr.height)]:null,
        fs:getComputedStyle(document.querySelector('.cd,.opt')||document.body).fontSize}});
    if(o.x||o.over||o.sOut||o.vis!==o.exp||(desk&&(o.y||o.boardOv)))out.push(`${w}x${h} Q${i+1} ${JSON.stringify(o)}`)}
  if(errs.length)out.push(`${w}x${h} ERR ${errs}`);
  await p.close();
 }
 console.log(out.join('\n')||'ALL OK');await b.close();
})();
