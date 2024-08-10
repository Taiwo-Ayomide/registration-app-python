from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title('LAUTECH BIOMETRIC SYSTEM')
        self.root.geometry('700x400+330+200')
        self.root.resizable(False, False)

        ############################################# Button FUnctions ###########################################################
        def iExit():
            messagebox.showwarning('Warning', 'Do you really want to exit?')
            self.root.destroy()

        def show():
            global filename
            global imgc
            filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image file", filetypes=(("PNG File", "*.png"),("JPG File", "*.jpg"),("All Files", "*.txt")))

            imgc = (Image.open(filename))
            resized_image = imgc.resize((180, 200))
            photo2 = ImageTk.PhotoImage(resized_image)
            newc.config(image=photo2)
            newc.image = photo2        
   

        #Top  Bar
        Label(self.root, text='LAUTECH BIOMETRIC CAPTURING SYSTEM', font='Vendana 18 bold').place(x=70, y=10)

        ################################################# Image ############################################################
        f = Frame(self.root, bd=3, bg='white', width=180, height=200, relief=GROOVE)
        f.place(x=500, y=60)

        imgc = PhotoImage(file='images/passport.png')
        newc = Label(f, image=imgc)
        newc.place(x=0,y=0)

        ############################################### Left Thumbprint Frame#####################################
        n = Frame(self.root, bd=3, bg='white', width=180, height=200, relief=GROOVE)
        n.place(x=50, y=60)

        ############################################### Right Thumbprint Frame #####################################
        r = Frame(self.root, bd=3, bg='white', width=180, height=200, relief=GROOVE)
        r.place(x=250, y=60)

        newb = Label(r)
        newb.place(x=0, y=0)
        ############################################# Checker ########################################################

        Checkbutton(self.root, text='Left Thumb').place(x=50, y=280)
        Checkbutton(self.root, text='Right Thumb').place(x=250, y=280)

        ############################################# Button ###############################################################
        Button(self.root, text='UPLOAD', bg='red', fg='white', font='Arial 15 bold', width=14, height=1, command=show).place(x=500, y=263)
        Button(self.root, text='SUBMIT', bg='yellow', fg='red', font='Arial 15 bold', width=14, height=1).place(x=500, y=307)
        Button(self.root, text='EXIT', bg='lightgreen', fg='white', font='Arial 15 bold', width=14, height=1, command=iExit).place(x=500, y=353)
        Button(self.root, text='CONTINUE', bg='red', fg='white', font='Arial 15 bold', width=14, height=1).place(x=50, y=325)
        



        self.root.mainloop()
Application()