# generates /og/<slug>.jpg (1200x630) in the studio palette
# run: python3 _tools/og.py
from PIL import Image, ImageDraw, ImageFont
import random
NAVY=(0,35,102); CREAM=(250,235,215); GREY=(160,160,160)
ROCK="/System/Library/Fonts/Supplemental/Rockwell.ttc"
MONO="/System/Library/Fonts/Supplemental/Courier New.ttf"
CARDS={
 "home":("silence is\na material","arnaud leroy + studio","lisbon + paris + tokyo"),
 "projects":("the archive\nof works","arnaud leroy + projects","data + digital + architecture + fashion"),
 "studio":("the perfect amount\nof something","arnaud leroy + studio","creative direction + data platforms"),
 "benchgecko":("bench\ngecko.","project 11 + the ai economy tracked","arnaud leroy + studio"),
 "coffeetrove":("coffee\ntrove.","project 10 + the golden pages of coffee","arnaud leroy + studio"),
 "facil":("facil.guide","project 09 + technology simplified","arnaud leroy + studio"),
 "dropthe":("drop\nthe_","project 08 + drop the noise keep the data","arnaud leroy + studio"),
 "oracle":("the\noracle","project 07 + computational divination","arnaud leroy + studio"),
 "arcade":("system\nevasion","project 06 + reactive arcade","arnaud leroy + studio"),
 "wooden-wall":("porous\nboundary","project 05 + timber joinery","arnaud leroy + studio"),
 "flooring":("broken\ngrid","project 04 + floor transition","arnaud leroy + studio"),
 "tree-knowledge":("tree of all\nknowledge","project 03 + visualization engine","arnaud leroy + studio"),
 "maison-automata":("maison\nautomata","project 02 + robotic fashion house","arnaud leroy + studio"),
 "birth-studio":("birth of\nthe studio","project 01 + origin + manifesto","arnaud leroy + studio"),
 "blog":("technical\nnotes","arnaud leroy + blog","building systems + shipping products"),
 "blog-knowledge-graph":("1.8 million\nentities","building a knowledge graph","arnaud leroy + blog"),
 "blog-golden-drop":("440,000\ncafes","designing a scoring system","arnaud leroy + blog"),
}
def card(slug,title,sub,foot):
    W,H=1200,630
    im=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(im)
    rnd=random.Random(slug)
    # grain
    for _ in range(9000):
        x,y=rnd.randrange(W),rnd.randrange(H); c=rnd.randrange(8,26)
        d.point((x,y),fill=(NAVY[0]+c,NAVY[1]+c,NAVY[2]+c))
    # axis lines + labels like the site
    for x in (40,W-40): d.line([(x,0),(x,H)],fill=(40,70,130),width=1)
    big=ImageFont.truetype(ROCK,96,index=2) if True else None
    mono=ImageFont.truetype(MONO,22); small=ImageFont.truetype(MONO,17)
    d.text((100,70),"arnaud leroy",font=ImageFont.truetype(ROCK,26,index=2),fill=CREAM)
    d.multiline_text((100,170),title,font=big,fill=CREAM,spacing=6)
    d.text((100,470),sub,font=mono,fill=CREAM)
    d.text((100,520),foot,font=small,fill=GREY)
    pf=ImageFont.truetype(ROCK,260,index=2)
    d.text((W-250,H-330),"+",font=pf,fill=(250,235,215))
    im.save(f"og/{slug}.jpg",quality=85,optimize=True)
for k,v in CARDS.items(): card(k,*v)
print("ok",len(CARDS))
