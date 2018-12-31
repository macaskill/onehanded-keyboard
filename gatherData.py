import turtle
import time

start = time.time()

def tupleBreaker(tup):
    ''' input tuple, return a list of each of the tuples entries'''
    if len(tup) == 1:
        return [tup[0]]
    else:
        return [tup[0]] + tupleBreaker(tup[1:])

def cleanString(string):
    """ cleans non-alpha characters and capitalizes the rest """
    s = ''
    for ch in string:
        if ch.isalpha():
            s = s + ch
        else:
            continue
    return s
# Global Variables :|||
# :||||||
alphaDict = {}

def initDict(iChr, fChr):
    ''' input a start and stop character to initialize a dictionary with key-pairs
    starting at iChr and finishing with fChr and all corresponding values set to zero'''
    if iChr == fChr:
        alphaDict[iChr] = 0
        return alphaDict
    else:
        alphaDict[iChr] = 0
        return initDict(chr(ord(iChr) + 1), fChr)



def countKeyFreq(string, key):
    """ counts a string for occurences of a
    given character, which is a key """
    i = 0
    for ch in string:
        if ord(ch) == ord(key):
            i = i + 1
        else:
            continue
    return i


def drawBar(tl, width, height):
    tl.left(90)
    tl.forward(height)
    tl.right(90)
    tl.forward(width-3)
    if height > 0:
        tl.write(height)
    tl.forward(2)
    tl.right(90)
    tl.forward(height)
    tl.left(90)


def main():
    s = "ADRHIA$N T$KAN#I$NAGNKEKRGA A gan#$GAKN#$grnagk $T"

    keyCount = initDict("A", "Z")


    for i in range(20):  #range of 10 is chosen because dataman.py was set to return 10 random articles
        path = "Wiki" + str(i+1) + ".txt"
        rawdoc = open(path, 'r')
        rawString = '',
        for line in rawdoc:
            for value in line.split():
                rawString = rawString + value
        rawString = cleanString(rawString.upper())
        rawdoc.close()
        for key in keyCount.keys():
            keyCount[key] = keyCount[key] + countKeyFreq(rawString, key)

    print(keyCount)
    totalChars = 0
    for key in keyCount.keys():
        totalChars = totalChars + keyCount[key]
    print(totalChars)

    wn = turtle.Screen()
    tess = turtle.Turtle()
    tess.setposition(20, 5)
    barWidth = 15
    tess.speed(0)
    tess.pensize(7)
    barHeight = int(max(keyCount.values()) * 1.15)
    wn.setworldcoordinates(0, 0, (26 * barWidth), barHeight)
    print("Computation took", time.time() - start, " seconds.")
    for key in keyCount.keys():
        tess.write(key)
        drawBar(tess, barWidth, int(keyCount[key]))

    print("Graphing took", time.time() - start, " seconds.")

    wn.exitonclick()


main()
