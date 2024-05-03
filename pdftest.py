from pypdf import PdfWriter
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

##pdfs = ["C:\\Users\\Owner\\Documents\\汎用版ハンドアウト\\【HP】2023 TAXES david hunter.pdf","C:\\Users\\Owner\\Documents\\汎用版ハンドアウト\\【HP】conceptual penis.pdf"]
##
##merger = PdfWriter()
##
##for pdf in pdfs:
##    merger.append(pdf)
##
##merger.write("C:\\Users\\Owner\\Documents\\NEW PDF.pdf")
##merger.close()

#in command console
#pip install pypdf

#in command consol
#pip install pyinstaller


root = tk.Tk()
root.title = "ISA File Merger"

root.geometry("1000x500")

mainframe = ttk.Frame(root)
mainframe["padding"] = (5,5)
#mainframe.grid()
mainframe.pack(expand = "True", fill="both")
#mainframe.columnconfigure(0, weight = 1)
#mainframe.columnconfigure(1, weight = 1)
#mainframe.columnconfigure(2, weight = 1)
#mainframe.columnconfigure(3, weight = 1)
#mainframe.columnconfigure(4, weight = 1)
#mainframe.columnconfigure(5, weight = 1)
#mainframe.columnconfigure(6, weight = 1)
#mainframe.columnconfigure(7, weight = 1)
#mainframe.columnconfigure(8, weight = 1)
#mainframe.columnconfigure(9, weight = 1)
#mainframe.columnconfigure(10, weight = 1)

maxCols = 6

def valChanged():
    global frames
    global loadBtns
    global labels
    global val
    global numbers
    global delBtns
    #print(numLessons.get())
    if numLessons.get().isdigit():
        if int(numLessons.get()) > val:
            #print("bigger")
            diff = int(numLessons.get())-val
            cur = len(frames)
            #print(diff)
            #print(cur)
            for i in range(diff):
                MakeFrame(i+cur)
                
                #print("added")
            #mainframe.update()
        elif int(numLessons.get()) < val:
            #print("smaller")
            diff = val - int(numLessons.get())
            cur = len(frames)
            #print(cur)
            for i in range(diff):
                #print(cur+i-1)
                f = frames.pop()
                f.grid_forget()
                b = loadBtns.pop()
                b.grid_forget()
                l = labels.pop()
                n = numbers.pop()
                n.grid_forget()
                d = delBtns.pop()
                d.grid_forget()
                del f
                del b
                del l
                del n
                del d
        val = int(numLessons.get())
        #print(val)

valstr = tk.StringVar()
val = 2

frames = []
loadBtns = []
delBtns = []
labels = []

numbers = []

numLessons = tk.Spinbox(mainframe,textvariable = valstr, from_ = 2,\
                        to = 35, increment = 1, command = lambda *args: valChanged())
numLessons.grid(column = 0,row = 3)
numLessons.bind("<Return>", lambda *args: valChanged())
#valstr.trace('w',lambda *args: valChanged(val))

schoolName = tk.StringVar()
schoolNameEntry = tk.Entry(mainframe, textvariable = schoolName)
schoolNameEntry.grid(column = 0,row = 1)

label = tk.Label(mainframe,text = "Enter school name")
label.grid(column = 0, row = 0)

label = tk.Label(mainframe,text = "Enter number of files to combine")
label.grid(column = 0, row = 2)

def Combine():
    if schoolName.get() == "":
        return
    pass

def load(i):
    print(i)
    n = tk.filedialog.askopenfilename()
    if n != "":
        #print(n)
        labels[i].configure(text = os.path.basename(n).split('.')[0])

def Del(i):
    print(i)

def MakeFrame(i):
    frame = ttk.Frame(mainframe)
    frame["padding"] = (10,5)
    #frame["borderwidth"] = 5
    frame["relief"] = "groove"
    
    
    label = tk.Label(frame, text = str(i+1).zfill(2))
    label.grid(column = 0,row = 0)
    numbers.append(label)
    
    label = tk.Label(frame, text = "N/A",wraplength=100)
    label.grid(column = 1,row = 0)
    labels.append(label)

    btn = tk.Button(frame,text = "Del", command = lambda b_i = i: Del(b_i))
    btn.grid(column = 2, row = 0)
    delBtns.append(btn)
                
    btn = tk.Button(frame,text = "Load", command = lambda b_i = i: load(b_i))
    btn.grid(column = 1, row = 1)
    loadBtns.append(btn)
                
    frame.grid(column = (i)%maxCols+1, row = int(3+i/maxCols))
                #print(i+cur)
                #print(int(2+(i+cur)/maxCols))
    frames.append(frame)

combineButton = tk.Button(mainframe, text = "Combine", command = Combine)
combineButton.place(relx = 1.0, rely = 1.0, anchor = tk.SE)



for i in range(2):
    frame = ttk.Frame(mainframe)
    frame["padding"] = (10,5)
    #frame["borderwidth"] = 5
    frame["relief"] = "groove"
    
    label = tk.Label(frame, text = str(i+1).zfill(2))
    label.grid(column = 0,row = 0)
    numbers.append(label)
    
    label = tk.Label(frame, text = "N/A",wraplength=100)
    label.grid(column = 1,row = 0)
    labels.append(label)
    
    btn = tk.Button(frame,text = "Load", command = lambda b_i = i: load(b_i))
    btn.grid(column = 1, row = 1)
    loadBtns.append(btn)

    btn = tk.Button(frame,text = "Del", command = lambda b_i = i: Del(b_i))
    btn.grid(column = 2, row = 0)
    delBtns.append(btn)
    
    frame.grid(column = i+1, row = 3)
    frames.append(frame)
    
    

root.mainloop()
