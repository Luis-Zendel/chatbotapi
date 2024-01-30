var = """Claro, aquí tienes un plan alimenticio para ayudarte a bajar de peso y reducir el consumo de azúcar:
Desayuno:
- Opción 1: Omelette de claras de huevo con espinacas y tomate.
- Opción 2: Yogur griego bajo en grasa con frutas frescas y un puñado de nueces.
- Opción 3: Batido de proteínas con leche de almendras, espinacas, plátano y una cucharada de mantequilla de maní sin azúcar."

Media mañana:
- Opción 1: Zanahorias baby con hummus.
- Opción 2: Un puñado de almendras.
- Opción 3: Rodajas de pepino con yogur griego bajo en grasa y hierbas frescas.

Almuerzo:
- Opción 1: Ensalada de pollo a la parrilla con verduras mixtas, aguacate y aderezo casero bajo en grasa.
- Opción 2: Salmón a la parrilla con espárragos y quinoa.
- Opción 3: Rollitos de lechuga rellenos de pavo, rodajas de tomate y aguacate.

Media tarde:
- Opción 1: Trozos de manzana con mantequilla de almendras sin azúcar.
- Opción 2: Palitos de apio con queso cottage bajo en grasa.
- Opción 3: Batido de proteínas con leche de almendras y una cucharada de cacao en polvo sin azúcar.

Cena:
- Opción 1: Pechuga de pollo a la plancha con espárragos y una ensalada de espinacas.
- Opción 2: Filete de pescado al horno con brócoli y puré de coliflor.
- Opción 3: Ensalada mixta con tofu a la parrilla y vinagreta sin azúcar.

Antes de dormir:
- Opción 1: Un puñado de nueces.
- Opción 2: Yogur griego bajo en grasa con una cucharadita de miel sin azúcar.
- Opción 3: Té verde o camomila.

Recuerda beber suficiente agua durante todo el día y limitar el consumo de bebidas azucaradas. Además, trata de evitar alimentos procesados y opta por opciones frescas y 
naturales.

Siempre es recomendable consultar a un profesional de la salud o un dietista antes de hacer cambios drásticos en tu dieta"""

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
        contenido_horario = plan_alimenticio[inicio_contenido:].strip()

    return contenido_horario

# Ejemplos de cómo utilizar la función
desayuno = separar_horario(var, "Desayuno:", "Media mañana:")
media_manana = separar_horario(var, "Media mañana:",  "Almuerzo:")
almuerzo = separar_horario(var, "Almuerzo:", "Media tarde:")
media_tarde = separar_horario(var, "Media tarde:",  "Cena:")
cena = separar_horario(var, "Cena:", "Antes de dormir:")
antes_de_dormir = separar_horario(var, "Antes de dormir:", "")

# Imprimir los resultados
print("Desayuno:\n", desayuno)
print("______________________________-")
print("\nMedia mañana:\n", media_manana)
print("______________________________-")
print("\nAlmuerzo:\n", almuerzo)
print("______________________________-")
print("\nMedia tarde:\n", media_tarde)
print("______________________________-")
print("\nCena:\n", cena)
print("______________________________-")
print("\nAntes de dormir:\n", antes_de_dormir)
print("______________________________-")



