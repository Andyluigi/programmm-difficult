import time

def cycle():
    while True():
        print ("hello", "hello world")
    return None

def anti_cycle():
    return SystemExit (cycle)

print (anti_cycle)

time.sleep (2)

def while_anti():
    anti_cycle
    while True():
        print ("hello")
    
    return None

time.sleep(2)
print (while_anti)