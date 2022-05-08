import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('PSYBOT')                                
        self.ventana.geometry('900x600')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)     
        utl.centrar_ventana(self.ventana,800,500)       
       
        Diario = tk.Button(self.ventana,text="Diario",font=('Arial', 15,BOLD),bg='#9F4CDE')
        self.ventana.mainloop()
        logo =utl.leer_imagen("./imagenes/logo.png", (100, 200))
                        
        label = tk.Label( self.ventana, image=logo,bg='#EECAFA' )
        label.place(x=0,y=0,relwidth=1, relheight=1)