from tkinter import *
from tkinter import messagebox
root = Tk()

#root properties
root.title("My Checklist App")
root.geometry("620x590")
root.resizable(0,0)
root.iconbitmap("logo.ico")

#setting up general fonts and colours
myFont=("Times New Roman",12)
rootColour = "#000080"
buttonColour = "#f7f7f7"
root.config(bg=rootColour)

#function definition
#function to add text in list box when add item button is clicked
def addItem():
    if listEntry.get()=="":
        messagebox.showinfo("Illegal Entry in the list","Cannot enter blank items in list box")
    else:
        listBox.insert(END,listEntry.get())
        listEntry.delete(0,END)

#function to remove the anchored(selected) item form the list
def removeItem():
        listBox.delete(ANCHOR)
        
#function to clear entire list
def clearList():
        listBox.delete(0,END)
        
def saveList():
    #we will open a file(in write mode) and write the required contents
    #with checklist.txt opened in write mode named as f for your future reference
    with open("checklist.txt","w") as f:
        #pass
        listTuple = listBox.get(0,END)
        
        for items in listTuple:
            f.write(items+"\n")
#function to recall stored elemnets in text file
def openList():
    try:
        with open("checklist.txt","r") as f:
            for line in f:
                listBox.insert(END,line)
    except:
        pass
        
        
#Creating layout of the app
#creating frames
inputFrame = Frame(root,bg=rootColour)
outputFrame = Frame(root,bg=rootColour)
buttonsFrame = Frame(root,bg=rootColour)
inputFrame.pack()
outputFrame.pack()
buttonsFrame.pack()

#create layout of elements in input frame-entry widget,add item button
listEntry = Entry(inputFrame,width=45,borderwidth=4,font=myFont)
listAddButton = Button(inputFrame,text="Add Item",borderwidth=2,font=myFont,bg=buttonColour,command=addItem)
listEntry.grid(row=0,column=0,padx=5,pady=5)
listAddButton.grid(row=0,column=1,padx=5,pady=5)

#create layout of elements in output frame-listbox and scrollbar
scrollBar=Scrollbar(outputFrame)
listBox=Listbox(outputFrame,height=20,width=53,borderwidth=3,font=myFont,yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview)
listBox.grid(row=0,column=0)
scrollBar.grid(row=0,column=1,sticky="NS")

#create layout of elements in buttons frame-list remove,list clear,save,quit
listRemoveButton =Button(buttonsFrame,text="Remove Item",borderwidth=4,font=myFont,bg=buttonColour,command=removeItem)
listClearButton =Button(buttonsFrame,text="Clear List",borderwidth=4,font=myFont,bg=buttonColour,command=clearList)
saveButton =Button(buttonsFrame,text="Save",borderwidth=4,font=myFont,bg=buttonColour,command=saveList)
quitButton =Button(buttonsFrame,text="Exit",borderwidth=4,font=myFont,bg=buttonColour,command=root.destroy)
listRemoveButton.grid(row=0,column=0,padx=2,pady=10)
listClearButton.grid(row=0,column=1,padx=2,pady=10,ipadx=5)
saveButton.grid(row=0,column=2,padx=2,pady=10,ipadx=15)
quitButton.grid(row=0,column=3,padx=2,pady=10,ipadx=15)



#main-logo
openList()
root.mainloop()