#Another "Hello World"

choice = 0
while int(choice) != 10:
  print("""   Another "Hello World"   """)
  print("1.Hello World!")
  print("2.Simple Calculator")
  print("10.Quit")
  choice = input("Please enter a choice:")
  if int(choice) == 1:
    print("Hello World!")
  elif int(choice) == 2:
    x = input("Please enter a number:")
    y = input("Please enter another number:")
    print("Here's what you get when you combine them(hopefully):" + str(int(x) + int(y)))
    
