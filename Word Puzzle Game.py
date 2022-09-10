word=['RAEHTF','KABRE','CYROTNU','RENEG','OAERELANP']
inp=0
word2=['FATHER','BRAKE','GREEN','COUNTRY','AEROPLANE']
while len(word)!=0:
    o=word.pop()
    a=input("Write the word by rearrenging the letters of {}: ".format(o)).upper()
    if a in word2:
        print("Correct")
        inp+=1
    else:
        print("incorrect")
        inp-=1

print("You have scored {} in this Game".format(inp))
