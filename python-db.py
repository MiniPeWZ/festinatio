import tkinter
import mysql.connector
from tkinter import Tk
import os


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Muffe123",
    database="bruhdb"

)


class Form(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_interface()

    def initialize_interface(self):
        self.parent.title("Login")
        self.parent.config(background="thistle")
        self.parent.geometry("300x100")
        self.parent.resizable(False, False)

        global username
        global password

        username = tkinter.StringVar()
        password = tkinter.StringVar()

        self.labelUser = tkinter.Label(self.parent, text="Username: ", background="royal blue", foreground="Beige",
                                       font="Arial 8 bold")
        self.labelUser.place(x=25, y=25)

        self.entryUser = tkinter.Entry(self.parent, textvariable=username)
        self.entryUser.place(x=100, y=25)

        self.labelPass = tkinter.Label(self.parent, text="Password: ", background="royal blue", foreground="Beige",
                                       font="Arial 8 bold")
        self.labelPass.place(x=25, y=50)

        self.entryPass = tkinter.Entry(self.parent, textvariable=password)
        self.entryPass.place(x=100, y=50)

        self.buttonLogin = tkinter.Button(self.parent, text="LOGIN", font="Arial 8 bold", command=logs)
        self.buttonLogin.place(height=45, width=60, x=230, y=25)


def logs():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM login WHERE BINARY username = '%s' AND BINARY password = '%s'" % (
    username.get(), password.get())

    mycursor.execute(sql)
    highscores = []
    if mycursor.fetchone():

        print("POG!")
        os.system("python main.py")

    else:

        print("sadge")



def main():
    root = tkinter.Tk()
    b = Form(root)
    b.mainloop()


if __name__ == "__main__":
    main()







