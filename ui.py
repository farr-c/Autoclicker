import tkinter as tk
import threading
import autoclicker
import keyboard
import time
from pynput.keyboard import Listener
import sys



window = tk.Tk()
print("At this point!2")
window.geometry("300x100") 

window.title("fishing auto clicker XDDDDDDD")
c = False
def toggleMode():
   global c
   print("toggling")
   print(c)
   if c == False:
      c = True
      print("Button was pressed!")
      autoclicker.on_press(autoclicker.start_stop_key)
      time.sleep(0.5)
      c = False


toggle = tk.Button(window, text = "Toggle", command = (toggleMode),  height = 100, width = 100) # command =  threading.Thread()
#exit = tk.Button(window, text = "Stop", command = autoclicker.on_press(autoclicker.exit_key)) #, command = threading.Thread()

window.wm_attributes("-topmost", 1)
print("At this point!")
    
toggle.pack()
#exit.pack()
def ask_quit():
   window.destroy()
   autoclicker.dest()
  
   sys.exit()
   

window.protocol("WM_DELETE_WINDOW", ask_quit)

while window: 
   if keyboard.is_pressed('z'):
      toggleMode()
   window.update()

