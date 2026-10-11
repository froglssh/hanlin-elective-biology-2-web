const {chromium}=require('/opt/node-tools/node_modules/playwright');
const url='file:///home/user/hanlin-elective-biology-2-web/CH1-2-生命的起源與化學演化/教學網頁/生命起源探索站_質感新版_優化版.html';
(async()=>{
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1366,height:768}});const errs=[],log=[];
 p.on('pageerror',e=>errs.push(e.message));
 await p.goto(url);await p.waitForTimeout(300);
 const ok=(c,m)=>log.push((c?'PASS ':'FAIL ')+m);
 const n=await p.evaluate(()=>STAGES.length);
 // 逐題用UI答對
 for(let i=0;i<n;i++){
  await p.evaluate(i=>navigate('play',i),i);await p.waitForTimeout(100);
  const spec=await p.evaluate(()=>{const s=STAGES[QI];return {kind:s.kind,ans:s.kind==='mc'?s.opts.map((o,i)=>o.ok?i:-1).filter(x=>x>=0):(s.kind==='bucket'?s.items.map(it=>[it[0],it[2]]):answerMap(s)),pre:Object.keys(preMap(s)),s:slotsOf(s)}});
  // 先空白檢查
  await p.click('#b-check');
  let st=await p.evaluate(()=>({e:R(STAGES[QI]).errors,t:R(STAGES[QI]).tries}));
  if(st.e!==0||st.t!==0)ok(false,`Q${i+1} 空白提交不應計次 ${JSON.stringify(st)}`);
  if(spec.kind==='mc'){for(const a of spec.ans)await p.click(`[data-opt="${a}"]`)}
  else if(spec.kind==='bucket'){
    const cnt={};
    for(const [id,bk] of spec.ans){if(spec.pre.length&&await p.evaluate(([id])=>Object.keys(STAGES[QI].pre||{}).includes(id),[id]))continue;
      await p.click(`[data-card="${id}"]`);
      const k=cnt[bk]=(cnt[bk]||0);
      // 找第一個空格
      const slot=await p.evaluate(([bk])=>{const pre=Object.values(preMap(STAGES[QI]));const d=D(STAGES[QI]);const bu=STAGES[QI].buckets.find(x=>x.id===bk);for(let i=0;i<bu.cap;i++){const sid=bk+'_'+i;if(!d.place[sid]&&!preMap(STAGES[QI])[sid])return sid}},[bk]);
      await p.click(`[data-slot="${slot}"]`);}
  }else{
    // label/order: 用拖放做一半、點選做一半
    let j=0;for(const [sl,card] of Object.entries(spec.ans)){
      if(j%2===0){await p.click(`[data-card="${card}"]`);await p.click(`[data-slot="${sl}"]`)}
      else{await p.dragAndDrop(`[data-card="${card}"]`,`[data-slot="${sl}"]`)}
      j++}
  }
  await p.click('#b-check');await p.waitForTimeout(80);
  const r=await p.evaluate(()=>({passed:R(STAGES[QI]).passed,rev:R(STAGES[QI]).revealed,e:R(STAGES[QI]).errors,fb:document.getElementById('qfb').textContent.slice(0,40)}));
  ok(r.passed&&!r.rev&&r.e===0,`Q${i+1} ${spec.kind} UI 答對 ${JSON.stringify(r)}`);
 }
 // 診斷
 await p.evaluate(()=>navigate('done'));await p.waitForTimeout(100);
 ok((await p.textContent('#done')).includes('17')&&true,'診斷頁可開');
 // reload 保存
 await p.reload();await p.waitForTimeout(300);
 const kept=await p.evaluate(()=>STAGES.filter(s=>R(s).passed).length);ok(kept===n,`重載後通關保留 ${kept}/${n}`);
 // 揭露測試：清除後Q3(單選) 連錯5次
 await p.evaluate(()=>{ST=INITIAL();save()});await p.reload();await p.waitForTimeout(200);
 await p.evaluate(()=>navigate('play',1));
 for(let k=0;k<5;k++){await p.click('[data-opt="0"]');await p.click('#b-check');if(k<4){const e=await p.evaluate(()=>R(STAGES[1]).round);ok(e===k+1,`錯誤計數 ${k+1} -> ${e}`)}}
 const rv=await p.evaluate(()=>({p:R(STAGES[1]).passed,r:R(STAGES[1]).revealed,pick:D(STAGES[1]).pick}));
 ok(rv.p&&rv.r,'5次錯誤後揭露 '+JSON.stringify(rv));
 // 重設 label 題:Q3(L1) 放錯→重設
 await p.evaluate(()=>navigate('play',2));
 await p.click('[data-card="s2"]');await p.click('[data-slot="s1"]');
 await p.click('[data-card="s1"]');await p.click('[data-slot="s2"]');await p.click('[data-card="x1"]');await p.click('[data-slot="s3"]');await p.click('[data-card="s4"]');await p.click('[data-slot="s4"]');
 await p.click('#b-check');
 const bad=await p.evaluate(()=>({bad:D(STAGES[2]).bad,e:R(STAGES[2]).errors}));ok(bad.bad.length===3&&bad.e===1,'答錯標示 '+JSON.stringify(bad));
 await p.click('[data-slot="s1"]');const bad2=await p.evaluate(()=>D(STAGES[2]).bad.length);ok(bad2===0,'修改後清除錯誤標記');
 await p.click('#b-reset');const rs=await p.evaluate(()=>({pl:Object.keys(D(STAGES[2]).place).length,round:R(STAGES[2]).round,err:R(STAGES[2]).errors}));ok(rs.pl===0&&rs.round===0&&rs.err===1,'重設後本輪歸零、累計保留 '+JSON.stringify(rs));
 // 放大圖
 await p.click('#zoombtn');await p.waitForSelector('dialog[open]');ok(true,'放大 dialog 開啟');await p.keyboard.press('Escape');await p.waitForTimeout(100);ok(await p.evaluate(()=>!document.querySelector('dialog')),'Esc 關閉 dialog');
 // 全螢幕
 await p.evaluate(()=>navigate('learn',2));await p.click('#l-full');await p.waitForTimeout(300);
 const fs=await p.evaluate(()=>!!document.fullscreenElement);ok(true,'全螢幕(原生:'+fs+')');if(fs){await p.evaluate(()=>document.exitFullscreen());await p.waitForTimeout(300);ok(await p.evaluate(()=>document.getElementById('l-full').textContent==='全螢幕播放'),'退出後按鈕文字還原')}
 // 簡報
 await p.evaluate(()=>navigate('show'));await p.click('#sh-next');await p.click('#sh-next');
 ok((await p.textContent('#sh-pos')).includes('3'),'簡報翻頁 '+await p.textContent('#sh-pos'));
 await p.click('#sh-play');await p.evaluate(()=>navigate('intro'));ok(await p.evaluate(()=>SPLAY===null),'離開簡報停止播放');
 // 影片
 await p.evaluate(()=>navigate('video'));ok(await p.evaluate(()=>!!document.querySelector('#vwrap iframe')),'影片頁 iframe');
 await p.evaluate(()=>navigate('intro'));ok(await p.evaluate(()=>!document.querySelector('#vwrap iframe')),'離開影片清空 iframe');
 // Aa / 深色
 await p.click('#t-font');ok(await p.evaluate(()=>parseFloat(getComputedStyle(document.documentElement).fontSize)>17),'Aa 放大');
 await p.click('#t-theme');ok(await p.evaluate(()=>document.documentElement.dataset.theme==='dark'),'深色模式');
 await p.screenshot({path:'shots/dark_home.png'});
 await p.evaluate(()=>navigate('play',0));await p.waitForTimeout(150);await p.screenshot({path:'shots/dark_q1.png'});
 console.log(log.join('\n'));console.log('pageerrors:',errs);await b.close();
})();
