/*
 * Strategies and checks for tools/simulate.js.
 *
 * This file is NOT require()d - simulate.js reads it as text and evaluates it in
 * the same scope as the game source, so it can see the game's own `let` bindings
 * (S, turn, ended, LEVELS...) directly. Keep it dependency-free.
 *
 * Each strategy is a policy over the choice list the game is currently offering.
 * Choices carry a `stat` tag on the money screen ("water", "grid", "trust",
 * "alignment", "team", "debt", "none"), which is how a policy expresses intent
 * without matching on button text.
 */
/* ---- drive the game headlessly ---- */
let CURRENT=[], TITLE="";
choices = l => { CURRENT=l; };
show = (t,b,c) => { TITLE=t; };
render = () => {}; log = () => {};

const isPace   = () => CURRENT.some(c => /pace$/i.test(c.label));
const isInvest = () => CURRENT.some(c => c.stat === "debt");
const byStat   = st => CURRENT.find(c => c.stat === st);
const notStat  = sts => CURRENT.find(c => c.stat && !sts.includes(c.stat) && c.stat !== "none" && c.stat !== "debt");
const byLabel  = re => CURRENT.find(c => re.test(c.label));

const POLICIES = {
  steward(){
    if(isPace()) return CURRENT[Math.min(S.water,S.grid,S.trust,S.alignment,S.team) < 45 ? 0 : 1];
    if(isInvest()) return (S.capital < 90 && S.debt < 400) ? byStat("debt") : CURRENT[0];
    return CURRENT[0];
  },
  prudent(){
    if(isPace()){
      const weak = Math.min(S.water,S.grid,S.trust,S.alignment,S.team);
      if(weak < 45 || S.capital < 120) return CURRENT[0];
      return CURRENT[1];
    }
    if(isInvest()) return S.capital < 90 ? byStat("none") : CURRENT[0];
    const decline = byLabel(/^Turn it down|^Pass\./);
    return decline || CURRENT[0];
  },
  reckless(){
    if(isPace()) return CURRENT[2];
    if(isInvest()) return S.capital < 150 ? byStat("debt") : byStat("none");
    return CURRENT[CURRENT.length-1];
  },
  speedrun(){
    if(isPace()) return CURRENT[2];
    if(isInvest()) return byStat("none");
    return CURRENT[CURRENT.length-1];
  },
  safetyOnly(){
    if(isPace()) return CURRENT[0];
    if(isInvest()) return byStat("alignment") || byStat("none");
    return CURRENT[0];
  },
  debtLover(){
    if(isPace()) return CURRENT[1];
    if(isInvest()) return byStat("debt");
    return CURRENT[0];
  },
  greenOnly(){
    if(isPace()) return CURRENT[0];
    if(isInvest()) return S.capital < 80 ? byStat("none") : (byStat("water") || byStat("grid") || byStat("none"));
    return CURRENT[0];
  },
  racer(){
    if(isPace()) return CURRENT[2];
    if(isInvest()){
      if(S.capital < 80) return byStat("debt");
      return byStat("trust") || notStat(["alignment"]) || byStat("none");
    }
    return CURRENT[CURRENT.length-1];
  },
  grinder(){
    if(isPace()) return CURRENT[2];
    if(isInvest()){
      if(S.capital < 80) return byStat("debt");
      return notStat(["team"]) || byStat("none");
    }
    return CURRENT[CURRENT.length-1];
  },
  ethicsOnly(){
    if(isPace()) return CURRENT[S.capital < 120 ? 0 : 1];
    if(isInvest()){
      if(S.capital < 80) return byStat("none");
      return byStat("alignment") || byStat("trust") || byStat("team") || byStat("none");
    }
    return CURRENT[0];
  },
  greenRacer(){
    if(isPace()) return (S.water < 45 || S.grid < 45) ? CURRENT[0] : (S.capital < 140 ? CURRENT[0] : CURRENT[1]);
    if(isInvest()){
      if(S.capital < 80) return byStat("none");
      return byStat("water") || byStat("grid") || byStat("none");
    }
    return CURRENT[CURRENT.length-1];
  },
  // props up everything except the people
  burnout(){
    if(isPace()) return CURRENT[2];
    if(isInvest()){
      if(S.capital < 90) return byStat("debt");
      if(S.trust < 60) return byStat("trust") || notStat(["team"]);
      if(S.water < 55) return byStat("water") || notStat(["team"]);
      if(S.grid  < 55) return byStat("grid")  || notStat(["team"]);
      return notStat(["team"]) || byStat("none");
    }
    const hard = byLabel(/Counter-offer|Enforce the agreement|Let them go|push to the deadline/);
    return hard || CURRENT[0];
  },
  random(){ return CURRENT[Math.floor(Math.random()*CURRENT.length)]; }
};

function playOne(policy, collect){
  newGame();
  let guard = 0;
  while(!ended && guard++ < 500){
    if(collect) collect(TITLE, CURRENT);
    const pick = POLICIES[policy]();
    if(!pick) return {id:"NONE"};
    pick.go();
  }
  const html = reg.story.innerHTML;
  return {id: (html.match(/ENDING (\d+) OF/) || [])[1] || "NONE",
          title: (html.match(/<h2[^>]*>([^<]+)<\/h2>/) || [])[1] || "LOOPED"};
}

/* ---------- 1. no repeated questions in a playthrough ---------- */
console.log("=== question variety in a single playthrough ===");
let titles = [], slates = [];
playOne("prudent", (t, c) => {
  titles.push(t);
  if(c.some(x => x.stat === "debt")) slates.push(c.map(x => x.label).join("|"));
});
const events = titles.filter(t => !/^LEG /.test(t));
const dupEvents = events.filter((t,i) => events.indexOf(t) !== i);
const legHeads  = titles.filter(t => /how hard do you push/.test(t));
console.log("  prompts shown:", titles.length);
console.log("  event/landmark screens:", events.length,
            "| repeated:", dupEvents.length, dupEvents.length ? "-> " + [...new Set(dupEvents)] : "");
console.log("  pace screens:", legHeads.length, "| unique:", new Set(legHeads).size);
console.log("  money slates:", slates.length, "| unique:", new Set(slates).size);
console.log("\n  first six money slates:");
slates.slice(0,6).forEach((s,i) => console.log("   L" + (i+1) + ": " + s.split("|").slice(0,3).join("  /  ")));

/* ---------- 2. balance unchanged ---------- */
console.log("\n=== balance ===");
const seen = {};
for(const pol of Object.keys(POLICIES)){
  const t = {}; const N = pol === "random" ? 300 : 150; let golden = 0;
  for(let i=0;i<N;i++){
    const r = playOne(pol);
    seen[r.id] = (seen[r.id]||0)+1;
    t[r.id + ". " + r.title] = (t[r.id + ". " + r.title]||0)+1;
    if(r.id === "12") golden++;
  }
  const top = Object.entries(t).sort((a,b)=>b[1]-a[1])[0];
  console.log(`  ${pol.padEnd(12)} ${top[0]} (${Math.round(top[1]/N*100)}%)` +
              (golden ? `  [LONG FUTURE ${Math.round(golden/N*100)}%]` : ""));
}
const missing = [];
for(let i=1;i<=12;i++) if(!seen[String(i)]) missing.push(i);
console.log("  endings never reached:", missing.length ? missing.join(",") : "none");
console.log("  dead ends:", seen["NONE"] || 0);
