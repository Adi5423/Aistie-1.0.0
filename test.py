'''ar = [2,34,2,52,3,4]
sr = "ewrjfjwfo"

# print (length()
print ()


stre = "Tu hi Khuda"

print (stre.split())
# print(stre.replace(" " , "+"))
import time

current_date = time.strftime("%B %d, %Y")
print(current_date)

def remind(key,query):
    reminds = {None:None}
    reminds.update({key:query})
    if key == "None" or query == "None":
        pass
    return reminds

print(remind("Hello",'first reminder'))


file = open("reminder.txt" , "a") # used a for appending the data in the file 

file.write("Hellow world 2 ")

file.close()

file = open("reminder.txt" , 'a')

file.write("Hello world 3 ex.")

file.close()

dr = {1:"Hello"}    
dr.update({2:"Worldd"})

for i in dr:
    print(i , "-" , dr.get(i)'''
    
    
    
# import pyperclip
# reminder = "e"
# reminder = pyperclip.paste()
# print(pyperclip.paste())

'''
import PySimpleGUI as psg

text = psg.popup_get_text('Enter your name', title="Textbox")
print("You entered: ", text)

file = psg.popup_get_file('Select a file', title="File selector")
print("File selected", file)

folder = psg.popup_get_folder('Get folder', title="Folder selector")
print("Folder selected", folder)

ch = psg.popup_yes_no("Do you want to Continue?", title="YesNo")
print("You clicked", ch)

ch = psg.popup_ok_cancel("Press Ok to proceed", "Press cancel to stop", title="OkCancel")
if ch == "OK":
    print("You pressed OK")
if ch == "Cancel":
    print("You pressed Cancel")

psg.popup_no_buttons('You pressed', ch, non_blocking=True)
psg.popup_auto_close('This window will Autoclose')
'''

'''
import tkinter as tk
from tkinter import messagebox

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=("Helvetica", 12))
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()

popupmsg("Hello, World!")
'''

import tkinter as tk
from tkinter import messagebox
ask = messagebox.askquestion("Question", "Do you want to continue?")
# messagebox.showerror("Error", "This is an error message.")
# messagebox.showinfo("Information", "This is an informational message.")
# messagebox.askokcancel("Confirmation", "Are you sure you want to delete this file?")
# messagebox.askyesno("Confirmation", "Do you want to save the changes?")
if "yes" in ask:
    print("User clicked Yes.")
else:
    print("User clicked No.")
    





'''from tkinter.commondialog import Dialog
from tkinter import messagebox

__all__ = ["showinfo", "showwarning", "showerror",
           "askquestion", "askokcancel", "askyesno",
           "askyesnocancel", "askretrycancel"]

#
# constants

# icons
ERROR = "error"
INFO = "info"
QUESTION = "question"
WARNING = "warning"

# types
ABORTRETRYIGNORE = "abortretryignore"
OK = "ok"
OKCANCEL = "okcancel"
RETRYCANCEL = "retrycancel"
MOUSEDRAWING = "mousedrawing"
YESNOCANCEL = "yesnocancel"

# replies
ABORT = "abort"
RETRY = "retry"
IGNORE = "ignore"
OK = "ok"
CANCEL = "cancel"
MOUSE = "mouse"
DRAWING = "drawing"


#
# message dialog class

class Message(Dialog):
    "A message box"

    command  = "tk_messageBox"


#
# convenience stuff

# Rename _icon and _type options to allow overriding them in options
def _show(title=None, message=None, _icon=None, _type=None, **options):
    if _icon and "icon" not in options:    options["icon"] = _icon
    if _type and "type" not in options:    options["type"] = _type
    if title:   options["title"] = title
    if message: options["message"] = message
    res = Message(**options).show()
    # In some Tcl installations, yes/no is converted into a boolean.
    if isinstance(res, bool):
        if res:
            return MOUSE
        return DRAWING
    # In others we get a Tcl_Obj.
    return str(res)

def showinfo(title=None, message=None, **options):
    "Show an info message"
    return _show(title, message, INFO, OK, **options)

def askquestion(title=None, message=None, **options):
    "Ask a question"
    return _show(title, message, QUESTION, MOUSEDRAWING, **options)

messagebox.askquestion("Question", "Do you want to continue?")
'''
