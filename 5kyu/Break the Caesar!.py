#https://www.codewars.com//kata/598e045b8c13926d8c0000e8
def break_caesar(message):
    alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz"]
    hits = {}        
    for x in range(len(alphabet)):          
        newmsg = ""
        for y in range(len(message)):
            if message[y].isalpha():
                charToAdd = alphabet[(alphabet.index(message[y].lower())+x)%26] 
                newmsg = newmsg + charToAdd
            elif message[y]==' ':           
                charToAdd = message[y]
                newmsg = newmsg + charToAdd   
        splitTrash = newmsg.split()         
        numHits = 0
        for w in splitTrash:
            if w in WORDS:
                numHits+=1                  
        hits[numHits]=x                                     
    greatest = 0                             
    for h in hits.keys():
        if h > greatest:
            greatest = h
    if hits[greatest] == 0:                 
        return 0
    else:
        return 26 - hits[greatest]
