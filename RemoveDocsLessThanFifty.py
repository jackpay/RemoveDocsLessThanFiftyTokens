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
    inLoc = "/Volumes/External/Datasets/pos-ner-samples-music/tok-pos-el/28-04-2014"
    outLoc = "/Volumes/External/Datasets/pos-ner-samples-music/above-20-tokens"
    copyDocsGreaterThanN(inLoc,outLoc,20)
