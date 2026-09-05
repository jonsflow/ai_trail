#!/usr/bin/env node
/*
 * Balance and integrity simulation for aitrail.html.
 *
 *   node tools/simulate.js
 *
 * No build step, no test framework. This pulls the <script> block straight out of
 * aitrail.html, runs it against a stub DOM, and plays the game thousands of times
 * under different strategies.
 *
 * It answers three questions:
 *   1. Can a careful, green, debt-aware player actually reach THE LONG FUTURE?
 *      If not, the game argues the opposite of what it means to.
 *   2. Does every shortcut fail in its own characteristic way?
 *   3. Are all 12 endings reachable, with no dead ends and no out-of-range stats?
 *
 * Run this before committing any change to pace yields, costs, revenue, interest,
 * or the ending thresholds. The first version of this game was unwinnable - every
 * strategy including the careful one went bankrupt 200/200 - and nothing but a
 * simulation catches that.
 */

const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const html = fs.readFileSync(path.join(root, "aitrail.html"), "utf8");
const GAME = html.slice(html.indexOf("<script>") + 8, html.lastIndexOf("</script>"));
const DRIVER = fs.readFileSync(path.join(__dirname, "strategies.js"), "utf8");

/* ---- stub DOM: enough for the game to run headlessly ---- */
function fakeEl(){
  const el={dataset:{},children:[],innerHTML:"",textContent:"",className:"",style:{},
    classList:{add:()=>{},remove:()=>{},toggle:()=>{}},
    appendChild:c=>el.children.push(c), querySelectorAll:()=>[], addEventListener:()=>{},
    scrollTop:0, scrollHeight:0};
  return el;
}
const reg={};
global.document={createElement:()=>fakeEl(), getElementById:id=>(reg[id]||=fakeEl()),
  querySelector:()=>fakeEl(), querySelectorAll:()=>[], addEventListener:()=>{}};

/* The game and the driver must be evaluated TOGETHER: `let` bindings inside an
   eval do not escape into module scope, so a separate eval could not see `S`,
   `turn` or `ended`. One eval, one shared scope. */
eval(GAME + "\n" + DRIVER);
