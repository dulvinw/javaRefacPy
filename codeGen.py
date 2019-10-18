import fileinput
import sys
import re, mmap

print(sys.argv[1])

textFile = open(sys.argv[1], 'r')
funcNameMatch = re.search('functionName = "(.*)"', textFile.read())
argList = []
with open(sys.argv[1], 'r') as File:
    for line in File:
        argMatch = re.search('(?:@Argument\(name = "(.*)", type = (.*), )+', line)
        if argMatch:
            argList.append(argMatch)

textFile.seek(0)
returnArg = re.search('@ReturnType\(type = (.*), ',textFile.read())
print(returnArg)
