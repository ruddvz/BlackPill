import json

HERBS_RAW = [
 (1,"Amla","Goose berry","Emblica officinalis","Fruit"),
 (2,"Haritaki","Chebulic myrobalan","Terminalia chebula","Fruit"),
 (3,"Vibhitak","Belleric myrobalan","Terminalia bellirica","Fruit"),
 (4,"Vashlochan","Bamboo manna","Bambusa arundinacea","Resin"),
 (5,"Shunthi","Ginger","Zingiber officinale","Stem"),
 (6,"Giloy","Tinospora","Tinospora cordifolia","Stem"),
 (7,"Pippali","Long Pepper","Piper longum","Fruit"),
 (8,"Methi","Fenugreek","Trigonella foenum-graecum","Seeds"),
 (9,"Ajwain","Carrom","Trachyspermum ammi","Seeds"),
 (10,"Mulethi","Liquorice","Glycyrrhiza glabra","Root"),
 (11,"Kali Mirch","Black pepper","Piper nigrum","Fruit"),
 (12,"Dalchini","Cinnamon","Cinnamomum zeylanicum","Stem bark"),
 (13,"Lavanga","Clove","Syzigium aromaticum","Fruit"),
 (14,"Jeera","Cumin","Cuminum cyminum","Seeds"),
 (15,"Tulsi","Holy Basil","Ocimum tenuiflorum","Leaves"),
 (16,"Arjuna","Arjun","Terminalia arjuna","Stem bark"),
 (17,"Lehsun","Garlic","Allium sativum","Bulb"),
 (18,"Pudina","Mint","Mentha arvensis","Leaves"),
 (19,"Nimbu","Lemon","Citrus limon","Fruit"),
 (20,"Shatavri","Buttermilk Root","Asparagus racemosus","Root"),
 (21,"Dhaniya","Coriander","Coriandrum sativum","Fruit"),
 (22,"Elaichi","Cardamom","Elettaria cardamomum","Fruit/Seeds"),
 (23,"Gudhal","Hibiscus","Hibiscus rosa-sinensis","Stem"),
 (24,"Haldi","Turmeric","Curcuma longa","Stem"),
 (25,"Ghritkumari","Aloe Vera","Aloe vera","Leaves"),
 (26,"Sarson","Mustard","Brassica juncea","Seed oil"),
 (27,"Lavender","Lavender","Lavandula angustifolia","Flower"),
 (28,"Lal Mirch","Cayenne Pepper","Capsicum annuum","Fruit"),
]
HNAME={n:nm for (n,nm,e,b,p) in HERBS_RAW}

# active compounds (verified vs Active Ingredient Reference Manual) keyed by herb number
ACT = {
 1:("Emblicanin-A, Emblicanin-B","Constipation, Immunity"),
 2:("Tannins: Chebulagic, Chebulin, Corilagin","Kidney & Liver"),
 3:("Glucoside (Bellericanin), Gallo-Tannic Acid","Energy Flow, Weakness"),
 4:("Silica (SiO₂) 70-90%","Bone Health, Respiratory Congestion"),
 5:("Gingerol, Shogaol","Pain Relief, Common Cold"),
 6:("Alkaloids: Berberine, Jatrorrhizine","Fever"),
 7:("Piperine","Muscle Pain, Respiratory Illness"),
 8:("Trigonelline","Diabetes"),
 9:("Thymol","Acidity"),
 10:("Glycyrrhizin","Sore Throat"),
 11:("Piperine","Indigestion"),
 12:("Cinnamaldehyde (74% of bark essential oil)","Cold, Headache"),
 13:("Eugenol","Oral Health"),
 14:("Cuminaldehyde, Safranal","Depression"),
 15:("Eugenol (~70%)","Anti-Viral"),
 16:("Tannins, Triterpenoid Saponins","Blood Pressure, Heart"),
 17:("Allicin","Anti-Cancer"),
 18:("Menthol","Nausea, Vomiting"),
 19:("Bioflavonoids, major: Hesperidin","Anti-Aging, Anti-Oxidant"),
 20:("Steroidal Saponins (Shatvarins I-VI)","Female Reproductive Health"),
 21:("Linalool / Coriandrol (60-70%)","Diabetes"),
 22:("Cineole","Cold, Headache"),
 23:("Beta-Sitosterol, Stigmasterol, Flavonoids","Blood Pressure"),
 24:("Curcumin","Anti-Inflammatory, Anti-Viral"),
 25:("75 potentially active constituents","Immunity, Skin Health"),
 26:("Phytoalexins, Flavonoids","Increases blood flow (massage)"),
}

# REMEDIES verified against the source remedy table (IMG_4815). ing = [[herbNum, qty]]
R = [
 dict(id="cold",name="Cold",cat="Respiratory",time="5 min",diff="Easy",popular=1,base="water",
   summary="A warm decoction to ease cold symptoms.",
   ing=[[15,"2 scoops"],[5,"1 scoop"],[12,"1 scoop"],[11,"1 scoop"]],
   method="boil",freq="4 times a day"),
 dict(id="cough",name="Cough",cat="Respiratory",time="5 min",diff="Easy",popular=1,base="water",
   summary="A soothing liquorice decoction to calm a cough.",
   ing=[[10,"4 scoops"]],method="boil",freq="3 times a day"),
 dict(id="blood-thinner",name="Blood Thinner",cat="Heart & Metabolic",time="5 min",diff="Easy",popular=0,base="water",
   summary="A warm drink taken after dinner.",
   ing=[[5,"2 scoops"],[17,"1 scoop"],[24,"1 scoop"]],method="boil",freq="Once a day after dinner"),
 dict(id="upper-respiratory",name="Upper Respiratory Congestion",cat="Respiratory",time="2 min",diff="Easy",popular=0,base="honey",
   summary="A honey blend for chest and sinus congestion.",
   ing=[[9,"4 scoops"],[7,"2 scoops"],[22,"1 scoop"],[1,"1 scoop"]],method="honey",honey="8 scoops",freq="2-3 times a day"),
 dict(id="constipation",name="Constipation",cat="Digestive",time="2 min",diff="Easy",popular=0,base="water",
   summary="The classic Triphala blend, taken cold.",
   ing=[[1,"2 scoops"],[2,"2 scoops"],[3,"2 scoops"]],method="mixcold",water="50 ml",freq="3 times a day"),
 dict(id="fever",name="Fever (above 102°F)",cat="Immunity",time="5 min",diff="Easy",popular=1,base="water",
   summary="A Giloy decoction for high fever.",
   ing=[[6,"6 scoops"],[5,"2 scoops"]],method="boil",freq="3-4 times a day",
   warn=["A fever above 102°F, or any fever that persists, needs medical attention."]),
 dict(id="headache",name="Headache",cat="Pain",time="5 min",diff="Easy",popular=1,base="water",
   summary="A warm spiced decoction for headaches.",
   ing=[[1,"1 scoop"],[2,"1 scoop"],[12,"1 scoop"],[5,"1 scoop"]],method="boil",freq="As needed"),
 dict(id="indigestion",name="Indigestion",cat="Digestive",time="5 min",diff="Easy",popular=0,base="water",
   summary="A carminative decoction with rock salt.",
   ing=[[9,"2 scoops"],[11,"1 scoop"],[10,"1 scoop"],[2,"1 scoop"]],extra="1 scoop rock salt",method="boil",freq="3-4 times a day"),
 dict(id="nausea",name="Nausea",cat="Digestive",time="2 min",diff="Easy",popular=0,base="water",
   summary="A cooling lemon-honey sip to settle the stomach.",
   ing=[[12,"2 scoops"],[14,"2 scoops"],[19,"½ lemon, juiced"]],extra="2 scoops honey",method="mixcold",water="50 ml",freq="2-3 times a day"),
 dict(id="joint-pain",name="Joint Pain",cat="Pain",time="3 min",diff="Easy",popular=0,base="water",
   summary="An anti-inflammatory drink plus an oil massage.",
   ing=[[5,"1 scoop"],[24,"1 scoop"],[11,"1 scoop"]],extra="a pinch of black salt; massage joints with Sarson oil (#26)",method="mixcold",water="50 ml",freq="2 times a day"),
 dict(id="diarrhea",name="Diarrhea",cat="Digestive",time="2 min",diff="Easy",popular=0,base="honey",
   summary="A binding spice-and-honey mixture.",
   ing=[[12,"2 scoops"],[14,"2 scoops"],[5,"2 scoops"],[13,"2 scoops"]],extra="2 scoops honey",method="honeymix",freq="3-4 times a day",
   warn=["Replace lost fluids. Ongoing or severe diarrhea, or blood in stool, needs medical care."]),
 dict(id="skin-rashes",name="Skin Rashes",cat="Skin",time="2 min",diff="Easy",popular=0,base="paste",
   summary="A Tulsi paste applied to the skin.",
   ing=[[15,"10 scoops"]],extra="10 drops water",method="paste",freq="4-5 times a day"),
 dict(id="stomach-ache",name="Stomach Ache",cat="Digestive",time="2 min",diff="Easy",popular=0,base="water",
   summary="A warming spice drink with rock salt.",
   ing=[[12,"2 scoops"],[13,"2 scoops"]],extra="1 scoop rock salt",method="mixcold",water="50 ml",freq="3 times a day"),
 dict(id="tooth-ache",name="Tooth Ache",cat="Dental",time="2 min",diff="Easy",popular=0,base="paste",
   summary="A clove paste applied to the aching tooth.",
   ing=[[13,"2 scoops"]],extra="a few drops of water",method="pastetooth",freq="3 times a day"),
 dict(id="cuts-wounds",name="Cuts & Wounds",cat="Skin",time="2 min",diff="Easy",popular=0,base="paste",
   summary="A turmeric and aloe paste for minor wounds.",
   ing=[[24,"10 scoops"],[25,"10 scoops"]],method="paste",freq="thrice a day",
   warn=["For minor cuts only. Deep, dirty or heavily bleeding wounds need medical care."]),
 dict(id="burns",name="Burns",cat="Skin",time="1 min",diff="Easy",popular=0,base="apply",
   summary="Aloe vera gel applied to the burn.",
   ing=[[25,"as needed"]],method="apply",freq="4-5 times a day",
   warn=["First cool a burn under running water. Large, deep or blistering burns need medical care."]),
 dict(id="ear-pain",name="Ear Pain",cat="Pain",time="5 min",diff="Medium",popular=0,base="oil",
   summary="A warm garlic-infused oil for the ear.",
   ing=[[17,"4 scoops"],[26,"20 ml Sarson oil"]],method="earoil",freq="twice a day",
   warn=["Do not use if the eardrum may be perforated or there is discharge. See a doctor for severe or persistent ear pain."]),
 dict(id="hypertension",name="Hypertension (>150/100)",cat="Heart & Metabolic",time="5 min",diff="Easy",popular=0,base="water",
   summary="An Arjuna-hibiscus decoction for high blood pressure.",
   ing=[[16,"4 scoops"],[23,"4 scoops"]],method="boil",freq="twice a day",
   warn=["Continue any prescribed blood-pressure medication. Monitor your blood pressure and consult your doctor."]),
 dict(id="diabetes",name="Diabetes (>250 mg/dl)",cat="Heart & Metabolic",time="5 min",diff="Easy",popular=0,base="water",
   summary="A spice decoction to support blood-sugar balance.",
   ing=[[21,"2 scoops"],[8,"2 scoops"],[24,"2 scoops"],[14,"2 scoops"]],method="boil",freq="3 times a day",
   warn=["Continue any prescribed diabetes medication and keep monitoring your blood sugar. Consult your doctor."]),
 dict(id="impotency",name="Impotency / Low Sperm Count",cat="Reproductive",time="2 min",diff="Easy",popular=0,base="water",
   summary="A restorative blend taken with warm water.",
   ing=[[4,"2 scoops"],[6,"2 scoops"],[20,"2 scoops"]],method="mixwarm",water="100 ml",freq="twice a day"),
 dict(id="female-reproductive",name="Female Reproductive Health",cat="Reproductive",time="5 min",diff="Easy",popular=0,base="water",
   summary="A Shatavari decoction for women's health.",
   ing=[[20,"4 scoops"]],method="boil",freq="twice a day"),
 dict(id="tooth-powder",name="Tooth Powder",cat="Dental",time="2 min",diff="Easy",popular=0,base="powder",
   summary="A daily herbal tooth powder.",
   ing=[[1,"1 scoop"],[2,"1 scoop"],[3,"1 scoop"],[13,"1 scoop"],[24,"1 scoop"]],extra="1 scoop rock salt",method="powder",freq="twice a day"),
 dict(id="head-wash",name="Head Wash",cat="Skin",time="Overnight",diff="Easy",popular=0,base="soak",
   summary="A Triphala soak for the scalp and hair.",
   ing=[[1,"1 part"],[2,"1 part"],[3,"1 part"]],method="soak",freq="As needed"),
 dict(id="face-wash",name="Face Wash",cat="Skin",time="5 min",diff="Easy",popular=0,base="paste",
   summary="A turmeric-aloe face mask.",
   ing=[[24,"½ scoop"],[25,"4 scoops"]],method="facemask",freq="As needed"),
 dict(id="heart-attack",name="Heart Attack — First Aid",cat="Emergency",time="Now",diff="First aid",popular=0,base="emergency",
   summary="Cayenne first-aid measure while emergency help is on the way.",
   ing=[[28,"1 tsp (conscious) / a few drops of extract (unconscious)"]],method="emergency",freq="One time, as first aid",
   warn=["CALL EMERGENCY SERVICES IMMEDIATELY. This is a folk first-aid measure only and is NOT a treatment for a heart attack."]),
]

# step generation by method
def steps_for(r):
    n=", ".join("%s (#%d)"%(HNAME[i],i) for i,q in r["ing"])
    w=r.get("water","100 ml")
    m=r["method"]
    if m=="boil":
        return [f"Add all ingredients to about {w if 'water' in r else '100 ml'} of water.","Boil for 5 minutes.","Strain and let it cool slightly.","Sip while warm."]
    if m=="honey":
        return [f"Measure out the ingredients.",f"Mix thoroughly with {r.get('honey','honey')} of honey.","Take the mixture directly."]
    if m=="honeymix":
        return ["Combine the ground ingredients.",f"Mix with {r.get('extra','honey')}.","Take the mixture directly."]
    if m=="mixcold":
        return [f"Add the ingredients to {w} of water"+(f" with {r['extra']}." if r.get('extra') else "."),"Stir well.","Drink it."]
    if m=="mixwarm":
        return ["Combine the ingredients.",f"Take with {w} of warm water."]
    if m=="paste":
        return ["Mix into a paste with a little water.","Apply over the affected area."]
    if m=="pastetooth":
        return ["Mix into a paste with a few drops of water.","Apply to the affected tooth with a cotton swab."]
    if m=="earoil":
        return ["Heat the garlic in the mustard oil until golden brown.","Strain and let the oil cool to a safe, warm temperature.","Put a little of the oil into the affected ear."]
    if m=="apply":
        return ["Apply the fresh aloe gel liberally over the affected area."]
    if m=="powder":
        return ["Mix all ingredients into a fine powder"+(f" with {r['extra']}." if r.get('extra') else "."),"Massage onto the teeth and gums."]
    if m=="soak":
        return ["Soak the ingredients overnight.","Apply to the scalp.","Leave for about half an hour.","Rinse away with water."]
    if m=="facemask":
        return ["Mix into a smooth paste.","Apply on the face.","Leave for 5 minutes, then wash off."]
    if m=="emergency":
        return ["Call your local emergency number immediately.","If the person is conscious: give warm water mixed with 1 teaspoon of cayenne pepper (Lal Mirch, #28).","If the person is unconscious: place a few drops of cayenne extract under the tongue.","Stay with them until emergency help arrives."]
    return ["Prepare and use as directed."]

remout=[]
for r in R:
    o=dict(r)
    o["ingredients"]=[{"n":i,"herb":HNAME[i],"qty":q} for i,q in r["ing"]]
    o.pop("ing")
    o["steps"]=steps_for(r)
    if "warn" not in o: o["warn"]=[]
    remout.append(o)

# HERBS enriched
herbout=[]
for (n,nm,en,bot,part) in HERBS_RAW:
    comp,use = ACT.get(n,("",""))
    related=[r["id"] for r in remout if any(i["n"]==n for i in r["ingredients"])]
    herbout.append({"n":n,"name":nm,"en":en,"bot":bot,"part":part,"compound":comp,"benefits":use,
                    "related":related})

# COMPOUNDS
compout=[]
for n in sorted(ACT):
    comp,use=ACT[n]
    compout.append({"n":n,"herb":HNAME[n],"compound":comp,"use":use})

# EMERGENCY (safe standard first aid + the source's own emergency codes, clearly labelled)
EMERG=[
 {"id":"chest-pain","name":"Chest Pain / Heart Attack","icon":"heart",
  "steps":["Call your local emergency number now.","Have the person sit down, rest and stay calm; loosen tight clothing.","If they take prescribed heart medication (e.g. nitroglycerin), help them use it as directed.","If they become unresponsive and are not breathing normally, begin CPR and use an AED if available."],
  "code":"98 88 119","codedesc":"the source lists this as a code for myocardial infarction on the way to hospital"},
 {"id":"stroke","name":"Stroke (F.A.S.T.)","icon":"brain",
  "steps":["Call emergency services immediately and note the time symptoms started.","Check F.A.S.T. — Face drooping, Arm weakness, Speech difficulty, Time to call.","Keep the person calm and still, lying with head and shoulders slightly raised.","Do not give food, drink or medication."],
  "code":"78 89 535","codedesc":"the source lists this for first aid in strokes on the way to hospital"},
 {"id":"bleeding","name":"Severe Bleeding","icon":"droplet",
  "steps":["Call emergency services.","Apply firm, direct pressure on the wound with a clean cloth or dressing.","Do not remove a soaked cloth — add more on top and keep pressing.","Keep the injured area raised if possible and maintain pressure until help arrives."],
  "code":"15 01 777","codedesc":"the source lists this for hemostasis in hemorrhage while seeking care"},
 {"id":"breathing","name":"Breathing Difficulty","icon":"lungs",
  "steps":["Call emergency services.","Help the person sit upright and stay calm.","If they have a prescribed inhaler, help them use it.","Loosen tight clothing and keep the area well ventilated."],
  "code":"87 65 423","codedesc":"the source lists this for respiratory distress"},
 {"id":"poisoning","name":"Poisoning","icon":"alert",
  "steps":["Call emergency services or your poison control centre immediately.","Do NOT make the person vomit unless specifically told to.","Try to identify the substance and have the container ready.","If they are unconscious and not breathing, begin CPR."],
  "code":"","codedesc":""},
 {"id":"burns","name":"Burns","icon":"alert",
  "steps":["Cool the burn under cool running water for at least 20 minutes.","Remove jewellery or tight items near the burn before it swells.","Cover loosely with a clean, non-stick dressing or cling film.","Do not apply ice, butter or pop blisters. Seek care for large, deep or facial burns."],
  "code":"19 19 311","codedesc":"the source lists this for burns and sunburn"},
]

QHC=json.load(open("qhc_final.json"))

bundle={"REMEDIES":remout,"HERBS":herbout,"COMPOUNDS":compout,"EMERG":EMERG,"QHC":QHC}
json.dump(bundle,open("v3data.json","w"),ensure_ascii=False,separators=(",",":"))
print("remedies:",len(remout)," herbs:",len(herbout)," compounds:",len(compout)," emerg:",len(EMERG)," codeSecs:",len(QHC))
# sanity: print corrected remedies
for r in remout:
    print(" ",r["id"].ljust(20),r["cat"].ljust(18),r["freq"])
