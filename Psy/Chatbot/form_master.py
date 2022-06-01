from tkinter import *
import os
import pygame
from chat import get_response, bot_name
from click import pass_context
pygame.mixer.init()
menor = "#D2B4DE"
mayor = "#512E5F"
grih = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class MasterPanel:
    
    def __init__(self): 
        self.window = Tk() #Creamos la root
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Pysbot") #Creamos el titulo
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=mayor) #Cpnfiguramos el ventana
        
        # Titulo
        Titulo = Label(self.window, bg=mayor, fg=grih,
                           text="PSYBOT", font=FONT_BOLD, pady=10)
        Titulo.place(relwidth=1)
        
        # Linea clara
        linea = Label(self.window, width=450, bg=menor)
        linea.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=mayor, fg=grih,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=0.8, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Boton de diario
        diario = Button(self.window, text="Diario", font=FONT_BOLD, command=lambda: self.abrirdiario(None))
        diario.place(relx=0.814, rely=0.09, relheight=0.15, relwidth=0.18)
                            

        # Boton de Test
        ansiedad = Button(self.window, text="Test", font=FONT_BOLD, command=lambda: self.test(None))
        ansiedad.place(relx=0.814, rely=0.29, relheight=0.15, relwidth=0.18)

        # Boton de Gratitud
        depresion = Button(self.window, text="Gratitud", font=FONT_BOLD, command=lambda: self.gratitud(None))
        depresion.place(relx=0.814, rely=0.48, relheight=0.15, relwidth=0.18)

        # Boton S.O.S
        xxx = Button(self.window, text="S.O.S", font=FONT_BOLD, command=lambda: self.sos(None))
        xxx.place(relx=0.814, rely=0.67, relheight=0.15, relwidth=0.18)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # contenedor de texto
        contenedor = Label(self.window, bg=menor, height=80)
        contenedor.place(relwidth=1, rely=0.825)
        
        # mensaje
        self.msg_entry = Entry(contenedor, bg=mayor, fg=grih, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # enviar
        enviar = Button(contenedor, text="Enviar", font=FONT_BOLD, width=20, bg=menor,
                             command=lambda: self._on_enter_pressed(None))
        enviar.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        # musica

        musica = Button(self.window, text="♫", font=FONT_BOLD, command=lambda: self.pm(None))
        musica.place(relx=0.01, rely=0.01, relheight=0.05, relwidth=0.08)

        # cancelar musica

        nomusica = Button(self.window, text="No ♫", font=FONT_BOLD, command=lambda: self.nopm(None))
        nomusica.place(relx=0.1, rely=0.01, relheight=0.05, relwidth=0.11)


        
    def nopm(self, event):
        pygame.mixer.music.stop() #Paramos la musica

    def pm(self, event):
           pygame.mixer.music.load("Psy\Chatbot\musica\musica.mp3") #Ingresamos la pista de audio
           pygame.mixer.music.play(loops=0) #Iniciamos la musica
     
    def _on_enter_pressed(self, event): #Mostramos el mensaje en pantalla 
        msg = self.msg_entry.get()
        self._insert_message(msg, "Tu")
        
    def _insert_message(self, msg, sender): #Recogemos el mensaje que debe mostrar el chatbot
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)

    def abrirdiario (self, event):
        self.window.destroy()
        Diario()
    
    def sos (self,event):
        sos = ("Mi sistema de S.O.S ha sido activado por una emergencia, si este es el caso aqui hay algunas cosas que puedes probar:  \n\nAtaque de ansiedad: \nhttps://www.sanitas.es/sanitas/seguros/es/particulares/biblioteca-de-salud/psicologia-psiquiatria/estres-ansiedad/como-actuar-crisis-ansiedad.html \n\nTelefono de la Esperanza-Barranquilla:\n(00 57 5) 372 27 27 \n \nTelefono de la Esparanza-Bogota:\n(57-1) 323 24 25 ")
        self._insert_message(sos, "Psybot")
    
    def test (self, event):
        test = ("En el siguiente link podras encontrar un test que te permitira comprender como te has sentido recientemiente, una vez lo hayas hecho por favor introduce los resultados:\nhttps://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/depression-anxiety-self-assessment-quiz/")
        self._insert_message(test, "Psybot")

    def gratitud (self, event):
        gratitud = ("gratitud")
        self._insert_message(gratitud, "Tu")


class Diario:
    def __init__(self):        
        self.ventana = Tk()                             
        self.ventana.title('Diario')
        self.ventana.geometry('470x550')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=False, height=False)    
        self.setup()
    
    
    def setup (self):
        # Titulo
        Titulo = Label(self.ventana, bg=mayor, fg=grih,
                           text="PSYBOT", font=FONT_BOLD, pady=10)
        Titulo.place(relwidth=1)
        
        # Linea clara
        linea = Label(self.ventana, width=450, bg=menor)
        linea.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.ventana, width=20, height=2, bg=mayor, fg=grih,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # contenedor de texto
        contenedor = Label(self.ventana, bg=menor, height=80)
        contenedor.place(relwidth=1, rely=0.825)
        
        # mensaje
        self.msg_entry = Entry(contenedor, bg=mayor, fg=grih, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self.guardar_entrada)
        
        # guardar
        guardar = Button(contenedor, text="Guardar", font=FONT_BOLD, width=20, bg=menor,
                             command=lambda: self.guardar_entrada(None))
        guardar.place(relx=0.77, rely=0.008, relheight=0.025, relwidth=0.22)

        # mostrar
        mostrar = Button(contenedor, text="Historial", font=FONT_BOLD, width=20, bg=menor,
                             command=lambda: self.mostrar_entradas(None))
        mostrar.place(relx=0.77, rely=0.04, relheight=0.025, relwidth=0.22)

        # volver

        volver = Button(self.ventana, text="<-", font=FONT_BOLD, command=lambda: self.volver(None))
        volver.place(relx=0.01, rely=0.01, relheight=0.05, relwidth=0.08)


    def volver(self, event):
        print("Entra")
        self.ventana.destroy()
        MasterPanel()

    def mostrar_entradas(self, event):
        hist = open("diario.txt", "r") #Abrimos el diario como lectura
        hist2 = hist.read()
        self._insert_message(hist2, "Psybot") #Ingresamos las entradas en pantalla
        hist.close()

    def guardar_entrada(self, event):
        msg = self.msg_entry.get()
        file = open("diario.txt", "a") #Abrimos el diario como escritura
        file.write(msg + "\n")
        file.close()
        self._insert_message(msg, "Entrada") #Mostramos el mensaje en pantalla


    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


    def run (self):
        self.ventana.mainloop()
