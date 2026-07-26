# hi code lurker

import random
import math
import os
import time
args=discord["variables"]["__args"]
if args:
    arg=args[0]
else:
    arg=None
attributes={
"Ball": 1,
"Common": 2,
"Uncommon": 4,
"Good": 5,
"Natural": 8,
"Rare": 16,
"Divinus": 32,
"Crystallized": 64,
"Dizzy": 123,
"Rage": 128,
"Topaz": 150,
"Ruby": 350,
"Forbidden": 403,
"Emerald": 500,
"Gilded": 512,
"Ink": 700,
"Jackpot": 777,
"Sapphire": 800,
"Aquamarine": 900,
"Wind": 900,
"Diaboli": 1004,
"Penumbra": 1010,
"Umbra": 1010,
"Precious": 1024,
"Hydrogen": 1111,
"Atomic": 1180,
"Glock": 1700,
"Magnetic": 2048,
"Ash": 2300,
"Glacier": 2304,
"Player": 3000,
"Flora": 3700,
"Cola": 3999,
"Sidereum": 4096,
"Bleeding": 4444,
"Flutter": 5000,
"Targeted": 5000,
"Flushed": 6900,
"Hazard": 7000,
"Doodle": 7500,
"Quartz": 8192,
"Honey": 8335,
"Lost Soul": 9200,
"Atomic:Ribonucleic": 9876,
"★": 10000,
"Undead": 12000,
"Corrosive": 12000,
"Kawaii": 12300,
"Rage:Heated": 12800,
"Ink:LEAK": 14000,
"Powered": 16384,
"Gilded:Crowned": 20000,
"Marsh": 25000,
"Copper": 29000,
"WATT": 32768,
"Aquatic": 40000,
"Solar": 50000,
"Lunar": 50000,
"STARLIGHT": 50000,
"Star Rider": 50000,
"Pleiades": 65358,
"Flushed:Lobotomy": 69000,
"HAZARD:RAYS": 70000,
"Nautilus": 70000,
"Permafrost": 73500,
"Pulsar": 83345,
"Constella": 86988,
"Flow": 87000,
"Stormal": 90000,
"FAULT": 90000,
"Exotic": 99999,
"★★": 100000,
"Eclipse": 100032,
"DIABOLI : VOID": 100400,
"COMET": 120000,
"Divinus : Angel": 120000,
"Jade": 125000,
"Spectre": 140000,
"Jazz": 160000,
"Aether": 180000,
"BOUNDED": 200000,
"Lantern": 333333,
"Celestial": 350000,
"Vortex": 399999,
"TERROR": 400000,
"HOPE": 488725,
"Raven": 500000,
"Warlock": 666000,
"UNDEAD : DEVIL": 666666,
"Kyawthuite": 850000,
"★★★": 1000000,
"Arcane": 1000000,
"STARLIGHT:KUNZITE": 1000000,
"ゴシック": 1000001,
"Magnetic : Reverse Polarity": 1024000,
"Undefined": 1111000,
"Rage:Brawler": 1280000,
"symbiosis": 1331201,
"Astral": 1336000,
"Cosmos": 1520000,
"Obsidian": 1750000,
"Archmage": 1766000,
"Player:Respawn": 1999999,
"Gravitational": 2000000,
"UNBOUND": 2000000,
"Buggify": 2000000,
"FLOWED": 2121121,
"Virtual": 2500000,
"Vega": 2580000,
"PARASITE": 3000000,
"Orion": 3000000,
"Apatite": 3133133,
"Savior": 3200000,
"Shiftlock": 3325000,
"Evanescent": 3360000,
"Cosmos:Alice": 3500000,
"Bejeweled": 3600000,
"Aquatic:Flame": 4000000,
"Poseidon": 4000000,
"METABYTES": 4000000,
"WRAITH": 4100000,
"Zeus": 4500000,
"Solar:Solstice": 5000000,
"Galaxy": 5000000,
"Lunar:Full Moon": 5000000,
"Anima": 5730000,
"Twilight": 6000000,
"ASTRONAUT": 6117186,
"Origin": 6500000,
"HADES": 6666666,
"CELESTIAL✰DIVINE": 7000000,
"Anubis": 7200000,
"Refraction": 7242000,
"Faith": 7250000,
"Hyper-Volt": 7500000,
"VELOCITY": 7630000,
"Nautilus:Lost": 7700000,
"Divinus:Guardian": 7777777,
"OUTLAW": 8000000,
"SPECTRE:REQUIEM": 8222000,
"Soultorn": 8333333,
"HARNESSED": 8500000,
"Nihility": 9000000,
"Helios": 9000000,
"Stargazer": 9200000,
"Jade//Purity": 9250000,
"Amethyst": 9333700,
"Starscourge": 10000000,
"Sharkyn": 10000000,
"Guardian": 10000000,
"Empty": 11111111,
"Melodic": 11300000,
"Sailor": 12000000,
"Graffiti": 12000000,
"Glitch": 12110110,
"Imaginary": 12200200,
"Borealis": 13333333,
"Stormal:Hurricane": 13500000,
"CellAstroides": 13770000,
"Sirius": 14000000,
"Arcane:Legacy": 15000000,
"Icarus": 15660000,
"Lullaby": 17000000,
"Chromatic": 20000000,
"Plasma": 20600000,
"Oculus": 23233340,
"Aviator": 24000000,
"Ruby:Brimstone": 24060000,
"Apotheosis": 24691356,
"Centurion": 25000000,
"Blizzard": 27315000,
"Arcane:Dark": 30000000,
"Flora:Florest": 32800000,
"Ethereal": 35000000,
"Virtual:Fatal Error": 40413000,
"Juxtaposition": 40440400,
"Overseer": 45000000,
"Exotic:Apex": 49999500,
"Matrix": 50000000,
"Runic": 50000000,
"Sentinel": 60000000,
"Twilight:IridescentMemory": 60000000,
"Antivirus": 62500000,
"Chromatic-HYPER": 68982670,
"Dominion": 70000000,
"Starborn": 72000000,
"Melodic:Serenade": 77000000,
"Sailor:Flying Dutchman": 80000000,
"Carriage": 80000000,
"Aquaria": 80000000,
"Virtual:Full Control": 80000000,
"Meta": 81111111,
"Harnessed:Elements": 85000000,
"Hellbound": 85000000,
"Runic:Wilt": 87388744,
"Virtual:WorldWide": 87500000,
"Atomic:Nucleus": 92118000,
"Quartz:Rose": 97500000,
"Chromatic : Genesis": 99999999,
"Starscourge : Radiant": 100000000,
"Spectraflow": 100000000,
"Lily": 112000000,
"Sharkyn:HammerHead": 120000000,
"Overture": 150000000,
"Bounded:Aichmalotos": 170000000,
"Symphony": 175000000,
"Twilight:WitheringGrace": 180000000,
"Felled": 180000000,
"Projection": 197000000,
"Impeached": 200000000,
"Raven:Plague": 200000000,
"Lumenpool": 220000000,
"Hyper-Volt:EverStorm": 225000000,
"VirtualMemory": 232232232,
"Astral:Zodiac": 267200000,
"Prophecy": 275649430,
"Exotic:Void": 299999999,
"Overture:History": 300000000,
"Bloodlust": 300000000,
"Maelstrom": 309999999,
"Dreamer": 315000000,
"Perpetual": 315000000,
"Lotusfall": 320000000,
"Cytokinesis": 330400472,
"Jazz:Orchestra": 336870912,
"Archangel": 350000000,
"Atlas": 360000000,
"Flora:Evergreen": 370073730,
"Chillsear": 375000000,
"Celestial:Eclipse": 384400000,
"Abyssal Hunter": 400000000,
"Gargantua": 430000000,
"Apostolos": 444000000,
"Unknown": 444444444,
"Kyawthuite:Remembrance": 450000000,
"Ruins": 500000000,
"Matrix:Overdrive": 503000000,
"Gravitational:Point-Zero": 521121900,
"A.T.L.A.S": 536870915,
"Sailor:Admiral": 540000000,
"Elude": 555555555,
"Sophyra": 570000000,
"Matrix:Reality": 601020102,
"Sloth": 650000000,
"Prologue": 666616111,
"Pythios": 666666666,
"Sovereign": 750000000,
"Ruins:Withered": 800000000,
"Aegis": 825000000,
"Eisveil": 830000000,
"Dreamscape": 850000000,
"Poseidon:Atlantis": 850000000,
"Ascendant": 935000000,
"Illusionary": 1000000000,
"Nyctophobia": 1011111010,
"Pixelation": 1073741824,
"Luminosity": 1200000000,
"AbyssalHunter:AWAKENED": 1638000000,
"Leviathan": 1730400000,
"Astraios": 1750000000,
"Matrix:Steampunk": 1841004000,
"Breakthrough": 1999999999,
"Dream Catcher": 2222222222,
"Equinox": 2500000000,
"Monarch": 3000000000,
    
}

sfxlinks=[
(r"https://cdn.discordapp.com/attachments/1516038860474159227/1529888359835631616/1sp.mp4?ex=6a639310&is=6a624190&hm=15740976cabe5cc3034eb49ce0a24607d651087d46ab0618d29be398644e97ce&", 1000000000000000000000000),
(r"https://cdn.discordapp.com/attachments/1516038860474159227/1529888360095547453/1sx.mp4?ex=6a639310&is=6a624190&hm=e768ef2a2869e907735abab49cf43aba96957fee337a5a4a869e454296c87f9e&", 1000000000000000000000),
(r"https://cdn.discordapp.com/attachments/1516038860474159227/1529888359508348988/1qn.mp4?ex=6a639310&is=6a624190&hm=866fa3a35bc8a91cb2699426cca2e24c94326eec5507882e4e6a9e7ae6ca39e8&", 1000000000000000000),
(r"https://cdn.discordapp.com/attachments/1516038860474159227/1529888359248560169/1qd.mp4?ex=6a639310&is=6a624190&hm=482f7a7da887408549914fa4e3a6a3a300767a017b97f817e8155cd418e832e8&", 1000000000000000),
(r"https://cdn.discordapp.com/attachments/1516038860474159227/1529888360301072574/1t.mp4?ex=6a639311&is=6a624191&hm=9f770d523b4191e9003df34bf778b17135e803b3cc8dddbba3340af022e87134&", 1000000000000),
(r"https://cdn.discordapp.com/attachments/1516038860474159227/1529888358841716957/1b.mp4?ex=6a639310&is=6a624190&hm=8f12bd178cba2def4717240927983d88b7df720051d094a8fc4cfd748a3efe16&", 1000000000),
(r"https://cdn.discordapp.com/attachments/1516038860474159227/1529888359026135102/1m.mp4?ex=6a639310&is=6a624190&hm=4ee674432ff0dc3a0557bab099457ec2a7885a02db71b0fb3aba8d6e0dbc2544&", 1000000),
(r"https://cdn.discordapp.com/attachments/1516038860474159227/1529888360603189459/100k.mp4?ex=6a639311&is=6a624191&hm=4492ac35ec4e712833ad303890d0e2ad081ec56ebc4be151ac83dd619f343bdc&", 100000),
(r"https://cdn.discordapp.com/attachments/1516038860474159227/1529888358656901210/1.mp4?ex=6a639310&is=6a624190&hm=17ecbf22c741111038783d6491b439e0892159112f41b6058f66c4c6d22f4b20&", 1)
]

def attkey(n):
    return attributes[n]


time.sleep(0.25)

def genball():
    brar=1
    batts=[]
    for i,ii in attributes.items():
        if random.randint(1,ii)==1:
            brar*=ii
            batts.insert(0, i)
    ball=[]
    ball.append(brar)
    ball.extend(batts)
    return ball
def secondstodhms(time):
    days, remainder = divmod(time, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (days, hours, minutes, seconds)

data = discord["storage"]["user"]
servdata = discord["storage"]["server"]

userrarest = data.get("rarestball", "1,Ball")
userdiscovered = data.get("discovered", "Ball")
servrarest = servdata.get("rarestball", "1,Ball")
servdiscovered = servdata.get("discovered", "Ball")
# because of nsb saving i do it this way, fuck you nsb
userrarest=userrarest.split(",")
servrarest=servrarest.split(",")
userdiscovered=userdiscovered.split(",")
servdiscovered=servdiscovered.split(",")

for j in userdiscovered[:]:
    if not (j in attributes):
        userdiscovered.remove(j)
        continue
    if not (j in servdiscovered):
        servdiscovered.append(j)

for j in servdiscovered[:]:
    if not (j in attributes):
        servdiscovered.remove(j)

userrarest[0]=int(userrarest[0])
servrarest[0]=int(servrarest[0])

userlast = round(float(data.get("last", time.time()-1)))
usertime = int(data.get("time", 1))

if arg:
    if arg=="get":
        print(data)
        print(servdata)
        exit()
    elif arg=="about":
        print("Tag by: Afjap\nThank's to Sol's RNG for the auras, inspired by the attrng tag by BonesYT.\nAn idle game where you roll for balls, which may have various attributes from Sol's RNG, from really common ones to extremely rare ones.\nNot much else to say.")
        exit()
    elif arg=="help":
        print("Usable arguments:\n`.t (tag) get` - prints user+server data. if you want to look at it then sure, but its mostly for debug purposes.\n`.t (tag) about` - info about the game\n`.t (tag) help` - <:g_:1501846104797352038>\n`.t (tag) stats` - shows your current stats and server stats.\n`.t (tag) [serv]attributes` - shows your (or entire server discovered if servattributes) discovered attributes.\n`.t (tag) showatt (attribute)` - shows the rarity of an attribute\n`.t (tag) topatts` - shows top 5 your and top 5 server discovered attributes")
        exit()
    elif arg=="stats":
        print("## User stats:")
        rball = ""
        for b in userrarest[1:]:
            rball+=f"{b} "
        rball += "(1/{:,})".format(int(userrarest[0])) 
        print(f"Rarest ball: {rball}")
        da,ho,mi,se=secondstodhms(round(time.time()-userlast))
        timetext=""
        if da: timetext+=f"{da}d{ho}h{mi}m{se}s"
        elif ho: timetext+=f"{ho}h{mi}m{se}s"
        elif mi: timetext+=f"{mi}m{se}s"
        else: timetext+=f"{se}s"
        print(f"Current afk time: {timetext}")
        da,ho,mi,se=secondstodhms(usertime)
        timetext=""
        if da: timetext+=f"{da}d{ho}h{mi}m{se}s"
        elif ho: timetext+=f"{ho}h{mi}m{se}s"
        elif mi: timetext+=f"{mi}m{se}s"
        else: timetext+=f"{se}s"
        print(f"Total rolls: {usertime*3} ({timetext})")
        attamt=len(userdiscovered)
        print(f"Discovered attributes: {attamt}/{len(attributes)}")
        rarestatt=(1, "Ball")
        for v in userdiscovered:
            if attributes[v] > rarestatt[0]:
                rarestatt=(attributes[v], v)
        print(f"Rarest attribute found: {rarestatt[1]}" +  "(1/{:,})".format(rarestatt[0]))
        print(f"## Server stats:")
        rball = ""
        for b in servrarest[1:]:
            rball+=f"{b} "
        rball += "(1/{:,})".format(int(servrarest[0])) 
        print(f"Rarest ball: {rball}")
        attamt=len(servdiscovered)
        print(f"Discovered attributes: {attamt}/{len(attributes)}")
        rarestatt=(1, "Ball")
        for v in servdiscovered:
            if attributes[v] > rarestatt[0]:
                rarestatt=(attributes[v], v)
        print(f"Rarest attribute found: {rarestatt[1]}" +  "(1/{:,})".format(rarestatt[0]))
        exit()
    elif arg=="attributes":
        attamt=len(userdiscovered)
        print(f"Discovered attributes: {attamt}/{len(attributes)}")
        if len(attributes)==attamt:
            print("All attributes discovered!")
        attsort=sorted(userdiscovered, key=attkey, reverse=True)
        print(f"{attsort}")
        exit()
    elif arg=="servattributes":
        attamt=len(servdiscovered)
        print(f"Discovered attributes: {attamt}/{len(attributes)}")
        if len(attributes)==attamt:
            print("All attributes discovered!")
        attsort=sorted(servdiscovered, key=attkey, reverse=True)
        print(f"{attsort}")
        exit()
    elif arg=="showatt":
        if len(args)>1:
            for h,hh in attributes.items():
                if h.lower() == args[1].lower():
                    print(f"{h}: 1/"+"{:,}".format(int(hh)))
                    exit()
            print("No such attribute found.")
            exit()
        else:
            print("No attribute provided.")
    elif arg=="topatts":
        attsort=sorted(userdiscovered, key=attkey, reverse=True)
        print("### Your top 5 discovered attributes:")
        for yy in range(5):
            print(f"{yy}. {attsort[yy]} (1/" + "{:,})".format(attributes[attsort[yy]]))
        attsort=sorted(servdiscovered, key=attkey, reverse=True)
        print("### Server top 5 discovered attributes:")
        for yy in range(5):
            print(f"{yy}. {attsort[yy]} (1/" + "{:,})".format(attributes[attsort[yy]]))
        exit()
    print("Invalid argument.")
    exit()
    
ttime = round(time.time()-userlast)

remain = 0
if ttime > 43200:
    remain = ttime-43200
    ttime = 43200
    
rolls = ttime*3

b=[]
attsfound = set({})
discv=0
for i in range(rolls):
    ball = genball()
    for l in ball[1:]:
        attsfound.add(l)
        if not (l in userdiscovered):
            userdiscovered.append(l)
            discv+=1
        if not (l in servdiscovered):
            servdiscovered.append(l)
            
    b.append(ball)
def key(n):
    return n[0]
b=sorted(b, key=key, reverse=True)
attsfound=sorted(list(attsfound), key=attkey, reverse=True)
top3att = attsfound[:3]

top10=b[:10]
top1=top10[0]
isurar, issrar = False, False
if top1[0] > userrarest[0]:
    isurar=True
    userrarest=top1
if top1[0] > servrarest[0]:
    issrar=True
    servrarest=top1
#
da,ho,mi,se=secondstodhms(ttime)
timetext=""
if da: timetext+=f"{da}d{ho}h{mi}m{se}s"
elif ho: timetext+=f"{ho}h{mi}m{se}s"
elif mi: timetext+=f"{mi}m{se}s"
else: timetext+=f"{se}s"
print(f"You were away for {timetext} and you rolled {rolls} times. Showing top 10 finds:")
sfxth="(https://cdn.discordapp.com/attachments/1516038860474159227/1529888358656901210/1.mp4?ex=6a639310&is=6a624190&hm=17ecbf22c741111038783d6491b439e0892159112f41b6058f66c4c6d22f4b20&)"
for bg in sfxlinks:
    if top1[0] > bg[1]:
        sfxth=f"({bg[0]})"
        break
        
for i,ii in enumerate(top10):
    bt=""
    for g in ii[1:]:
        bt+=f"{g} "
    if i == 0:
        print(f"[{i+1}]{sfxth}. {bt}(1/"+"{:,})".format(int(ii[0]))) 
    else:
        print(f"{i+1}. {bt}(1/"+"{:,})".format(int(ii[0]))) 
print("Showing top 3 rarest attribute finds:")
for i,ii in enumerate(top3att):
    if ii == "DIVORCED!!!!":
        print(f"{i+1}. [{ii}]" + r"(https://cdn.discordapp.com/attachments/1307066414531743846/1479243377169010729/ok_sooo_that_happened.mp4?ex=6a61ec00&is=6a609a80&hm=3da32bb1b2e4149e24b4fb6986062e18b1f2b2d6040b62d019d85c1b0f6aaa33&)" + " (1/{:,})".format(attributes[ii]))
    else:
        print(f"{i+1}. {ii}" + " (1/{:,})".format(attributes[ii]))
if issrar: print("# *NEW SERVER BEST!*")
elif isurar: print("## NEW USER BEST!")
if discv:
    print(f"You discovered {discv} new attributes!")
    
if remain:
    da,ho,mi,se=secondstodhms(remain)
    timetext=""
    if da: timetext+=f"{da}d{ho}h{mi}m{se}s"
    elif ho: timetext+=f"{ho}h{mi}m{se}s"
    elif mi: timetext+=f"{mi}m{se}s"
    else: timetext+=f"{se}s"
    print(f"You were away for {timetext} and you rolled {rolls} times. Showing top 10 finds:")
    print(f"## Rolls per command are capped to 12h of afk, _use this tag again_ to roll the remaining {remain*3} ({timetext}) rolls")


rball = ""
for b in userrarest[1:]:
    rball+=f"{b} "
rball += "(1/{:,})".format(int(userrarest[0])) 
print(f"-# User rarest: {rball}")
rball = ""
for b in servrarest[1:]:
    rball+=f"{b} "
rball += "(1/{:,})".format(int(servrarest[0])) 
print(f"-# Server rarest: {rball}")
print(f"-# Use `.t (tag) help` for the argument list.")

# user data
discord["storage"]["user"]["rarestball"] = userrarest
discord["storage"]["user"]["last"] = time.time()-remain
discord["storage"]["user"]["discovered"] = userdiscovered
discord["storage"]["user"]["time"] = usertime+ttime
# server data
discord["storage"]["server"]["rarestball"] = servrarest
discord["storage"]["server"]["discovered"] = servdiscovered
