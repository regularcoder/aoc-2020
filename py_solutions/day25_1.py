# To run: python day25_1.py

publicKey1 = 9789649
publicKey2 = 3647239

def transform(subject, loopSize):
    val = 1

    for i in range(loopSize):
        val *= subject
        val %= 20201227

    return val

def findLoopSize(subject, targetNumber):
    val = 1
    loopSize = 0

    while True:
        loopSize += 1
        val *= subject
        val %= 20201227

        if val == targetNumber:
            return loopSize

loopSize1 = findLoopSize(7, publicKey1)
loopSize2 = findLoopSize(7, publicKey2)

print(transform(publicKey1, loopSize2))
print(transform(publicKey2, loopSize1))