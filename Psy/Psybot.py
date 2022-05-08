class Chatbot :
    def decir_afirmacion() -> str:
        pass
    def dato_curioso() -> str:
        pass
    def mostrar_respuestas() -> str:
        pass
    def responder() -> str: 
        pass

    class Diario :

        def guardar_entrada() -> str:
            pass
        def mostrar_historial() -> str:
            pass
        def borrar_entrada() -> str:
            pass

class usuario :

    def __init__(self, name, puntaje_a, puntaje_d) -> None: #Instanciar usuarios
        self.name = name
        self.puntaje_a = puntaje_a
        self.puntaje_d = puntaje_d
    
    def test_ansiedad() -> int:
        pass
    def test_depresion() -> int:
        pass

class estado (usuario) :
    def __init__(self, puntaje_a, puntaje_d) -> None: #Instanciar usuarios
        self.puntaje_a = puntaje_a
        self.puntaje_d = puntaje_d
        
    def mostrar_puntaje() -> int: 
        pass
    
    class ansiedad (estado) : 
        
        def __init__(self, puntaje_a) -> None: #Instanciar usuarios
            self.puntaje_a = puntaje_a
        
    
    class depresion (estado) :
        def __init__(self, puntaje_d) -> None: #Instanciar usuarios
            self.puntaje_a = puntaje_d