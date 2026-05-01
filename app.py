import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scientific Notebook", page_icon="📓", layout="wide")

st.markdown("""
<style>
header[data-testid="stHeader"]{display:none;}
footer{display:none;}
#MainMenu{display:none;}
.block-container{padding:0!important;max-width:100%!important;}
[data-testid="stAppViewContainer"]{padding:0!important;}
</style>
""", unsafe_allow_html=True)

APP = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Scientific Notebook</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css"/>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
<style>
*{box-sizing:border-box;margin:0;padding:0;}
:root{
  /* Spring Lilac palette */
  --bg:      #f3eeff;
  --sb:      #ede4fb;
  --tb:      #e4d9f7;
  --bd:      #c9b8ed;
  --tx:      #2d1b6e;
  --muted:   #7a5fa8;
  --accent:  #8b5cf6;
  --accentL: #6d3fc4;
  --hover:   #ddd0f5;
  --active:  #c9b8ed;
  --red:     #c0392b;
  --pageBar: #d8c9f2;
  --pageTxt: #3d2080;
}
html,body{margin:0;padding:0;height:100%;overflow:hidden;}
body{background:var(--bg);color:var(--tx);font-family:system-ui,-apple-system,sans-serif;}
#app{display:flex;flex-direction:column;height:100%;}

/* ── AUTH ─────────────────────────────────────── */
#auth{position:fixed;inset:0;background:linear-gradient(135deg,#e8d9ff,#f3eeff);display:flex;align-items:center;justify-content:center;z-index:9999;}
.abox{background:#fff;border:1.5px solid var(--bd);border-radius:20px;padding:44px 40px;width:410px;box-shadow:0 20px 60px rgba(139,92,246,.18);}
.alogo{font-size:32px;text-align:center;margin-bottom:6px;}
.atitle{font-size:22px;font-weight:600;text-align:center;color:var(--accentL);margin-bottom:4px;}
.asub{font-size:13px;color:var(--muted);text-align:center;margin-bottom:26px;}
.atabs{display:flex;background:var(--hover);border-radius:10px;padding:3px;margin-bottom:22px;}
.atab{flex:1;padding:9px;text-align:center;border-radius:8px;cursor:pointer;font-size:13px;color:var(--muted);font-weight:500;transition:all .15s;user-select:none;}
.atab.on{background:var(--accent);color:#fff;}
.afield{margin-bottom:14px;}
.afield label{display:block;font-size:11px;color:var(--muted);letter-spacing:.7px;font-weight:600;margin-bottom:6px;}
.afield input{width:100%;background:var(--hover);border:1.5px solid var(--bd);border-radius:9px;padding:10px 14px;color:var(--tx);font-size:14px;font-family:inherit;outline:none;transition:border-color .15s;}
.afield input:focus{border-color:var(--accent);}
.aerr{font-size:12px;color:var(--red);min-height:18px;margin-bottom:12px;text-align:center;font-weight:500;}
.abtn{width:100%;padding:12px;background:var(--accent);border:none;border-radius:9px;color:#fff;font-size:14px;font-family:inherit;font-weight:600;cursor:pointer;transition:opacity .15s;letter-spacing:.3px;}
.abtn:hover{opacity:.87;}
#ulist{margin-bottom:16px;}
.ulabel{font-size:11px;color:var(--muted);letter-spacing:.5px;font-weight:600;margin-bottom:8px;}
.uchip{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:9px;background:var(--hover);border:1.5px solid var(--bd);cursor:pointer;margin-bottom:6px;transition:border-color .15s;}
.uchip:hover{border-color:var(--accent);}
.uav{width:34px;height:34px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;flex-shrink:0;}
.uname{font-size:14px;flex:1;color:var(--tx);font-weight:500;}
.uhint{font-size:11px;color:var(--muted);}

/* ── TOP TOOLBAR ──────────────────────────────── */
#toolbar{display:flex;align-items:center;gap:3px;background:var(--tb);border-bottom:2px solid var(--bd);padding:0 10px;height:48px;flex-shrink:0;overflow-x:auto;overflow-y:hidden;}
#toolbar::-webkit-scrollbar{height:3px;}
#toolbar::-webkit-scrollbar-thumb{background:var(--bd);}
.tbdiv{width:1px;height:26px;background:var(--bd);flex-shrink:0;margin:0 5px;}
#symtabs{display:flex;gap:2px;}
.tabtn{padding:0 12px;height:32px;background:transparent;border:none;border-radius:6px;color:var(--muted);cursor:pointer;font-size:13px;font-family:inherit;font-weight:500;white-space:nowrap;transition:all .15s;}
.tabtn.on{background:var(--accent);color:#fff;}
.tabtn:hover:not(.on){background:var(--hover);color:var(--tx);}
#symarea{display:flex;gap:3px;align-items:center;flex-wrap:nowrap;}
.sybtn{width:31px;height:31px;background:var(--bg);border:1.5px solid var(--bd);border-radius:5px;color:var(--accentL);cursor:pointer;font-size:15px;display:flex;align-items:center;justify-content:center;font-family:Georgia,serif;flex-shrink:0;font-weight:600;transition:all .1s;}
.sybtn:hover{background:var(--active);border-color:var(--accent);}
.fmbtn{padding:2px 11px;height:28px;background:var(--bg);border:1.5px solid var(--bd);border-radius:6px;color:var(--accentL);cursor:pointer;font-size:12px;font-family:inherit;font-weight:600;white-space:nowrap;transition:all .15s;}
.fmbtn:hover{background:var(--hover);border-color:var(--accent);}
.fmbtn.on{background:var(--accent);color:#fff;border-color:var(--accent);}
.fmbtn.red{color:var(--red);border-color:var(--red);}
#rgroup{margin-left:auto;display:flex;align-items:center;gap:8px;}
.ibtn{width:34px;height:34px;padding:0;background:var(--bg);border:1.5px solid var(--bd);border-radius:6px;color:var(--accentL);cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center;font-weight:700;transition:all .15s;}
.ibtn:hover{background:var(--hover);border-color:var(--accent);}
.mwrap{position:relative;}
#mpop{position:absolute;right:0;top:calc(100% + 7px);background:#fff;border:1.5px solid var(--bd);border-radius:13px;padding:6px;z-index:1000;min-width:210px;box-shadow:0 12px 40px rgba(139,92,246,.18);display:none;}
.mlabel{font-size:10px;color:var(--muted);padding:4px 10px 6px;letter-spacing:1px;font-weight:700;}
.mitem{display:flex;align-items:center;padding:9px 13px;border-radius:8px;cursor:pointer;font-size:13px;color:var(--tx);font-weight:500;transition:background .1s;}
.mitem:hover{background:var(--hover);}
.mitem.red{color:var(--red);}
.mdivide{height:1px;background:var(--bd);margin:5px 0;}
#drawpanel{display:none;align-items:center;gap:5px;padding-left:8px;margin-left:4px;border-left:2px solid var(--bd);}
.pdot{width:17px;height:17px;border-radius:50%;cursor:pointer;border:2.5px solid transparent;flex-shrink:0;transition:border-color .1s;}
.dlabel{font-size:11px;color:var(--muted);font-weight:600;}

/* ── SEARCH BAR ───────────────────────────────── */
#sbar{display:none;align-items:center;gap:8px;background:var(--tb);border-bottom:2px solid var(--bd);padding:8px 16px;position:relative;flex-shrink:0;}
#sinp{flex:1;background:#fff;border:1.5px solid var(--bd);border-radius:7px;padding:7px 13px;color:var(--tx);font-size:14px;font-family:inherit;outline:none;font-weight:500;}
#sinp:focus{border-color:var(--accent);}
#sres{display:none;position:absolute;top:100%;left:16px;right:16px;background:#fff;border:1.5px solid var(--bd);border-radius:10px;z-index:500;max-height:220px;overflow-y:auto;box-shadow:0 8px 30px rgba(139,92,246,.15);}
.sitem{padding:10px 16px;cursor:pointer;border-bottom:1px solid var(--bd);}
.sitem:last-child{border-bottom:none;}
.sitem:hover{background:var(--hover);}
.snm{font-size:13px;color:var(--tx);font-weight:500;}
.ssb{font-size:11px;color:var(--muted);margin-top:2px;font-weight:500;}

/* ── MAIN LAYOUT ──────────────────────────────── */
#main{display:flex;flex:1;overflow:hidden;min-height:0;}

/* ── SIDEBAR ──────────────────────────────────── */
#sidebar{width:235px;background:var(--sb);border-right:2px solid var(--bd);display:flex;flex-direction:column;overflow:hidden;flex-shrink:0;}
.sbhead{padding:14px 15px 10px;border-bottom:2px solid var(--bd);font-size:10px;font-weight:800;letter-spacing:1.8px;color:var(--accentL);flex-shrink:0;}
#sblist{flex:1;overflow-y:auto;padding:6px 0;min-height:0;}
#sblist::-webkit-scrollbar{width:4px;}
#sblist::-webkit-scrollbar-thumb{background:var(--bd);border-radius:2px;}
.subrow{display:flex;align-items:center;gap:8px;padding:8px 14px;cursor:pointer;border-radius:7px;margin:1px 5px;user-select:none;transition:background .1s;}
.subrow:hover{background:var(--hover);}
.sarrow{font-size:9px;color:var(--muted);width:10px;flex-shrink:0;font-weight:700;}
.sdot{width:10px;height:10px;border-radius:50%;flex-shrink:0;box-shadow:0 1px 3px rgba(0,0,0,.15);}
.sname{font-size:13px;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--tx);font-weight:600;}
.nblist{padding-left:12px;}
.nbrow{display:flex;align-items:center;gap:7px;padding:7px 12px;cursor:pointer;border-radius:7px;margin:1px 5px;font-size:13px;border-left:3px solid transparent;transition:all .1s;}
.nbrow:hover{background:var(--hover);}
.nbrow.on{background:var(--active);}
.nbico{font-size:12px;flex-shrink:0;}
.nbname{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--tx);font-weight:600;}
.addnb{display:flex;align-items:center;gap:6px;padding:6px 12px;cursor:pointer;border-radius:7px;margin:1px 5px;color:var(--muted);font-size:12px;font-weight:600;transition:color .1s;}
.addnb:hover{color:var(--accent);}
.addsub{display:flex;align-items:center;gap:7px;padding:10px 16px;cursor:pointer;color:var(--accent);font-size:13px;font-weight:700;margin-top:4px;transition:color .1s;}
.addsub:hover{color:var(--accentL);}
.ninp{width:calc(100% - 20px);margin:3px 10px;padding:6px 10px;background:#fff;border:1.5px solid var(--accent);border-radius:7px;color:var(--tx);font-size:13px;font-family:inherit;outline:none;font-weight:500;}
#sbfoot{padding:10px 14px;border-top:2px solid var(--bd);display:flex;align-items:center;gap:9px;flex-shrink:0;background:var(--hover);}
.sfav{width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0;}
.sfname{font-size:13px;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--tx);font-weight:600;}
.logbtn{font-size:11px;color:var(--muted);cursor:pointer;padding:4px 8px;border-radius:5px;background:var(--bg);border:1.5px solid var(--bd);font-family:inherit;font-weight:600;transition:color .1s;}
.logbtn:hover{color:var(--red);border-color:var(--red);}

/* ── EDITOR AREA ──────────────────────────────── */
#edarea{flex:1;display:flex;flex-direction:column;overflow:hidden;min-height:0;background:var(--bg);}
#edhdr{padding:12px 52px 10px;border-bottom:2px solid var(--bd);background:var(--sb);flex-shrink:0;display:none;}
#edbc{font-size:11px;color:var(--muted);margin-bottom:3px;font-weight:600;letter-spacing:.3px;}
#edtit{font-size:20px;font-weight:700;color:var(--accentL);}
#edwrap{flex:1;overflow:auto;position:relative;display:none;min-height:0;background:#faf7ff;}
#edwrap::-webkit-scrollbar{width:6px;}
#edwrap::-webkit-scrollbar-thumb{background:var(--bd);border-radius:3px;}
#editor{min-height:700px;padding:40px 56px;outline:none;font-size:16px;line-height:1.95;font-family:Georgia,'Times New Roman',serif;color:#1a0a4a;caret-color:var(--accent);}
#editor:empty::before{content:attr(data-ph);color:#c4b0e0;pointer-events:none;font-style:italic;}
#editor strong{font-weight:700;color:#1a0a4a;}
#editor em{font-style:italic;}
#editor code{background:#ede4fb;padding:2px 7px;border-radius:4px;font-size:14px;font-family:monospace;color:var(--accentL);font-weight:600;}
.mathnode{display:inline-block;vertical-align:middle;cursor:default;user-select:none;}
#drawcv{position:absolute;top:0;left:0;cursor:crosshair;z-index:10;display:none;}

/* ── PAGE BAR (Excel-style bottom) ─────────────── */
#pagebar{height:36px;background:var(--pageBar);border-top:2px solid var(--bd);display:none;align-items:center;gap:0;flex-shrink:0;overflow-x:auto;overflow-y:hidden;padding:0 4px;}
#pagebar::-webkit-scrollbar{height:3px;}
#pagebar::-webkit-scrollbar-thumb{background:var(--bd);}
.pagetab{display:flex;align-items:center;gap:5px;padding:0 14px;height:100%;border-right:1.5px solid var(--bd);cursor:pointer;font-size:12px;font-weight:600;color:var(--pageTxt);white-space:nowrap;flex-shrink:0;transition:background .1s;position:relative;user-select:none;}
.pagetab:hover{background:var(--hover);}
.pagetab.on{background:#fff;color:var(--accentL);border-bottom:3px solid var(--accent);}
.pagetab .pdel{font-size:10px;color:var(--muted);margin-left:3px;opacity:0;transition:opacity .15s;cursor:pointer;padding:2px 3px;border-radius:3px;}
.pagetab:hover .pdel{opacity:1;}
.pagetab .pdel:hover{background:var(--red);color:#fff;}
#addpage{display:flex;align-items:center;gap:5px;padding:0 14px;height:100%;cursor:pointer;font-size:13px;font-weight:700;color:var(--accent);white-space:nowrap;flex-shrink:0;transition:background .1s;}
#addpage:hover{background:var(--hover);}

/* ── EMPTY STATE ──────────────────────────────── */
#empty{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;color:var(--muted);}
.eico{font-size:52px;}
.etit{font-size:21px;color:var(--accentL);font-weight:700;}
.esub{font-size:14px;color:var(--muted);font-weight:500;}

/* ── CONTEXT MENU ─────────────────────────────── */
#ctx{position:fixed;background:#fff;border:1.5px solid var(--bd);border-radius:12px;padding:5px;z-index:2000;min-width:165px;box-shadow:0 10px 40px rgba(139,92,246,.2);display:none;}
.citem{padding:9px 14px;border-radius:7px;cursor:pointer;font-size:13px;color:var(--tx);font-weight:500;transition:background .1s;}
.citem:hover{background:var(--hover);}
.citem.red{color:var(--red);}

/* ── MATH DIALOG ──────────────────────────────── */
#mathov{position:fixed;inset:0;background:rgba(139,92,246,.18);z-index:3000;display:none;align-items:center;justify-content:center;}
#mathdlg{background:#fff;border:1.5px solid var(--bd);border-radius:18px;padding:32px;width:520px;box-shadow:0 20px 80px rgba(139,92,246,.25);}
#mathdlg h2{font-size:18px;font-weight:700;color:var(--accentL);margin-bottom:6px;}
.mhint{font-size:12px;color:var(--muted);margin-bottom:16px;font-weight:500;}
.mhint code{background:var(--hover);padding:2px 6px;border-radius:4px;color:var(--accentL);font-weight:700;}
#mathinp{width:100%;background:var(--hover);border:1.5px solid var(--bd);border-radius:9px;padding:11px 14px;color:var(--tx);font-size:14px;font-family:monospace;resize:vertical;outline:none;transition:border-color .15s;font-weight:500;}
#mathinp:focus{border-color:var(--accent);}
.mchk{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted);cursor:pointer;margin:13px 0;font-weight:500;}
#mathprev{background:var(--hover);border-radius:9px;padding:18px;margin-bottom:18px;min-height:54px;overflow-x:auto;}
.dbtns{display:flex;gap:8px;justify-content:flex-end;}
.sbtn{padding:8px 18px;background:var(--hover);border:1.5px solid var(--bd);border-radius:7px;color:var(--tx);font-size:13px;font-family:inherit;cursor:pointer;font-weight:600;transition:all .15s;}
.sbtn:hover{background:var(--active);}
.sbtn.pri{background:var(--accent);color:#fff;border-color:var(--accent);}
.sbtn.pri:hover{opacity:.87;}

@media print{
  #toolbar,#sidebar,#edhdr,#sbar,#pagebar{display:none!important;}
  #main{display:block;}
  #edwrap{display:block!important;overflow:visible;}
  #editor{color:#000;background:#fff;padding:40px;font-size:14px;min-height:unset;}
}
</style>
</head>
<body>

<!-- AUTH -->
<div id="auth">
  <div class="abox">
    <div class="alogo">📓</div>
    <h1 class="atitle">Scientific Notebook</h1>
    <p class="asub" id="asub">Sign in to your account</p>
    <div class="atabs">
      <div class="atab on" id="tlogin" onclick="switchTab('login')">Sign In</div>
      <div class="atab" id="tsignup" onclick="switchTab('signup')">Sign Up</div>
    </div>
    <div id="ulist"></div>
    <div id="lform">
      <div class="afield"><label>USERNAME</label><input id="lu" placeholder="your username" autocomplete="username"/></div>
      <div class="afield"><label>PASSWORD</label><input id="lp" type="password" placeholder="••••••••" autocomplete="current-password"/></div>
      <p class="aerr" id="lerr"></p>
      <button class="abtn" onclick="doLogin()">Sign In</button>
    </div>
    <div id="sform" style="display:none;">
      <div class="afield"><label>USERNAME</label><input id="su" placeholder="choose a username"/></div>
      <div class="afield"><label>PASSWORD</label><input id="sp" type="password" placeholder="at least 4 characters"/></div>
      <div class="afield"><label>CONFIRM PASSWORD</label><input id="sp2" type="password" placeholder="repeat password"/></div>
      <p class="aerr" id="serr"></p>
      <button class="abtn" onclick="doSignup()">Create Account</button>
    </div>
  </div>
</div>

<!-- APP -->
<div id="app" style="display:none;">
  <div id="toolbar">
    <div id="symtabs"></div>
    <div class="tbdiv"></div>
    <div id="symarea"></div>
    <div id="drawpanel"></div>
    <div id="rgroup">
      <div class="mwrap">
        <button class="ibtn" id="mbtn">&#8801;</button>
        <div id="mpop">
          <p class="mlabel">MENU</p>
          <div class="mitem" id="msearch">&#128269;&nbsp; Search</div>
          <div class="mitem" id="mexport">&#128196;&nbsp; Export as PDF</div>
          <div class="mitem" id="mcopy">&#128203;&nbsp; Copy as Text</div>
          <div class="mdivide"></div>
          <div class="mitem red" id="mlogout">&#128682;&nbsp; Sign Out</div>
        </div>
      </div>
    </div>
  </div>

  <div id="sbar">
    <input id="sinp" placeholder="Search notebooks…"/>
    <button class="sbtn" id="sclose">&#10005;</button>
    <div id="sres"></div>
  </div>

  <div id="main">
    <div id="sidebar">
      <div class="sbhead">SUBJECTS</div>
      <div id="sblist"></div>
      <div id="sbfoot"></div>
    </div>

    <div id="edarea">
      <div id="edhdr">
        <div id="edbc"></div>
        <div id="edtit"></div>
      </div>
      <div id="edwrap">
        <div id="editor" contenteditable="true"
          data-ph="Start writing…   shortcuts: alpha → α  ·  intg → ∫  ·  theta → θ  ·  -> → →   Use toolbar above for symbols & math"></div>
        <canvas id="drawcv"></canvas>
      </div>
      <div id="empty">
        <div class="eico">📓</div>
        <p class="etit">No notebook open</p>
        <p class="esub">Select or create a notebook from the sidebar</p>
      </div>
    </div>
  </div>

  <!-- PAGE BAR — Excel-style tabs at bottom -->
  <div id="pagebar">
    <!-- page tabs injected here by JS -->
    <div id="addpage" onclick="addPage()">&#43; Add Page</div>
  </div>
</div>

<!-- CONTEXT MENU -->
<div id="ctx">
  <div class="citem" id="cren">✏️&nbsp; Rename</div>
  <div class="citem red" id="cdel">🗑️&nbsp; Delete</div>
</div>

<!-- MATH DIALOG -->
<div id="mathov">
  <div id="mathdlg">
    <h2>Insert Math Expression</h2>
    <p class="mhint">LaTeX syntax — e.g. <code>\\int_0^1 x^2\\,dx</code> or <code>E=mc^2</code></p>
    <textarea id="mathinp" rows="3" placeholder="\\frac{d}{dx}e^x = e^x"></textarea>
    <label class="mchk"><input type="checkbox" id="mblock"/> Display mode (large centred)</label>
    <div id="mathprev"></div>
    <div class="dbtns">
      <button class="sbtn" id="mcancel">Cancel</button>
      <button class="sbtn pri" id="mins">Insert</button>
    </div>
  </div>
</div>

<script>
'use strict';

/* ── CONSTANTS ────────────────────────────────── */
const COLORS=['#8b5cf6','#7c3aed','#6d28d9','#a78bfa','#c4b5fd','#6366f1','#8b5cf6','#7e22ce'];
const GROUPS=[
  {id:'math',label:'∑ Math',syms:['∫','∬','∑','∏','√','∞','∂','∇','±','×','÷','≠','≈','≡','≤','≥','∈','∅','∀','∃','∝','π']},
  {id:'greek',label:'α Greek',syms:['α','β','γ','δ','ε','θ','λ','μ','π','σ','φ','ω','ξ','ψ','χ','Γ','Δ','Θ','Λ','Σ','Φ','Ω']},
  {id:'chem',label:'⚗ Chem',syms:['→','⇌','↑','↓','·','°','Δ','⊕','⊖','≡','≈','~','±']},
  {id:'phys',label:'⚡ Phys',syms:['⊥','∥','∠','°','ℏ','↔','⇒','∝','∇','∂','⊗','→']},
  {id:'fmt',label:'Aa',special:true},
];
const WSH={alpha:'α',beta:'β',gamma:'γ',delta:'δ',epsilon:'ε',zeta:'ζ',eta:'η',theta:'θ',iota:'ι',kappa:'κ',lambda:'λ',mu:'μ',nu:'ν',xi:'ξ',rho:'ρ',sigma:'σ',tau:'τ',phi:'φ',chi:'χ',psi:'ψ',omega:'ω',pi:'π',Gamma:'Γ',Delta:'Δ',Theta:'Θ',Lambda:'Λ',Sigma:'Σ',Phi:'Φ',Omega:'Ω',Pi:'Π',intg:'∫',iint:'∬',oint:'∮',sum:'∑',prod:'∏',sqrt:'√',inf:'∞',partial:'∂',nabla:'∇',pm:'±',mp:'∓',times:'×',div:'÷',neq:'≠',approx:'≈',equiv:'≡',leq:'≤',geq:'≥',elem:'∈',notin:'∉',subset:'⊂',supset:'⊃',union:'∪',inter:'∩',empty:'∅',forall:'∀',exists:'∃',prop:'∝',deg:'°',ang:'∠',perp:'⊥',para:'∥',hbar:'ℏ',uarr:'↑',darr:'↓'};
const LSH={'->':'→','<-':'←','<->':'↔','=>':'⇒','<=':'⇐','<=>':'⇔'};

const genId=()=>Math.random().toString(36).slice(2,10);
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const ini=s=>s.slice(0,2).toUpperCase();
const $=id=>document.getElementById(id);
const hash=s=>{let h=5381;for(let i=0;i<s.length;i++)h=(h*33^s.charCodeAt(i))>>>0;return h.toString(36);};
const LS={
  get:k=>{try{return JSON.parse(localStorage.getItem(k));}catch{return null;}},
  set:(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v));}catch{}}
};

/* ── AUTH ─────────────────────────────────────── */
let CU=null;
const getUsers=()=>LS.get('snb-users')||[];
const saveUsers=u=>LS.set('snb-users',u);
const getUD=id=>LS.get('snb-d-'+id);
const saveUD=(id,d)=>LS.set('snb-d-'+id,d);

function switchTab(m){
  $('tlogin').className='atab'+(m==='login'?' on':'');
  $('tsignup').className='atab'+(m==='signup'?' on':'');
  $('lform').style.display=m==='login'?'':'none';
  $('sform').style.display=m==='signup'?'':'none';
  $('asub').textContent=m==='login'?'Sign in to your account':'Create a new account';
}

function renderChips(){
  const ul=$('ulist');ul.innerHTML='';
  const users=getUsers();if(!users.length)return;
  const lbl=document.createElement('p');lbl.className='ulabel';lbl.textContent='EXISTING ACCOUNTS';ul.appendChild(lbl);
  users.forEach(u=>{
    const c=document.createElement('div');c.className='uchip';
    c.innerHTML=`<div class="uav" style="background:${u.color}22;color:${u.color}">${ini(u.username)}</div><span class="uname">${esc(u.username)}</span><span class="uhint">tap to fill</span>`;
    c.onclick=()=>{$('lu').value=u.username;$('lp').focus();};
    ul.appendChild(c);
  });
}

function doLogin(){
  const un=$('lu').value.trim(),pw=$('lp').value,err=$('lerr');
  if(!un||!pw){err.textContent='Please fill all fields.';return;}
  const users=getUsers(),u=users.find(x=>x.username.toLowerCase()===un.toLowerCase());
  if(!u){err.textContent='Account not found — sign up first!';return;}
  if(u.hash!==hash(pw)){err.textContent='Wrong password.';return;}
  err.textContent='';loginAs(u);
}

function doSignup(){
  const un=$('su').value.trim(),pw=$('sp').value,pw2=$('sp2').value,err=$('serr');
  if(!un||!pw||!pw2){err.textContent='Please fill all fields.';return;}
  if(un.length<3){err.textContent='Username must be ≥ 3 characters.';return;}
  if(pw.length<4){err.textContent='Password must be ≥ 4 characters.';return;}
  if(pw!==pw2){err.textContent='Passwords do not match.';return;}
  const users=getUsers();
  if(users.find(x=>x.username.toLowerCase()===un.toLowerCase())){err.textContent='Username taken.';return;}
  const nu={id:genId(),username:un,hash:hash(pw),color:COLORS[users.length%COLORS.length]};
  users.push(nu);saveUsers(users);
  const sid=genId(),nid=genId(),pid=genId();
  saveUD(nu.id,{
    subjects:[{id:sid,name:'My Notes',color:nu.color,notebooks:[
      {id:nid,name:'First Notebook',activePage:pid,pages:[
        {id:pid,name:'Page 1',content:`<p>Welcome, <strong>${esc(un)}</strong>! Your private notebook.</p><p>Try shortcuts: type <code>alpha</code> + Space → α &nbsp;·&nbsp; <code>intg</code> + Space → ∫ &nbsp;·&nbsp; <code>-></code> + Space → →</p><p>Add more pages using the <strong>+ Add Page</strong> button at the bottom.</p>`}
      ]}
    ]}],
    activeNbId:nid,expanded:{[sid]:true}
  });
  err.textContent='';loginAs(nu);
}

function loginAs(u){
  CU=u;$('auth').style.display='none';$('app').style.display='flex';
  const d=getUD(u.id);
  if(d&&d.subjects&&d.subjects.length){
    ST.subjects=d.subjects;ST.activeNbId=d.activeNbId||null;ST.expanded=d.expanded||{};
  } else {
    ST={subjects:[{id:genId(),name:'My Notes',color:u.color,notebooks:[{id:genId(),name:'First Notebook',activePage:null,pages:[{id:genId(),name:'Page 1',content:'<p><br></p>'}]}]}],activeNbId:null,expanded:{}};
  }
  // migrate old notebooks that don't have pages
  ST.subjects.forEach(s=>s.notebooks.forEach(nb=>{
    if(!nb.pages){
      const pid=genId();
      nb.pages=[{id:pid,name:'Page 1',content:nb.content||'<p><br></p>'}];
      nb.activePage=pid;
      delete nb.content;
    }
    if(!nb.activePage&&nb.pages.length>0)nb.activePage=nb.pages[0].id;
  }));
  renderAll();loadContent();renderFoot();setTimeout(fixH,200);setTimeout(fixH,600);
}

function doLogout(){
  savePageToState();persist();CU=null;ST=defST();
  $('app').style.display='none';$('auth').style.display='flex';
  $('lu').value='';$('lp').value='';$('lerr').textContent='';
  menuOpen=false;$('mpop').style.display='none';renderChips();
}

/* ── APP STATE ────────────────────────────────── */
const defST=()=>({subjects:[],activeNbId:null,expanded:{}});
let ST=defST();
let aTab=0,menuOpen=false,drawMode=false,penColor='#8b5cf6',penSize=2;
let isDrawing=false,lastPos=null,savedRange=null,saveTimer=null,ctxTgt=null,mpTimer=null;
let addingSub=false,addingNbFor=null,renaming=null;

const persist=()=>{if(CU)saveUD(CU.id,ST);};
const sched=()=>{clearTimeout(saveTimer);saveTimer=setTimeout(()=>{savePageToState();persist();},600);};

/* ── PAGE HELPERS ─────────────────────────────── */
function getAN(){
  for(const s of ST.subjects)for(const n of s.notebooks)if(n.id===ST.activeNbId)return n;
  return null;
}
function getAS(){
  for(const s of ST.subjects)for(const n of s.notebooks)if(n.id===ST.activeNbId)return s;
  return null;
}
function getActivePage(nb){
  if(!nb||!nb.pages||!nb.pages.length)return null;
  return nb.pages.find(p=>p.id===nb.activePage)||nb.pages[0];
}

function savePageToState(){
  const ed=$('editor');if(!ed)return;
  const nb=getAN();if(!nb)return;
  const pg=getActivePage(nb);if(!pg)return;
  pg.content=ed.innerHTML;
}

function loadContent(){
  const ed=$('editor');if(!ed)return;
  const nb=getAN();
  if(!nb){ed.innerHTML='';return;}
  const pg=getActivePage(nb);
  ed.innerHTML=pg?(pg.content||'<p><br></p>'):'<p><br></p>';
}

function openNB(id){
  savePageToState();
  ST.activeNbId=id;
  persist();
  renderAll();
  loadContent();
  setTimeout(fixH,60);
}

function switchPage(pageId){
  savePageToState();
  const nb=getAN();if(!nb)return;
  nb.activePage=pageId;
  persist();
  renderPageBar();
  loadContent();
}

function addPage(){
  const nb=getAN();if(!nb)return;
  const id=genId();
  const num=nb.pages.length+1;
  nb.pages.push({id,name:'Page '+num,content:'<p><br></p>'});
  nb.activePage=id;
  persist();
  renderPageBar();
  loadContent();
  // scroll page bar to end
  const pb=$('pagebar');if(pb)pb.scrollLeft=pb.scrollWidth;
}

function deletePage(pageId,e){
  e.stopPropagation();
  const nb=getAN();if(!nb)return;
  if(nb.pages.length<=1){alert('A notebook must have at least one page.');return;}
  const idx=nb.pages.findIndex(p=>p.id===pageId);
  nb.pages=nb.pages.filter(p=>p.id!==pageId);
  if(nb.activePage===pageId){
    nb.activePage=nb.pages[Math.max(0,idx-1)].id;
  }
  persist();
  renderPageBar();
  if(nb.activePage!==pageId)loadContent();
  else{nb.activePage=nb.pages[0].id;loadContent();}
}

function renderPageBar(){
  const nb=getAN();
  const pb=$('pagebar');
  if(!nb){pb.style.display='none';return;}
  pb.style.display='flex';
  // clear old tabs (keep addpage btn)
  Array.from(pb.querySelectorAll('.pagetab')).forEach(t=>t.remove());
  const addBtn=$('addpage');
  nb.pages.forEach(pg=>{
    const tab=document.createElement('div');
    tab.className='pagetab'+(pg.id===nb.activePage?' on':'');
    tab.dataset.id=pg.id;
    tab.innerHTML=`<span>${esc(pg.name)}</span><span class="pdel" onclick="deletePage('${pg.id}',event)" title="Delete page">✕</span>`;
    tab.onclick=()=>switchPage(pg.id);
    pb.insertBefore(tab,addBtn);
  });
}

/* ── RENDER ───────────────────────────────────── */
function renderAll(){renderTB();renderSB();renderEH();renderPageBar();}

function renderTB(){
  const tabs=$('symtabs');tabs.innerHTML='';
  GROUPS.forEach((g,i)=>{
    const b=document.createElement('button');b.className='tabtn'+(i===aTab?' on':'');b.textContent=g.label;
    b.onclick=()=>{aTab=i;renderTB();};tabs.appendChild(b);
  });
  const sa=$('symarea');sa.innerHTML='';
  const g=GROUPS[aTab];
  if(g.syms){
    g.syms.forEach(s=>{
      const b=document.createElement('button');b.className='sybtn';b.textContent=s;b.title='Insert '+s;
      b.onclick=()=>insSym(s);sa.appendChild(b);
    });
  }else if(g.special){
    [{l:'B',c:'bold',s:'font-weight:bold'},{l:'I',c:'italic',s:'font-style:italic'},{l:'x²',c:'superscript'},{l:'x₂',c:'subscript'},{l:'∫ Math',c:'math'},{l:'✎ Draw',c:'draw'}].forEach(({l,c,s})=>{
      const b=document.createElement('button');b.className='fmbtn'+(c==='draw'&&drawMode?' on':'');
      if(s)b.style.cssText=s;b.textContent=l;
      b.onmousedown=e=>{e.preventDefault();saveSel();};
      b.onclick=()=>fmtCmd(c);sa.appendChild(b);
    });
  }
  renderDP();
}

function renderSB(){
  const list=$('sblist');list.innerHTML='';
  ST.subjects.forEach(sub=>{
    if(renaming?.type==='sub'&&renaming.id===sub.id){
      const inp=mkInp(sub.name,v=>{if(v)sub.name=v;renaming=null;persist();renderSB();},()=>{renaming=null;renderSB();});
      list.appendChild(inp);setTimeout(()=>inp.focus(),30);return;
    }
    const row=document.createElement('div');row.className='subrow';
    row.innerHTML=`<span class="sarrow">${ST.expanded[sub.id]?'▼':'▶'}</span><div class="sdot" style="background:${sub.color}"></div><span class="sname">${esc(sub.name)}</span>`;
    row.onclick=()=>{ST.expanded[sub.id]=!ST.expanded[sub.id];persist();renderSB();};
    row.oncontextmenu=e=>{e.preventDefault();e.stopPropagation();showCtx(e,{type:'sub',id:sub.id});};
    list.appendChild(row);
    if(!ST.expanded[sub.id])return;
    const nbl=document.createElement('div');nbl.className='nblist';
    sub.notebooks.forEach(nb=>{
      if(renaming?.type==='nb'&&renaming.id===nb.id){
        const inp=mkInp(nb.name,v=>{if(v)nb.name=v;renaming=null;persist();renderSB();renderEH();},()=>{renaming=null;renderSB();});
        nbl.appendChild(inp);setTimeout(()=>inp.focus(),30);return;
      }
      const active=ST.activeNbId===nb.id;
      const r=document.createElement('div');r.className='nbrow'+(active?' on':'');
      if(active)r.style.borderLeftColor=sub.color;
      r.innerHTML=`<span class="nbico">📓</span><span class="nbname">${esc(nb.name)}</span>`;
      r.onclick=()=>openNB(nb.id);
      r.oncontextmenu=e=>{e.preventDefault();e.stopPropagation();showCtx(e,{type:'nb',id:nb.id,pid:sub.id});};
      nbl.appendChild(r);
    });
    if(addingNbFor===sub.id){
      const inp=mkInp('',v=>{
        if(v){
          const pid=genId();
          sub.notebooks.push({id:genId(),name:v,activePage:pid,pages:[{id:pid,name:'Page 1',content:'<p><br></p>'}]});
        }
        persist();addingNbFor=null;renderSB();
      },()=>{addingNbFor=null;renderSB();});
      nbl.appendChild(inp);setTimeout(()=>inp.focus(),30);
    }else{
      const ar=document.createElement('div');ar.className='addnb';ar.textContent='+ notebook';
      ar.onclick=e=>{e.stopPropagation();addingNbFor=sub.id;renderSB();};nbl.appendChild(ar);
    }
    list.appendChild(nbl);
  });
  if(addingSub){
    const inp=mkInp('',v=>{
      if(v)ST.subjects.push({id:genId(),name:v,color:COLORS[ST.subjects.length%COLORS.length],notebooks:[]});
      persist();addingSub=false;renderSB();
    },()=>{addingSub=false;renderSB();});
    list.appendChild(inp);setTimeout(()=>inp.focus(),30);
  }else{
    const as=document.createElement('div');as.className='addsub';as.textContent='+ Add Subject';
    as.onclick=()=>{addingSub=true;renderSB();};list.appendChild(as);
  }
}

function mkInp(val,onOK,onX){
  const i=document.createElement('input');i.className='ninp';i.value=val;i.placeholder='Name…';
  const commit=()=>onOK(i.value.trim());
  i.onblur=commit;
  i.onkeydown=e=>{if(e.key==='Enter'){e.preventDefault();commit();}if(e.key==='Escape'){e.preventDefault();onX();}e.stopPropagation();};
  return i;
}

function renderEH(){
  const nb=getAN(),sub=getAS();
  $('edhdr').style.display=nb?'':'none';
  $('edwrap').style.display=nb?'block':'none';
  $('empty').style.display=nb?'none':'';
  if(nb){
    $('edbc').textContent=(sub?sub.name+' / ':'')+nb.name;
    const pg=getActivePage(nb);
    $('edtit').textContent=pg?pg.name:nb.name;
  }
}

function renderFoot(){
  const f=$('sbfoot');if(!CU){f.innerHTML='';return;}
  const{username,color}=CU;
  f.innerHTML=`<div class="sfav" style="background:${color}22;color:${color}">${ini(username)}</div><span class="sfname">${esc(username)}</span><button class="logbtn" onclick="doLogout()">Sign out</button>`;
}

/* ── EDITOR ───────────────────────────────────── */
function saveSel(){const s=window.getSelection();if(s&&s.rangeCount>0)savedRange=s.getRangeAt(0).cloneRange();}
function restSel(){if(!savedRange)return;const s=window.getSelection();s.removeAllRanges();s.addRange(savedRange);}

function insSym(sym){$('editor').focus();restSel();document.execCommand('insertText',false,sym);savePageToState();persist();}

function fmtCmd(cmd){
  if(cmd==='math'){saveSel();$('mathov').style.display='flex';$('mathinp').focus();return;}
  if(cmd==='draw'){toggleDraw();return;}
  $('editor').focus();restSel();document.execCommand(cmd,false,null);savePageToState();persist();
}

function tryShortcut(e){
  if(e.key!==' '&&e.key!=='Enter')return;
  const sel=window.getSelection();if(!sel||sel.rangeCount===0)return;
  const r=sel.getRangeAt(0),node=r.startContainer;if(node.nodeType!==3)return;
  const before=node.textContent.slice(0,r.startOffset);
  for(const[k,v]of Object.entries(LSH)){
    if(before.endsWith(k)){
      e.preventDefault();repNode(node,r,k,v,e.key===' ',sel);
      if(e.key==='Enter')document.execCommand('insertParagraph',false);
      savePageToState();persist();return;
    }
  }
  const m=before.match(/([A-Za-z]+)$/);if(!m||!WSH[m[1]])return;
  e.preventDefault();repNode(node,r,m[1],WSH[m[1]],e.key===' ',sel);
  if(e.key==='Enter')document.execCommand('insertParagraph',false);
  savePageToState();persist();
}

function repNode(node,r,orig,repl,space,sel){
  const st=r.startOffset-orig.length,after=node.textContent.slice(r.startOffset);
  node.textContent=node.textContent.slice(0,st)+repl+(space?' ':'')+after;
  const nr=document.createRange();nr.setStart(node,Math.min(st+repl.length+(space?1:0),node.textContent.length));nr.collapse(true);
  sel.removeAllRanges();sel.addRange(nr);
}

/* ── MATH ─────────────────────────────────────── */
function updPrev(){
  clearTimeout(mpTimer);
  const tex=$('mathinp').value.trim(),bl=$('mblock').checked;
  if(!tex){$('mathprev').innerHTML='';return;}
  mpTimer=setTimeout(()=>{
    try{if(typeof katex!=='undefined')$('mathprev').innerHTML=katex.renderToString(tex,{displayMode:bl,throwOnError:false});}
    catch{$('mathprev').innerHTML='<span style="color:#c0392b">Invalid LaTeX</span>';}
  },280);
}
function closeMath(){$('mathov').style.display='none';$('mathinp').value='';$('mathprev').innerHTML='';$('mblock').checked=false;}
function insMath(){
  const tex=$('mathinp').value.trim();if(!tex){closeMath();return;}
  const bl=$('mblock').checked;
  const sp=document.createElement('span');sp.className='mathnode';sp.contentEditable='false';
  try{if(typeof katex!=='undefined')katex.render(tex,sp,{displayMode:bl,throwOnError:false});else sp.textContent=tex;}catch{sp.textContent=tex;}
  $('editor').focus();restSel();
  const sel=window.getSelection();
  if(sel&&sel.rangeCount>0){
    const r=sel.getRangeAt(0);r.deleteContents();r.insertNode(sp);
    const tx=document.createTextNode('\u00a0');sp.after(tx);
    r.setStartAfter(tx);r.collapse(true);sel.removeAllRanges();sel.addRange(r);
  }
  closeMath();savePageToState();persist();
}

/* ── DRAW ─────────────────────────────────────── */
function toggleDraw(){
  drawMode=!drawMode;
  const cv=$('drawcv'),w=$('edwrap');
  if(drawMode){cv.width=w.offsetWidth;cv.height=Math.max(w.offsetHeight,w.scrollHeight);cv.style.display='block';}
  else cv.style.display='none';
  renderTB();
}
function renderDP(){
  const dp=$('drawpanel');dp.style.display=drawMode?'flex':'none';if(!drawMode)return;
  dp.innerHTML='<span class="dlabel">Color</span>';
  ['#8b5cf6','#6366f1','#06b6d4','#22c55e','#f97316','#1a0a4a'].forEach(c=>{
    const d=document.createElement('div');d.className='pdot';d.style.background=c;d.style.borderColor=penColor===c?'#333':'transparent';
    d.onclick=()=>{penColor=c;renderDP();};dp.appendChild(d);
  });
  const sl=document.createElement('span');sl.className='dlabel';sl.style.marginLeft='6px';sl.textContent='Size';dp.appendChild(sl);
  [1,2,4,8].forEach(sz=>{
    const b=document.createElement('button');b.className='fmbtn'+(penSize===sz?' on':'');b.style.cssText='width:28px;height:28px;padding:0;';b.textContent=sz;
    b.onclick=()=>{penSize=sz;renderDP();};dp.appendChild(b);
  });
  const cl=document.createElement('button');cl.className='fmbtn red';cl.style.marginLeft='4px';cl.textContent='Clear';
  cl.onclick=()=>{const ctx=$('drawcv').getContext('2d');ctx.clearRect(0,0,$('drawcv').width,$('drawcv').height);};dp.appendChild(cl);
  const em=document.createElement('button');em.className='fmbtn on';em.style.marginLeft='2px';em.textContent='Embed ↵';em.onclick=embedDraw;dp.appendChild(em);
}
function embedDraw(){
  const cv=$('drawcv'),du=cv.toDataURL();cv.getContext('2d').clearRect(0,0,cv.width,cv.height);toggleDraw();
  const img=document.createElement('img');img.src=du;img.style.cssText='max-width:100%;display:block;margin:8px 0;border-radius:8px;border:2px solid var(--bd);';
  const ed=$('editor');ed.focus();
  const sel=window.getSelection(),r=document.createRange();r.selectNodeContents(ed);r.collapse(false);sel.removeAllRanges();sel.addRange(r);
  r.insertNode(img);r.setStartAfter(img);r.collapse(true);sel.removeAllRanges();sel.addRange(r);
  savePageToState();persist();
}
function cvPos(e){const rc=$('drawcv').getBoundingClientRect();return{x:e.clientX-rc.left,y:e.clientY-rc.top};}

/* ── CTX MENU ─────────────────────────────────── */
function showCtx(e,t){ctxTgt=t;const m=$('ctx');m.style.display='block';m.style.left=e.clientX+'px';m.style.top=e.clientY+'px';}
function hideCtx(){$('ctx').style.display='none';ctxTgt=null;}

/* ── SEARCH ───────────────────────────────────── */
function openSearch(){$('sbar').style.display='flex';menuOpen=false;$('mpop').style.display='none';setTimeout(()=>$('sinp').focus(),50);}
function closeSearch(){$('sbar').style.display='none';$('sres').style.display='none';}
function doSearch(){
  const q=$('sinp').value.trim().toLowerCase(),sr=$('sres');
  if(!q){sr.style.display='none';return;}
  const hits=[];ST.subjects.forEach(s=>s.notebooks.forEach(n=>{if(n.name.toLowerCase().includes(q))hits.push({nb:n,sub:s});}));
  if(!hits.length){sr.style.display='none';return;}
  sr.innerHTML='';
  hits.forEach(({nb,sub})=>{
    const d=document.createElement('div');d.className='sitem';
    d.innerHTML=`<div class="snm">${esc(nb.name)}</div><div class="ssb">${esc(sub.name)}</div>`;
    d.onclick=()=>{openNB(nb.id);closeSearch();};sr.appendChild(d);
  });
  sr.style.display='block';
}

/* ── HEIGHT FIX ───────────────────────────────── */
function fixH(){
  const tot=window.innerHeight;
  const tb=$('toolbar');const tbH=tb?tb.offsetHeight:48;
  const sb2=$('sbar');const sbH=(sb2&&sb2.style.display!=='none')?sb2.offsetHeight:0;
  const pb=$('pagebar');const pbH=(pb&&pb.style.display!=='none')?pb.offsetHeight:0;
  const rem=tot-tbH-sbH-pbH-4;

  const mn=$('main');if(mn)mn.style.height=rem+'px';
  const sideEl=$('sidebar');if(sideEl)sideEl.style.height=rem+'px';

  const sbhead=document.querySelector('.sbhead');
  const sbfoot=$('sbfoot');
  const sbl=$('sblist');
  if(sbl&&sbhead&&sbfoot){
    const h=rem-sbhead.offsetHeight-sbfoot.offsetHeight;
    sbl.style.height=Math.max(h,80)+'px';
    sbl.style.overflow='auto';
  }

  const ea=$('edarea');if(ea)ea.style.height=rem+'px';
  const hdrH=($('edhdr')&&$('edhdr').style.display!=='none')?$('edhdr').offsetHeight:0;
  const ew=$('edwrap');
  if(ew&&ew.style.display!=='none'){
    const ewH=rem-hdrH;
    ew.style.height=Math.max(ewH,300)+'px';
  }
  const emp=$('empty');if(emp)emp.style.height=rem+'px';
}

/* ── EVENT LISTENERS ──────────────────────────── */
const ed=$('editor');
ed.addEventListener('keydown',e=>{tryShortcut(e);if(e.key!==' '&&e.key!=='Enter')sched();});
ed.addEventListener('input',()=>{savePageToState();persist();});
ed.addEventListener('mouseup',saveSel);
ed.addEventListener('keyup',saveSel);
ed.addEventListener('focus',()=>setTimeout(fixH,50));

const cv=$('drawcv');
cv.addEventListener('mousedown',e=>{if(!drawMode)return;isDrawing=true;lastPos=cvPos(e);});
cv.addEventListener('mousemove',e=>{
  if(!drawMode||!isDrawing)return;
  const ctx=cv.getContext('2d'),p=cvPos(e);
  ctx.strokeStyle=penColor;ctx.lineWidth=penSize;ctx.lineCap='round';ctx.lineJoin='round';
  ctx.beginPath();ctx.moveTo(lastPos.x,lastPos.y);ctx.lineTo(p.x,p.y);ctx.stroke();lastPos=p;
});
cv.addEventListener('mouseup',()=>{isDrawing=false;});
cv.addEventListener('mouseleave',()=>{isDrawing=false;});

$('mbtn').addEventListener('click',e=>{e.stopPropagation();menuOpen=!menuOpen;$('mpop').style.display=menuOpen?'block':'none';});
$('msearch').addEventListener('click',openSearch);
$('mexport').addEventListener('click',()=>{window.print();menuOpen=false;$('mpop').style.display='none';});
$('mcopy').addEventListener('click',()=>{navigator.clipboard?.writeText($('editor').innerText||'');menuOpen=false;$('mpop').style.display='none';});
$('mlogout').addEventListener('click',doLogout);
$('sinp').addEventListener('input',doSearch);
$('sclose').addEventListener('click',closeSearch);
$('mathinp').addEventListener('input',updPrev);
$('mblock').addEventListener('change',updPrev);
$('mins').addEventListener('click',insMath);
$('mcancel').addEventListener('click',closeMath);
$('mathov').addEventListener('click',e=>{if(e.target===$('mathov'))closeMath();});
$('mathinp').addEventListener('keydown',e=>{if(e.key==='Enter'&&(e.ctrlKey||e.metaKey))insMath();if(e.key==='Escape')closeMath();});
$('cren').addEventListener('click',()=>{if(!ctxTgt)return;renaming=ctxTgt;hideCtx();renderSB();});
$('cdel').addEventListener('click',()=>{
  if(!ctxTgt)return;
  if(ctxTgt.type==='nb'){
    ST.subjects.forEach(s=>{if(s.id===ctxTgt.pid)s.notebooks=s.notebooks.filter(n=>n.id!==ctxTgt.id);});
    if(ST.activeNbId===ctxTgt.id){ST.activeNbId=null;renderEH();renderPageBar();$('editor').innerHTML='';}
  }else{
    const sub=ST.subjects.find(s=>s.id===ctxTgt.id);
    if(sub?.notebooks.some(n=>n.id===ST.activeNbId)){ST.activeNbId=null;renderEH();renderPageBar();$('editor').innerHTML='';}
    ST.subjects=ST.subjects.filter(s=>s.id!==ctxTgt.id);
  }
  hideCtx();persist();renderSB();
});
$('lu').addEventListener('keydown',e=>{if(e.key==='Enter')$('lp').focus();});
$('lp').addEventListener('keydown',e=>{if(e.key==='Enter')doLogin();});
$('sp').addEventListener('keydown',e=>{if(e.key==='Enter')$('sp2').focus();});
$('sp2').addEventListener('keydown',e=>{if(e.key==='Enter')doSignup();});
document.addEventListener('mousedown',e=>{
  if(!e.target.closest('#ctx'))hideCtx();
  if(!e.target.closest('#mbtn')&&!e.target.closest('#mpop')){menuOpen=false;$('mpop').style.display='none';}
});
window.addEventListener('resize',fixH);
setTimeout(fixH,200);setTimeout(fixH,700);

renderChips();
</script>
</body>
</html>
"""

components.html(APP, height=1000, scrolling=False)
