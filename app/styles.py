"""HireFlow visual design system — Streamlit native controls, accessible contrast."""
import streamlit as st


def apply_styles():
    st.markdown("""<style>
    :root {--hf-forest:#153E36;--hf-deep:#102C27;--hf-teal:#267B6C;--hf-muted:#62746C;--hf-line:#DFE7DF;--hf-cream:#F7F8F4;--hf-amber:#B8793D;}
    .stApp {background:linear-gradient(145deg,#F8FAF6 0%,#F3F7F2 55%,#F9FAF7 100%);color:#1B302A;}
    .stMain .block-container {max-width:1320px;padding-top:1.7rem;padding-bottom:4rem;}
    h1,h2,h3 {color:#173C33;letter-spacing:-.035em;}
    h1 {font-size:clamp(2rem,3vw,3rem)!important;font-weight:760!important;line-height:1.15!important;margin-bottom:.55rem!important;}
    h2 {font-weight:720!important;} h3 {font-weight:680!important;}
    p,li {line-height:1.65;}
    [data-testid="stSidebar"] {background:#13392F!important;border-right:1px solid #245144!important;}
    [data-testid="stSidebar"] * {color:#E8F2EB;}
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {color:#D6E7DD;}
    [data-testid="stSidebar"] hr {border-color:#33594D!important;}
    [data-testid="stSidebar"] [role="radiogroup"] label {border-radius:10px;padding:8px 9px;margin:2px 0;transition:background .15s ease;}
    [data-testid="stSidebar"] [role="radiogroup"] label:hover {background:#285648;}
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {background:#2C6454;box-shadow:inset 3px 0 #D6A765;}
    [data-testid="stSidebar"] [role="radiogroup"] label span {color:#F0F8F2!important;}
    .hf-brand {display:flex;align-items:center;gap:12px;padding:8px 0 12px;}
    .hf-logo {height:44px;width:44px;display:flex;align-items:center;justify-content:center;background:#E5EFE4;color:#173E34!important;font-weight:850;font-size:25px;border-radius:13px;}
    .hf-logo span {color:#B87743!important;font-size:13px;align-self:flex-start;padding-top:5px;}
    .hf-brand-name {font-size:23px;font-weight:800;letter-spacing:-.055em;color:#FFF!important;line-height:1.1;}
    .hf-brand-name span {font-weight:500;color:#D6A765!important;}
    .hf-brand-sub {font-size:9px;letter-spacing:.18em;font-weight:750;color:#A6C8B5!important;margin-top:5px;}
    .hf-sidebar-footer {border:1px solid #3C6756;background:#204B3F;border-radius:12px;padding:15px 12px;font-size:10px;font-weight:750;letter-spacing:.1em;color:#E6F4EB!important;line-height:1.9;}
    .hf-sidebar-footer small {font-size:11px;letter-spacing:0;font-weight:450;color:#C0D7C8!important;}
    .hf-status-dot {display:inline-block;width:7px;height:7px;border-radius:50%;background:#A6D8AE;margin-right:5px;}
    .eyebrow,.hf-section-label {font-size:11px;letter-spacing:.16em;font-weight:800;color:#267B6C;text-transform:uppercase;margin:4px 0 12px;}
    .hf-section-label {margin-top:12px;display:flex;justify-content:space-between;align-items:center;}
    .hf-section-label span {color:#779487;font-size:10px;letter-spacing:.08em;}
    [data-testid="stMetric"] {background:#FFFFFF;border:1px solid #E1EAE2;border-radius:16px;padding:17px 19px;min-height:116px;box-shadow:0 5px 24px rgba(22,55,42,.035);}
    [data-testid="stMetricLabel"] {color:#66776D!important;font-size:13px!important;}
    [data-testid="stMetricValue"] {color:#173E35!important;font-weight:770;letter-spacing:-.04em;}
    [data-testid="stMetric"]:nth-child(2n) {border-top:3px solid #B9824E;}
    [data-testid="stMetric"]:nth-child(2n+1) {border-top:3px solid #2A806E;}
    [data-testid="stVerticalBlockBorderWrapper"]:has([data-testid="stPlotlyChart"]) {border-radius:16px;}
    [data-testid="stPlotlyChart"] {background:white;border:1px solid #E1EAE2;border-radius:16px;padding:8px;box-shadow:0 5px 24px rgba(22,55,42,.025);}
    [data-testid="stDataFrame"] {border:1px solid #DFE8E0;border-radius:12px;overflow:hidden;}
    [data-testid="stFileUploader"] {border:1px dashed #98B5A6;border-radius:14px;background:#FBFDFB;padding:10px;}
    [data-testid="stExpander"] {background:#FFF;border:1px solid #E0E8E1;border-radius:12px;overflow:hidden;}
    [data-testid="stForm"] {background:#FFF;border:1px solid #E0E8E1;border-radius:16px;padding:20px;}
    .stButton>button,.stFormSubmitButton>button {min-height:2.85rem;border-radius:10px;font-weight:650;transition:transform .15s ease,box-shadow .15s ease;}
    .stButton>button:hover,.stFormSubmitButton>button:hover {transform:translateY(-1px);}
    button[kind="primary"],button[data-testid="stBaseButton-primary"] {background:#1E6555!important;border-color:#1E6555!important;color:white!important;box-shadow:0 4px 12px rgba(27,91,72,.13);}
    button[kind="primary"]:hover,button[data-testid="stBaseButton-primary"]:hover {background:#154B3E!important;}
    div[data-baseweb="select"]>div,.stTextInput input,.stTextArea textarea {border-radius:10px!important;border-color:#CFDED3!important;}
    .hf-step {display:flex;align-items:center;gap:14px;background:#FFF;border:1px solid #DFE8DF;border-left:4px solid #2C816E;border-radius:13px;padding:16px 19px;margin:12px 0 18px;}
    .hf-step>span {background:#E9F3EC;color:#246F5D;font-size:15px;font-weight:850;padding:9px 11px;border-radius:10px;}
    .hf-step strong {display:block;color:#193F34;font-size:17px;}
    .hf-step small {display:block;color:#6E8175;font-size:12px;margin-top:2px;}
    .step-hint {border-left:3px solid #B8793D;padding:.7rem 1rem;background:#FFF8F0;border-radius:0 8px 8px 0;margin:.5rem 0 1rem;}
    .review-note {font-size:.86rem;color:#52645D;}
    hr {border-color:#E0E9E1!important;margin:1.6rem 0!important;}
    [data-testid="stAlert"] {border-radius:12px;}
    @media(max-width:850px) {.stMain .block-container {padding:1rem .9rem 2.5rem;}[data-testid="stMetric"] {min-height:95px;padding:12px;}.hf-step {padding:12px;}}

    /* Emerald Galaxy: luminous, dimensional, but restrained around real data */
    .stApp {background:radial-gradient(ellipse at 95% 0%,#e4e0fa 0%,transparent 33%),radial-gradient(ellipse at 0% 42%,#dff5eb 0%,transparent 34%),#f7f9f8!important;}
    .hf-motion-hero {background:radial-gradient(circle at 83% 22%,#59459a 0%,transparent 34%),radial-gradient(circle at 75% 95%,#227f79 0%,transparent 48%),linear-gradient(120deg,#10292d,#183c45 62%,#27325a)!important;box-shadow:0 23px 58px #283a6940!important;}
    [data-testid="stMetric"] {transition:transform .25s ease,box-shadow .25s ease;}
    [data-testid="stMetric"]:hover {transform:translateY(-4px);box-shadow:0 16px 32px #254a3b20;}
    .hf-explorer-banner {position:relative;display:flex;align-items:center;gap:16px;padding:22px 26px;margin:12px 0 18px;border-radius:19px;overflow:hidden;background:linear-gradient(110deg,#143d3c,#225d59 58%,#594c94);box-shadow:0 14px 36px #193d4925;color:#fff;}
    .hf-explorer-banner strong {display:block;font-size:20px;letter-spacing:-.03em;}
    .hf-explorer-banner small {display:block;color:#d9ece8;font-size:12px;max-width:650px;margin-top:5px;}
    .hf-explorer-spark {display:grid;place-items:center;flex:0 0 52px;height:52px;border-radius:16px;background:#ffffff20;color:#a5f1db;font-size:30px;animation:hf-explorer-float 4s ease-in-out infinite;}
    .hf-explorer-orb {position:absolute;right:38px;font-size:68px;color:#ffffff18;animation:hf-explorer-rotate 18s linear infinite;}
    .hf-evidence-label {display:inline-block;font-size:11px;font-weight:800;letter-spacing:.11em;border-radius:30px;padding:9px 13px;margin:10px 0;}
    .hf-evidence-found {background:#e0f5e9;color:#155b46;}.hf-evidence-gap {background:#fff0df;color:#86542d;}
    .hf-passage-heading {font-size:11px;font-weight:800;letter-spacing:.1em;color:#577368;margin:8px 0;}
    @keyframes hf-explorer-float {0%,100%{transform:translateY(0) rotate(-5deg)}50%{transform:translateY(-7px) rotate(7deg)}}
    @keyframes hf-explorer-rotate {to{transform:rotate(360deg)}}
    @media (prefers-reduced-motion:reduce){.hf-explorer-spark,.hf-explorer-orb{animation:none!important}[data-testid="stMetric"]{transition:none!important}}

    /* Motion hero: CSS-only, no scripts, accessible reduced-motion fallback */
    .hf-motion-hero{position:relative;isolation:isolate;overflow:hidden;display:grid;grid-template-columns:1.05fr .95fr;align-items:center;min-height:345px;border-radius:23px;padding:36px 38px;background:radial-gradient(circle at 85% 18%,#2a7569 0%,transparent 37%),linear-gradient(115deg,#102d2a,#173e37 62%,#17463e);box-shadow:0 18px 44px rgba(20,60,48,.14);margin-bottom:16px}
    .hf-motion-hero:before{content:"";position:absolute;inset:0;pointer-events:none;background-image:radial-gradient(#ffffff20 .8px,transparent .8px);background-size:22px 22px;mask-image:linear-gradient(90deg,transparent 15%,#000)}
    .hf-hero-copy{position:relative;z-index:3;max-width:520px}
    .hf-hero-pill{display:inline-flex;align-items:center;gap:9px;border:1px solid #ffffff32;border-radius:100px;padding:7px 12px;color:#bfe6d7;font-size:10px;font-weight:800;letter-spacing:.12em;background:#ffffff0c}
    .hf-pulse{width:7px;height:7px;background:#77dfb6;border-radius:50%;box-shadow:0 0 0 4px #77dfb621;animation:hf-pulse 2.6s ease-in-out infinite}
    .hf-motion-hero h2{color:white!important;font-size:clamp(2rem,3.4vw,3.4rem)!important;line-height:1.07;letter-spacing:-.055em;margin:20px 0 16px;font-weight:800!important}
    .hf-motion-hero h2 em{color:#b7e7c9;font-style:normal}
    .hf-motion-hero p{color:#c9ded5;font-size:15px;line-height:1.7;max-width:450px;margin-bottom:22px}
    .hf-hero-chips{display:flex;flex-wrap:wrap;gap:8px}
    .hf-hero-chips span{border:1px solid #ffffff2b;background:#ffffff0d;border-radius:8px;padding:8px 10px;color:#e3f4ec;font-size:11px;font-weight:600}
    .hf-hero-art{position:relative;height:290px;min-width:0;perspective:850px}
    .hf-art-orbit{position:absolute;border:1px solid #b1e4d224;border-radius:50%;width:360px;height:360px;top:-35px;left:15%;animation:hf-orbit 24s linear infinite}
    .hf-orbit-two{width:260px;height:260px;top:12px;left:26%;animation-duration:32s;animation-direction:reverse;border-style:dashed}
    .hf-art-glow{position:absolute;width:260px;height:240px;left:30%;top:12%;background:#5dbca14d;filter:blur(65px);border-radius:50%}
    .hf-document-card{position:absolute;z-index:2;top:13px;left:22%;width:min(285px,72%);padding:17px 17px 19px;background:#fcfffc;color:#193c34;border-radius:16px;box-shadow:0 24px 60px #041e1a7a;transform:rotate(-5deg);animation:hf-card 7s ease-in-out infinite}
    .hf-doc-header{display:flex;align-items:center;gap:8px;font-size:9px;font-weight:850;letter-spacing:.09em;color:#607d70}.hf-doc-icon{display:grid;place-items:center;background:#e2f1e9;color:#27745d;width:27px;height:27px;border-radius:7px;font-size:16px}.hf-doc-dots{margin-left:auto;color:#a3b7ac;letter-spacing:1px}
    .hf-doc-person{display:flex;align-items:center;gap:9px;margin-top:17px}.hf-doc-avatar{display:grid;place-items:center;background:#e9eee8;color:#2e7765;width:34px;height:34px;border-radius:50%;font-size:20px}.hf-doc-person b{display:block;font-size:12px}.hf-doc-person small{display:block;font-size:10px;color:#829489;margin-top:2px}.hf-doc-rule{height:1px;background:#e9eee9;margin:15px 0}.hf-doc-line{height:6px;background:#e5ece7;border-radius:8px;margin:9px 0}.hf-line-long{width:88%}.hf-line-short{width:58%}.hf-line-medium{width:76%}
    .hf-doc-match,.hf-doc-gap{font-size:10px;font-weight:650;padding:9px 8px;border-radius:7px;margin-top:12px}.hf-doc-match{background:#e6f5ed;color:#287b5a}.hf-doc-gap{background:#fff3e7;color:#9d7040;margin-top:9px}.hf-doc-match span,.hf-doc-gap span{margin-right:7px}
    .hf-float{position:absolute;z-index:4;display:flex;align-items:center;gap:10px;background:#fff;border:1px solid #e4eee8;box-shadow:0 14px 35px #071e1a55;border-radius:12px;padding:11px 13px;animation:hf-float 5s ease-in-out infinite}.hf-float b{display:block;color:#1d4439;font-size:11px}.hf-float small{display:block;color:#7b9488;font-size:9px;margin-top:3px}.hf-float-icon{display:grid;place-items:center;width:32px;height:32px;background:#e2f4e9;color:#2b8a65;border-radius:9px;font-size:19px}.hf-float-human{background:#f8ebdb;color:#a57743}.hf-float-top{top:12px;right:-2%;animation-delay:-1s}.hf-float-bottom{bottom:10px;left:1%;animation-delay:-3s}
    .hf-art-spark{position:absolute;color:#b4ead3;font-size:24px;animation:hf-twinkle 4s ease-in-out infinite}.hf-spark-one{right:12%;bottom:28px}.hf-spark-two{left:8%;top:30px;animation-delay:-2s}
    @keyframes hf-float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}@keyframes hf-card{0%,100%{transform:rotate(-5deg) translateY(0)}50%{transform:rotate(-3deg) translateY(-8px)}}@keyframes hf-orbit{to{transform:rotate(360deg)}}@keyframes hf-pulse{50%{box-shadow:0 0 0 8px #77dfb600}}@keyframes hf-twinkle{50%{opacity:.25;transform:scale(.7)}}
    [data-testid="stMetric"]{transition:transform .2s ease,box-shadow .2s ease}[data-testid="stMetric"]:hover{transform:translateY(-3px);box-shadow:0 12px 28px #153e3614}
    @media(max-width:1050px){.hf-motion-hero{grid-template-columns:1fr .8fr;padding:27px}.hf-float-top{right:-6%}.hf-document-card{left:12%}}
    @media(max-width:750px){.hf-motion-hero{display:block;padding:27px 22px}.hf-hero-art{height:260px;margin-top:12px}.hf-document-card{left:24%}.hf-float-top{right:0}.hf-float-bottom{left:0}.hf-motion-hero h2{font-size:2.4rem!important}}
    @media(prefers-reduced-motion:reduce){.hf-motion-hero *,[data-testid="stMetric"]{animation:none!important;transition:none!important}.hf-motion-hero .hf-document-card{transform:rotate(-4deg)}}
    
/* Stage 3: expressive review studio; isolated to hf- classes. */
.hf-review-hero{position:relative;overflow:hidden;display:grid;grid-template-columns:1.15fr .85fr;min-height:320px;margin:1rem 0 1.25rem;padding:2.4rem 2.7rem;border-radius:26px;background:radial-gradient(circle at 84% 28%,#337b78 0,transparent 37%),linear-gradient(120deg,#102b35 0%,#193d42 48%,#29205b 100%);color:#fff;isolation:isolate;box-shadow:0 22px 55px rgba(15,37,47,.18)}
.hf-review-hero:before{content:'';position:absolute;width:400px;height:400px;border:1px solid rgba(183,255,231,.12);border-radius:50%;right:-100px;top:-180px;pointer-events:none}
.hf-rh-copy{position:relative;z-index:2;align-self:center}.hf-rh-kicker{font-size:.72rem;letter-spacing:.18em;font-weight:800;color:#b4f5dc}.hf-rh-copy h2{font-size:clamp(2.15rem,3.8vw,3.55rem)!important;line-height:1.1;color:#fff!important;letter-spacing:-.055em;margin:1rem 0}.hf-rh-copy h2 em{font-style:normal;background:linear-gradient(90deg,#a2f5c9,#d4b5ff);background-clip:text;-webkit-background-clip:text;color:transparent}.hf-rh-copy p{max-width:510px;color:#d5e6e6;font-size:1rem;line-height:1.8}.hf-rh-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1.4rem}.hf-rh-pills span{border:1px solid #ffffff35;border-radius:30px;padding:.42rem .75rem;background:#ffffff12;font-size:.8rem;color:#e7f9f3}
.hf-rh-scene{position:relative;min-height:280px;display:grid;place-items:center}.hf-rh-halo{position:absolute;width:245px;height:245px;border-radius:50%;border:1px dashed #b9f3de66;box-shadow:0 0 0 40px #ffffff06,0 0 0 85px #ffffff04;animation:hf-orbit 35s linear infinite}.hf-rh-sheet{position:relative;width:235px;padding:17px 17px 20px;border-radius:16px;background:linear-gradient(145deg,#fff,#e7f7f0);box-shadow:0 25px 60px #071b3066;transform:rotate(-8deg);animation:hf-float 6s ease-in-out infinite;color:#1e3b3c}.hf-rh-sheet-head{font-size:10px;letter-spacing:.08em;font-weight:800;border-bottom:1px solid #d9e5e0;padding-bottom:10px}.hf-rh-sheet-head span{float:right;color:#6a58df}.hf-rh-avatar{height:26px;width:26px;border-radius:50%;background:linear-gradient(135deg,#79d7ba,#7865d9);margin:14px 0}.hf-rh-line{height:7px;width:77%;border-radius:10px;background:#cbdcd7;margin:10px 0}.hf-rh-line.long{width:92%}.hf-rh-line.short{width:55%}.hf-rh-highlight{font-size:11px;font-weight:750;border-radius:8px;background:#d4f7e7;color:#216a58;padding:9px}.hf-rh-highlight.muted{background:#fff0df;color:#9a612e}.hf-rh-orbit{position:absolute;font-size:2rem;color:#c7b6ff;text-shadow:0 0 20px #9a79ff}.hf-rh-orbit.one{top:10%;right:8%;animation:hf-float 4s ease-in-out infinite}.hf-rh-orbit.two{bottom:13%;left:8%;color:#90eac4;animation:hf-float 5s ease-in-out infinite reverse}.hf-rh-tag{position:absolute;right:0;bottom:12%;padding:11px 14px;border:1px solid #ffffff44;border-radius:14px;background:#132b4bd9;backdrop-filter:blur(10px);font-size:.75rem;box-shadow:0 12px 30px #05152b66;animation:hf-float 5s ease-in-out infinite}
.hf-journey{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;margin:1.2rem 0;padding:1rem 1.2rem;border-radius:16px;background:#eff7f4;border:1px solid #dcece5}.hf-j-item{display:flex;align-items:center;gap:.55rem;color:#60776f;font-weight:700;font-size:.84rem}.hf-j-item.active{color:#176a58}.hf-j-num{display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:#e2e9e6;color:#5b716a;font-size:.75rem}.hf-j-item.active .hf-j-num{background:#176a58;color:#fff;box-shadow:0 0 0 5px #176a5819}.hf-j-item.done .hf-j-num{background:#c9eade;color:#155e50}.hf-j-separator{color:#9eb5ad;font-size:.65rem}
.hf-trace-card{display:flex;flex-direction:column;gap:.45rem;min-height:105px;border:1px solid #d9e8e1;border-radius:15px;padding:1rem;margin:.4rem 0;background:linear-gradient(145deg,#fff,#f0faf6);box-shadow:0 8px 22px #183c3010}.hf-trace-check{font-size:1.1rem;color:#21816a}.hf-trace-card small{font-size:.62rem;letter-spacing:.14em;color:#738a81;font-weight:800}.hf-trace-card strong{font-size:.85rem;color:#1d4840;overflow-wrap:anywhere}
.hf-queue-strip{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;margin:1rem 0 1.7rem}.hf-queue-stat{position:relative;display:flex;flex-direction:column;gap:.3rem;padding:1.4rem 1.5rem;border-radius:20px;border:1px solid #e3e9e7;background:#fff;box-shadow:0 10px 26px #102f2810;transition:transform .25s,box-shadow .25s}.hf-queue-stat:hover{transform:translateY(-5px);box-shadow:0 16px 36px #102f2820}.hf-queue-stat strong{font-size:2.15rem;line-height:1.1;color:#1c3d38}.hf-queue-stat small{font-size:.8rem;color:#61736d}.hf-queue-symbol{font-size:1.3rem}.hf-queue-stat.mint .hf-queue-symbol{color:#168e73}.hf-queue-stat.coral .hf-queue-symbol{color:#ca7757}.hf-queue-stat.amber .hf-queue-symbol{color:#bd8c3d}
@keyframes hf-orbit{to{transform:rotate(360deg)}}
@media(max-width:900px){.hf-review-hero{grid-template-columns:1fr;padding:1.8rem}.hf-rh-scene{min-height:270px}.hf-queue-strip{grid-template-columns:1fr 1fr}}@media(max-width:540px){.hf-queue-strip{grid-template-columns:1fr}.hf-review-hero{padding:1.4rem}.hf-rh-sheet{transform:scale(.9) rotate(-8deg)}}
@media(prefers-reduced-motion:reduce){.hf-rh-halo,.hf-rh-sheet,.hf-rh-orbit,.hf-rh-tag{animation:none!important}.hf-queue-stat{transition:none!important}}


/* STAGE 4 / THE EVIDENCE ATELIER — editorial collage, bold type, accessible contrast */
.stApp {background:#F5F1E9!important;}
.stMain .block-container{max-width:1360px;padding-top:1.1rem;}
[data-testid="stSidebar"]{background:#12382F!important;border-right:0!important;}
[data-testid="stSidebar"] .hf-brand{margin-bottom:1.2rem;}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"]{gap:5px;}
[data-testid="stSidebar"] [data-testid="stRadio"] label{border-radius:12px!important;transition:background .2s ease,transform .2s ease;}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover{transform:translateX(4px);background:#ffffff16!important;}
/* Hide native selection circles only within sidebar navigation; radio functionality retained. */
[data-testid="stSidebar"] [data-testid="stRadio"] label [data-testid="stMarkdownContainer"] p{font-weight:650!important;}
[data-testid="stSidebar"] [data-testid="stExpander"]{background:#214B3D!important;border:1px solid #70A18A!important;border-radius:15px!important;overflow:hidden;}
[data-testid="stSidebar"] [data-testid="stExpander"] summary{background:#DFF1DE!important;border:0!important;padding:13px 14px!important;}
[data-testid="stSidebar"] [data-testid="stExpander"] summary p{color:#153F33!important;font-weight:800!important;opacity:1!important;}
[data-testid="stSidebar"] [data-testid="stExpander"] summary svg{color:#153F33!important;}
[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"]{background:#214B3D!important;color:#F7F7E9!important;padding:14px!important;}
[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"] p,
[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"] small,
[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"] span{color:#F4F6E8!important;opacity:1!important;}
.hf-help-steps{color:#fff!important;}.hf-help-intro{display:flex;justify-content:space-between;font-size:11px;font-weight:850;letter-spacing:.12em;color:#B7E5C7!important}.hf-help-intro span{font-size:24px;color:#F6CB75!important}.hf-help-steps>p{font-size:13px;line-height:1.5;margin:8px 0 18px;color:#fff!important}.hf-help-item{display:flex;gap:12px;padding:12px 0;border-top:1px solid #ffffff32}.hf-help-item b{color:#F9D483!important;font-size:15px}.hf-help-item strong{display:block;color:#fff!important;font-size:13px}.hf-help-item small{display:block;color:#D4E9D9!important;line-height:1.5;margin-top:3px}
.hf-atelier-hero{position:relative;display:grid;grid-template-columns:1.03fr .97fr;overflow:hidden;isolation:isolate;min-height:515px;border-radius:8px 90px 8px 8px;background:#F6C5AC;box-shadow:13px 16px 0 #163C35;margin:8px 16px 46px 0;}
.hf-atelier-grain{position:absolute;inset:0;background:radial-gradient(circle at 30% 80%,#FCE9C3 0%,transparent 43%),radial-gradient(circle at 82% 15%,#C5B7F3 0%,transparent 38%);pointer-events:none}
.hf-atelier-copy{position:relative;z-index:3;padding:43px 0 35px 48px;display:flex;flex-direction:column;align-items:flex-start;}
.hf-atelier-topline{font-size:12px;letter-spacing:.1em;font-weight:900;color:#174337;display:flex;align-items:center;gap:13px}.hf-atelier-star{font-size:31px;line-height:1;animation:hf-spin 18s linear infinite}.hf-atelier-no{font-size:10px;letter-spacing:.04em;opacity:.65}
.hf-atelier-copy h1{font-family:Georgia,'Times New Roman',serif!important;font-size:clamp(3.8rem,6vw,7.6rem)!important;font-weight:700!important;line-height:.96!important;letter-spacing:-.075em!important;color:#12392F!important;margin:53px 0 27px!important;white-space:nowrap}.hf-atelier-copy h1 em{font-weight:400;color:#8A2F52;font-style:italic;}
.hf-atelier-copy>p{max-width:420px;font-size:17px;line-height:1.65;color:#254A40;margin:0 0 36px}
.hf-atelier-stamp{position:absolute;right:1%;bottom:87px;display:flex;align-items:center;gap:8px;transform:rotate(13deg);border:3px double #8A2F52;border-radius:50%;width:98px;height:98px;justify-content:center;font-size:16px;font-weight:900;line-height:1.1;color:#8A2F52;opacity:.85}.hf-atelier-stamp span{font-size:21px}
.hf-atelier-foot{margin-top:auto;display:flex;gap:22px;font-size:10px;letter-spacing:.08em;font-weight:850;color:#194F42}
.hf-atelier-scene{position:relative;min-height:500px;perspective:1100px}.hf-atelier-sun{position:absolute;inset:8% 5% 5% 5%;border-radius:48% 52% 55% 45%;background:#C6B2E9;transform:rotate(-13deg);animation:hf-blob 10s ease-in-out infinite alternate}.hf-atelier-halo{position:absolute;left:10%;top:7%;width:420px;height:420px;border:2px dashed #FFFFFF88;border-radius:50%;animation:hf-spin 38s linear infinite}
.hf-atelier-back-paper{position:absolute;left:15%;top:18%;width:235px;height:300px;background:#E0E8CF;border:2px solid #214E3B;box-shadow:12px 13px 0 #163D37;transform:rotate(-17deg);padding:20px;color:#1B4B3B;font-family:Georgia,serif;font-size:23px;font-weight:bold;line-height:1.1;animation:hf-paper-back 7s ease-in-out infinite}.hf-atelier-back-line{height:7px;background:#A6BFA7;margin-top:30px;border-radius:20px}.hf-atelier-back-line.short{width:65%;margin-top:12px}
.hf-atelier-paper{position:absolute;left:31%;top:12%;width:300px;min-height:370px;background:#FFFDF2;border:2px solid #1E453A;box-shadow:15px 19px 0 #153C34;transform:rotate(7deg);padding:21px 21px 18px;color:#1C4036;animation:hf-paper-front 7s ease-in-out infinite}.hf-paper-top{display:flex;align-items:center;gap:7px;font-size:9px;letter-spacing:.1em;font-weight:900;border-bottom:2px solid #204638;padding-bottom:12px}.hf-paper-top span:first-child{font-size:23px;color:#D16C69}.hf-paper-top span:last-child{margin-left:auto}.hf-paper-title{font-family:Georgia,serif;font-size:27px;font-weight:700;line-height:1.1;margin:25px 0}.hf-paper-line{height:7px;width:94%;border-radius:10px;background:#DCE6D7;margin:12px 0}.hf-paper-line.short{width:55%}.hf-paper-line.medium{width:75%}.hf-paper-highlight,.hf-paper-gap{font-size:12px;font-weight:800;padding:12px 10px;margin-top:17px;border-radius:2px}.hf-paper-highlight{background:#B9E5C5;color:#174D3D}.hf-paper-gap{background:#F9DFB8;color:#76502A}.hf-paper-bottom{border-top:1px dashed #9CB1A4;margin-top:22px;padding-top:10px;font-size:9px;letter-spacing:.09em;font-weight:900}
.hf-atelier-label{position:absolute;z-index:5;background:#193F36;color:#FFF9E8;font-size:10px;font-weight:900;letter-spacing:.1em;padding:12px 16px;border-radius:40px;box-shadow:6px 6px 0 #F7E3B3;animation:hf-label-float 5s ease-in-out infinite}.hf-atelier-label.one{top:10%;right:0;transform:rotate(10deg)}.hf-atelier-label.two{bottom:11%;left:4%;background:#8A2F52;animation-delay:-2s}.hf-atelier-flower{position:absolute;z-index:4;right:0;bottom:3%;font-size:110px;color:#E99D5D;line-height:1;animation:hf-spin 28s linear infinite}.hf-atelier-arrow{position:absolute;z-index:4;left:0;top:0;width:150px;transform:rotate(14deg)}
.hf-editorial-rule{display:flex;justify-content:space-between;border-top:2px solid #17463A;padding:11px 0;font-size:11px;letter-spacing:.13em;font-weight:900;color:#1C4D3E}.hf-editorial-heading{display:flex;justify-content:space-between;align-items:end;gap:25px;margin:22px 0 28px}.hf-editorial-heading small{font-size:11px;letter-spacing:.15em;font-weight:850;color:#8A2F52}.hf-editorial-heading h2{font-family:Georgia,serif!important;font-size:clamp(2rem,3.5vw,3.9rem)!important;line-height:1.08!important;letter-spacing:-.06em!important;margin:10px 0!important;color:#173C32!important}.hf-editorial-heading h2 i{color:#8A2F52;font-weight:400}.hf-editorial-heading p{max-width:290px;font-size:14px;line-height:1.65;color:#486057}
[data-testid="stMetric"]{border:2px solid #1F4B3D!important;border-radius:4px 22px 4px 4px!important;background:#FFF9E9!important;box-shadow:5px 6px 0 #D5E1CE!important;min-height:135px!important;padding:22px!important}
[data-testid="stMetric"] [data-testid="stMetricValue"]{font-family:Georgia,serif!important;font-size:3rem!important;color:#184637!important}
[data-testid="stMetric"]:nth-child(even){background:#F5E6F0!important}
.hf-review-hero{border-radius:5px 65px 5px 5px!important;background:radial-gradient(circle at 90% 10%,#E3B7CF 0,transparent 43%),linear-gradient(125deg,#153D35,#315F53 60%,#7B4C78)!important;}
.hf-queue-stat{border:2px solid #214B3F!important;border-radius:4px 28px 4px 4px!important;box-shadow:7px 8px 0 #D4D9C8!important}.hf-queue-stat:nth-child(2){background:#FFF0D8!important}.hf-queue-stat:nth-child(3){background:#F1E7F5!important}
@keyframes hf-spin{to{transform:rotate(360deg)}}@keyframes hf-blob{to{border-radius:58% 42% 43% 57%;transform:rotate(12deg) scale(1.05)}}@keyframes hf-paper-front{50%{transform:rotate(4deg) translateY(-15px)}}@keyframes hf-paper-back{50%{transform:rotate(-13deg) translateY(10px)}}@keyframes hf-label-float{50%{translate:0 -10px}}
@media(max-width:1150px){.hf-atelier-hero{grid-template-columns:1fr 1fr}.hf-atelier-copy{padding:32px 0 25px 30px}.hf-atelier-copy h1{font-size:clamp(3rem,5vw,5.4rem)!important}.hf-atelier-paper{left:22%;width:260px}.hf-atelier-back-paper{left:7%}.hf-atelier-label.one{right:0}.hf-atelier-stamp{display:none}}
@media(max-width:790px){.hf-atelier-hero{display:block;border-radius:5px 45px 5px 5px;margin-right:9px}.hf-atelier-copy{padding:30px}.hf-atelier-copy h1{margin:30px 0 20px!important;font-size:clamp(3.2rem,10vw,5.2rem)!important}.hf-atelier-scene{min-height:435px}.hf-atelier-paper{left:34%;top:5%}.hf-atelier-back-paper{left:18%;top:13%}.hf-atelier-foot{flex-wrap:wrap}.hf-editorial-heading{display:block}.hf-editorial-heading p{max-width:480px}.hf-atelier-label.one{right:4%}}
@media(max-width:480px){.hf-atelier-scene{min-height:365px;transform:scale(.76);transform-origin:top left;width:130%}.hf-atelier-paper{left:25%}.hf-atelier-copy>p{font-size:15px}.hf-atelier-label.one{right:5%}.hf-atelier-hero{overflow:hidden}.hf-editorial-rule{font-size:9px}.hf-atelier-foot{font-size:9px}}
@media(prefers-reduced-motion:reduce){.hf-atelier-hero *,[data-testid="stMetric"]{animation:none!important;transition:none!important}}


/* STAGE 5 — ONE VISUAL SYSTEM: GLOBAL HEADER + EDITORIAL NAVIGATION */
:root{--hf-header-height:84px}
.hf-global-header{position:fixed;z-index:999990;top:0;left:0;right:0;height:var(--hf-header-height);display:flex;align-items:center;justify-content:space-between;padding:0 clamp(20px,3.2vw,56px);background:#153D32;border-bottom:5px solid #E6A36F;box-shadow:0 4px 18px #132f291c;pointer-events:none}
.hf-global-header *{box-sizing:border-box}.hf-global-brand{display:flex;align-items:center;gap:14px}.hf-global-monogram{display:flex;align-items:center;justify-content:center;position:relative;width:49px;height:49px;border-radius:12px 12px 4px 12px;background:#F8EAD2;color:#173E32;font-family:Georgia,serif;font-size:30px;font-weight:900;box-shadow:4px 4px 0 #F2AF7D}.hf-global-monogram span{position:absolute;top:1px;right:3px;font:16px Georgia,serif;color:#AA3E61}.hf-global-title{font-family:Georgia,serif;font-size:28px;font-weight:800;color:#FFF8E9;line-height:1;letter-spacing:-.055em}.hf-global-title em{font-style:italic;font-weight:400;color:#F3B88B}.hf-global-title small{display:block;font:700 9px/1.5 system-ui,sans-serif;letter-spacing:.21em;color:#CDE6D5;margin-top:6px}.hf-global-right{display:flex;align-items:center;gap:23px}.hf-header-squiggle{font-size:35px;color:#F6B57F;animation:hf-spin 22s linear infinite}.hf-header-copy{font-family:Georgia,serif;font-style:italic;letter-spacing:.025em;font-size:15px;color:#F4D7C4}.hf-header-status{font:800 10px system-ui,sans-serif;letter-spacing:.12em;color:#173E32;background:#E4EFCF;border-radius:40px;padding:10px 14px;white-space:nowrap}.hf-header-status i{display:inline-block;width:7px;height:7px;background:#318A68;border-radius:50%;margin-right:7px;box-shadow:0 0 0 3px #318A6820}
/* The header is visual only; native Streamlit widgets remain fully functional. */
[data-testid="stAppViewContainer"]{padding-top:var(--hf-header-height)}
[data-testid="stHeader"]{top:var(--hf-header-height)!important;background:transparent!important}
[data-testid="stSidebar"]{top:var(--hf-header-height)!important;height:calc(100vh - var(--hf-header-height))!important;background:#E7EDDF!important;border-right:2px solid #C4D7C5!important}
[data-testid="stSidebar"]>div:first-child{background:#E7EDDF!important}
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"]{padding-top:22px!important}
[data-testid="stSidebar"] *{color:#1B4538}
.hf-rail-intro{padding:7px 6px 22px;border-bottom:1px solid #BDD1BF;margin-bottom:19px}.hf-rail-index{font-size:10px!important;letter-spacing:.17em;font-weight:900;color:#9B4761!important}.hf-rail-intro strong{display:block;font-family:Georgia,serif;font-size:28px;letter-spacing:-.045em;line-height:1.12;color:#194338!important;margin:13px 0 9px}.hf-rail-intro strong em{font-weight:400;color:#9A3C5D!important}.hf-rail-intro>span:last-child{font-size:12px;color:#577063!important}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"]{gap:8px!important}
[data-testid="stSidebar"] [data-testid="stRadio"] label{position:relative;min-height:48px;border:1px solid transparent;border-radius:6px 18px 6px 6px!important;padding:10px 10px!important;transition:background .2s,transform .2s!important}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover{background:#D4E3D3!important;transform:translateX(3px)}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked){background:#153D32!important;box-shadow:4px 5px 0 #E7AE82!important;border-color:#153D32!important}
[data-testid="stSidebar"] [data-testid="stRadio"] label [data-testid="stMarkdownContainer"] p{font-size:13px!important;font-weight:750!important;color:#204A3C!important}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) [data-testid="stMarkdownContainer"] p{color:#FFF9E9!important}
/* Hide default circles visually while retaining accessible native radio inputs. */
[data-testid="stSidebar"] [data-testid="stRadio"] label [data-baseweb="radio"]>div:first-child{opacity:0;width:0;min-width:0;margin:0;padding:0;overflow:hidden}
[data-testid="stSidebar"] [data-testid="stRadio"] label [data-testid="stMarkdownContainer"] p:before{display:inline-block;width:25px;margin-right:8px;font-size:18px;vertical-align:middle}
[data-testid="stSidebar"] [data-testid="stRadio"] label:nth-child(1) [data-testid="stMarkdownContainer"] p:before{content:"⌂"}
[data-testid="stSidebar"] [data-testid="stRadio"] label:nth-child(2) [data-testid="stMarkdownContainer"] p:before{content:"✎"}
[data-testid="stSidebar"] [data-testid="stRadio"] label:nth-child(3) [data-testid="stMarkdownContainer"] p:before{content:"▤"}
[data-testid="stSidebar"] [data-testid="stRadio"] label:nth-child(4) [data-testid="stMarkdownContainer"] p:before{content:"☷"}
.hf-rail-guide-label{margin:27px 4px 9px;font-size:10px;font-weight:900;letter-spacing:.11em;color:#8D4861!important;display:flex;justify-content:space-between}.hf-rail-guide-label span{font-size:17px;color:#C57C52!important}
[data-testid="stSidebar"] [data-testid="stExpander"]{background:#FFF8E9!important;border:2px solid #204A3C!important;border-radius:5px 18px 5px 5px!important;box-shadow:4px 5px 0 #C9D9C5!important}
[data-testid="stSidebar"] [data-testid="stExpander"] summary{background:#F5C8A9!important;padding:13px!important}
[data-testid="stSidebar"] [data-testid="stExpander"] summary p{color:#153D32!important}
[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"]{background:#FFF8E9!important}
[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"] p,[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"] small,[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"] span{color:#244C3D!important}
.hf-help-intro,.hf-help-intro span{color:#A0465E!important}.hf-help-item{border-color:#D8D9C7!important}.hf-help-item b{color:#A0475E!important}.hf-help-item strong{color:#153D32!important}.hf-help-item small{color:#4C6555!important}
[data-testid="stSidebar"] .hf-sidebar-footer{background:#D7E5D6!important;border:1px solid #A8C4AE!important;color:#244C3D!important;margin-top:24px}.hf-sidebar-footer small{color:#456554!important}
/* Remove the disconnected top gutter without touching the illustrated hero. */
.stMain .block-container{padding-top:1.25rem!important}
@media(max-width:850px){:root{--hf-header-height:72px}.hf-global-header{padding:0 15px}.hf-global-title{font-size:22px}.hf-global-monogram{width:40px;height:40px;font-size:24px}.hf-header-copy,.hf-header-squiggle{display:none}.hf-header-status{font-size:9px;padding:8px 10px}}
@media(max-width:530px){.hf-global-header{padding:0 12px}.hf-global-title{font-size:20px}.hf-global-title small{font-size:7px}.hf-header-status{font-size:0;padding:8px}.hf-header-status i{margin:0}}
@media(prefers-reduced-motion:reduce){.hf-header-squiggle{animation:none!important}}


/* STAGE 5.1 / Harmonized editorial layout — final overrides, no backend changes */
:root{--hf-header-height:76px;--hf-ink:#173D34;--hf-apricot:#EBC8B9;--hf-paper:#F7F2EA;--hf-sage:#E7EDE4;--hf-berry:#924C67}
.stApp{background-color:var(--hf-paper)!important;background-image:radial-gradient(circle at 75% 18%,rgba(216,204,233,.25),transparent 35%),radial-gradient(circle at 15% 75%,rgba(214,232,211,.3),transparent 35%),radial-gradient(#244b3c0b .65px,transparent .65px)!important;background-size:auto,auto,20px 20px!important}
.hf-global-header{background:var(--hf-ink)!important;border-bottom:3px solid #D7BBA8!important;box-shadow:none!important}
.hf-global-monogram{background:#F8EFE1!important;box-shadow:3px 3px 0 #CDAE9C!important}
.hf-global-title em{color:#EBC8B9!important}.hf-header-squiggle{color:#EBC8B9!important}.hf-header-copy{color:#F3E3D8!important}
[data-testid="stSidebar"]{background:var(--hf-sage)!important;border-right:1px solid #CAD9CA!important}
[data-testid="stSidebar"]>div:first-child{background:var(--hf-sage)!important}
/* Streamlit's internal sidebar block padding caused the large blank strip. */
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"]{padding-top:0!important}
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"]>.stVerticalBlock{gap:.55rem!important}
.hf-rail-intro{padding:8px 5px 14px!important;margin-bottom:6px!important;border-color:#C9D9CC!important}
.hf-rail-intro strong{font-size:26px!important;margin:8px 0!important}
.hf-rail-icons{display:flex;gap:8px;margin-top:15px}
.hf-rail-icons span{display:grid;place-items:center;width:38px;height:38px;border:1px solid #C6D8C8;border-radius:11px;background:#F9F6EE;color:#1C5947!important;font-size:20px;box-shadow:2px 3px 0 #D2DED1;transition:transform .2s ease}
.hf-rail-icons span:nth-child(2){background:#F3DCD0}.hf-rail-icons span:nth-child(3){background:#E5DDF0}.hf-rail-icons span:nth-child(4){background:#D5EAD8}
.hf-rail-icons span:hover{transform:translateY(-3px)}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked){box-shadow:3px 4px 0 #D3B6A5!important}
[data-testid="stSidebar"] [data-testid="stRadio"] label [data-testid="stMarkdownContainer"] p:before{font-size:19px!important;color:#246A53!important}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) [data-testid="stMarkdownContainer"] p:before{color:#F6E4D3!important}
[data-testid="stSidebar"] [data-testid="stExpander"] summary{background:#EBC8B9!important}
[data-testid="stSidebar"] [data-testid="stExpander"]{box-shadow:3px 4px 0 #CBD9CA!important}
.hf-rail-guide-label{margin-top:17px!important}
.hf-atelier-hero{background:#EECDBF!important;box-shadow:9px 11px 0 #214A3E!important;min-height:500px!important}
.hf-atelier-grain{background:radial-gradient(circle at 26% 76%,#F8E8D0 0%,transparent 43%),radial-gradient(circle at 83% 18%,#D8CBE9 0%,transparent 40%)!important}
.hf-atelier-sun{background:#D8CBE9!important}
.hf-atelier-copy h1 em{color:#924C67!important}
.hf-atelier-stamp{display:none!important}
.hf-scene-human-tag{position:absolute;z-index:7;left:3%;bottom:5%;background:#F7F1E7;border:2px solid #21483A;border-radius:50px;padding:10px 14px;color:#21483A;font-size:10px;letter-spacing:.11em;font-weight:900;transform:rotate(-6deg);box-shadow:3px 4px 0 #D6B3B8;white-space:nowrap}
.hf-atelier-label.two{bottom:16%!important}
.stMain .block-container{padding-top:1rem!important}
@media(max-width:900px){.hf-scene-human-tag{left:4%;bottom:1%;font-size:9px}.hf-rail-icons span{width:33px;height:33px}}
@media(max-width:530px){.hf-scene-human-tag{left:4%;bottom:0;transform:none}.hf-rail-icons{gap:5px}}
@media(prefers-reduced-motion:reduce){.hf-rail-icons span{transition:none!important}}


/* STAGE 5.2 — Layout repair. A single top offset: the fixed header is NOT
   added as padding to the entire Streamlit view (which displaced the rail). */
:root {--hf-header-height:76px;--hf-sage:#E7EDE4;--hf-paper:#F7F2EA;}
[data-testid="stAppViewContainer"] {padding-top:0!important; background:transparent!important;}
[data-testid="stSidebar"] {
  position:fixed!important; top:var(--hf-header-height)!important;
  bottom:0!important; height:calc(100dvh - var(--hf-header-height))!important;
  background:var(--hf-sage)!important; border-right:1px solid #B9CDBB!important;
}
[data-testid="stSidebar"]>div:first-child,
[data-testid="stSidebar"] [data-testid="stSidebarContent"],
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
  background:var(--hf-sage)!important;
}
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
  padding-top:0!important; margin-top:0!important;
}
[data-testid="stSidebar"] [data-testid="stSidebarContent"] {padding-top:0!important;}
/* Native Streamlit toolbar is kept available for deployment and debugging. */
[data-testid="stHeader"] {top:var(--hf-header-height)!important; background:transparent!important;}
.stMain .block-container {padding-top:calc(var(--hf-header-height) + 16px)!important;}
/* The backdrop is an illustrated editorial paper, not an empty flat fill. */
.stApp {
  background-color:#F7F2EA!important;
  background-image:
    radial-gradient(ellipse 340px 320px at 94% 28%,rgba(213,190,229,.43) 0%,transparent 75%),
    radial-gradient(ellipse 380px 300px at 10% 85%,rgba(234,191,172,.33) 0%,transparent 73%),
    radial-gradient(ellipse 280px 260px at 80% 92%,rgba(188,218,189,.35) 0%,transparent 74%),
    repeating-linear-gradient(0deg,transparent 0px,transparent 39px,rgba(28,75,59,.028) 40px),
    repeating-linear-gradient(90deg,transparent 0px,transparent 39px,rgba(28,75,59,.028) 40px)!important;
  background-attachment:fixed!important;
}
/* Whimsical decorative marks in the margin, never over text or controls. */
.stMain {position:relative;isolation:isolate;}
.stMain::before,.stMain::after {
  position:fixed;z-index:-1;pointer-events:none;line-height:1;
  font-family:Georgia,serif;font-weight:400;
}
.stMain::before {content:"✳";font-size:165px;color:rgba(165,86,113,.10);right:1.5vw;top:53vh;transform:rotate(-12deg);}
.stMain::after {content:"✿";font-size:135px;color:rgba(42,115,85,.10);left:21vw;bottom:3vh;transform:rotate(20deg);}
/* Bring the hero closer to the header, and retain illustrated separation. */
.hf-atelier-hero {margin-top:0!important;}
.hf-editorial-rule {border-top-width:2px!important;}
/* Small-screen rail is Streamlit-controlled: no forced overlay when collapsed. */
@media(max-width:850px) {
 :root {--hf-header-height:72px;}
 .stMain .block-container {padding-top:calc(var(--hf-header-height) + 12px)!important;}
 .stMain::before {font-size:85px;opacity:.5;}
 .stMain::after {display:none;}
}
@media(prefers-reduced-motion:reduce) {
 .stMain::before,.stMain::after {transform:none!important;}
}


/* STAGE 5.3 — structural reset: native Streamlit sidebar reserves its own width.
   The previous position:fixed rule caused the rail to overlay the hero. */
:root{--hf-header-height:76px;--hf-forest:#173E34;--hf-sage:#E8EEE6;--hf-ivory:#F7F1E8;--hf-peach:#EFC9B8;--hf-berry:#A45A70}
[data-testid="stAppViewContainer"]{padding-top:var(--hf-header-height)!important;background:transparent!important}
[data-testid="stSidebar"]{
  position:relative!important;top:auto!important;bottom:auto!important;
  height:calc(100dvh - var(--hf-header-height))!important;
  flex-shrink:0!important;z-index:10!important;
  background:var(--hf-sage)!important;
  border-right:1px solid #C5D5C7!important;
}
[data-testid="stSidebar"]>div:first-child,
[data-testid="stSidebar"] [data-testid="stSidebarContent"],
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"]{background:var(--hf-sage)!important}
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"]{padding-top:20px!important}
[data-testid="stHeader"]{top:var(--hf-header-height)!important}
.stMain{min-width:0!important;position:relative!important}
.stMain .block-container{padding-top:1.35rem!important;padding-left:clamp(18px,3vw,54px)!important;padding-right:clamp(18px,3vw,54px)!important;max-width:1500px!important}
.hf-global-header{background:var(--hf-forest)!important;border-bottom:3px solid #C8AFA1!important}
.hf-atelier-hero{background:#EFD3C5!important;max-width:100%!important;min-width:0!important}
.hf-atelier-grain{background:radial-gradient(circle at 25% 78%,#F7E9D8 0%,transparent 44%),radial-gradient(circle at 83% 18%,#D9D0E3 0%,transparent 42%)!important}
.hf-atelier-sun{background:#D9D0E3!important}
.hf-atelier-flower{color:#DFA27B!important}
.hf-atelier-copy h1 em{color:var(--hf-berry)!important}
.hf-rail-icons{display:none!important}
/* Real clickable radio labels, with an icon attached to each corresponding function. */
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label{
 display:flex!important;align-items:center!important;gap:10px!important;min-height:51px!important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label [data-testid="stMarkdownContainer"] p{
 display:flex!important;align-items:center!important;gap:12px!important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label [data-testid="stMarkdownContainer"] p::before{
 display:inline-grid!important;place-items:center!important;position:static!important;
 width:27px!important;height:27px!important;flex:0 0 27px!important;
 border-radius:8px!important;background:#F8F5ED!important;
 color:var(--hf-forest)!important;font-size:17px!important;line-height:1!important;
 box-shadow:1px 2px 0 #C7D8C7!important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label:nth-child(1) [data-testid="stMarkdownContainer"] p::before{content:"⌂"!important}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label:nth-child(2) [data-testid="stMarkdownContainer"] p::before{content:"✎"!important}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label:nth-child(3) [data-testid="stMarkdownContainer"] p::before{content:"▤"!important}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label:nth-child(4) [data-testid="stMarkdownContainer"] p::before{content:"☑"!important}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) [data-testid="stMarkdownContainer"] p::before{background:#F2D4C5!important;color:#173E34!important}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked){background:#173E34!important;box-shadow:3px 4px 0 #D2B6A7!important}
[data-testid="stSidebar"] [data-testid="stRadio"] label [data-baseweb="radio"]>div:first-child{opacity:0!important;width:0!important;min-width:0!important;margin:0!important}
.stApp{background-color:var(--hf-ivory)!important;background-image:
 radial-gradient(ellipse 340px 320px at 95% 26%,rgba(217,208,227,.32),transparent 78%),
 radial-gradient(ellipse 330px 310px at 10% 85%,rgba(239,201,184,.26),transparent 76%),
 repeating-linear-gradient(0deg,transparent 0,transparent 47px,rgba(23,62,52,.018) 48px),
 repeating-linear-gradient(90deg,transparent 0,transparent 47px,rgba(23,62,52,.018) 48px)!important}
@media(max-width:850px){.stMain .block-container{padding:1rem!important}[data-testid="stSidebar"]{height:calc(100dvh - var(--hf-header-height))!important}}


/* FINAL WATERCOLOR ATELIER — cohesive paint washes and crisp work surfaces */
:root {--hf-forest:#173E34;--hf-sage:#E8EEE6;--hf-ivory:#F8F3E9;--hf-peach:#EBC7B6;--hf-rose:#A66C80;}
.stApp {
 background-color:var(--hf-ivory)!important;
 background-image:
  radial-gradient(ellipse 410px 520px at 93% 26%,rgba(169,191,169,.24) 0%,rgba(169,191,169,.12) 48%,transparent 76%),
  radial-gradient(ellipse 460px 420px at 71% 78%,rgba(235,199,182,.26) 0%,rgba(235,199,182,.12) 50%,transparent 78%),
  radial-gradient(ellipse 360px 420px at 19% 42%,rgba(166,108,128,.10),transparent 75%),
  repeating-linear-gradient(0deg,rgba(71,65,48,.012) 0px,rgba(71,65,48,.012) 1px,transparent 1px,transparent 6px)!important;
}
[data-testid="stAppViewContainer"] {padding-top:76px!important;}
[data-testid="stSidebar"] {
 position:relative!important;top:auto!important;bottom:auto!important;
 height:calc(100dvh - 76px)!important;flex-shrink:0!important;
 background:#E8EEE6!important;border-right:1px solid #C9D8C8!important;
}
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {padding-top:18px!important;}
.stMain .block-container {padding-top:1.1rem!important;max-width:1460px!important;}
.hf-global-header {background:#173E34!important;border-bottom:2px solid #D5B5A7!important;}
.hf-rail-intro {padding-top:8px!important;}
/* Native radio remains fully keyboard operable; SVGs are decorative only. */
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label {
 display:flex!important;align-items:center!important;min-height:54px!important;
 border-radius:10px!important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label [data-testid="stMarkdownContainer"] p {
 display:flex!important;align-items:center!important;gap:12px!important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label [data-testid="stMarkdownContainer"] p::before {
 display:inline-block!important;position:static!important;flex:0 0 32px!important;
 width:32px!important;height:32px!important;border-radius:9px!important;
 box-shadow:none!important;border:1px solid #D3DDCE!important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label:nth-child(1) [data-testid="stMarkdownContainer"] p::before{content:""!important;background:#F9F5EC url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%23173E34%22%20stroke-width%3D%221.8%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpath%20d%3D%22m3%2010%209-7%209%207%22%2F%3E%3Cpath%20d%3D%22M5%209v12h14V9%22%2F%3E%3Cpath%20d%3D%22M9%2021v-8h6v8%22%2F%3E%3C%2Fsvg%3E") center/19px 19px no-repeat!important;}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label:nth-child(2) [data-testid="stMarkdownContainer"] p::before{content:""!important;background:#F9F5EC url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%23173E34%22%20stroke-width%3D%221.8%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpath%20d%3D%22M4%2020h16%22%2F%3E%3Cpath%20d%3D%22m14%204%206%206-9.5%209.5-6%201%201-6z%22%2F%3E%3Cpath%20d%3D%22m12%206%206%206%22%2F%3E%3C%2Fsvg%3E") center/19px 19px no-repeat!important;}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label:nth-child(3) [data-testid="stMarkdownContainer"] p::before{content:""!important;background:#F9F5EC url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%23173E34%22%20stroke-width%3D%221.8%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Crect%20x%3D%223%22%20y%3D%227%22%20width%3D%2218%22%20height%3D%2214%22%20rx%3D%222%22%2F%3E%3Cpath%20d%3D%22M8%207V5a2%202%200%200%201%202-2h4a2%202%200%200%201%202%202v2%22%2F%3E%3Cpath%20d%3D%22M3%2013h18%22%2F%3E%3C%2Fsvg%3E") center/19px 19px no-repeat!important;}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label:nth-child(4) [data-testid="stMarkdownContainer"] p::before{content:""!important;background:#F9F5EC url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%23173E34%22%20stroke-width%3D%221.8%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Crect%20x%3D%225%22%20y%3D%223%22%20width%3D%2214%22%20height%3D%2218%22%20rx%3D%222%22%2F%3E%3Cpath%20d%3D%22M9%203.5h6%22%2F%3E%3Cpath%20d%3D%22m8%2012%202%202%205-5%22%2F%3E%3Cpath%20d%3D%22M8%2018h8%22%2F%3E%3C%2Fsvg%3E") center/19px 19px no-repeat!important;}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
 background:#173E34!important;box-shadow:3px 3px 0 #D6B8AA!important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label [data-baseweb="radio"]>div:first-child {
 opacity:0!important;width:0!important;min-width:0!important;margin:0!important;
}
/* Painted-paper hero: softened washes instead of saturated flat shapes. */
.hf-atelier-hero {
 background:#F0D8C9!important;
 box-shadow:8px 10px 0 #214A3E!important;
 border-radius:10px 75px 10px 10px!important;
 margin:4px 10px 40px 0!important;
}
.hf-atelier-grain {
 background:
  radial-gradient(ellipse at 17% 85%,rgba(255,249,224,.86),transparent 55%),
  radial-gradient(ellipse at 82% 16%,rgba(195,188,217,.55),transparent 56%),
  radial-gradient(ellipse at 62% 80%,rgba(171,194,168,.25),transparent 62%)!important;
 filter:saturate(.82);
}
.hf-atelier-sun {background:#D9D0E3!important;opacity:.7;}
.hf-atelier-flower {color:#D79C7D!important;opacity:.85;}
.hf-atelier-copy h1 em {color:#985C72!important;}
.hf-atelier-copy h1 {white-space:normal!important;font-size:clamp(3.5rem,5.5vw,6.9rem)!important;}
.hf-atelier-stamp {pointer-events:none!important;}
/* Restrained brush-stroke details outside the working controls. */
.hf-editorial-heading {position:relative;}
.hf-editorial-heading::after {
 content:"✳";position:absolute;right:2%;top:0;font-size:60px;
 color:rgba(166,108,128,.20);transform:rotate(-14deg);pointer-events:none;
}
.stMain::before {color:rgba(166,108,128,.09)!important;right:1vw!important;}
.stMain::after {color:rgba(70,112,83,.10)!important;left:21vw!important;}
[data-testid="stMetric"],[data-testid="stPlotlyChart"],[data-testid="stForm"] {
 background:rgba(255,253,248,.94)!important;
 border-color:#DADFD3!important;
}
[data-testid="stMetric"] {border-radius:12px!important;}
[data-testid="stExpander"] {background:#FDFBF5!important;border-color:#C9D8C8!important;}
[data-testid="stSidebar"] [data-testid="stExpander"] {background:#F6E7DC!important;}
[data-testid="stSidebar"] [data-testid="stExpander"] * {color:#173E34!important;}
@media(max-width:950px) {
 .hf-atelier-copy h1 {font-size:clamp(2.8rem,5.4vw,5rem)!important;}
 .hf-editorial-heading::after {display:none;}
}
@media(max-width:790px) {
 .hf-atelier-hero {border-radius:10px 38px 10px 10px!important;}
 .hf-atelier-copy h1 {font-size:clamp(3rem,10vw,5rem)!important;}
}
@media(prefers-reduced-motion:reduce) {
 .hf-atelier-hero *, .hf-atelier-stamp {animation:none!important;transition:none!important;}
}


/* FINAL CONSISTENCY PATCH: icons now come from st.radio format_func, not brittle nth-child CSS. */
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label [data-testid="stMarkdownContainer"] p::before {
 content:none!important;display:none!important;background:none!important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] label [data-testid="stMarkdownContainer"] p {
 font-family:system-ui,-apple-system,"Segoe UI",sans-serif!important;
 font-size:14px!important;font-weight:650!important;letter-spacing:0!important;
}
/* Replace Streamlit's default violet-tinted controls with warm, accessible neutrals. */
.stMain div[data-baseweb="select"]>div,
.stMain div[data-baseweb="input"]>div,
.stMain div[data-baseweb="textarea"]>div,
.stMain .stTextInput input,
.stMain .stTextArea textarea {
 background:#FFFCF6!important;color:#173E34!important;
 border-color:#C7D6C8!important;
}
.stMain input:focus,.stMain textarea:focus {outline-color:#417D69!important;}
.stMain button[kind="primary"],
.stMain button[data-testid="stBaseButton-primary"],
.stMain .stFormSubmitButton button[kind="primary"] {
 background:#173E34!important;border:1px solid #173E34!important;
 color:#FFFCF6!important;box-shadow:3px 4px 0 #D4B4A5!important;
}
.stMain button[kind="primary"]:hover,
.stMain button[data-testid="stBaseButton-primary"]:hover {
 background:#2C6454!important;border-color:#2C6454!important;
}
.stMain [data-testid="stForm"] {background:#FFFCF7!important;border:1px solid #D4DCD0!important;}

</style>""", unsafe_allow_html=True)
