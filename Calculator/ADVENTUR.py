import ti_system

print("PRESS enter TO START")
key = ti_system.wait_key()

def wait():
  while ti_system.wait_key() != 5:
    pass

playerChoices = []

personality = {
    "curiosity": 0, # Interest in the unknown 
    "bravery": 0, # Willingness to face danger 
    "defiance": 0, # Resistance to authority 
    "caution": 0, # Preference for safety 
    "compassion": 0, # Willingness to help others 
    "cruelty": 0, # Selfishness or malicious intent 
    "certainty": 0 # Confidence in one's decisions 
}

def wakeUp():
  print("Wake up TBA")

def nightmareOP1():
  print("You approach the light, it gets brighter as you get closer...")
  wait()
  print("You can't help but reach your hand out...")
  wakeUp()

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
      break
    elif choice == "2":
      playerChoices.append("Ran_from_the_light")
      personality["bravery"] -= 1
      personality["caution"] += 1
      nightmareOP2()
      break
    elif choice == "3":
      personality["defiance"] += 1
      playerChoices.append("Stood_still_at_light")
      nightmareOP3()
      break
    else:
      print("Dumbass, choose something.") # this is a placeholder, CHANGE IT. 
  print(playerChoices)


def main():
  print("WELCOME TO ADVENTURE!")
  print("Controls:")
  print("ENTER Sart/Continue")
  print("1,2,3,4,5 then press ENTER to choose")
  wait()
  nightmare()
  


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