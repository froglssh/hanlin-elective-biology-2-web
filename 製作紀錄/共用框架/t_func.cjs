// 功能測試：node t_func.cjs <html路徑>
const {chromium}=require('/opt/node-tools/node_modules/playwright');
const url='file://'+process.argv[2];
(async()=>{
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1366,height:768}});const errs=[],log=[];
 p.on('pageerror',e=>errs.push(e.message));
 await p.goto(url);await p.waitForTimeout(300);
 const ok=(c,m)=>log.push((c?'PASS ':'FAIL ')+m);
 const n=await p.evaluate(()=>STAGES.length);
 for(let i=0;i<n;i++){
  await p.evaluate(i=>navigate('play',i),i);await p.waitForTimeout(80);
  const spec=await p.evaluate(()=>{const s=STAGES[QI];return {kind:s.kind,ans:s.kind==='mc'?s.opts.map((o,i)=>o.ok?i:-1).filter(x=>x>=0):(s.kind==='bucket'?s.items.map(it=>[it[0],it[2]]):answerMap(s)),pre:Object.keys(s.pre||{})}});
  await p.click('#b-check');
  const st=await p.evaluate(()=>({e:R(STAGES[QI]).errors,t:R(STAGES[QI]).tries}));
  if(st.e||st.t)ok(false,`Q${i+1} 空白提交計次`);
  if(spec.kind==='mc'){for(const a of spec.ans)await p.click(`[data-opt="${a}"]`)}
  else if(spec.kind==='bucket'){
    for(const [id,bk] of spec.ans){if(spec.pre.includes(id))continue;
      await p.click(`[data-card="${id}"]`);
      const slot=await p.evaluate(([bk])=>{const s=STAGES[QI],d=D(s),pm=preMap(s),bu=s.buckets.find(x=>x.id===bk);for(let i=0;i<bu.cap;i++){const sid=bk+'_'+i;if(!d.place[sid]&&!pm[sid])return sid}},[bk]);
      await p.click(`[data-slot="${slot}"]`);}
  }else{let j=0;for(const [sl,card] of Object.entries(spec.ans)){
      if(j%2===0){await p.click(`[data-card="${card}"]`);await p.click(`[data-slot="${sl}"]`)}else{await p.dragAndDrop(`[data-card="${card}"]`,`[data-slot="${sl}"]`)}j++}}
  await p.click('#b-check');await p.waitForTimeout(60);
  const r=await p.evaluate(()=>({passed:R(STAGES[QI]).passed,rev:R(STAGES[QI]).revealed,e:R(STAGES[QI]).errors}));
  ok(r.passed&&!r.rev&&r.e===0,`Q${i+1} ${spec.kind} UI 答對`);
 }
 await p.reload();await p.waitForTimeout(300);
 const kept=await p.evaluate(()=>STAGES.filter(s=>R(s).passed).length);ok(kept===n,`重載後通關保留 ${kept}/${n}`);
 await p.evaluate(()=>{ST=INITIAL();save()});await p.reload();await p.waitForTimeout(200);
 const mi=await p.evaluate(()=>STAGES.findIndex(s=>s.kind==='mc'&&!s.multi&&!s.opts[0].ok));
 if(mi>=0){await p.evaluate(i=>navigate('play',i),mi);
  for(let k=0;k<5;k++){await p.click('[data-opt="0"]');await p.click('#b-check')}
  const rv=await p.evaluate(i=>({p:R(STAGES[i]).passed,r:R(STAGES[i]).revealed,e:R(STAGES[i]).errors}),mi);ok(rv.p&&rv.r&&rv.e===5,'5次錯誤後揭露 '+JSON.stringify(rv));}
 const li=await p.evaluate(()=>STAGES.findIndex(s=>s.kind==='label'&&Q_SLOTS[s.fig].slots.length>=2));
 if(li>=0){await p.evaluate(i=>navigate('play',i),li);
  const ids=await p.evaluate(i=>Q_SLOTS[STAGES[i].fig].slots.map(x=>x.id),li);
  for(let k=0;k<ids.length;k++){await p.click(`[data-card="${ids[(k+1)%ids.length]}"]`);await p.click(`[data-slot="${ids[k]}"]`)}
  await p.click('#b-check');
  const bad=await p.evaluate(i=>({bad:D(STAGES[i]).bad.length,e:R(STAGES[i]).errors}),li);ok(bad.bad===ids.length&&bad.e===1,'答錯標示 '+JSON.stringify(bad));
  await p.click(`[data-slot="${ids[0]}"]`);ok(await p.evaluate(i=>D(STAGES[i]).bad.length===0,li),'修改後清除錯誤標記');
  await p.click('#b-reset');const rs=await p.evaluate(i=>({pl:Object.keys(D(STAGES[i]).place).length,round:R(STAGES[i]).round,err:R(STAGES[i]).errors}),li);ok(rs.pl===0&&rs.round===0&&rs.err===1,'重設 '+JSON.stringify(rs));
  await p.click('#zoombtn');await p.waitForSelector('dialog[open]');await p.keyboard.press('Escape');await p.waitForTimeout(100);ok(await p.evaluate(()=>!document.querySelector('dialog')),'放大 dialog 開關');}
 await p.evaluate(()=>navigate('learn',0));await p.click('#l-full');await p.waitForTimeout(250);
 if(await p.evaluate(()=>!!document.fullscreenElement)){await p.evaluate(()=>document.exitFullscreen());await p.waitForTimeout(250)}
 ok(await p.evaluate(()=>document.getElementById('l-full').textContent==='全螢幕播放'),'全螢幕進出');
 await p.evaluate(()=>navigate('show'));await p.click('#sh-next');ok(await p.evaluate(()=>SI===1),'簡報翻頁 '+await p.textContent('#sh-pos'));
 await p.click('#sh-play');await p.evaluate(()=>navigate('intro'));ok(await p.evaluate(()=>SPLAY===null),'離開簡報停止播放');
 await p.evaluate(()=>navigate('video'));ok(await p.evaluate(()=>!!document.querySelector('#vwrap iframe')),'影片頁 iframe');
 await p.evaluate(()=>navigate('done'));ok(await p.evaluate(()=>document.getElementById('done').textContent.includes('學習診斷')),'診斷頁');
 // 圖解卡皆有圖且載入
 const nl=await p.evaluate(()=>LEARN.length);let bad=0;
 for(let i=0;i<nl;i++){await p.evaluate(i=>navigate('learn',i),i);await p.waitForTimeout(60);if(await p.evaluate(()=>[...document.querySelectorAll('#l-fig img')].some(x=>!x.naturalWidth)))bad++}
 ok(bad===0,'圖解圖片全部載入');
 const f=log.filter(x=>x.startsWith('FAIL'));
 console.log(f.join('\n'));console.log(`PASS ${log.length-f.length} / ${log.length}`,'pageerrors:',errs);await b.close();
})();
