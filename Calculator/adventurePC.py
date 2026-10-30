print("PRESS enter TO START")
key = input()

def wait():
  input("\n[Press Enter to continue]")

playerChoices = []

def characterGender():
  global playerGender
  while True:
    print("1. Male")
    print("2. Female")
    print("3. Nonbinary")
    print("4. Rage.")
    print("5. Other")
    choice = input("What is your gender? ")
    if choice == "1":
      playerGender = "Male"
      break
    elif choice == "2":
      playerGender = "Female"
      break
    elif choice == "3":
      playerGender = "Nonbinary"
      break
    elif choice == "4":
      playerGender = "Nonbinary"
      break
    elif choice == "5":
      playerGender = "Nonbinary"
      break
    else:
      print("Try again.")
      continue

def characterCreator():
  global playerName

  while True:
    playerName = input("What is your name? ")
    print("You've chosen the name " + playerName + ".")
    print("1. Yes")
    print("2. No")
    choice = input("Would you like to change your name? ")
    if choice == "1":
      continue
    elif choice == "2":
      break
    else:
      print("Not an answer.")
  characterGender()
  if playerGender == "Male":
    print("What a name...")
    wait()
    print("Time to begin your story, " + playerName + ".")
    wait()
    return
  elif playerGender == "Female":
    print("What a beautiful name.")
    wait()
    print("I suppose it is time to begin your story, " + playerName + ".")
    wait()
    return
  elif playerGender == "Nonbinary":
    print("Quite the name, " + playerName + ".")
    wait()
    print("Anyway, your adventure begins now...")
    wait()
    return


personality = {
    "curiosity": 0, # Interest in the unknown 
    "bravery": 0, # Willingness to face danger 
    "defiance": 0, # Resistance to authority 
    "caution": 0, # Preference for safety 
    "compassion": 0, # Willingness to help others 
    "cruelty": 0, # Selfishness or malicious intent 
    "certainty": 0 # Confidence in one's decisions 
}

def wakeUpCurious():
  print("You wake up curious PLACEHOLDER")

def wakeUpCautious():
  print("You wake up cautious PLACEHOLDER")

def wakeUpDefiant():
  print("You wake up defiant PLACEHOLDER")

def wakeUpCuriCautious():
  print("You wake up feeling curious yet cautious PLACEHOLDER")

def wakeUpBasic():
  print("You wake up a basic bitch. Placeholder.")

def wakeUp():
  print("Wake up TBA")
  wait()
  if personality["curiosity"] >= 2:
    wakeUpCurious()
  elif personality["caution"] >= 1:
    wakeUpCautious()
  elif personality["defiance"] >= 1:
    wakeUpDefiant()

def nightmareOP1():
  print("You approach the light, it gets brighter as you get closer...")
  wait()
  print("You can't help but reach your hand out...")

def nightmareOP2():
  print("OP2 TBA")

def nightmareOP3():
  print("OP3 TBA")

def nightmare():
  print("It's dark...")
  wait()
  print("There's a light ahead...")
  wait()
  while True:
    print("What will you do?")
    print("")
    print("1. Approach the light")
    print("2. Run from the light") 
    print("3. Stay put")
    choice = input("Choose: ")
    if choice == "1":
      personality["curiosity"] += 2
      personality["bravery"] += 1
      playerChoices.append("Approached_the_light")
      nightmareOP1()
      return
    elif choice == "2":
      playerChoices.append("Ran_from_the_light")
      personality["bravery"] -= 1
      personality["caution"] += 1
      nightmareOP2()
      return
    elif choice == "3":
      personality["defiance"] += 1
      playerChoices.append("Stood_still_at_light")
      nightmareOP3()
      return
    else:
      print("Dumbass, choose something.") # this is a placeholder, CHANGE IT. 

def main():
  print("WELCOME TO ADVENTURE!")
  print("Controls:")
  print("ENTER Sart/Continue")
  print("1,2,3,4,5 then press ENTER to choose")
  print("In rare cases, words are accepted, press ENTER to choose.")
  wait()
  characterCreator()
  nightmare()
  if "Approached_the_light" in playerChoices:
    print("Approached light")
  elif "Ran_from_the_light" in playerChoices:
    print("Ran light")
  elif "Stood_still_at_light" in playerChoices:
    print("Stood light")

def devmenu():
  print("dev menu")
  print("pick a scene")
  while True:
    print("1=main")
    print("2=nightmare")
    choice = input("scene#: ")
    if choice == "1":
      main()
      break
    elif choice == "2":
      nightmare()
      break
    else:
      print("Pick something or quit wasting my time.")



if key == 5:
  main()
elif key == 147:
  devmenu()
else:
  print("Bruh.")