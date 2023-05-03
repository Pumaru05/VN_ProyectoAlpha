# PROYECTO DE VISUAL NOVEL CON NOMBRE POR DETERMINAR

# Declara los personajes usados en el juego como en el ejemplo:

define PJ = Character("...")


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene black_scene

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    #show eileen happy

    # Presenta las líneas del diálogo.

    "Donde... ¿Donde estoy?"

    PJ "Aaaaaaaaaaaagh... Mi cabeza... Que... ¿Qué ha pasado?"

    'Mira alrededor de la estancia oscura.'

    scene white_light
    
    PJ "Qu... ¿Que es eso? Parece una luz."

    'Se levanta y comienza a andar hacia la luz.'

    'Se tropieza con algunos guijarros del suelo de piedra.'

    PJ "¡Auch! ¡Mis pies! ¡Qué daño!"

    scene lake_mountain
    
    'Se ve un lago en medio de la montaña iluminada por el rayo de luz de la luna.'

    # scene lake_Mara

    PJ "Allí hay alguien, iré a preguntarla para saber donde estoy."

    # Finaliza el juego:

    return