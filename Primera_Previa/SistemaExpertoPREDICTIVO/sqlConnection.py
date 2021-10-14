import sqlite3


def sql_connection():#Se conecta a la BD, si esta vacia la crea

    try: 

        con = sqlite3.connect("SEP")
        pointer = con.cursor()

        pointer.execute('''
           CREATE TABLE "arbol" (
	            nodo	INTEGER NOT NULL UNIQUE,
	            elemento	TEXT NOT NULL ,
              EsAtributo BOOL,
	            PRIMARY KEY("nodo")
            );
        
        ''')

        return 0

    except:
      return 1
    
    finally:
      con.close()
      

def sql_AddFirstData(Nodo, Elemento, EsAtributo):#Agrega datos individuales
  data = (Nodo, Elemento, EsAtributo)
  con = sqlite3.connect("SEP")
  pointer = con.cursor()

  pointer.execute("INSERT INTO arbol VALUES (?,?,?)", data)

  con.commit()

def sql_AddNewData(Nodo, Elemento, EsAtributo):#Agrega Padre, HijoI, HijoD
  con = sqlite3.connect("SEP")
  pointer = con.cursor()

  pointer.execute("SELECT * FROM arbol WHERE nodo ="+ str(Nodo))
  rows = pointer.fetchone()
  print(rows)

  print(Nodo, Elemento, EsAtributo)
  NodoHijoI = Nodo * 2
  NodoHijoD = Nodo * 2 + 1 

  Atributo = Elemento[1]
  Objeto = Elemento[0]
  Objeto2 = rows[1]

  

  AgregarHijoI = (NodoHijoI, Objeto, False)
  AgregarHijoD = (NodoHijoD, Objeto2, False)
  ActualizarPadre = (Nodo, Atributo, True, Nodo)
  

  pointer.execute("INSERT INTO arbol VALUES (?,?,?)", AgregarHijoI)

  pointer.execute("INSERT INTO arbol VALUES (?,?,?)", AgregarHijoD)

  pointer.execute("UPDATE arbol SET nodo = ?, elemento = ? ,EsAtributo = ?  WHERE nodo = ?", ActualizarPadre)

  con.commit()

  
  
  

def sql_ViewData():#Muestra toda la BD
  con = sqlite3.connect("SEP")
  pointer = con.cursor()

  pointer.execute("SELECT * FROM arbol")
  rows = pointer.fetchall()

  print(rows)

  con.close()

def sql_ViewOneData(NumeroNodo):#Muestra solo un dato de la BD
    con = sqlite3.connect("SEP")
    pointer = con.cursor()

    pointer.execute("SELECT * FROM arbol WHERE nodo ="+ str(NumeroNodo))
    rows = pointer.fetchone()

    if rows == None:
      rows = (0,0,0)
      return(rows)
    else:
      return(rows)
    con.close()
  
  
  


  

  

  






