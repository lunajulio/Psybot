import tkinter as tk
from tkinter import END, Button, Entry, Label, StringVar, Toplevel, ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from form_master import MasterPanel

class App:

    def verificar(self):
        entro = False
        usu = self.user.get()
        password = self.password.get()    
        file1 = open("usuarios.txt","r")
        for i in file1:
            a,b = i.split(",")
            b = b.strip()    
            print(a,b)    
            if(a == usu and b == password) :
                entro = True
                break    
        file1.close()
        if(entro):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")
        file1.close()
                

        

    def Registrar_Usuario(self):
        username_info = self.usuario.get()
        password_info = self.contrasena.get()

        file = open("usuarios.txt","a")
        file.write("\n"+username_info+","+password_info)
        file.close

        messagebox.showinfo(message="El usuario ha sido registrado con exito",title="Mensaje")

        self.contrasena.delete(0, END)
        self.usuario.delete(0, END)
        self.reg.destroy()

    def registrar(self):
        self.reg = tk.Tk()                             
        self.reg.title('PSYBOT')
        self.reg.geometry('470x550')
        self.reg.config(bg='#fcfcfc')
        self.reg.resizable(width=0, height=0)    
        utl.centrar_ventana(self.reg,370,450)
        
        #frame_form
        frame_form = tk.Frame(self.reg, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="PSYBOT",font=('Arial', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Arial', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Arial', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=5)

        etiqueta_contrasena = tk.Label(frame_form_fill, text="Contraseña", font=('Arial', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_contrasena.pack(fill=tk.X, padx=20,pady=5)
        self.contrasena = ttk.Entry(frame_form_fill, font=('Arial', 14))
        self.contrasena.pack(fill=tk.X, padx=20,pady=5)
        self.contrasena.config(show="*")

        Registro = tk.Button(frame_form_fill,text="Registrar",font=('Arial', 15,BOLD),bg='#9F4CDE', bd=0,fg="#fff",command=self.Registrar_Usuario)
        Registro.pack(fill=tk.X, padx=20,pady=25)        
        Registro.bind("<Return>", (lambda event: self.Registrar_Usuario()))

                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('PSYBOT')
        self.ventana.geometry('470x550')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,370,450)
        
        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="PSYBOT",font=('Arial', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_user = tk.Label(frame_form_fill, text="Usuario", font=('Arial', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_user.pack(fill=tk.X, padx=20,pady=5)
        self.user = ttk.Entry(frame_form_fill, font=('Arial', 14))
        self.user.pack(fill=tk.X, padx=20,pady=5)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Arial', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Arial', 14))
        self.password.pack(fill=tk.X, padx=20,pady=5)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill,text="Iniciar",font=('Arial', 15,BOLD),bg='#9F4CDE', bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=25)        
        inicio.bind("<Return>", (lambda event: self.verificar()))

        registrar = tk.Button(frame_form_fill,text="Registrar",font=('Arial', 15,BOLD),bg='#9F4CDE', bd=0,fg="#fff",command=self.registrar)
        registrar.pack(fill=tk.X, padx=20,pady=5)

        #end frame_form_fill
        self.ventana.mainloop()
        
if __name__ == "__main__":
   App()
