# part two of the game 
# in this part we just added an attempts counter toto track how many guesses the player makes before before finding the secret number 
# here is the code 

import random 
def get_secret_number():
  return number.random(1,20)
number = guess_ssecret_number()
attempts = 0   # we statrt the counter from the zero befor the player start guessing
while True :
  guess = int(input("guess the secret number from 01 to 20"))
  attempts + = 1       # form here , after each guess we start adding a try tell the playeer finf the number 
if guess < number :
  print ("the number is bigger")
elif guess > number :
  print ("the number is smaller")
else :
  print ("you found the number , attempts , "atempts")
  break 
