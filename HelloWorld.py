#Another "Hello World"

choice = 0
while int(choice) != 10:
  print("""   Another "Hello World"   """)
  print("1.Hello World!")
  print("10.Quit")
  choice = input("Please enter a choice:")
  if int(choice) == 1:
    print("Hello World!")
    
