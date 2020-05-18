import random;

class Die:
    """This generates the roll"""
    def __init__(faceCount):
        faceCount = faceCount
    def Roll(faceCount):
        return(random.randint(1,faceCount))



class Roll:
    def __init__(self,diceCount, faceCount):
        diceCount = diceCount
        faceCount = faceCount
    def DoRolls(diceCount, faceCount):
        i = 0
        rolls = diceCount
        #roll = random.randint(1,faceCount)
        value = 0
        while i < rolls:
            roll = random.randint(1,faceCount)
            value = value + roll
            print(roll)
            i += 1
       
        return value
    
class PRoll:
    def __init__(self,diceCount, faceCount):
        diceCount = diceCount
        faceCount = faceCount
    def DoPRoll(diceCount, faceCount):
        roll = random.randint(0,faceCount)
        return roll

