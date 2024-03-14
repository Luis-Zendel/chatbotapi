def separar_horario(plan_alimenticio, horario, siguiente_horario):
    # Encontrar el índice del horario en el plan alimenticio
    indice_horario = plan_alimenticio.find(horario)
    print("Se encontro indice horario", indice_horario)
    # Si el horario no se encuentra, retornar None
    if indice_horario == -1:
        return None

    # Encontrar el inicio del contenido del horario (línea siguiente al horario)
    inicio_contenido = plan_alimenticio.find('\n', indice_horario) + 1

    # Encontrar el final del contenido del horario (inicio del siguiente horario o el final de la cadena)

    fin_contenido = plan_alimenticio.find(siguiente_horario) 
    print("Fin de contenido ", fin_contenido)
    # Extraer el contenido del horario
    if siguiente_horario != "":
        contenido_horario = plan_alimenticio[inicio_contenido:fin_contenido].strip()
    else:
        div = plan_alimenticio[inicio_contenido:].strip()
        partes = div.split('\n\n', 1)
        contenido_horario = partes[0]

    return contenido_horario