# rebuilds the <head> of every page from one table + writes json-ld
# run from repo root: python3 _tools/head.py
import re, json
SITE="https://arnaudleroy.com"
PERSON={"@id":SITE+"/#arnaud"}
STUDIO={"@id":SITE+"/#studio"}
# file: path, title, description, og title, og desc, og image slug, kind, extra
P={
 "index.html":("/","arnaud leroy + studio + silence is a material","Arnaud Leroy is a designer and builder in Lisbon, Paris and Tokyo. His studio makes data platforms like BenchGecko, CoffeeTrove and DropThe, apps and games.","arnaud leroy + studio","silence is a material + design + data platforms + quiet systems","home","home",None),
 "projects.html":("/projects.html","projects + arnaud leroy + studio archive","The archive of works by Arnaud Leroy: BenchGecko, CoffeeTrove, facil.guide, DropThe, The Oracle, System Evasion and architecture and fashion research.","arnaud leroy + projects","the archive of works + data + digital + architecture + fashion + research","projects","collection",None),
 "studio.html":("/studio.html","studio + about arnaud leroy","About Arnaud Leroy and his studio, founded in 2024 at the intersection of fashion, visual culture, data and pure creation. Silence is a material.","arnaud leroy + studio","silence is a material + it is the perfect amount of something","studio","about",None),
 "journal.html":("/journal.html","journal + arnaud leroy","Journal of Arnaud Leroy Studio. Notes on brutalism, digital texture, and silence.","arnaud leroy + journal","notes on brutalism + digital texture + silence","home","page",None),
 "contact.html":("/contact.html","contact + arnaud leroy","Contact Arnaud Leroy Studio for new business and collaborations. Lisbon, with satellites in Paris and Tokyo.","arnaud leroy + contact","new business + inquiries","home","contact",None),
 "game.html":("/game.html","system evasion + a hidden arcade game + arnaud leroy","System Evasion: a minimal arcade game hidden inside the studio website. Avoid the noise, catch the plus, turn off the lights for Nightmare Drive.","system evasion + arcade","avoid the noise + catch the plus + turn off the lights","arcade","game",None),
 "404.html":(None,"signal lost","Signal lost. This page does not exist.","signal lost","404 + void detected","home","noindex",None),
 "secret.html":(None,"arnaud leroy + ???","You have found the backstage.","arnaud leroy + ???","you have found the backstage","home","noindex",None),
 "project-benchgecko.html":("/project-benchgecko.html","benchgecko + the ai economy tracked + arnaud leroy","BenchGecko by Arnaud Leroy: the AI economy, tracked. Models, benchmarks, pricing, companies and compute, refreshed daily by bots with sources and dates.","benchgecko + the ai economy tracked","models + benchmarks + pricing + companies + compute + measured daily","benchgecko","work",{"name":"BenchGecko","url":"https://benchgecko.ai","year":"2026","type":"WebApplication","cat":"AI data platform"}),
 "project-coffeetrove.html":("/project-coffeetrove.html","coffeetrove + the golden drop score + arnaud leroy","CoffeeTrove by Arnaud Leroy: the golden pages of coffee. The Golden Drop score ranks cafes worldwide on what can be known, with a bonus for independents.","coffeetrove + the golden pages of coffee","one honest number for every cafe","coffeetrove","work",{"name":"CoffeeTrove","url":"https://coffeetrove.com","year":"2026","type":"WebApplication","cat":"Coffee discovery platform"}),
 "project-facil.html":("/project-facil.html","facil.guide + tech guides for seniors + arnaud leroy","facil.guide by Arnaud Leroy: technology simplified for seniors. Step by step guides in 5 languages, static, accessible and free forever.","facil.guide + technology simplified","step by step guides in 5 languages","facil","work",{"name":"facil.guide","url":"https://facil.guide","year":"2026","type":"WebSite","cat":"Accessibility guides"}),
 "project-dropthe.html":("/project-dropthe.html","dropthe + data utility network + arnaud leroy","DropThe by Arnaud Leroy: a data utility network covering AI, technology, money and society, backed by a knowledge graph. Drop the noise, keep the data.","dropthe + drop the noise keep the data","a data utility network backed by a knowledge graph","dropthe","work",{"name":"DropThe","url":"https://dropthe.org","year":"2026","type":"WebSite","cat":"Data media platform"}),
 "project-the-oracle.html":("/project-the-oracle.html","the oracle + ios activation engine + arnaud leroy","The Oracle by Arnaud Leroy: an iOS and watchOS activation engine built to break executive dysfunction. Shake the device, receive one instruction, sit with it.","the oracle + computational divination","shake the device + receive one instruction","oracle","work",{"name":"The Oracle","year":"2025","type":"SoftwareApplication","cat":"iOS + watchOS app"}),
 "project-arcade.html":("/project-arcade.html","system evasion + reactive arcade + arnaud leroy","System Evasion by Arnaud Leroy: a reactive arcade engine in pure code. Time dilation, glitch storms, combo architecture and a dark mode Nightmare Drive.","system evasion + reactive arcade","time dilation + glitch storms + nightmare drive","arcade","work",{"name":"System Evasion","url":SITE+"/game.html","year":"2025","type":"VideoGame","cat":"Browser arcade game"}),
 "project-wooden-wall.html":("/project-wooden-wall.html","porous boundary + timber wall study + arnaud leroy","Porous Boundary by Arnaud Leroy: architectural study of a wooden structural wall. Permeability, habitable thickness and a gradient of privacy.","porous boundary + timber joinery","a wall that is not a line but a volume","wooden-wall","work",{"name":"Porous Boundary","year":"2025","type":"CreativeWork","cat":"Architecture study"}),
 "project-flooring.html":("/project-flooring.html","broken grid + floor transition study + arnaud leroy","Broken Grid by Arnaud Leroy: interior study of a floor where kitchen tile dissolves into oak parquet instead of ending at a threshold strip.","broken grid + controlled error","the tile does not end + it dissolves","flooring","work",{"name":"Broken Grid","year":"2025","type":"CreativeWork","cat":"Interior study"}),
 "project-tree-knowledge.html":("/project-tree-knowledge.html","tree of all knowledge + visualization engine + arnaud leroy","Tree of All Knowledge by Arnaud Leroy: a data visualization engine and interactive encyclopedia mapping the evolution of technology.","tree of all knowledge","visualization engine + encyclopedia","tree-knowledge","work",{"name":"Tree of All Knowledge","year":"2025","type":"CreativeWork","cat":"Data visualization"}),
 "project-maison-automata.html":("/project-maison-automata.html","maison automata + robotic fashion house + arnaud leroy","Maison Automata by Arnaud Leroy: a robotic fashion house exploring the protocol of synthetic tailoring, clothing the machine to give it presence.","maison automata + anima machina","robotic fashion house + synthetic tailoring","maison-automata","work",{"name":"Maison Automata","url":"https://maisonautomata.com","year":"2025","type":"CreativeWork","cat":"Fashion research"}),
 "project-birth-studio.html":("/project-birth-studio.html","birth of the studio + manifesto + arnaud leroy","The origin story and manifesto of Arnaud Leroy Studio: silence as a material, the plus as identity, the syntax of absence.","birth of the studio + manifesto","silence is a material + the syntax of absence","birth-studio","work",{"name":"Birth of the Studio","year":"2024","type":"CreativeWork","cat":"Manifesto"}),
 "blog/index.html":("/blog/","blog + technical notes + arnaud leroy","Technical notes by Arnaud Leroy on building data platforms, scoring systems and knowledge graphs.","arnaud leroy + blog","technical notes + building systems + shipping products","blog","blogindex",None),
 "blog/building-dropthe-knowledge-graph.html":("/blog/building-dropthe-knowledge-graph.html","building a knowledge graph with 1.8 million entities + arnaud leroy","How Arnaud Leroy built DropThe's entity system: a Postgres knowledge graph linking 1.8 million entities with 2.9 million links, and the discipline behind it.","building a knowledge graph with 1.8 million entities","postgres + an entity table + a links table + discipline","blog-knowledge-graph","post",{"headline":"Building a Knowledge Graph with 1.8 Million Entities","date":"2026-03-28","about":"project-dropthe.html"}),
 "blog/coffeetrove-golden-drop-scoring.html":("/blog/coffeetrove-golden-drop-scoring.html","designing a scoring system for 440,000 cafes + arnaud leroy","How Arnaud Leroy designed CoffeeTrove's Golden Drop score: turning incomplete cafe data into fair rankings for 440,000 cafes, with a bonus for independents.","designing a scoring system for 440,000 cafes","the golden drop score + values encoded as math","blog-golden-drop","post",{"headline":"Designing a Scoring System for 440,000 Cafes","date":"2026-03-25","about":"project-coffeetrove.html"}),
}
def esc(x): return x.replace('&','&amp;').replace('"','&quot;')
def crumbs(items):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":SITE+u} for i,(n,u) in enumerate(items)]}
def ld_for(f):
    path,title,desc,ogt,ogd,og,kind,x=P[f]
    url=SITE+(path or "/")
    g=[]
    if kind=="home":
        g=[{"@type":"Person","@id":PERSON["@id"],"name":"Arnaud Leroy","url":SITE,"image":SITE+"/apple-touch-icon.png","jobTitle":"Designer + Builder","worksFor":STUDIO,
            "knowsAbout":["data platforms","knowledge graphs","creative direction","product design","AI economy data"],
            "sameAs":["https://github.com/arnaudleroy-studio"]},
           {"@type":"Organization","@id":STUDIO["@id"],"name":"Arnaud Leroy Studio","url":SITE,"logo":SITE+"/apple-touch-icon.png","slogan":"Silence is a material","foundingDate":"2024","founder":PERSON,
            "location":[{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":c,"addressCountry":k}} for c,k in (("Lisbon","PT"),("Paris","FR"),("Tokyo","JP"))]},
           {"@type":"WebSite","@id":SITE+"/#site","url":SITE,"name":"arnaud leroy + studio","publisher":STUDIO,"author":PERSON}]
    elif kind=="work":
        w={"@type":x["type"],"name":x["name"],"description":desc,"creator":PERSON,"author":PERSON,"dateCreated":x["year"],"image":f"{SITE}/og/{og}.jpg","mainEntityOfPage":url}
        if "url" in x: w["url"]=x["url"]
        if x["type"] in ("WebApplication","SoftwareApplication"):
            w["applicationCategory"]=x["cat"]; w["operatingSystem"]="Web" if x["type"]=="WebApplication" else "iOS, watchOS"
        else: w["genre"]=x["cat"]
        g=[w,crumbs([("arnaud leroy","/"),("projects","/projects.html"),(x["name"].lower(),path)])]
    elif kind=="post":
        g=[{"@type":"BlogPosting","headline":x["headline"],"description":desc,"datePublished":x["date"],"dateModified":"2026-10-06","author":PERSON,"publisher":STUDIO,
            "image":f"{SITE}/og/{og}.jpg","url":url,"mainEntityOfPage":url,"about":{"@id":SITE+"/"+x["about"]}},
           crumbs([("arnaud leroy","/"),("blog","/blog/"),(x["headline"].lower(),path)])]
    elif kind in ("collection","blogindex"):
        g=[{"@type":"CollectionPage","name":ogt,"url":url,"description":desc,"author":PERSON},crumbs([("arnaud leroy","/"),(ogt.split(" + ")[-1],path)])]
    elif kind=="about":
        g=[{"@type":"AboutPage","url":url,"name":ogt,"mainEntity":PERSON},crumbs([("arnaud leroy","/"),("studio",path)])]
    elif kind=="contact":
        g=[{"@type":"ContactPage","url":url,"name":ogt,"mainEntity":STUDIO}]
    elif kind=="game":
        g=[{"@type":"VideoGame","name":"System Evasion","url":url,"description":desc,"author":PERSON,"gamePlatform":"Web browser","genre":"Arcade"}]
    if not g: return ""
    data={"@context":"https://schema.org","@graph":g}
    body=json.dumps(data,indent=2,ensure_ascii=False)
    return '    <script type="application/ld+json">\n'+"\n".join("    "+l for l in body.split("\n"))+'\n    </script>'
def head(f):
    path,title,desc,ogt,ogd,og,kind,x=P[f]
    url=SITE+(path or "/"); noindex = kind=="noindex"
    t="article" if kind in ("work","post") else "website"
    L=['    <meta charset="UTF-8">','    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
       f'    <title>{title}</title>',f'    <meta name="description" content="{esc(desc)}">','    <meta name="author" content="Arnaud Leroy">']
    L.append('    <meta name="robots" content="noindex">' if noindex else f'    <link rel="canonical" href="{url}">')
    L+=[f'    <meta property="og:type" content="{t}">','    <meta property="og:site_name" content="arnaud leroy + studio">','    <meta property="og:locale" content="en_US">',
        f'    <meta property="og:title" content="{esc(ogt)}">',f'    <meta property="og:description" content="{esc(ogd)}">',f'    <meta property="og:url" content="{url}">',
        f'    <meta property="og:image" content="{SITE}/og/{og}.jpg">',f'    <meta property="og:image:alt" content="{esc(ogt)}">','    <meta property="og:image:width" content="1200">','    <meta property="og:image:height" content="630">',
        '    <meta name="twitter:card" content="summary_large_image">',f'    <meta name="twitter:title" content="{esc(ogt)}">',f'    <meta name="twitter:description" content="{esc(ogd)}">',f'    <meta name="twitter:image" content="{SITE}/og/{og}.jpg">']
    if kind=="post":
        L+=[f'    <meta property="article:published_time" content="{x["date"]}">','    <meta property="article:modified_time" content="2026-10-06">','    <meta property="article:author" content="Arnaud Leroy">']
    L+=['    <meta name="theme-color" content="#FAEBD7" media="(prefers-color-scheme: light)">','    <meta name="theme-color" content="#002366" media="(prefers-color-scheme: dark)">',
        '    <link rel="icon" type="image/svg+xml" href="/favicon.svg">','    <link rel="icon" href="/favicon.ico" sizes="any">','    <link rel="apple-touch-icon" href="/apple-touch-icon.png">',
        '    <meta name="apple-mobile-web-app-title" content="+">','    <link rel="author" href="/humans.txt">','    <link rel="sitemap" type="application/xml" href="/sitemap.xml">',
        '    <link rel="preconnect" href="https://fonts.googleapis.com">','    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '    <!-- rockwell first + roboto slab only where rockwell is not installed -->',
        '    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap">',
        '    <link rel="stylesheet" href="/style.css">','    <script src="/components.js" defer></script>']
    return "\n".join(L)
for f in P:
    s=open(f).read()
    m=re.search(r'<head>(.*?)</head>', s, re.S)
    styles=re.findall(r'[ \t]*<style>.*?</style>', m.group(1), re.S)
    ld=ld_for(f)
    new="<head>\n"+head(f)+("\n"+ld if ld else "")+("\n"+"\n".join(styles) if styles else "")+"\n</head>"
    s=s[:m.start()]+new+s[m.end():]
    open(f,'w').write(s)
print("heads rebuilt:",len(P))
