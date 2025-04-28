#Ask the user to input the current temperature .
temp=int(input("enter the current tempurature in celsius: "))
#based on the input display the appropriate message
if temp >= 30:
    print("it is a hot day. stay hydrated!")
elif temp >= 20 and temp <= 29:
    print("it is a warm day. Enjoy the weather!")
elif temp >= 10 and temp <= 19:
  print("it is a cool day. Wear a jacket!") 
else:
   print("it ia a cold day. Stay warm!")

