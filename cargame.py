command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("car already stopped.")
        else:
            started = False
            print("car is stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit       
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")