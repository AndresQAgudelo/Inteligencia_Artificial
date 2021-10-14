import pandas as pd

dFrame_h = pd.read_csv("tablaHechos.csv", index_col = "id")
dFrame_r = pd.read_csv("tablaReglas.csv", index_col = "ID_R")

print (dFrame_h, "\n\n", dFrame_r)







def agendar(id_h):
  dFrame_h.loc[id_h, "agenda"] = (dFrame_h.at[id_h, "agenda"]) + 1 #Modifica el valor de la celda aunmenta en 1

  

def inferencia(nombre): #Retorna

  antecedente = int(dFrame_h[dFrame_h["nombre"] == nombre].index.tolist()[0])#Verifica un hecho de entrada
  consecuente = dFrame_r[dFrame_r["ID_Ante"] == antecedente].index.tolist() #Encuentra el consecuente

  for datos in consecuente:
    agendar (dFrame_r.at[datos, "ID_Conse"])
    

def MenuPpal():
  dFrame_h["agenda"] = 0 #Crea una agenda 
  bd_sintomas = []
  salir = 0
  maxs = 0
  



  print ("\n \tBIENVENIDO\t", "Soy el Dr D \n")
  

  while (salir == 0):
    sintoma = str(input ("¿Que sistoma tiene? \n")) #Se pide una entrada  
    if (len(dFrame_h[dFrame_h["nombre"]==sintoma])) > 0: #Verfica que la entrada sea un hecho existente
      for i in bd_sintomas:
        if sintoma == i:
          salir = 1
          break

      bd_sintomas.append(sintoma) 
      inferencia(sintoma)
      maxs= dFrame_h["agenda"].max()
        
    elif(sintoma == ""):
      salir = 1
      break
    
    else:
      print("\t \nSintoma no valido\n")
    

  if (maxs == 0 ):
    print ("\t \n Le enviare un conjuento de examenes")

  else:
    enfermedad = dFrame_h[dFrame_h["agenda"] == maxs].index.tolist()
   

    if len(enfermedad) == 1:
      print ("Usted tiene...  \n")
      print(dFrame_h.at[enfermedad[0], "nombre"])
    
    else:
      print("Usted podria tener")
      for i in enfermedad:
        print(dFrame_h.at[i, "nombre"])

      print("Le enviare un conjuento de examenes")        

def main():
  MenuPpal()
  print("\t\n Hasta Luego\n\t")


 


   

main()
  










