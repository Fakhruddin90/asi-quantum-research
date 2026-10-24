import glob,os
parts=["hero","asi","quantum","relationship","business","conclusion"]
body="\n".join(open(f"sections/{p}.html").read() for p in parts)
css="".join(f'<link rel="stylesheet" href="css/{os.path.basename(f)}">\n' for f in ["css/base.css"]+sorted(glob.glob("css/sec-*.css")))
nav='<nav class="top"><b>ASI × Quantum</b><a href="#overview">Overview</a><a href="#asi">Superintelligence</a><a href="#quantum">Quantum</a><a href="#relationship">Relationship</a><a href="#business">Business</a><a href="#conclusion">Verdict</a></nav>'
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Superintelligence × Quantum Computing — Research &amp; Business Guide</title><meta name="description" content="Deep research on how superintelligence and quantum computing relate, and where the business value is."><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
{css}</head><body>{nav}<main>{body}</main><script src="js/main.js"></script></body></html>'''
open("index.html","w").write(html);print("built",len(html))
