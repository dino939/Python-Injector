#byDenger 28.08.2022
#Dinjector open-sorce for нишибродов
import tkinter
import customtkinter
from concurrent.futures import process
from pymem import *
import requests
import os
import os.path
import time
import tkinter as tk
from tkinter import messagebox as mb
#url
img = 'https://cdn.discordapp.com/attachments/981448833940742154/1013518850907709511/di.png'#url to image 
r2 = requests.get(img, allow_redirects=True)
img_exists = os.path.exists('C:\Program Files (x86)\Microsoft\Temp\di.png')# where save img
file_exists = os.path.exists('C:\Program Files (x86)\Microsoft\Temp\secur32.dll')# where save dll

if img_exists == True:
        pass
else:
     open('C:\Program Files (x86)\Microsoft\Temp\di.png', 'wb').write(r2.content)

#Settings
app = customtkinter.CTk() 
customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue") 
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)
label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT,text="DINJECTOR")
label_1.pack(pady=12, padx=10) 
app.geometry("300x400")
app.resizable(width=False,height=False)
app.title("dinjector")
app.iconphoto(False, tk.PhotoImage(file='C:\Program Files (x86)\Microsoft\Temp\di.png'))
app.wm_attributes('-alpha', 0.95) 

#function
def button_function():
    url = requests.get("https://pastebin.com/raw/pgGp24zC").text#pastbin with dll url
    response = requests.get(url)
    status = requests.get("https://pastebin.com/raw/0yQ717ji").text#status pastbin 1 or why is off
    if status == "1":
        open("C:\Program Files (x86)\Microsoft\Temp\secur32.dll", "wb").write(response.content)
        dll_path = "C:\Program Files (x86)\Microsoft\Temp\secur32.dll"
        dll_path_bytes = bytes(dll_path, "UTF-8")
        process_name = "java.exe"
        try:
            open_process = Pymem(process_name)
            process.inject_dll(open_process.process_handle, dll_path_bytes)
            mb.showinfo('D-success', 'Injected')
        except:
            mb.showinfo('D-error', 'Запустите Minecraft')
    else:
    
        mb.showinfo('D-error', f'Инжектор отключен по причине:{status}')
        exit()


#workspace
optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Noise", "Naomitian"])
optionmenu_1.pack(pady=12, padx=10)
optionmenu_1.set("Cheat.Version")
button = customtkinter.CTkButton(master=app, text="Inject", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()