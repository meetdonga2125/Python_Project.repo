import random

def check(comp,user):
    if comp==user:
        return 0
    
    elif(comp==0 and user==1):
        return -1
    
    elif(comp==1 and user==2):
        return -1
    
    elif(comp==2 and user==0):
        return -1
    
    else:
        return 1


comp = random.randint(0,2)
user = int(input("0 for Snake, 1 for water and 2 for Gun: "))

score = check(comp,user)
print(score)

print(f'comp: {comp}')
print(f'user: {user}')

if score==0:
    print("Game draw")
    
elif score==1:
    print("You win")
    
elif score==-1:
    print("You lose")    




