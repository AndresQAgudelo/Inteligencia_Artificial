from tkinter import *
from tkinter import font
from tkinter.font import Font



def menuEnseñar(): #Devuelve los dato que ingresa el usuari Objeto/Atributo

  screen = Tk()
  screen.title("Adivina, Adivinador...")
  screen.config(bg = "#9999FF")

  #Aqui va la imagen del adivino triste
  img = PhotoImage(file = "triste.png")
  Titulos = Font(family="Lucida Grande", size=12)


  
  #Agrega la imagen
  Label(screen, image = img, bg = "#9999FF").grid(row = 0, column = 3, rowspan = 5, sticky="e", padx=10, pady=10)

  #Pregunta por el objeto
  Objeto = Label(screen, text = " En que estas pensando ... ?", bg = "#9999FF", font = Titulos )
  Objeto.grid(row = 0, column = 0, columnspan = 3,sticky="ew", padx=10, pady=10)

  ObjetoEntry = Entry(screen, width = 5)
  ObjetoEntry.grid(row = 1, column = 1, sticky = "we", padx=10, pady=10, columnspan = 2)

  #Pregunta por el atributo
  Atributo = Label(screen, text = "Que lo diferencia de otros ... ?", bg = "#9999FF", font = Titulos)
  Atributo.grid(row = 2, column = 0, columnspan = 3,sticky="we", padx=10, pady=10)

  AtributoEntry = Entry(screen)
  AtributoEntry.grid(row = 3, column = 1, padx=10, pady=10, sticky = "we", columnspan = 2)


  def Enseñar():
    global O, A #O = Objeto, A = Atributo
    O = ObjetoEntry.get()
    A = AtributoEntry.get()
    screen.destroy()



  ButtonEnseñar = Button(screen, text = "Enseñar", command = Enseñar)
  ButtonEnseñar.grid(row = 4, column = 2, padx=10, pady=10, sticky = "w")



  screen.mainloop()

  return (O, A)