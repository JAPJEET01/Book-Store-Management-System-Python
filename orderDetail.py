
from tkinter import *
from tkinter.ttk import Treeview
# from .database import AddEmployee
import database
import add_employee
import employee_tables
from tkinter import messagebox

class orderDetail():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('EMPLOYEE DETAILS')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2 )
        self.height=int((self.fullheight-500)/2)

        s = "1000x500+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def ViewEmployee(self, id):
        self.orderId = id

        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="1000", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F'), selectmode="extended")

        self.tr.heading('#0',text="ID")
        self.tr.column('#0',minwidth=0,width=25,stretch=NO)

        self.tr.heading('#1',text="Book Name")
        self.tr.column('#1',minwidth=0,width=170 ,stretch=NO)

        self.tr.heading('#2', text="Cost")
        self.tr.column('#2', minwidth=0, width=170, stretch=NO)
        
        self.tr.heading('#3', text="Quantity")
        self.tr.column('#3', minwidth=0, width=170, stretch=NO)

        self.tr.heading('#4', text="T.Cost")
        self.tr.column('#4', minwidth=0, width=170, stretch=NO)



        self.tr.place(x=0,y=0,width="1000",height="500")

        j = 0
        # print("manage",database.allEmployees)
        for i in database.orderDetail(self.orderId):
            self.tr.insert('', 0, text=i[0], values=(i[1],i[2],i[3], (int(i[2]) * int(i[3]))))        

        self.tr.bind('<Double-Button-1>', self.actions)

        self.root.mainloop()

    def actions(self,e):
        #get the values of the selected row
        tt=self.tr.focus()

        #get the column Id
        col= self.tr.identify_column(e.x)
        print(col)
        print(self.tr.item(tt))

        id=(
            self.tr.item(tt).get('text'),
        )

        print(id, col)
        # if col == '#6':
            



        # self.root.mainloop()
if __name__ == '__main__':
    obj = orderDetail()
    obj.ViewEmployee()