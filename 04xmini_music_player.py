def music_player():
    repeat = False
    print("Welcome to the Music Player!")
    print("Press 'r' to toggle repeat on/off.")
    print("Press 'q' to quit.")

while True:
    command = input("Enter command: ")
    if command == "r":
        repeat = not repeat
        if repeat:
            print("Repeat is on, playing music")
            
            
