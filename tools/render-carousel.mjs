#!/usr/bin/env node
// Render a carousel to PNGs from a post's carousel.json — local, deterministic, on-brand.
// Usage:  node tools/render-carousel.mjs content/<year>/<date>-<slug>
// Reads:  <postdir>/carousel.json     Writes: <postdir>/carousel-01.png ... NN.png
//
// carousel.json shape:
// {
//   "size": [1080, 1350],
//   "brand": { "navy":"#161a45","cream":"#F4EFE3","red":"#eb2027",
//              "titleFont":"Cormorant Garamond","bodyFont":"Lato",
//              "handle":"@mzsnetworks","url":"mzsnetworks.com" },
//   "slides": [
//     {"type":"cover","title":"NetOps vs\nNetDevOps is\nthe *wrong question*","body":"...","motif":"doors"},
//     {"type":"body","title":"...","body":"...","motif":"cases|stairs|none"},
//     {"type":"data","title":"The data answers it","rows":[{"num":"25%","label":"..."}],"source":"Gartner"},
//     {"type":"triad","title":"...","steps":["The CLI made us operators.","...","AI makes us *judges*."]},
//     {"type":"cta","title":"...","body":"Follow *@mzsnetworks* ..."}
//   ]
// }
// Accent: wrap text in *asterisks* to color it red (italic in titles).

import { mkdirSync, writeFileSync, readFileSync, rmSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, resolve } from 'node:path';

const postdir = process.argv[2];
if (!postdir) { console.error('usage: node tools/render-carousel.mjs <postdir>'); process.exit(1); }
const cfg = JSON.parse(readFileSync(join(postdir, 'carousel.json'), 'utf8'));

const B = { navy:'#161a45', cream:'#F4EFE3', red:'#eb2027',
            titleFont:'Cormorant Garamond', bodyFont:'Lato',
            handle:'@mzsnetworks', url:'', ...(cfg.brand||{}) };
const [W, H] = cfg.size || [1080, 1350];
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
// *accent* -> red span; \n -> <br>.  italic=true for serif titles.
const rich = (s, italic) => esc(s)
  .replace(/\*([^*]+)\*/g, (_,t)=>`<span style="color:${B.red}${italic?';font-style:italic':''}">${t}</span>`)
  .replace(/\n/g,'<br>');

const ic = {
  doc:`<svg viewBox="0 0 24 24" fill="none" stroke="${B.cream}" stroke-width="1.4"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9.5 13.5 8 15l1.5 1.5M14.5 13.5 16 15l-1.5 1.5"/></svg>`,
  cpu:`<svg viewBox="0 0 24 24" fill="none" stroke="${B.cream}" stroke-width="1.4"><rect x="7" y="7" width="10" height="10" rx="2"/><path d="M10 2v3M14 2v3M10 19v3M14 19v3M2 10h3M2 14h3M19 10h3M19 14h3"/></svg>`,
  chart:`<svg viewBox="0 0 24 24" fill="none" stroke="${B.cream}" stroke-width="1.4"><path d="M4 19h16"/><path d="M6 16l4-5 3 3 5-7"/><path d="M18 5h3v3"/></svg>`,
  term:`<svg viewBox="0 0 24 24" fill="none" stroke="${B.cream}" stroke-width="1.4"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 2.5L7 14M12.5 14h4"/></svg>`,
  code:`<svg viewBox="0 0 24 24" fill="none" stroke="${B.cream}" stroke-width="1.4"><path d="M8.5 8 5 12l3.5 4M15.5 8 19 12l-3.5 4"/></svg>`,
  scale:`<svg viewBox="0 0 24 24" fill="none" stroke="${B.cream}" stroke-width="1.4"><path d="M12 4v16M6 20h12M4 8l4-2 4 2M4 8l2 5a2.5 2.5 0 0 0 4 0l2-5M20 8l-4-2-4 2M20 8l-2 5a2.5 2.5 0 0 1-4 0"/></svg>`,
};
const dataIcons = [ic.doc, ic.cpu, ic.chart];
const triadIcons = [ic.term, ic.code, ic.scale];

const motifs = {
  doors:`<div style="position:absolute;left:0;right:0;bottom:150px;height:340px;display:flex;justify-content:center;gap:60px;align-items:flex-end">
    <div style="width:150px;height:280px;background:linear-gradient(180deg,#1d2aed,#0c1233);border:3px solid #2b3a8f;box-shadow:0 0 60px 8px rgba(60,110,255,.45);transform:perspective(600px) rotateY(20deg)"></div>
    <div style="width:150px;height:300px;background:linear-gradient(180deg,${B.red},#7c0f14);border:3px solid #ff5a5f;box-shadow:0 0 70px 10px rgba(235,32,39,.5);transform:perspective(600px) rotateY(-20deg)"></div></div>`,
  cases:`<div style="position:absolute;right:120px;bottom:150px;display:flex;gap:34px;align-items:flex-end">
    <div style="width:150px;height:200px;background:linear-gradient(180deg,#27347a,${B.navy});border-radius:18px;border:2px solid #3a4aa0"></div>
    <div style="width:170px;height:230px;background:linear-gradient(180deg,${B.red},#8d1318);border-radius:18px;border:2px solid #ff5a5f"></div></div>`,
  stairs:`<div style="position:absolute;right:100px;bottom:150px;display:flex;align-items:flex-end">
    ${[0,1,2,3].map(i=>`<div style="width:74px;height:${60+i*52}px;border:2px solid rgba(244,239,227,.4);border-bottom:none"></div>`).join('')}
    <div style="position:absolute;right:30px;bottom:30px;color:${B.red};font-size:60px">&#8593;</div></div>`,
  none:'',
};

function content(s) {
  if (s.type === 'data') {
    const rows = s.rows.map((r,i)=>`<div style="display:flex;align-items:center;gap:34px;padding:26px 0;border-bottom:1px solid rgba(244,239,227,.16)">
      <div style="flex:0 0 54px">${dataIcons[i%3]}</div>
      <div><span style="font-family:'${B.titleFont}',Georgia,serif;font-weight:500;font-size:72px;color:${B.red};line-height:1">${rich(r.num,false)}</span>
      <span style="font-size:30px;color:${B.cream};margin-left:16px">${rich(r.label,false)}</span></div></div>`).join('');
    return `<div class="title" style="font-size:76px">${rich(s.title,true)}</div><div class="rule"></div>
      <div style="margin-top:6px">${rows}</div>
      ${s.source?`<div style="margin-top:24px;font-size:24px;color:rgba(244,239,227,.55)">Source: ${esc(s.source)}</div>`:''}`;
  }
  if (s.type === 'triad') {
    const steps = s.steps.map((t,i)=>`<div style="display:flex;align-items:center;gap:30px;margin:22px 0">
      <div style="flex:0 0 78px;height:78px;border:2px solid rgba(244,239,227,.45);border-radius:50%;display:flex;align-items:center;justify-content:center">${triadIcons[i%3]}</div>
      <div style="font-size:34px;color:${B.cream}">${rich(t,false)}</div></div>`).join('');
    return `<div class="title" style="font-size:64px">${rich(s.title,true)}</div><div class="rule"></div><div style="margin-top:6px">${steps}</div>`;
  }
  if (s.type === 'cta') {
    return `<div style="background:${B.red};padding:46px 40px;border-radius:6px;margin-right:30px">
      <div class="title" style="font-size:62px;color:${B.cream}">${rich(s.title,true)}</div></div>
      <div class="rule"></div>
      <div class="body" style="font-size:34px">${rich(s.body,false)}</div>`;
  }
  // cover / body
  const size = s.type === 'cover' ? 82 : 78;
  return `<div class="title" style="font-size:${size}px">${rich(s.title,true)}</div><div class="rule"></div>
    <div class="body">${rich(s.body,false)}</div>${motifs[s.motif]||''}`;
}

const page = (s, n) => {
  const center = s.type !== 'cover';           // cover top-aligned (motif sits below); others vertically centered
  const padBottom = (motifs[s.motif] && s.motif!=='none') ? 520 : 96;
  return `<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<style>
 *{margin:0;padding:0;box-sizing:border-box}
 html,body{width:${W}px;height:${H}px}
 .slide{width:${W}px;height:${H}px;background:${B.navy};color:${B.cream};position:relative;
   padding:96px 90px ${padBottom}px;overflow:hidden;
   font-family:'${B.bodyFont}',-apple-system,Helvetica,sans-serif;
   display:flex;flex-direction:column;${center?'justify-content:center':''}}
 .title{font-family:'${B.titleFont}',Georgia,serif;font-weight:500;color:${B.cream};line-height:1.05;letter-spacing:.5px}
 .rule{width:84px;height:3px;background:${B.red};margin:30px 0}
 .body{font-size:34px;line-height:1.55;color:${B.cream};max-width:80%}
 .mark{position:absolute;left:90px;bottom:78px;font-size:26px;color:rgba(244,239,227,.62);letter-spacing:.5px;line-height:1.3}
 .mark small{color:rgba(244,239,227,.5);font-size:22px}
 .num{position:absolute;right:90px;bottom:74px;font-family:'${B.bodyFont}',sans-serif;font-weight:400;font-size:34px;color:rgba(244,239,227,.5);font-variant-numeric:tabular-nums}
 svg{width:54px;height:54px}
</style></head><body><div class="slide">
 ${content(s)}
 <div class="mark">${esc(B.handle)}${s.type==='cta'&&B.url?`<br><small>${esc(B.url)}</small>`:''}</div>
 <div class="num">${n}</div>
</div></body></html>`;
};

const tmp = join(postdir, '.carousel-html');
mkdirSync(tmp, { recursive: true });
cfg.slides.forEach((s,i)=>{
  const n = String(i+1).padStart(2,'0');
  const html = join(tmp, `slide-${n}.html`);
  writeFileSync(html, page(s, n));
  execFileSync(CHROME, ['--headless=new','--disable-gpu','--hide-scrollbars','--no-sandbox',
    '--force-device-scale-factor=2', `--window-size=${W},${H}`,
    `--screenshot=${resolve(join(postdir, `carousel-${n}.png`))}`, `file://${resolve(html)}`],
    { stdio: 'ignore' });
  console.log(`rendered carousel-${n}.png`);
});
rmSync(tmp, { recursive: true, force: true });
console.log(`done — ${cfg.slides.length} slides in ${postdir}`);
