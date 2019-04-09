#!/usr/bin/python
mappings = {
        "04":["a","A"],
        "05":["b","B"],
        "06":["c","C"],
        "07":["d","D"],
        "08":["e","E"],
        "09":["f","F"],
        "0A":["g","G"],
        "0B":["h","H"],
        "0C":["i","I"],
        "0D":["j","J"],
        "0E":["k","K"],
        "0F":["l","L"],
        "10":["m","M"],
        "11":["n","N"],
        "12":["o","O"],
        "13":["p","P"],
        "14":["q","Q"],
        "15":["r","R"],
        "16":["s","S"],
        "17":["t","T"],
        "18":["u","U"],
        "19":["v","V"],
        "1A":["w","W"],
        "1B":["x","X"],
        "1C":["y","Y"],
        "1D":["z","Z"],
        "1E":["1","!"],
        "1F":["2","@"],
        "20":["3","#"],
        "21":["4","$"],
        "22":["5","%"],
        "23":["6","^"],
        "24":["7","&"],
        "25":["8","*"],
        "26":["9","("],
        "27":["0",")"],
        "28":"\n",
        "29":"ESC",
        "2A":"BKSPC",
        "2B":"  ",
        "2C":" ",
        "2D":["-","_"],
        "2E":["=","+"],
        "2F":["[","{"],
        "30":["]","}"],
        "31":["\\","|"],
        "32":"(INT 2)",
        "33":[";",":"],
        "34":[",",'"'],
        "35":["`","~"],
        "36":[",","<"],
        "37":[".",">"],
        "38":["/","?"],
        "39":"CAPSLOCK",
        "3A":"F1",
        "3B":"F2",
        "3C":"F3",
        "3D":"F4",
        "3E":"F5",
        "3F":"F6",
        "40":"F7",
        "41":"F8",
        "42":"F9",
        "43":"F10",
        "44":"F11",
        "45":"F12",
        "46":"PRTSCR",
        "47":"SCRLOCK",
        "48":"PAUSE",
        "49":"INS",
        "4A":"HOME",
        "4B":"PGUP",
        "4C":"DEL",
        "4D":"END",
        "4E":"PGDOWN",
        "4F":"RIGHT",
        "50":"LEFT",
        "51":"DOWN",
        "52":"UP",
        "53":"NUMLOCK",
	"54":["/"],
	"55":["*"],
	"56":["-"],
	"57":["+"],
	"58":"ENTER",
	"59":["1"],
	"5A":["2"],
	"5B":["3"],
	"5C":["4"],
	"5D":["5"],
	"5E":["6"],
	"5F":["7"],
	"60":["8"],
	"61":["9"],
	"62":["0"]
        }

nums = []
keys = open('captured.txt')
for line in keys:
        nums.append(line.strip().upper())
keys.close()
output = list()
for n in nums:
    push=n.split(":")
    if push[2] == "00":
        continue
    else:
        key=push[2]
    if push[0] != "02":
        islist=mappings[key]
        if type(islist) is list:
            output.append(mappings[key][0])
        else:
            output.append(mappings[key])
    else:
        output.append(mappings[key][1])
final=dict()
empty_line=list()
final[0]=[]
counter=0
for i in output:
    if i == "\n":
        counter += 1
        final[counter]=["\n"]
    elif i == "DOWN":
        if counter < len(final):
            counter += 1
    elif i== "UP":
        if counter != 0:
            counter -= 1
    else:
        final[counter].append(i)

output=""
for x in final.keys():
    for y in final[x]:
        output+=y
print output
