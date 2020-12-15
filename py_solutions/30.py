input = [0,13,1,16,6,17]

counter = 1

lastSeenDict = {}
for i in input:
    lastSeenDict[i] = [counter]
    counter = counter + 1

lastSpoken = input[-1]

def speak(numToSpeak):
    global spoken, lastSpoken, lastSeenDict, counter
    lastSpoken = numToSpeak

    if(lastSeenDict.get(lastSpoken, -1) != -1):
        lastSeenDict[lastSpoken].append(counter)
        lastSeenDict[lastSpoken] = lastSeenDict[lastSpoken][-2:]
    else:
        lastSeenDict[lastSpoken] = [counter]

while True:
    if (lastSpoken in lastSeenDict) and len(lastSeenDict[lastSpoken]) == 2:
        speakNow = lastSeenDict[lastSpoken][1] - lastSeenDict[lastSpoken][0]

        speak(speakNow)
    else:
        speak(0)
        
    if counter == 30000000:
        break
    counter = counter + 1

print("lastSpoken", lastSpoken)