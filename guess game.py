import random

n = 20
to_be_guessed=int(n*random.random())+1
print(to_be_guessed)
flag="true"
while flag=="true":
    m=3
    life=0
    guess=0
    while guess!=to_be_guessed:
         life = life + 1
         if life > m:
             print("sorry!! You have Give Up")
             break
         guess = int(input("\nEnter a New Number: "))

         if guess > to_be_guessed:
             print("Number Too Large")
         elif guess < to_be_guessed:
             print("Number Too Small")
         else:
             print("Congratulations!! You Made It")
             break
         print(" lifes remaining: ", m - life)
    choice=input("\nWould you like to continue? (y/n)\n")
    if choice=='n':
        break
exit()