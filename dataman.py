from lxml import html
import requests

#This program will grab text from random WikiPedia articles and store text files in chosen dir
#https://en.wikipedia.org/wiki/Special:Random

wikiDict = {}


def cleanString(string):
    """ cleans non-alpha characters and capitalizes the rest """
    s = ''
    for ch in string:
        if ch.isalpha():
            s = s + ch
        else:
            continue
    return s



def getPageText(link):
    """ import html link string, receive a string containing all text on page"""
    page = requests.get(link)
    tree = html.fromstring(page.content)
    return tree.text_content().strip()

def saveTextFile(title, content, path):
    ''' saves text file of given string to specified path'''
    file = open(path + str(title) + '.txt', "w")
    for line in content:
        file.write(line)
    file.close()



def getArticles(n):
    """ will retrieve and save n articles from wikipedia"""
    for i in range(n):
         saveTextFile("Wiki" + str(i+1), getPageText("https://en.wikipedia.org/wiki/Special:Random"), "/Users/jmacaskill/PycharmProjects/OHKeys/")
         file = open("/Users/jmacaskill/PycharmProjects/OHKeys/" + "Wiki" + str(i+1) + ".txt", 'r')
         title = file.readline(-1)
         title = title[0:len(title)-12]
         wikiDict["Wiki" + str(i+1) + '.txt'] = title
         file.close()

def main():

    getArticles(20)
    print(wikiDict)

main()