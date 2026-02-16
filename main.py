import random
def get_secret_number():
  return random.randint(1,20)
number = get_secret_number()

while True :
  guess = int(input("guess the secret number from 01 to 20 :"))

if guess < number:
  print ("the number is bigger")
elif guess > number:
  print ("the number  is smaller")
else:
  print("you find the number")
  break
  
