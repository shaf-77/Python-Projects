print("Welcome to my Computer Quiz!")

playing=input("Do you want to play? ")

#lower() changes case of the user input to lower case to match the 'if' condition
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score=0

answer=input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer=input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer=input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer=input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer=input("What does USB stand for? ").lower()
if answer == "universal serial bus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got "+ str(score) +" questions correct!")
print("You got "+ str((score/5)*100) +"%")