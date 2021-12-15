from art import logo
from art import vs
from game_data import data
import random
from replit import clear

def get(x):
    if x == "":
        A = data.pop (data.index(random.choice(data)))
        B = data.pop (data.index(random.choice(data)))
    else:
        A = x
        B = data.pop (data.index(random.choice(data)))
    while B['follower_count']==A['follower_count']:
        B = data.pop (data.index(random.choice(data)))
    return (A,B)

def compare(i,a,b):
    if i == "A" :
        if a['follower_count']>b['follower_count']:
            return True
        else: return False
    else:
        if a['follower_count']<b['follower_count']:
            return True
        else: return False
        
def check(i):
    return False if (i!="A" or i!="B")else True 
      
score=0
looper=True
while looper:
    print(f"SCORE: {score}")
    (A,B)=get("")
    print(logo)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
    i=input("Who has more followers? Type 'A' or 'B': ")
    while check(i):
        i = input("Bad input! Who has more followers? Type 'A' or 'B': ")
    if not compare(i,A,B):
        print(f"Game Over! Your score is {score}")
        if input("Press any key for new game or 'n' to quit game! " )=="n":looper=False
        else:score=0
    else:
        score+=1
        (A,B)= get(A) if i=="A" else get(B)
    clear()