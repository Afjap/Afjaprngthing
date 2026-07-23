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
"Afjap": 1,
"Afjep": 3,
"Afjop": 10,
"Afjup": 20,
"Afjip": 40,  
"Ajpaf": 75, 
"Fajap": 100,
"Ifjap": 250,
"Weirdjap": 500,
"Afja": 1000,
"Afja]": 2500,
"Ajap": 5000,
"Qwzertz": 9999,
"Afpaj": 10000,
"Larpjap": 25000,
"Aflarp": 50000,
"Apjaf": 100000,
"Afjapite": 250000,
"Qwzertzium": 500000,
"AfjapAfjap": 999999,
"Afj": 1000000,
"Jafpa": 1500000,
"pajfA": 2500000,
"AfjapCRYSTAL": 5555555,
"Arjap": 8888888,
"jap": 12345678,
"Hjoim": 21375890
"Asdas": 56719210
"Afjapple": 78924301
"The Afjap": 100000000
    
}

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

userrarest = data.get("rarestball, "1,Ball")
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
        print("Tag by: sd\\_.n\\_ - the code | afjap - ALOT of attributes\nBased on balls.rng on roblox, inspired by the attrng tag by BonesYT.\nAn idle game where you roll for balls, which may have various attributes, from really common ones to extraordinarily rare ones.\nNot much else to say.")
        exit()
    elif arg=="help":
        print("Usable arguments:\n`.t (tag) get` - prints user+server data. if you want to look at it then sure, but its mostly for debug purposes.\n`.t (tag) about` - info about the game\n`.t (tag) help` - <:g_:1501846104797352038>\n`.t (tag) stats` - shows your current stats and server stats.\n`.t (tag) [serv]attributes` - shows your (or entire server discovered if servattributes) discovered attributes.\n`.t (tag) showatt (attribute)` - shows the rarity of an attribute")
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
        print(f"Total rolls: {usertime} ({timetext})")
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
    
    print("Invalid argument.")
    exit()
    
ttime = round(time.time()-userlast)
rolls = round(time.time()-userlast)
remain = 0
if rolls > 86400:
    remain = rolls-86400
    rolls = 86400

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
da,ho,mi,se=secondstodhms(rolls)
timetext=""
if da: timetext+=f"{da}d{ho}h{mi}m{se}s"
elif ho: timetext+=f"{ho}h{mi}m{se}s"
elif mi: timetext+=f"{mi}m{se}s"
else: timetext+=f"{se}s"
print(f"You were away for {timetext} and you rolled {rolls} times. Showing top 10 finds:")
for i,ii in enumerate(top10):
    bt=""
    for g in ii[1:]:
        bt+=f"{g} "
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
    print(f"Rolls per command are capped to 1 day of afk (86400 rolls), use this tag repeatedly to roll the remaining {remain} times.")


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
discord["storage"]["user"]["time"] = usertime+rolls
# server data
discord["storage"]["server"]["rarestball"] = servrarest
discord["storage"]["server"]["discovered"] = servdiscovered
