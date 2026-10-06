# writes the "next project" trail at the bottom of every project page
# run from repo root: python3 _tools/links.py
import re
ORDER=[("project-benchgecko.html","benchgecko","11"),("project-coffeetrove.html","coffeetrove","10"),("project-facil.html","facil.guide","09"),
("project-dropthe.html","dropthe","08"),("project-the-oracle.html","the oracle","07"),("project-arcade.html","system evasion","06"),
("project-wooden-wall.html","porous boundary","05"),("project-flooring.html","broken grid","04"),("project-tree-knowledge.html","tree of knowledge","03"),
("project-maison-automata.html","maison automata","02"),("project-birth-studio.html","birth of the studio","01")]
START="<!-- [ TRAIL ] -->"; END="<!-- [ /TRAIL ] -->"
for i,(f,name,num) in enumerate(ORDER):
    nf,nn,nnum=ORDER[(i+1)%len(ORDER)]
    pf,pn,pnum=ORDER[i-1]
    block=f'''{START}
        <div class="project-trail mono-font" role="navigation" aria-label="more projects">
            <a href="/{pf}" class="trail-link">&lt; {pnum} <span class="plus">+</span> {pn}</a>
            <a href="/projects.html" class="trail-link trail-archive">archive</a>
            <a href="/{nf}" class="trail-link">{nnum} <span class="plus">+</span> {nn} &gt;</a>
        </div>
        {END}'''
    s=open(f).read()
    s=re.sub(re.escape(START)+r'.*?'+re.escape(END)+r'\s*','',s,flags=re.S)
    idx=s.rindex('</main>')
    s=s[:idx]+"    "+block+"\n    "+s[idx:]
    open(f,'w').write(s)
print("trail ok")
