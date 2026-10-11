// 截圖：node shots.cjs <html> <out> learn:0,3 play:1,2
const {chromium}=require('/opt/node-tools/node_modules/playwright');
const [,,html,out,...specs]=process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1366,height:768}});
await p.goto('file://'+html);await p.waitForTimeout(300);require('fs').mkdirSync(out,{recursive:true});
await p.screenshot({path:`${out}/home.png`});
for(const sp of specs){const [pg,list]=sp.split(':');for(const i of list.split(',')){await p.evaluate(([pg,i])=>navigate(pg,+i),[pg,i]);await p.waitForTimeout(150);
 if(pg==='play'&&process.env.FILL){await p.evaluate(()=>{const s=STAGES[QI];if(s.kind==='label'){D(s).place=answerMap(s);renderQ()}});await p.waitForTimeout(100)}
 await p.screenshot({path:`${out}/${pg}${+i+1}.png`})}}
await b.close()})();
