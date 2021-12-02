import json,os
print("Welcome to JDNLyricsMaker by Zanga and (StevenSB updated)")
codename=input("Codename of song: ")
running=True
a=0
b=False
lines={'lyrics':[]}
while running==True:
    ready=input("Ready? y=Lrc file(input.lrc) n=Make JDNLyrics [y/n] ")
    if ready=="n":
        time=int(input("Time: "))
        if b==True:
            lines["lyrics"][-1]["duration"]=time-int(lines["lyrics"][-1]["time"])
            b=False
        elif b==False:
            pass
        answer=input("Make duration automatically [y/n]: ")
        if answer=="y":
            b=True
            duration=0
        elif answer=='n':
            b=False
            duration=int(input("Duration: "))
        text=input("text: ")
        islineending=int(input("isLineEnding [0 is no, 1 is yes]: "))
        line={"time":time,"duration":duration,"text":text,"isLineEnding":islineending}
        lines["lyrics"].append(line)
    elif ready=="y":
        with open("input.lrc", encoding="utf-8") as f:
            lrcfile = f.read().splitlines()
        outputjson = []
        count = 0
        for line in lrcfile:
            i = 0
            while i < len(line):
                if line == "":
                    break
                elif line[i] == "[":
                    i += 1
                    if line[i] + line[i+1] == "ti":
                        name = line.split(":")[-1].replace("]", "")
                        break
                    elif line[i] + line[i+1] == "ar":
                        artist = line.split(":")[-1].replace("]", "")
                        break
                    elif line[i] + line[i+1] == "la":
                        language = line.split(":")[-1].replace("]", "")
                        break
                    elif line[i] + line[i+1] == "re":
                        creator = line.split(":")[-1].replace("]", "")
                        break
                    elif line[i] + line[i+1] == "ve":
                        version = line.split(":")[-1].replace("]", "")
                        break
                    elif line[i].isdigit() == True:
                        words = line.split("  ")
                        o = i
                        l = 0
                        b = False
                        while l < len(words):
                            textwithtime = words[l]
                            timefromlrc = textwithtime[o:o+8]
                            timelist = timefromlrc.split(":")
                            minute = int(timelist[0])
                            second = int(timelist[-1].split(".")[0])
                            millisecond = int(timelist[-1].split(".")[-1])
                            finaltime = (minute * 60000) + (second * 1000) + millisecond
                            duration = 100
                            if textwithtime[o+8] == "]":
                                shit = True
                            else:
                                shit = False
                            if words[-1] == textwithtime:
                                isLineEnding = 1
                                if shit == True:
                                    text = textwithtime.split("]")[-1]
                                else:
                                    text = textwithtime.split(">")[-1]
                            else:
                                isLineEnding = 0
                                if shit == True:
                                    text = textwithtime.split("]")[-1] + " "
                                else:
                                    text = textwithtime.split(">")[-1] + " "
                            lyric = {
                                "time": finaltime,
                                "duration": duration,
                                "text": text,
                                "isLineEnding": isLineEnding
                            }
                            outputjson.append(lyric)
                            l += 1
                            count += 1
                        i+=len(line)
                    else:
                        break
                    i += 1
        with open(codename+"_lyrics.json","w") as c:
            json.dump(outputjson, c)
            print("Done!!")
        running=False

