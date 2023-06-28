 # -----------------Coding___Decoding__Project-----------------------
from random import sample
st = input("Enter message: ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if coding=="1" else False
if(coding):
    nwords = []
    for word in words:
        if len(word)>=3:
            r1 = "dsf"    #[0:3]
            r2 = "jkr"    #[-3:]
            stnew = "".join((sample(r1,3))) + word[1:] + (word[0]) +  "".join((sample(r2,3)))
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])    
            
           # print(nwords)     #It gives an list to convert list into string we are using join function.....................
    print(" ".join(nwords))  
else:
    nwords = []
    for word in words:
        if (len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
            
    print(" ".join(nwords))            
    




