class Chatbot :
    
    def decir_afirmacion() -> str:
    def dato_curioso() -> str:
    def mostrar_respuestas() -> str:
    def responder() -> str: 


    class Diario :

        def guardar_entrada() -> str:
        def mostrar_historial() -> str:
        def borrar_entrada() -> str:

class usuario :

    def __init__(self, name, puntaje_a, puntaje_d) -> None: #Instanciar usuarios
        self.name = name
        self.puntaje_a = puntaje_a
        self.puntaje_d = puntaje_d
    
    def test_ansiedad() -> int:
    def test_depresion() -> int:

class estado (usuario) :
    def __init__(self, puntaje_a, puntaje_d) -> None: #Instanciar usuarios
        self.puntaje_a = puntaje_a
        self.puntaje_d = puntaje_d
    def mostrar_puntaje() -> int: 
    
    class ansiedad (estado) : 
        def __init__(self, puntaje_a) -> None: #Instanciar usuarios
        self.puntaje_a = puntaje_a
        
    
    class depresion (estado) :
        def __init__(self, puntaje_d) -> None: #Instanciar usuarios
        self.puntaje_a = puntaje_d
