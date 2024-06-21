print("Fill in the blank lyrics ")
print()
print("Type in the blank lyrics and see if you are as cool as me.")
print()

counter = 1
while True:
  print("Never going to ______ you up.")
  lyrics = input("What is the missing lyric? ").lower()
  if lyrics == "give":
    print("You got it!")
  else:
    print("Nope, try again.")
    counter += 1
  if lyrics == "give": 
    break
print("Thanks for playing!")

print("You got the correct lyrics im", counter,  "Attempt(s). ")