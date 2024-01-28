strTxt = "Hello world"
intNum = 10
floatNum = 10.5
complexNum = 10j
listSeq = ["a", "b", "c"]
tupleSeq = ("d", "e", "f")
rangeSeq = range(5)
dictMap = {"a1" : 1, "b2" : 2}
setSet = {"g", "h", "i"}
frozeSet = frozenset({"j", "k", "l"})
boolBool = False
bytesBin = b"Test"
bytArrBin = bytearray(4)
memVewBin = memoryview(bytesBin)
noType =  None

strCast = str(15)
listCast = list(("A", "B", "C"))
tupleCast = tuple(("D", "E", "F"))
dictCast = dict(a3 = 3, b4 = 4)
setCast = set(("G", "H", "I"))
frozeCast = frozenset(("J", "K", "L"))
boolCast = bool(2)
bytesCast = bytes(4)

intStr = int("11")
intFloat = int(12.2)
floatInt = float(13)
floatStr = float("14.3")
strInt = str(15)
strFloat = str(16.4)

simpleStr = " Hey, sup"
longStr = """This string is designed to be
comically long. Note that it uses three
double quotations on each end. Single
quotes can be used as well."""
numStr = "0123456789"
formatStr = "Input values are: {}, {}, and {}"
formatStrI = "Value 2: {2} | Value 1: {1} | Value 0: {0}"
print("\tString START\n")

print(simpleStr[3])
for x in simpleStr:
    print(x)
print(len(simpleStr))
if "string" in longStr:
    print("Yep, string is in longStr.")
if simpleStr not in longStr:
    print("Nope, simpleStr is not in longStr.")

print(numStr[2:6])
print(numStr[:6])
print(numStr[2:])
print(numStr[-6:-3])

print(simpleStr.upper())
print(simpleStr.lower())
print(simpleStr.strip())
print(simpleStr.replace(",", "!"))
print(simpleStr.split(", "))
#There's many more string methods to show off.

print(simpleStr + " - " + numStr)

print(formatStr.format(21, 22, 23))
print(formatStrI.format(24, 25, 26))

print("A \'guy\' \\ dude\n made\troom\rfor \bodd \fstuff")


print("\tString END\n")


a, b, c = "Aa", "Bb", "Cc"

first = "part ONE"
second = first + ", part TWO"

lGroup = ["el", "al", "ol"]
l1, l2, l3 = lGroup
#use a global variable somewhere

#print("Type of input: " + str(type(intNum)))
print(a, b, c)
print(first, second)
print(l1, l2, l3)