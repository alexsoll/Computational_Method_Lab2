from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from math import floor
import calc
import new_calc

class form:
    def __init__(self, master):

        frame = LabelFrame(master, text = "Введите коэффициенты : ")
        frame.pack(anchor = W)

        self.labelT = Label(frame, text = "T : ")
        self.labelT.pack(padx = 3, pady = 7, side = LEFT)
        self.T = Entry(frame, width = 5)
        self.T.pack(side = LEFT)
        self.T.insert(0, "1")
        self.labelL = Label(frame, text = "l : ")
        self.labelL.pack(side = LEFT)
        self.l = Entry(frame, width = 5)
        self.l.pack(side = LEFT)
        self.l.insert(0, "42")
        self.labelA = Label(frame, text = "a : ")
        self.labelA.pack(side = LEFT)
        self.a = Entry(frame, width = 5)
        self.a.pack(side = LEFT)
        self.a.insert(0, "1")
        self.labelH = Label(frame, text = "h : ")
        self.labelH.pack(side = LEFT)
        self.h = Entry(frame, width = 5)
        self.h.pack(side = LEFT)
        self.h.insert(0, "1")
        self.labelTau = Label(frame, text = "tau : ")
        self.labelTau.pack(side = LEFT)
        self.tau = Entry(frame, width = 5)
        self.tau.pack(padx = 3, pady = 7, side = LEFT)
        self.tau.insert(0, "0.1")

        self.coefFi = []
        self.labelFi = []
        self.coefB = []
        self.labelB = []

        frameFi = LabelFrame(master, text = "Введите коэффициенты для уравнения \u03C6 : ")
        frameFi.pack(anchor=W)

        for i in range(3):
            self.coefFi.append(Entry(frameFi,  width = 5))
            self.coefFi[i].pack(padx = 3, pady = 7, side = LEFT)
            self.labelFi.append(Label(frameFi))
            self.labelFi[i].pack(side = LEFT)
        self.labelFi[0].config(text = " + ")
        self.labelFi[1].config(text = " cos(pi * x / l) + ")
        self.labelFi[2].config(text = " cos(2 * pi * x / l) ")

        self.coefFi[0].insert(0, "0.14")
        self.coefFi[1].insert(0, "0")
        self.coefFi[2].insert(0, "0")
        
        frameB = LabelFrame(master, text = "Введите коэффициенты для уравнения b : ")
        frameB.pack(anchor=W)


        for i in range(5):
            self.coefB.append(Entry(frameB,  width = 5))
            self.coefB[i].pack(padx = 3, pady = 7, side = LEFT)
            self.labelB.append(Label(frameB))
            self.labelB[i].pack(side = LEFT)
        self.labelB[0].config(text = " + ")
        self.labelB[1].config(text = " cos(pi * x / l) + ")
        self.labelB[2].config(text = " sin(pi * x / l) + ")
        self.labelB[3].config(text = " cos(2 * pi * x / l) + ")
        self.labelB[4].config(text = " sin(2 * pi * x / l) ")

        self.coefB[0].insert(0, "0")
        self.coefB[1].insert(0, "1")
        self.coefB[2].insert(0, "0")
        self.coefB[3].insert(0, "0")
        self.coefB[4].insert(0, "0")

        ButtonFrame = Frame(master)
        ButtonFrame.pack(anchor=W, padx = 3, pady = 3   )
        self.CalcButton = Button(ButtonFrame, text = "Calculate", command= lambda: self.Calculate(master))
        self.CalcButton.pack(side = LEFT)

    def Calculate(self, master):
        self.args = []
        self.args.append(int(self.T.get()))
        self.args.append(float(self.l.get()))
        self.args.append(float(self.a.get()))
        self.args.append(float(self.h.get()))
        self.args.append(float(self.tau.get()))

        self.args.append(float(self.coefFi[0].get()))
        self.args.append(float(self.coefFi[1].get()))
        self.args.append(float(self.coefFi[2].get()))


        self.args.append(float(self.coefB[0].get()))
        self.args.append(float(self.coefB[1].get()))
        self.args.append(float(self.coefB[2].get()))
        self.args.append(float(self.coefB[3].get()))
        self.args.append(float(self.coefB[4].get()))

        #calc.main(self.args)
        new_calc.main(self.args)
        


root = Tk()
fb = form(root)
root.title("Сomputational_method_Lab2")
root.geometry("600x450")
root.mainloop()