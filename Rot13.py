import pickle, random, string
from Language import language


"""Rot 13 is a specified rotation or caesar cipher for that play's on a specific idea, that 13 is the mid-point of the alphabet"""
class rot13(language):
    def __init__(self, pt):
        super().__init__()
        self.plainText = pt
        self.plainTextSpaces = self.plainText
        self.rot13LCAlphabet = ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    def ciphering(self):
        self.plainText = self.plainText.lower()
        self.plainText = self.plainText.replace(" ", "")
        for x in range(0, len(self.plainText)):
            for y in range(0, len(self.rot13LCAlphabet)):
                if self.PlaintextAlphabet[y] == self.plainText[x]:
                    self.CipherText += self.rot13LCAlphabet[y]

        self.sortCaps()
    def sortCaps(self):
        spaceList = self.capsDefiner()
        letterList = []
        if spaceList != []:
            for x in range(0,len(self.CipherText)):
                if x in spaceList:
                    letterList.append(self.CipherText[x].upper())
                    print(self.CipherText[x])
                else:
                    letterList.append(self.CipherText[x])
                    print(self.CipherText[x])
        else:
            for x in range(0,len(self.CipherText)):
                letterList.append(self.CipherText[x])
        tempWord = ""
        for x in range(0, len(self.CipherText)):
            tempWord += letterList[x]
        self.CipherText = tempWord
        self.plainText = self.plainTextSpaces
        self.sortSpacing()


    def sortSpacing(self):
        spaceList = self.spaceDefiner()
        letterList = []
        for x in range(0, len(self.CipherText)):
            letterList.append(self.CipherText[x])
        if spaceList != []:
            for x in range(0, len(letterList)):
                if x in spaceList:
                    letterList.insert(x, " ")
            
        tempWord = ""
        for x in range(0, len(letterList)):
            tempWord += letterList[x]
        self.CipherText = tempWord
        



            
    
