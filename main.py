from tkinter import *
import pyperclip
from functions import encode, decode
# tkinter module is imported for GUI
# pyperclip module is used to copy strings and texts to clipboard
# encode and decode functions are imported from the function file

root = Tk()
# creating an tkinter frame
# storing the frame in root

# defining variables to store the strings
msg = StringVar()
key = StringVar()
mode = StringVar()
result = StringVar()

root.geometry("1200x6000")
root.title("Python Project")

top = Frame(root, width=1600, relief=SUNKEN)
top.pack(side=TOP)
top_msg = Label(top, font=('helvetica', 50, 'bold'), text="Message Encoder-Decoder",
                fg="Black", bd=10, anchor='w')
top_msg.grid(row=0, column=0)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)


# function for the reset button
def Reset():
    msg.set("")
    key.set("")
    mode.set("")
    result.set("")


# function for the copy button
def Copy(txt=result):
    txt = str(txt.get())
    pyperclip.copy(txt)


# function for the exit button
def xit():
    root.destroy()


# function for encoding / decoding
def Ref():
    clr = msg.get()
    k = key.get()
    m = mode.get()
    if m == 'e':
        result.set(encode(k, clr))
    else:
        result.set(decode(k, clr))


# Creating labels
message_label = Label(f1, font=('arial', 16, 'bold'), text="Enter the Message: ", bd=16,
                      anchor='w')
message_label.grid(row=0, column=0)
message_text = Entry(f1, font=('arial', 16, 'bold'), textvariable=msg, bd=10, insertwidth=4,
                     bg='yellow', justify='right')
message_text.grid(row=0, column=1)

key_label = Label(f1, font=('arial', 16, 'bold'), text="KEY", bd=16, anchor='w')
key_label.grid(row=1, column=0)
key_text = Entry(f1, font=('arial', 16, 'bold'), textvariable=key, bd=10, insertwidth=4,
                 bg='yellow', justify='right')
key_text.grid(row=1, column=1)

mode_label = Label(f1, font=('arial', 16, 'bold'), text="MODE(e for Encode / d for Decode)",
                   bd=16, anchor='w')
mode_label.grid(row=2, column=0)
mode_text = Entry(f1, font=('arial', 16, 'bold'), textvariable=mode, bd=10, insertwidth=4,
                  bg='yellow', justify='right')
mode_text.grid(row=2, column=1)

result_label = Label(f1, font=('arial', 16, 'bold'), text="Result :- ",
                     bd=16, anchor='w')
result_label.grid(row=3, column=0)
result_text = Entry(f1, font=('arial', 16, 'bold'), textvariable=result, bd=10, insertwidth=4,
                    bg='yellow', justify='right')
result_text.grid(row=3, column=1)

# Creating buttons
calc_button = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'),
                     width=10, text='Calculate', bg='green', command=Ref).grid(row=3, column=2)
reset_button = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'),
                      width=10, text='RESET', bg='green', command=Reset).grid(row=7, column=1)
copy_button = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'),
                     width=10, text='COPY TEXT', bg='blue', command=Copy).grid(row=7, column=2)
exit_button = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'),
                     width=10, text='EXIT', bg='red', command=xit).grid(row=7, column=3)

root.mainloop()
