from tkinter import *
from tkinter.tix import TEXT


from click import pass_context

BG_GRAY = "#D2B4DE"
BG_COLOR = "#512E5F"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class MasterPanel:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Pysbot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)
        
        # Titulo
        Titulo = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="PSYBOT", font=FONT_BOLD, pady=10)
        Titulo.place(relwidth=1)
        
        # Linea clara
        linea = Label(self.window, width=450, bg=BG_GRAY)
        linea.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=0.8, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Boton de diario
        diario = Button(self.window, text="Diario", font=FONT_BOLD, command=lambda: self.abrirdiario(None))
        diario.place(relx=0.814, rely=0.09, relheight=0.15, relwidth=0.18)
                            

        # Boton de Test
        ansiedad = Button(self.window, text="Test", font=FONT_BOLD)
        ansiedad.place(relx=0.814, rely=0.29, relheight=0.15, relwidth=0.18)

        # Boton de Gratitud
        depresion = Button(self.window, text="Practicar gratitud", font=FONT_BOLD)
        depresion.place(relx=0.814, rely=0.48, relheight=0.15, relwidth=0.18)

        # Boton S.O.S
        xxx = Button(self.window, text="S.O.S", font=FONT_BOLD)
        xxx.place(relx=0.814, rely=0.67, relheight=0.15, relwidth=0.18)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # contenedor de texto
        contenedor = Label(self.window, bg=BG_GRAY, height=80)
        contenedor.place(relwidth=1, rely=0.825)
        
        # mensaje
        self.msg_entry = Entry(contenedor, bg="#512E5F", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # enviar
        enviar = Button(contenedor, text="Enviar", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        enviar.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
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
        print("Entra")
        self.window.destroy()
        Diario()

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
        Titulo = Label(self.ventana, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="PSYBOT", font=FONT_BOLD, pady=10)
        Titulo.place(relwidth=1)
        
        # Linea clara
        linea = Label(self.ventana, width=450, bg=BG_GRAY)
        linea.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.ventana, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # contenedor de texto
        contenedor = Label(self.ventana, bg=BG_GRAY, height=80)
        contenedor.place(relwidth=1, rely=0.825)
        
        # mensaje
        self.msg_entry = Entry(contenedor, bg="#512E5F", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # enviar
        enviar = Button(contenedor, text="Guardar", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        enviar.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "Entrada")

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
