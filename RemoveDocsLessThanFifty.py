__author__ = 'jp242'

import os
def copyDocsGreaterThanN(inLoc,outLoc, n=50):
    files = os.listdir(inLoc)
    for f in files:
        doc = open(inLoc + "/" + f, 'r')
        docStr = doc.read()
        tokens = docStr.split("\t")
        if len(tokens) > n:
            newDoc = open(outLoc + "/" + f,"w")
            newDoc.write(docStr)
            newDoc.close()
        doc.close()


if __name__ == "__main__":
    inLoc = "/Users/jp242/Documents/Projects/Lumi/Experiments/ner-two/non-music-parsed/tok-pos-per-loc-org/22-04-2014"
    outLoc = "/Users/jp242/Documents/Projects/Lumi/Experiments/ner-two/non-music-parsed-100"
    copyDocsGreaterThanN(inLoc,outLoc,100)
