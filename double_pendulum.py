from random import randint
from tkinter import *
import numpy as np

class Pendulum:
    """docstring for Pendulum"""
    def __init__(self):
        self.l1, self.l2 = 100, 100
        self.m1, self.m2 = 20, 20
        self.g = 9.81
        self.theta1, self.theta2 = randint(0,360), randint(0, 360)
        self.theta1dot, self.theta2dot = 0, 0

        self.init()

    def theta1prime(self):
            inst1 = -self.g*(2*self.m1+self.m2)*np.sin(self.theta1)-self.m2*self.g*np.sin(self.theta1-2*self.theta2)
            inst2 = -2*np.sin(self.theta1-self.theta2)*self.m2*(self.theta2dot**2*self.l2+self.theta1dot**2*self.l1*np.cos(self.theta1-self.theta2))
            divise = self.l1*(2*self.m1+self.m2-self.m2*np.cos(2*self.theta1-2*self.theta2))
            
            return (inst1 + inst2)/divise

    def theta2prime(self):
            inst1 = 2*np.sin(self.theta1-self.theta2)
            inst2 = self.theta1dot**2*self.l1*(self.m1+self.m2)
            inst3 = self.g*(self.m1+self.m2)*np.cos(self.theta1)+self.theta2dot**2*self.l2*self.m2*np.cos(self.theta1-self.theta2)
            divise = self.l2*(2*self.m1+self.m2-self.m2*np.cos(2*self.theta1-2*self.theta2))
            
            return (inst1*(inst2+inst3))/divise

    def launch(self):
        while 1:
            self.formula1 = self.theta1prime()
            self.formula2 = self.theta2prime()

            self.theta1dot = self.theta1dot + self.formula1 * 0.01
            self.theta2dot = self.theta2dot + self.formula2 * 0.01
            self.theta1 = self.theta1 + self.theta1dot * 0.01
            self.theta2 = self.theta2 + self.theta2dot * 0.01

            self.x1, self.y1 = self.l1*np.sin(self.theta1), self.l1*np.cos(self.theta1)
            self.x2, self.y2 = self.x1 + self.l2*np.sin(self.theta2), self.y1 + self.l2*np.cos(self.theta2)

            self.canvas()

    def canvas(self):
            self.canv.create_oval(self.x1+225, self.y1+90, self.x1+245, self.y1+110, fill='red')
            self.canv.create_oval(self.x2+225, self.y2+90, self.x2+245, self.y2+110, fill='red')
            self.canv.create_line(270, 100, 200, 100, width=5, fill='black')
            self.canv.create_line(235, 100, self.x1+235, self.y1+100, width=2, fill='red')
            self.canv.create_line(self.x1+235, self.y1+100, self.x2+235, self.y2+100, width=2, fill='red')
            
            self.canv.update()
            self.canv.delete("all")

    def init(self):
        self.app = Tk()
        self.app.title('Double Pendulum')
        self.app.configure(background='gray')
        self.app.geometry("830x350")
        self.canv = Canvas(self.app)
        self.canv.place(x=10,y=10)

        self.widget()

        self.app.mainloop()

    def widget(self):
        self.m1input = IntVar()
        self.m2input = IntVar()
        self.l1input = IntVar()
        self.l2input = IntVar()

        m1text = Label(self.app, height=2, width=2,text='M1',fg='black', bg='grey')
        m1text.place(x=550, y=20)

        m1entry = Entry(self.app, textvariable=self.m1input, background='white')
        m1entry.bind("<Return>", self.m1var)
        m1entry.place(width=90,height=25)
        m1entry.place(x=600, y=30)

        m2text = Label(self.app, height=2, width=2,text='M2',fg='black', bg='grey')
        m2text.place(x=550, y=80)

        m2entry = Entry(self.app, textvariable=self.m2input, background='white')
        m2entry.bind("<Return>", self.m2var)
        m2entry.place(width=90,height=25)
        m2entry.place(x=600, y=90)

        l1text = Label(self.app, height=2, width=2,text='L1',fg='black', bg='grey')
        l1text.place(x=550, y=210)

        l1entry = Entry(self.app, textvariable=self.l1input, background='white')
        l1entry.bind("<Return>", self.l1var)
        l1entry.place(width=90,height=25)
        l1entry.place(x=600, y=220)

        l2text = Label(self.app, height=2, width=2,text='L2',fg='black', bg='grey')
        l2text.place(x=550, y=280)

        l2entry = Entry(self.app, textvariable=self.l2input, background='white')
        l2entry.bind("<Return>", self.l2var)
        l2entry.place(width=90,height=25)
        l2entry.place(x=600, y=290)
        
        self.launch()

    def m1var(self, event=None):
        self.m1 = self.m1input.get()
        print(str(self.m1)+" > M1 change")

    def m2var(self, event=None):
        self.m2 = self.m2input.get()
        print(str(self.m2)+" > M2 change")

    def l1var(self, event=None):
        self.l1 = self.l1input.get()
        print(str(self.l1)+" > L1 change")

    def l2var(self, event=None):
        self.l2 = self.l2input.get()
        print(str(self.l2)+" > L2 change")

if __name__ == '__main__':
    Pendulum()
