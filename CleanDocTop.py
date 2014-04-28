__author__ = 'jp242'
import os

def cleanDocs(inFile):
    f = open(inFile,'r')
    out = open(inFile + "-1.txt","w")
    strLine = str(f.readline())
    while strLine:
        newLine = strLine.split()
        doc = newLine[1]
        doc = doc.replace("{","").replace("}","")
        probs = doc.split(",")
        i = 0
        newLine = ""
        while i < len(probs):
            newLine += probs[i].split(":")[1] + "\t"
            i += 1
        out.write(newLine + "\n")
        strLine = str(f.readline())
    f.close()
    out.close()




if __name__ == "__main__":
    f = "/Users/jp242/Documents/Projects/Lumi/Experiments/functional-tests/parsed-doc-topic-model-0-out.txt"
    cleanDocs(f)