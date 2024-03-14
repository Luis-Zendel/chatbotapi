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

var2 = """
>  ¡Hola Yesenia! Claro que sí, puedo ayudarte a elaborar un plan de dieta personalizado para ayudarte a perder peso y mantener tu energía a lo 
largo del día. A continuación te presento un ejemplo de plan de alimentación en el formato solicitado:

**Desayuno:**
1. Opción 1: Tazón de yogur natural con frutas frescas y granola.
2. Opción 2: Omelette de claras de huevo con espinacas, champiñones y tomate.
3. Opción 3: Batido de proteínas con plátano, espinacas y almendra.

**Media Mañana:**
1. Opción 1: Puñado de frutos secos (nueces, almendras, pistachos).
2. Opción 2: Batido de proteínas con leche de almendra y una cucharada de crema de cacahuate.
3. Opción 3: Rodajas de manzana con mantequilla de almendra.

**Almuerzo:**
1. Opción 1: Pechuga de pollo a la parrilla con ensalada de quinoa, aguacate y tomate.
2. Opción 2: Salmón al horno con brócoli al vapor y batata asada.
3. Opción 3: Tacos de tinga de pollo en tortillas de maíz con guacamole y ensalada de col.

**Media Tarde:**
1. Opción 1: Zanahorias baby con hummus.
2. Opción 2: Yogur griego natural con bayas frescas y semillas de chía.
3. Opción 3: Smoothie de espinacas, piña y jengibre.

**Cena:**
1. Opción 1: Ensalada de garbanzos con tomate, pepino, pimiento y vinagreta de limón.
2. Opción 2: Filete de pescado al horno con espárragos a la parrilla y quinoa.
3. Opción 3: Pollo al curry con leche de coco, verduras al wok y arroz integral.

**Antes de Dormir:**
1. Opción 1: Té de manzanilla o infusión relajante sin azúcar.
2. Opción 2: Un vaso de leche tibia con canela.
3. Opción 3: Puñado de almendras y nueces como snack nocturno.

Espero que este plan de dieta te sea de utilidad en tu objetivo de perder peso y mantener tu energía a lo largo del día. Recuerda que es 
importante mantener un equilibrio en tus comidas y adaptar las porciones a tus necesidades calóricas. ¡Si tienes alguna otra pregunta no dudes 
en contactarme! ¡Mucho éxito en tu camino hacia una vida más saludable!"""

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

# Ejemplos de cómo utilizar la función
desayuno = separar_horario(var2, "**Desayuno:**", "**Media Mañana:**")
media_manana = separar_horario(var2, "**Media Mañana:**",  "**Almuerzo:**")
almuerzo = separar_horario(var2, "**Almuerzo:**", "**Media Tarde:**")
media_tarde = separar_horario(var2, "**Media Tarde:**",  "**Cena:**")
cena = separar_horario(var2, "**Cena:**", "**Antes de Dormir:**")
antes_de_dormir = separar_horario(var2, "**Antes de Dormir:**", "Espero")

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
# Texto completo
texto_completo = """1. Opción 1: Té de manzanilla o infusión relajante sin azúcar.
2. Opción 2: Un vaso de leche tibia con canela.
3. Opción 3: Puñado de almendras y nueces como snack nocturno.

Espero que este plan de dieta te sea de utilidad en tu objetivo de perder peso y mantener tu energía a lo largo del día. Recuerda que es 
importante mantener un equilibrio en tus comidas y adaptar las porciones a tus necesidades calóricas. ¡Si tienes alguna otra pregunta no dudes 
en contactarme! ¡Mucho éxito en tu camino hacia una vida más saludable!."""

# Utilizamos split() para dividir el texto en dos partes usando el primer doble salto de línea como separador
partes = texto_completo.split('\n\n', 1)

# Asignamos las partes a variables separadas
opciones = partes[0]  # Parte con las opciones
mensaje_final = partes[1]  # Resto del texto

# Imprimir las variables para verificar
print("Opciones:")
print(opciones)
print("\nMensaje Final:")
print(mensaje_final)




