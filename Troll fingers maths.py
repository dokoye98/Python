#Troll fingers maths game

name=input("I am the great Troll IV, what is your name?  ")
print (name)
print ("you are required to pay a fine to cross my bridge\n I want to eat gold coins :)")
totalcoins=0
while totalcoins<8:
    coins =int(input("how many coins are you going to give me "))
    totalcoins=totalcoins+coins
    print ("total so far-",totalcoins)
print ("you may cross ",name)
if totalcoins>8:
    change=totalcoins-8
    print ("you gave me too much so i will give you one last chance to earn your money back")
    question=(" how many coins should i give back")
    print ("now young ",name,question)
    guess=input()
if guess==change:
    print("correct here you go",change,"you will need to cross this bridge again soon and you better have more gold coins")
else:
    for x in range(4):
        print("HAHAHA")
print ("your change was ",totalcoins -8,"but it is mine now" )
if guess != change:
    print ("thank you for the extra portion -",change," gold coins")