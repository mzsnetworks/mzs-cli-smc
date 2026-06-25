#!/usr/bin/env node
// Render a single tall infographic to PNG from a post's infographic.json.
// Usage:  node tools/render-infographic.mjs content/<year>/<date>-<slug>
// Reads:  <postdir>/infographic.json     Writes: <postdir>/infographic.png
//
// infographic.json shape:
// {
//   "size": [1080, 1920],
//   "brand": { navy,cream,red,titleFont,bodyFont,handle,url },   // from rules/VOICE.md
//   "title": "Plug-and-Play Wi-Fi *Is a Myth*",
//   "subtitle": "You don't plug it in. You engineer it.",
//   "sections": [
//     {"type":"compare","left":{"title":"The demo","items":["..."]},"right":{"title":"Monday morning","items":["..."]}},
//     {"type":"list","title":"What 'slow Wi-Fi' really is","items":["coverage holes","co-channel interference","sticky clients"]},
//     {"type":"stats","title":"...","rows":[{"num":"3","label":"non-overlapping 2.4GHz channels"}]},
//     {"type":"steps","title":"...","steps":[{"title":"Survey","body":"..."}]},
//     {"type":"heading","title":"...","body":"..."}
//   ],
//   "footer": "Wireless fails politely — never on your dashboard.",   // optional closing line
//   "source": "Gartner"                                              // optional
// }
// Accent: wrap text in *asterisks* to color it red (italic in headings). \n = line break.

import { mkdirSync, writeFileSync, readFileSync, rmSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, resolve } from 'node:path';

const postdir = process.argv[2];
if (!postdir) { console.error('usage: node tools/render-infographic.mjs <postdir>'); process.exit(1); }
const cfg = JSON.parse(readFileSync(join(postdir, 'infographic.json'), 'utf8'));

const B = { navy:'#161a45', cream:'#F4EFE3', red:'#eb2027',
            titleFont:'Cormorant Garamond', bodyFont:'Lato',
            handle:'@mzsnetworks', url:'', ...(cfg.brand||{}) };
const [W, H] = cfg.size || [1080, 1920];
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const rich = (s, italic) => esc(s)
  .replace(/\*([^*]+)\*/g, (_,t)=>`<span style="color:${B.red}${italic?';font-style:italic':''}">${t}</span>`)
  .replace(/\n/g,'<br>');

const tick = `<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="${B.red}" stroke-width="2"><path d="M5 12l4 4 10-11"/></svg>`;
const heading = (t, size=46) => `<div class="h" style="font-size:${size}px">${rich(t,true)}</div>`;

function section(s) {
  if (s.type === 'heading')
    return `<div class="sec">${s.title?heading(s.title):''}${s.body?`<div class="body">${rich(s.body,false)}</div>`:''}</div>`;

  if (s.type === 'list')
    return `<div class="sec">${s.title?heading(s.title):''}
      <div style="margin-top:18px">${s.items.map(it=>`<div style="display:flex;gap:18px;align-items:flex-start;margin:14px 0">
        <div style="flex:0 0 26px;margin-top:6px">${tick}</div><div class="body" style="margin:0">${rich(it,false)}</div></div>`).join('')}</div></div>`;

  if (s.type === 'stats')
    return `<div class="sec">${s.title?heading(s.title):''}
      <div style="margin-top:14px">${s.rows.map(r=>`<div style="display:flex;align-items:baseline;gap:24px;padding:18px 0;border-bottom:1px solid rgba(244,239,227,.16)">
        <div style="font-family:'${B.titleFont}',serif;font-weight:500;font-size:66px;color:${B.red};line-height:1">${rich(r.num,false)}</div>
        <div class="body" style="margin:0;font-size:30px">${rich(r.label,false)}</div></div>`).join('')}</div></div>`;

  if (s.type === 'steps')
    return `<div class="sec">${s.title?heading(s.title):''}
      <div style="margin-top:14px">${s.steps.map((st,i)=>`<div style="display:flex;gap:24px;margin:20px 0">
        <div style="flex:0 0 56px;height:56px;border:2px solid ${B.red};border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'${B.titleFont}',serif;font-size:34px;color:${B.cream}">${i+1}</div>
        <div><div style="font-family:'${B.titleFont}',serif;font-size:38px;color:${B.cream};line-height:1.1">${rich(st.title,false)}</div>
        ${st.body?`<div class="body" style="margin:6px 0 0;font-size:28px">${rich(st.body,false)}</div>`:''}</div></div>`).join('')}</div></div>`;

  if (s.type === 'compare') {
    const col = (c, accent) => `<div style="flex:1;background:rgba(255,255,255,.04);border-top:3px solid ${accent?B.red:'rgba(244,239,227,.4)'};padding:28px 26px">
      <div style="font-family:'${B.titleFont}',serif;font-size:36px;color:${accent?B.red:B.cream};margin-bottom:14px">${rich(c.title,false)}</div>
      ${c.items.map(it=>`<div class="body" style="margin:10px 0;font-size:28px">${rich(it,false)}</div>`).join('')}</div>`;
    return `<div class="sec">${s.title?heading(s.title):''}
      <div style="display:flex;gap:24px;margin-top:18px">${col(s.left,false)}${col(s.right,true)}</div></div>`;
  }
  return '';
}

const html = `<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<style>
 *{margin:0;padding:0;box-sizing:border-box}
 html,body{width:${W}px;height:${H}px}
 .page{width:${W}px;height:${H}px;background:${B.navy};color:${B.cream};position:relative;
   padding:90px 80px 150px;overflow:hidden;font-family:'${B.bodyFont}',-apple-system,Helvetica,sans-serif;
   display:flex;flex-direction:column}
 .title{font-family:'${B.titleFont}',Georgia,serif;font-weight:500;color:${B.cream};font-size:86px;line-height:1.04;letter-spacing:.5px}
 .subtitle{font-size:34px;color:rgba(244,239,227,.85);margin-top:18px;max-width:88%}
 .toprule{width:96px;height:4px;background:${B.red};margin:26px 0}
 .h{font-family:'${B.titleFont}',serif;font-weight:500;color:${B.cream};line-height:1.08}
 .body{font-size:30px;line-height:1.5;color:${B.cream}}
 .sec{margin-top:46px}
 .footerline{margin-top:46px;font-family:'${B.titleFont}',serif;font-size:40px;font-style:italic;color:${B.cream};line-height:1.2}
 .mark{position:absolute;left:80px;bottom:64px;font-size:26px;color:rgba(244,239,227,.62)}
 .src{position:absolute;right:80px;bottom:66px;font-size:24px;color:rgba(244,239,227,.5)}
</style></head><body><div class="page">
 <div class="title">${rich(cfg.title,true)}</div>
 ${cfg.subtitle?`<div class="subtitle">${rich(cfg.subtitle,false)}</div>`:''}
 <div class="toprule"></div>
 ${(cfg.sections||[]).map(section).join('')}
 ${cfg.footer?`<div class="footerline">${rich(cfg.footer,false)}</div>`:''}
 <div class="mark">${esc(B.handle)}${B.url?` &middot; ${esc(B.url)}`:''}</div>
 ${cfg.source?`<div class="src">Source: ${esc(cfg.source)}</div>`:''}
</div></body></html>`;

const tmp = join(postdir, '.carousel-html');
mkdirSync(tmp, { recursive: true });
const f = join(tmp, 'infographic.html');
writeFileSync(f, html);
execFileSync(CHROME, ['--headless=new','--disable-gpu','--hide-scrollbars','--no-sandbox',
  '--force-device-scale-factor=2', `--window-size=${W},${H}`,
  `--screenshot=${resolve(join(postdir, 'infographic.png'))}`, `file://${resolve(f)}`],
  { stdio: 'ignore' });
rmSync(tmp, { recursive: true, force: true });
console.log(`rendered infographic.png (${W}x${H} @2x) in ${postdir}`);
