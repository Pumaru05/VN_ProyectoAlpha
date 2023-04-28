# PROYECTO DE VISUAL NOVEL CON NOMBRE POR DETERMINAR

# Declara los personajes usados en el juego como en el ejemplo:

define Prota = Character("Jon")


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg black_scene.png

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    #show eileen happy

    # Presenta las líneas del diálogo.

    "Donde... ¿Donde estoy?"

    Prota "Aaaaaaaaaaaagh... Mi cabeza... Que... ¿Qué ha pasado?"

    'Mira alrededor de la estancia oscura'

    Prota "Qu... ¿Que es eso? Parece una luz"

    # Finaliza el juego:

    return