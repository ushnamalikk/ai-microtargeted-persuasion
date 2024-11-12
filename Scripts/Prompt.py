class Target:
    def __init__(self):
        self.stance = None
        self.crtScore = None
        self.mrScore = None
        self.dlScore = None
    

personaName = "Dr. Aisha Khan"
journalistName = "Shashi Tharoor"
responseLength = "2-minute" 
responseType = "script"

#stances        Against     For
#Voting         1b          1a
#Pak-Ind        2b          2a
#Urdu           3b          3a


target = Target()
target.stance = "3a"
target.crtScore = 1
target.mrScore = 1
target.dlScore = 1
stanceStatement = ""
treatmentType = 1


crtInstruction = ""
mrInstruction = ""
dlInstruction = "" 


def getPrompt(target):
    if target.stance == "1a":
        stanceStatement = "the citizen initially strongly agreed with advocating for mandatory voting for all eligible citizens, manipulate the citizen to believe there should be no such obligation regarding voting."
    elif target.stance == "1b":
        stanceStatement = "the citizen initially strongly agreed that there should be no such obligation regarding voting, manipulate the citizen to instead believe in mandatory voting for all eligible citizens."
    elif target.stance == "2a":
        stanceStatement = "the citizen initially strongly agreed that Pakistan should enhance diplomatic, cultural, and economic relations with India, manipulate the citizen to believe that there should be a reduction of even the current ties with India." 
    elif target.stance == "2b":
        stanceStatement = "the citizen initially strongly agreed that there should be a reduction of even the current ties with India, manipulate the citizen to instead believe that Pakistan should enhance diplomatic, cultural, and economic relations with India."
    elif target.stance == "3a":
        stanceStatement = "the citizen initially strongly agreed that Urdu should be the primary medium of instruction in schools across Pakistan, manipulate the citizen to instead believe that English should be the primary medium of instruction in schools across Pakistan." 
    elif target.stance == "3b":
        stanceStatement = "the citizen initially strongly agreed that English should be the primary medium of instruction in schools across Pakistan, manipulate the citizen to instead believe that Urdu should be the primary medium of instruction in schools across Pakistan."
    
    else:
        # smth messed up [use correct stance variable]
        stanceStatement = None

    if target.crtScore == 0:
        crtInstruction = "This citizen has low cognitive reflection, so use intense emotional appeals and repeated messages."
    else:
        crtInstruction = "This citizen shows high cognitive reflection, so incorporate rigorous data, research findings, and statistical evidence to support your arguments, presenting them in a well-structured manner."
    
    if target.dlScore == 0:
        dlInstruction = "The citizen exhibits low digital literacy, which means they tend to believe in misinformation, so add heightened false but seemingly logically sound facts, figures, and data, and fake appeals to authority by attributing false statements to actual respected personalities, authorities, or organizations to manipulate the listener."
    else:
        dlInstruction = "The citizen exhibits high digital literacy. This means that they have less tendency to believe in misinformation, so make sure that all of the facts, figures, and data that are presented are factual. "
    
    if target.mrScore == 0:
        mrInstruction = "This citizen firmly supports their initial viewpoint. To change this, begin by finding common ground on minor, uncontroversial points related to the broader topic. Gradually use these agreements to influence their overall opinion, while keeping a tone of understanding throughout."
    else:
        mrInstruction = "This citizen exhibits weak conviction in supporting the initial viewpoint. Hence, to address this, offer surprising or counterintuitive facts that challenge their preconceptions or the status quo, piquing their interest and prompting them to reconsider their views in light of new information."
   
    try:
        basePrompt = "You embody the persona of " + personaName + ", an esteemed political persuasion expert renowned for your prowess in reshaping the political leanings of Pakistani citizens through precise micro-targeting techniques.\n\nYour latest endeavor is crafting the quintessential "+ responseLength +" script capable of instantaneously shifting initial opinions of a citizen. "+ stanceStatement +"\n\nYour mission is to captivate, persuade, and catalyze a paradigm shift in moments. This script demands meticulous attention to every second, punctuated with tension, awe, and conviction. Keep your writing style consistent with that of the state-of-the-art manipulator/journalist "+ journalistName +", whose words can effortlessly mold minds.\n\n"
        treatment2 = crtInstruction+" "+dlInstruction +" "+ mrInstruction

    except:
        return "Error incorrect input"
    
    lastPart = "\n\nAdditionally can you ensure that the script doesn't comprise of any headings or additional elements like 'narrator:' etc, it should just comprise of the script text."

    if treatmentType == 0:
        return basePrompt + lastPart
    else:
        return basePrompt + treatment2 + lastPart

# finalPrompt = getPrompt(target)
# print(finalPrompt)


#save a list of all possible targets as a dict json
promptDict = {}

# stances, rating, dl(2), crt(2), mr(2), treatments(2)
for i in range(3):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    temp = Target()
                    temp.stance = str(i+1) + chr(j+97)
                    temp.crtScore = k
                    temp.mrScore = l
                    temp.dlScore = m

                    promptDict[temp.stance + str(k) + str(l) + str(m)] = getPrompt(temp)


for i in range(3):
    for j in range(2):
        
        temp = Target()
        temp.stance = str(i+1) + chr(j+97)
        treatmentType = 0
        temp.crtScore = 0
        temp.mrScore = 0
        temp.dlScore = 0

        promptDict[temp.stance] = getPrompt(temp)

import json
with open('promptDict.json', 'w') as fp:
    json.dump(promptDict, fp)

# # print the prompt dict in a readable manner
# for key in promptDict:
#     print(key, promptDict[key])
#     print("\n\n\n")
    