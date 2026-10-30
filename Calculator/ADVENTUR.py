import ti_system

print("PRESS enter TO START")
key = ti_system.wait_key()

def wait():
  while ti_system.wait_key() != 5:
    pass

def devmenu():
  print("dev menu")
  print("pick a scene")
  print("1=main")
  print("2=nightmare")

def nightmare():
  pass
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
      print("1 was chosen, a function would go here")
      break
    elif choice == "2":
      print("2 was chosen, a function would go here")
      break
    elif choice == "3":
      print("A scene would go here---you picked 3.")
      break
    else:
      print("Dumbass, choose something.")
  


def main():
  print("WELCOME TO ADVENTURE!")
  print("Controls:")
  print("ENTER Sart/Continue")
  print("1,2,3,4,5 Option select")
  wait()
  nightmare()
  

if key == 5:
  main()
elif key == 147:
  devmenu()
else:
  print("GAME OVER!")