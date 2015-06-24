from Tkinter import Tk, Frame, BOTH, StringVar, Entry, Text, Label
from ttk import Combobox, Button, Style
import csv

#from tkinter import Tk, Frame, BOTH
#from ttk import Frame, Button, Style


class Example(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.value_of_combo = 'X'

        self.initUI()
        
    def inputReader(self):
        box1=[]
        box2=[]
        box4=[]
        box5=[]
        box6=[]
        box7=[]
        fin = open('input.csv', 'rU')
        csv_fin = csv.reader(fin)

        for row in csv_fin:
            box1.append(str(row[0]))
            box2.append(str(row[1]))
            box4.append(str(row[3]))
            box5.append(str(row[4])) 
            box6.append(str(row[5]))
            box7.append(str(row[6]))           
        return box1, box2, box4, box5, box6, box7

    def newselection(self, event, updatedBox4, updatedBox5, updatedBox6, updatedBox7):
        choice=''
        index = ''
        colorVar = 'black'
        textVar = ''
               
        self.value_of_combo = self.box.get()
        choice = self.value_of_combo

        index = self.box.current()

        self.label = Label(self.parent, text='Date Created:    ' + updatedBox4[index]).place(x=50, y=400)
        self.label = Label(self.parent, text='Date Deleted:    ' + updatedBox5[index]).place(x=50, y=450)
        self.label = Label(self.parent, text='Explanation:    ' + updatedBox7[index]).place(x=50, y=350)

        print updatedBox6[index]
        if updatedBox6[index] == '0':
            colorVar = 'red'
            textVar = 'NOT ALLOWED!    Don'+"'"+'t even think about it.'
            fontVar = "Helvetica 16 bold italic"
            MUE = Label(self.parent, fg = colorVar, font = fontVar, text= textVar).place(x=100, y=300)
        if updatedBox6[index] == '1':
            colorVar = 'green'
            textVar = 'ALLOWED!    You can totally bill that.                '
            fontVar = "Helvetica 16 bold italic"
            MUE = Label(self.parent, fg = colorVar,font = fontVar, text= textVar).place(x=100, y=300)

    def dropdownUpdater(self, code2selection, updatedBox4, updatedBox5, updatedBox6, updatedBox7):
        select_index=''
        
        self.label = Label(self.parent, text="select a column 2 code")
        code2Label = self.label
        code2Label.place(x=300, y=225)
        
        self.box_value = StringVar()
        self.box = Combobox(self.parent, textvariable=self.box_value)
        combo2=self.box
        combo2.place(x=300, y=250)
        combo2['values'] = code2selection
        combo2.bind("<<ComboboxSelected>>", lambda event, updatedBox4=updatedBox4,updatedBox5=updatedBox5, updatedBox6=updatedBox6, updatedBox7=updatedBox7: self.newselection(event, updatedBox4, updatedBox5, updatedBox6, updatedBox7))
        print select_index

    def OnPressEnter(self, event):
        code2selection = []
        code2index=[]
        updatedBox4=[]
        updatedBox5=[]
        updatedBox6=[]
        updatedBox7=[]
        
        box1, box2, box4, box5, box6, box7 = self.inputReader()

        for i in range(len(box1)):
            if self.entry.get() == box1[i]:
                code2selection.append(box2[i])
                updatedBox4.append(box4[i])
                updatedBox5.append(box5[i])
                updatedBox6.append(box6[i])
                updatedBox7.append(box7[i])
        self.dropdownUpdater(code2selection, updatedBox4, updatedBox5, updatedBox6, updatedBox7)
    
    def initUI(self):
        choice1 =''
        current_entry = ''
        searchresult=''
        
        self.parent.title("CPT code checker")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.label = Label(self.parent, text="enter a column 1 code and press enter"+'\n'+ "(e.g. C1080)")
        code1Label = self.label
        code1Label.place(x=25, y=200)


        self.entry = Entry(self.parent)
        searchbox = self.entry
        searchbox.place(x=50, y=250)      
        searchbox.bind("<Return>", self.OnPressEnter)        

def main():
    root = Tk()
    root.geometry("500x500")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()  
