import Conectar_BBDD as bd
from tkinter import *

from tkinter import Tk, Frame, Button, Canvas

root = Tk()

def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

root.overrideredirect(True) # turns off title bar, geometry
root.geometry('400x100+200+200') # set new geometry

# make a frame for the title bar
title_bar = Frame(root, bg='white', relief='raised', bd=2)

# put a close button on the title bar
close_button = Button(title_bar, text='Close this Window', command=root.destroy)

# a canvas for the main area of the window
window = Canvas(root, bg='black')

# pack the widgets
title_bar.pack(expand=1, fill="x")
close_button.pack(side="right")
window.pack(expand=1, fill="both")

# bind title bar motion to the move window function
title_bar.bind('<B1-Motion>', move_window)

root.mainloop()

app = Tk()
dark_blue = "#2B2D42"
white = "#DBD9DB"
app.title("Geeks For Geeks")
app.geometry("800x500")

p1 = PhotoImage(file='2021-12-03_16h59_00.png')
app.iconphoto(False, p1)

menu_bar = Menu(app, bg='black', fg='white', activebackground='#004c99', activeforeground='white')
# filemenu = Menu(menubar, tearoff=0, background='#000099')

file = Menu(menu_bar, tearoff=False, background=dark_blue, fg=white)

file.add_command(label="New")
file.add_command(label="Exit", command=app.quit)
menu_bar.add_cascade(label="File", menu=file)

edit = Menu(menu_bar, tearoff=False, background=dark_blue, fg=white)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
menu_bar.add_cascade(label="Edit", menu=edit)


app.config(menu=menu_bar)
colors = "https://coolors.co/337ab7-2b2d42-f7e733-c6e2e9-f4faff-dbd9db-131b23"
app.mainloop()


# tecnoempleo = bd.Conectar_BBDD("proyecto_python_tecnoempleo")
# print(tecnoempleo.consultar_todos("empleo"))
# values = ["nombre_puesto", "nombre_empresa", "fecha_empleo", "modo_remoto", "tipo_jornada", "tipo_contrato"]
# ordered = "fecha_empleo"
# a = "desc"
# print(tecnoempleo.consultar("empleo", ordered, a, values))




