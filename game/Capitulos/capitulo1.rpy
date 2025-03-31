
define pensamiento = Character(None, what_italic=True)  # Sin nombre, en cursiva

# Variables
$ musica = 'F'
$ correo = 'F'
$ videojuegos = 'F'
$ libro = 'F'
default noticia = 'F'


label introduccion:
    #Muscia Algo tipo jazz, o algo similar a esto https://www.youtube.com/watch?v=JW_gPeHT9CI
    #Fondo una habitacion, quisas un estudio con una ventana, un sofa y un televisor o computador
    """
        {i}Noches como estas son las que me ponen a pensar, todo el ambiente
        esta adecuado, esta lloviendo en la cuidad y las gotas de lluvia
        caen en mi ventana, haciendo eco poco a poco en la habitacion,
        acompañando las suaves melodias de la musica.{/i}
    """

    pensamiento """
        Mientras estoy sentado en un sofa, solo contemplado el techo de
        donde duermo, esa sinconia entre las gotas y la musica, hacen
        que me sienta con ganas de dormir, pero tambien es el ambiente
        perfecto para leer.
    """

    #Cambio de escena a una biblioteca con libros

    pensamiento """
        En Mi vieja biblioteca, tengo diversos libros de diferentes temas
        que antes solia leer muy seguido, pero con el paso de los años
        y la acumulacion de resposabilidades, uno tiende a sacrificar sus
        pasatiempos a favor de la vida adulta
    """

    pensamiento """
        con el tiempo, añoro mas esos dias en los que podia dedicar mi tiempo
        a consultar diversos temas, principalmente fantasia, ciencia ficcion
        y paranormales, la vida es demasiado gris aveces, y estas historias
        asi sean falsas cambian eso
    """

    #Cambio de escena a estar frente a un televisor o computador

    pensamiento """
        A pesar de que puedo usar los videojuegos o el internet para escapar
        de la realidad, es dificil centrarse, tras estar todo el dia frente
        a un ordenador programando codigo, uno solo quiere alejarse de este
        al final del dia, quisas solo vea las noticias antes de leer
    """

    pensamiento """
        sentado en el computador, me dispongo a
    """

    menu:
        "Apagar la musica para leer":
            jump apagarMusica
        "Revisar el correo":
            jump revisarCorreo
        "Revisar algun videojuego":
            jump revisarVideoJuegos
        "Revisar el libro":
            jump revisarLibro
        "Revisar Noticias":
            jump revisarNoticias
        "Apagarlo E ir a dormir":
            jump irAdormir

label apagarMusica:
    
    pensamiento """
        Dicen que es mejor leer en silecio, pero el silencio era lo ultimo 
        que queria yo en esos momentos, solo el hecho de sentir mi cumpleaños numero
        30, aproximandome, me pone nostaslgico, y reflexivo, como si dijiera
        que he hecho yo con mi vida
    """
    $ musica = "V"
    menu:
        "Encender la música para leer" if musica == "V":
            jump encenderMusica
        "Apagar la música para leer" if musica == "F":
            jump apagarMusica
        "Revisar el correo":
            jump revisarCorreo
        "Revisar algún videojuego":
            jump revisarVideoJuegos
        "Revisar el libro":
            jump revisarLibro
        "Revisar Noticias":
            jump revisarNoticias
        "Apagarlo e ir a dormir":
            jump irAdormir


label irAdormir:
    if noticia == 'F':
        jump gameOver
    elif noticia == 'V':
        jump capitulo1

label gameOver:
    pensamiento """
       Me quede dormido mas de la cuenta, y casi llego tarde al trabajo
       cuando sali, me di cuenta que el insituto, habia caido bajo su 
       propio peso, y una tragedia habia pasado
    """
    return

label capitulo1:
    pensamiento """
       me dio tiempo para pedir permiso, de trabajar en casa, no me gusta
       mentir, pero esto lo amerita
    """