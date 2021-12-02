from tkinter import *
import Conectar_BBDD as bd

root = Tk()

root.title("¡Welcome!")
root.geometry('350x200')
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

tecnoempleo = bd.Conectar_BBDD("proyecto_python_tecnoempleo")
# print(tecnoempleo.consulta("empleo"))
values = ["nombre_puesto", "nombre_empresa", "fecha_empleo", "modo_remoto", "tipo_jornada", "tipo_contrato"]
ordered = "nombre_puesto"
a = "asc"
print(tecnoempleo.consultar("empleo", ordered, a, values))

# root.mainloop()