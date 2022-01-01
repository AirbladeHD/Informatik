from tkinter import *
from tkinter import filedialog as fd

def button_action():
    print("Neue Datei wird erstellt")

def buttonOpen():
    filetypes = (
        ('Duke App File', '*.daf'),
        ('All files', '*.*')
    )
    file = fd.askopenfilename(filetypes=filetypes)
    print(file)

def buttonSave():
    f = fd.asksaveasfile(mode='w', defaultextension=".daf")
    if f is None:
        return
    text2save = "<Duke_App_File>"
    f.write(text2save)
    f.close()
    print("Datei erstellt")

def dragStart(event):
    block.move()
    block2.move()

class Element:
    def __init__(self, rect_x1, rect_y1, rect_x2, rect_y2, col, row, name):
        self.id = canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill="#476042")
        #self.canvas.grid(row = 0,column = 0)
        x = rect_x2-rect_x1
        y = rect_y2-rect_y1
        if(not x%2 == 0):
            x += 1
        if(not y%2 == 0):
            y += 1
        x = x/2
        y = y/2
        self.tx = x
        self.ty = y
        #self.text = self.canvas.create_text(x, y, text=text, fill="#fff")
        #self.canvas.grid(row=row, column=col)
        #print(id)
        canvas.tag_bind(self.id, "<Button-1>", dragStart)

    def move(self):
        def motion(event):
            canvas.moveto(self.id, event.x, event.y)
            #newCoords = self.canvas.coords(self.id)
            #self.canvas.moveto(self.text, event.x+self.tx, event.y+self.ty/1.5)
        canvas.tag_bind(self.id, "<B1-Motion>", motion)
        

mainWindow = Tk()
mainWindow.title("Duke App Designer")
mainWindow.geometry("1900x1200")
mainWindow.iconphoto(False, PhotoImage(file='icon.ico'))

menu = Menu(mainWindow)

file_menu = Menu(menu, tearoff=0)
help_menu = Menu(menu, tearoff=0)

file_menu.add_command(label="Neu", command=button_action)
file_menu.add_command(label="Speichern", command=button_action)
file_menu.add_command(label="Speichern unter", command=buttonSave)
file_menu.add_command(label="Öffnen", command=buttonOpen)
file_menu.add_separator()
file_menu.add_command(label="Beenden", command=mainWindow.quit)

menu.add_cascade(label="Datei", menu=file_menu)
menu.add_cascade(label="Hilfe", menu=help_menu)

mainWindow.config(menu=menu)

canvas = Canvas(mainWindow, width=1900, height=1200)
canvas.pack()

block = Element(0, 0, 150, 80, 0, 0, "block")
block2 = Element(0, 100, 150, 180, 0, 1, "block2")

mainWindow.mainloop()