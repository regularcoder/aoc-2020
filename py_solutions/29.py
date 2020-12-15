input = [0,13,1,16,6,17]

counter = 1

lastSeenDict = {}
for i in input:
    lastSeenDict[i] = [counter]
    counter = counter + 1

lastSpoken = input[-1]

def speak(numToSpeak):
    global lastSpoken, lastSeenDict, counter
    lastSpoken = numToSpeak

    if(lastSpoken in lastSeenDict):
        lastSeenDict[lastSpoken].append(counter)
        lastSeenDict[lastSpoken] = lastSeenDict[lastSpoken][-2:]
    else:
        lastSeenDict[lastSpoken] = [counter]

while True:
    print("\n")
    print("lastSpoken: ", lastSpoken, "lastSeenDict", lastSeenDict)
    if (lastSpoken in lastSeenDict) and len(lastSeenDict[lastSpoken]) == 2:
        speakNow = lastSeenDict[lastSpoken][1] - lastSeenDict[lastSpoken][0]
        print("appending", speakNow, "since ", lastSpoken, "was spoken before.")
        speak(speakNow)
    else:
        print("appending 0 since ", lastSpoken, " was NOT spoken before")
        speak(0)
        
    if counter == 2020:
        break
    counter = counter + 1
    
   
print("lastSpoken", lastSpoken)