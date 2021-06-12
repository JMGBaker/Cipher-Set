
"""
This class is the class from which all the ciphers are derrived as it makes it easier
to create a new cipher class from this
"""
class Language:
      def __init__(self):
        self.plainText = ""
        self.CipherText = ""
        self.ShiftVal = 0
        self.plainTextList = []
        self.PlaintextAlphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.PlaintextLCAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
      "Finds the spaces in plain text"
      def spaceDefiner(self, List = []):
          for x in range(0,len(self.plainText)-1):
            if self.plainText[x] == " ":
                  List.append(x)
          return List
      
      "Finds the Capital letters in plain text"
      def capsDefiner(self, List = []):
          for x in range(0,len(self.plainText)-1):
            if self.plainText[x] in self.PlaintextAlphabet:
               List.append(x)
          return List

