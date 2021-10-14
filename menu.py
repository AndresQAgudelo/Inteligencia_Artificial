from tkinter import *
from tkinter import font
from tkinter.font import Font
import main


def menuPpal(NumeroNodo, NombreElemento): #Menu Principal, recibe numero de nodo y numero de elemento
  screen = Tk()
  screen.title("Adivina, Adivinador...")
  screen.config(bg = "#9999FF")
  #Aqui va la imagen del adivino sonriente
  img = PhotoImage(file = "dudoso.png")
  Titulos = Font(family="Lucida Grande", size=12)
  
  
  #Agrega la imagen
  Label(screen, image = img, bg = "#9999FF", font = Titulos).grid(row = 0, column = 3, rowspan = 4, sticky="e", padx=10, pady=10)


  
  Pregunta = Label(screen, text = " Estas pensando en ... ?", bg = "#9999FF", font = Titulos)
  Pregunta.grid(row = 0, column = 0, columnspan = 3, sticky="we", padx=10, pady=10)


  #Muestra el elemento Atributo/Objeto en pantalla
  Label(screen, text = NombreElemento, bg = "#C3ABD0", fg= "black").grid(row = 1, column = 0, columnspan = 3, sticky="we", padx=10, pady=10)


  def Yes():#Aumenta el nodo * 2
    global nuevo, GoP
    GoP = 1
    nuevo = NumeroNodo * 2
    screen.destroy()
  

  def No():#Aumenta el nodo * 2 + 1
    global nuevo, GoP
    GoP = 0
    nuevo = NumeroNodo * 2 + 1
    screen.destroy()
  
    


  ButtonYes = Button(screen, text = "Yes", command = Yes, bg = "#B9E0A5")
  ButtonYes.grid(row = 3, column = 1, padx=10, pady=10)

  ButtonNo = Button(screen, text = "No", command = No, bg = "#FF9999")
  ButtonNo.grid(row = 3, column = 2, padx=10, pady=10)



  screen.mainloop()

  return (nuevo, GoP)


def MenuGanar():#Menu de Ganar
  screen = Tk()
  screen.title("Adivina, Adivinador...")
  screen.config(bg = "#9999FF")
  img = PhotoImage(file = "feliz.png")
  Titulos = Font(family="Lucida Grande", size=12)

  Label(screen, image = img, bg = "#9999FF").grid(row = 0, column = 3, rowspan = 3, sticky="we", padx=10, pady=10)

  Label(screen, text = "!HE GANADO¡", bg = "#9999FF", font = Titulos).grid(row = 0, column = 0, columnspan = 3, sticky="we", padx=10, pady=10)

  Label(screen, text = "¿Quieres seguir jugando?", bg = "#9999FF").grid(row = 1, column = 0, columnspan = 3, sticky="we", padx=10, pady=10)


  def Yes():
    global salir
    salir = True
    screen.destroy()
  
  def No():
    global salir
    salir = False
    screen.destroy()

  ButtonYes = Button(screen, text = "Yes",  bg = "#B9E0A5", command = Yes)
  ButtonYes.grid(row = 2, column = 1, padx=10, pady=10)

  ButtonNo = Button(screen, text = "No", bg = "#FF9999", command = No)
  ButtonNo.grid(row = 2, column = 2, padx=10, pady=10)

  screen.mainloop()

  return(salir)



  








