#Another "Hello World"

choice = 0
while choice != 10:
  print("""   Another "Hello World"   """)
  print("1.Hello World!")
  print("2.Simple Calculator")
  print("10.Quit")
  choice = input("Please enter a choice:")
  if int(choice) == 1:
     choice = input("Do you want your name in here(Y/N)?")
     if choice.upper() == 'Y':
        name = input("Please enter your name:")
        print("Hello " + name + "!")
     else:
        print("Hello World!")
     choice = 0 #If I don't do this we'll get a value error later.
  elif int(choice) == 2:
    x = input("Please enter a number:")
    y = input("Please enter another number:")
    print("Here's what you get when you combine them(hopefully):" + str(int(x) + int(y)))
