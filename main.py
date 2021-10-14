import sqlConnection as sql
import menu as m
import enseñar


def main():
  #Variables numnodo = primer nodo
  continuar = True
  numnodo = 1
  while(continuar == True):  
    menu = sql.sql_connection() #Coneccion a la BD si no existe la crea
    
    if menu == 0: #Si la BD no tienen nada
        Nuevonodo = enseñar.menuEnseñar() # Toma los valores ingresados por el usuario

        #Asigna los nuevos valores (Objeto, Atributo)
        sql.sql_AddFirstData(2, Nuevonodo[0], False)
        sql.sql_AddFirstData(1, Nuevonodo[1], True)

        sql.sql_ViewData()
        
      
    else:
    
      #Busca en la base de datos el nodo
      Elemento = sql.sql_ViewOneData(numnodo)

      #Agrega Objeto, Atributo hijo a la izquierda
      if Elemento == (0,0,0):
        Nuevonodo = enseñar.menuEnseñar()
        print(Nuevonodo)
        sql.sql_AddFirstData(numnodo * 2, Nuevonodo[0], False)
        sql.sql_AddFirstData(numnodo, Nuevonodo[1], True)
        numnodo =1
        continue


      if  Elemento[2] == 0: #SI ES OBJETO, LLEGO AL FINAL DE LA RAMA
        entonces = m.menuPpal(numnodo, Elemento[1])
         
          #Respuesta negativa, Enseñar
        if entonces[1] == 0:
            
          Nuevonodo = enseñar.menuEnseñar()
          print(Nuevonodo)

          sql.sql_AddNewData(numnodo, Nuevonodo, False)
          sql.sql_ViewData()
          numnodo = 1
          
        #Respuesta afirmativa Gano, Jugar de nuevo?
        else:
          continuar = m.MenuGanar()
          numnodo = 1

          # Jugar de nuevo = si, Continuar
          # Jugar de nuevo = no, Salir

        
      else: # SI ES UN ATRIBUTO
        
        #Busca en la base de datos el nodo
        Elemento = sql.sql_ViewOneData(numnodo)

        #Muestra el nombre del Atribbto/Objeto en pantalla
        entonces = m.menuPpal(numnodo, Elemento[1])

        #Se mueve al nuevo nodo, Respuesta Si = nodo* 2, No = nodo * 2 + 1
        numnodo = entonces[0]
  


if __name__ == "__main__":
    main()
    
    

        
      

      
    
  



