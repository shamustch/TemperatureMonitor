import time
import tkinter as tk
import subprocess

window = tk.Tk()
window.title("Temp Monitor")
window.iconphoto(False, tk.PhotoImage(file='img/icon.png'))
window.geometry("300x100")
v = tk.StringVar()
tk.Label(textvariable=v).pack(fill=tk.X,pady=5,padx=10)
button = tk.Button(text='Exit',command=window.destroy).pack(fill=tk.X,pady=2,padx=10)
def update_label():
    tempcmd = ['hostname']##['vcgencmd','measure_temp']
    while 1:
        v.set(subprocess.Popen( tempcmd, stdout=subprocess.PIPE ).communicate()[0])
        try:
            window.update()
        except tk.TclError:
            quit
while True:
    update_label()
    time.sleep(0.8)
window.mainloop()