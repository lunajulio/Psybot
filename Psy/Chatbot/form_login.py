import tkinter as tk
from tkinter import END, Button, Entry, Label, StringVar, Toplevel, ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from form_master import MasterPanel

class App:

    def verificar(self): 
        entro = False
        usu = self.user.get() #Conseguimos el usuario que entro el usuario
        password = self.password.get() #Conseguimos la contraseña que entro el usuario
        file1 = open("usuarios.txt","r") #Abrimos el archivo
        for i in file1:
            a,b = i.split(",")
            b = b.strip() #Separamos las entradas para poder buscar en cada una    
            print(a,b)    
            if(a == usu and b == password) : #Comparamos
                entro = True
                break    
        file1.close()
        if(entro):
            self.ventana.destroy() #Destruimos esta ventana
            MasterPanel() #Abrimos la nueva ventana
        else:
            messagebox.showerror(message="La contraseña no es correcta",title="Mensaje") #Mensaje de error
        file1.close()
                

        

    def Registrar_Usuario(self):
        username_info = self.usuario.get() #Conseguimos el usuario que entro el usuario
        password_info = self.contrasena.get() #Conseguimos la contraseña que entro el usuario

        file = open("usuarios.txt","a") #Abrimos el archivo para ingresar los datos
        file.write("\n"+username_info+","+password_info)
        file.close

        messagebox.showinfo(message="El usuario ha sido registrado con exito",title="Mensaje")

        self.contrasena.delete(0, END) #Borramos la informacion del TextField
        self.usuario.delete(0, END) #Borramos la informacion del TextField
        self.reg.destroy() #Cerramos la ventana

    def registrar(self):
        self.reg = tk.Tk() #Ingresamos la root                        
        self.reg.title('PSYBOT') #Configuramos la ventana
        self.reg.geometry('470x550')
        self.reg.config(bg='#fcfcfc')
        self.reg.resizable(width=0, height=0)    
        utl.centrar_ventana(self.reg,370,450) #Centramos la ventana
        
        frame_form = tk.Frame(self.reg, bd=0, relief=tk.SOLID, bg='#fcfcfc') #Configuraciones de la ventana
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="PSYBOT",font=('Arial', 30), fg="#666a88",bg='#fcfcfc',pady=50) #Ingresamos el titulo
        title.pack(expand=tk.YES,fill=tk.BOTH)

        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Arial', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w") 
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Arial', 14)) #Ponemos el textField
        self.usuario.pack(fill=tk.X, padx=20,pady=5)

        etiqueta_contrasena = tk.Label(frame_form_fill, text="Contraseña", font=('Arial', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_contrasena.pack(fill=tk.X, padx=20,pady=5)
        self.contrasena = ttk.Entry(frame_form_fill, font=('Arial', 14)) #Ponemos el textField
        self.contrasena.pack(fill=tk.X, padx=20,pady=5)
        self.contrasena.config(show="*") #Escondemos las letras de la contraseña

        Registro = tk.Button(frame_form_fill,text="Registrar",font=('Arial', 15,BOLD),bg='#9F4CDE', bd=0,fg="#fff",command=self.Registrar_Usuario) #Creamoe el boton
        Registro.pack(fill=tk.X, padx=20,pady=25)        
        Registro.bind("<Return>", (lambda event: self.Registrar_Usuario()))

                      
    def __init__(self):        
        self.ventana = tk.Tk() #Ingresamos la root                              
        self.ventana.title('PSYBOT') #Configuramos la ventana
        self.ventana.geometry('470x550')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,370,450) #Centramos la ventana
        
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc') #Configuramos la ventana
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="PSYBOT",font=('Arial', 30), fg="#666a88",bg='#fcfcfc',pady=50) #Ingresamos el titulo
        title.pack(expand=tk.YES,fill=tk.BOTH)

        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_user = tk.Label(frame_form_fill, text="Usuario", font=('Arial', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_user.pack(fill=tk.X, padx=20,pady=5)
        self.user = ttk.Entry(frame_form_fill, font=('Arial', 14)) #Ponemos el textField
        self.user.pack(fill=tk.X, padx=20,pady=5)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Arial', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Arial', 14)) #Ponemos el textField
        self.password.pack(fill=tk.X, padx=20,pady=5)
        self.password.config(show="*") #Escondemos la clave

        inicio = tk.Button(frame_form_fill,text="Iniciar",font=('Arial', 15,BOLD),bg='#9F4CDE', bd=0,fg="#fff",command=self.verificar) #Creamos el boton para ingresar
        inicio.pack(fill=tk.X, padx=20,pady=25)        
        inicio.bind("<Return>", (lambda event: self.verificar()))

        registrar = tk.Button(frame_form_fill,text="Registrar",font=('Arial', 15,BOLD),bg='#9F4CDE', bd=0,fg="#fff",command=self.registrar) #Creamos el boton para registrarse
        registrar.pack(fill=tk.X, padx=20,pady=5)

        self.ventana.mainloop()
        
if __name__ == "__main__":
   App()
