from Language import Language


class Rot(Language):
    def __init__(self, ShiftVal, pt):
        super().__init__()
        self.ShiftVal = ShiftVal
        self.plainText = pt
        self.plainTextSpaces = self.plainText
        self.ciphering()
    "Find the letter in the list"
    def findLetter(self, L):
        for x in range(0, len(self.PlaintextLCAlphabet)-1):
            if L == self.PlaintextLCAlphabet[x]:
                return x
            
    "Cipher the plaintext sentence"
    def ciphering(self):
        self.plainText = self.plainText.lower()
        self.plainText = self.plainText.replace(" ","")
        
        for letter in self.plainText:
            "print(letter)"
            letterPos = self.findLetter(letter)
            if letterPos + self.ShiftVal > 26:
                diff = letterPos + self.ShiftVal - 26
                self.CipherText += self.PlaintextLCAlphabet[diff]
                "print(self.CipherText)"
            else:
                self.CipherText += self.PlaintextLCAlphabet[letterPos + self.ShiftVal]
                "print(self.CipherText)"
        
        self.sortCaps()
        
    "Finds each capital letter in plaintext sentence"
    def sortCaps(self):
        spaceList = self.capsDefiner()
        letterList = []
        "print(spaceList)"
        if spaceList != []:
            for x in range(0,len(self.CipherText)):
                "print(x)"
                if x in spaceList:
                    letterList.append(self.CipherText[x].upper())
                    print(self.CipherText[x])
                else:
                    letterList.append(self.CipherText[x])
                    print(self.CipherText[x])
        else:
            for x in range(0,len(self.CipherText)):
                "print(self.CipherText[x])"
                letterList.append(self.CipherText[x])
        "print(letterList)"
        tempWord = ""
        for x in range(0, len(self.CipherText)):
            tempWord += letterList[x]
        self.CipherText = tempWord
        "print(self.CipherText)"
        self.plainText = self.plainTextSpaces
        self.sortSpacing()
        
    "Finds each space in plaintext sentence"
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
        
            

            
                
                
