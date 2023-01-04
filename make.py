import FieldPredictor as fp
from operator import itemgetter
import time

def spacePrt(s,l):
    if(type(s) == float):
        s = round(s,3)
    return(str(s)+(" "*(l-len(str(s))) if len(str(s))<= l else "#"))

def colPrt(s,l):
    if(type(s) == float):
        s = round(s,3)
    CSI="\x1B["
    return(CSI+"31;40m" + str(s) + CSI + "0m"+(" "*(l-len(str(s))) if len(str(s))<= l else "#"))
	
def red(s):
    CSI="\x1B["
    return(CSI+"31;40m" + str(s) + CSI + "0m")

class smarty:
    def __init__(self):
        self.things = [] # row names
        self.attrs = [] # col names
        self.data = []
        self.predTable = []
    def learn(self,s,verbose = False):
        if verbose:
            print(s)
        s = s.lower()
        s = s.split(" ")
        rn = s[0]
        cn = s[len(s)-1]
        neg = False
        neg = True if "not" in s else False
        if len(self.data) == 0:
            self.data.append([None])
            self.attrs.append(cn)
            self.things.append(rn)
        else:
            if (rn in self.things) == False:
                self.things.append(rn)
                self.data.append([None]*len(self.data[0]))
            if (cn in self.attrs) == False:
                self.attrs.append(cn)
                for k in self.data:
                    k.append(None)
        self.data[self.things.index(rn)][self.attrs.index(cn)] = 0 if neg else 1
        if verbose:
            print(self.data)
    def think(self):
        predictions = []
        for n,k in enumerate(self.data):
            for n2,k2 in enumerate(k):
                if(k2 == None):
                    predictions.append((self.things[n],self.attrs[n2],fp.fetchpPrediction(self.data, n, n2)))
        """thirdCol = map(itemgetter(2), predictions)
        Pos = thirdCol.index(max(thirdCol))
        Neg = thirdCol.index(max(thirdCol))
        print(predictions[Pos])
        print(predictions[Neg])"""
    def prt(self):
        out = ""
        out+=spacePrt("",15)
        for k in self.attrs:
            out+=spacePrt(k,15)
        for n,k in enumerate(self.data):
            out+="\n"+spacePrt(self.things[n],15)
            for k2 in k:
                out+=spacePrt(str(k2),15)
        print("\n\n"+out+"\n\n")
    def predPrt(self):
        out = ""
        out+=spacePrt("",15)
        for k in self.attrs:
            out+=spacePrt(k,15)
        for n,k in enumerate(self.data):
            out+="\n"+spacePrt(self.things[n],15)
            for n2,k2 in enumerate(k):
                if(k2 == None):
                    out+=spacePrt(fp.fetchpPrediction(self.data,n,n2),15)
                else:
                    out+=spacePrt(str(k2),15)
        print("\n\n"+out+"\n\n")

