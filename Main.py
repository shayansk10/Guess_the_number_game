import random

n = random.randint(1, 100)
a = -1

guesses = 1

print("------ Welcome to Guess the number game: ------")

while(a != n):
    a = int(input("Enter the number: "))
    if(a > n):
        print("Lower number please !")
        guesses +=1
    elif(a < n):
        print("Higher number please !")
        guesses += 1

    
print(f"You have guessed the number {n} correctly in {guesses} attempts...")

