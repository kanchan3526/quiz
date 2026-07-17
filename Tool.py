import time
name=input("Enter You name=")
hour = int(time.strftime("%H"))
if hour<12:
    print("Good Morning..!",name)
elif hour<18:
    print("Good Afternoon..!",name)
else:
    print("Good Night...!",name)
# print("How can  You help You,",name)
while True:
    command = input("\nEnter What you are saying..").lower()

    if command == "hello" :
        print("Hello! How are you?")
    elif command =='fine':
        print("Okay..!How can You help You.")
    elif command == "time":
        print("Current Time:", time.strftime("%H:%M:%S"))

    elif command == "date":
        print("Today's Date:", time.strftime("%d/%m/%Y"))

    elif command == "bye":
        print("Goodbye! Have a nice day.")
        break

    else:
        print("Sorry! I don't understand this command.")
        
            