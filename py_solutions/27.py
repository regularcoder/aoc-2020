def appplyMask(mask, number):
    mask1 = int(mask.replace("X", "0"), 2)
    mask0 = int(mask.replace("X", "1"), 2)
    
    return (number | mask1) & mask0

filepath = 'input_14.txt'
addressDict = {}
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   mask = ""
   while line:
       if "mask" in line:
           print("Setting mask to " + line[7:])
           mask = line[7:]
       else:
            splitLines = line.split(" = ")
            address = splitLines[0][4:-1]
            number = int(splitLines[1])

            masked = appplyMask(mask, number)

            addressDict[address] = masked
            print(" number " + number.__str__() + ", address " + address + ", masked " + masked.__str__())
       line = fp.readline()
       cnt += 1

   sum = 0
   for k, v in addressDict.items():
    sum += v
   
   print("sum = " + sum.__str__())