addressDict = {}

def appplyMask(mask, numberToMask, value):
    # mask 1 becomes 1 on number, all else unchanged
    apply1 = int(mask.replace("X", "0"), 2)
    initial = numberToMask | apply1

    # Change all X's to 0 for initial
    changeX0 = int(mask.replace("0", "1").replace("X", "0"), 2)
    initial0 = initial & changeX0

    counter = initial0
    for i in range(pow(2, mask.count("X"))):
        # everything except X's becomes 1
        counter = (counter | changeX0) + 1
        # keep only X's
        keepX = int(mask.replace("1", "0").replace("X", "1"), 2)
        counter = (counter & keepX) | initial0

        addressDict[counter] = value
        print("ini2 " + "{0:b}".format(counter).zfill(36) + " " + counter.__str__())

filepath = 'input_14.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   mask = ""
   while line:
       if "mask" in line:
           mask = line[7:]
       else:
            splitLines = line.split(" = ")
            address = int(splitLines[0][4:-1])
            number = int(splitLines[1])

            appplyMask(mask, address, number)
  
       line = fp.readline()
       cnt += 1

   sum = 0
   for k, v in addressDict.items():
    sum += v
   
   print("sum = " + sum.__str__())