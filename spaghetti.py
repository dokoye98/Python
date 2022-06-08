#i am eating spaghetti now and im bored :)
from lib2to3.pgen2.token import EQUAL


answer= "to eat some spaghetti"
question=" why do you think i am here today"

name =input("what is your name ")
print ("Gretting ",name, question)
guess=input().lower()
if guess==answer:
    print("correct")
else:
    for x in range(4):
        print ("WRONG!!")

print ("how can you be so wrong")
