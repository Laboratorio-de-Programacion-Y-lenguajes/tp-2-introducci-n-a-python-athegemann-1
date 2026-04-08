# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: GPT-5.4

**Prompt usado**:
> Actuá como tutor de Python 3.13. Dame una receta paso a paso para:
>   Crear una funcion llamada crear_saludo
>   Enviar como parametro el nombre de una persona
>   Devolver un string con el formato "Hola, " y el nombre de la persona. 
>   No uses librerías externas. Mostrá la función con docstring.

**Resultado obtenido**:
1. Definí la función con el nombre solicitado y un parámetro para el nombre:
```python
def crear_saludo(nombre):
```

2. Agregá un docstring justo debajo de la firma para explicar qué hace:
```python
    """Devuelve un saludo con el formato 'Hola, <nombre>'."""
```

3. Construí y devolvé el texto usando f-string:
```python
    return f"Hola, {nombre}"
```

4. Resultado completo:
```python
def crear_saludo(nombre: str) -> str:
    """Devuelve un saludo con el formato 'Hola, <nombre>'."""
    return f"Hola, {nombre}"
```

5. Ejemplo de uso:
```python
saludo = crear_saludo("Ana")
print(saludo)  # Hola, Ana
```

Sin librerías externas, compatible con Python 3.13.

**¿Lo usaste tal cual o lo modificaste?**
Agregue el '!' al final del nombre como piden los tests.

---

### 2 - condicionales.py

**Herramienta**: GPT-5.4

**Prompt usado**:
> Quiero implementar una función clasificar_numero en Python.
> Antes de escribir el código, haceme 3 preguntas para confirmar:
>
>    qué mensajes exactos debo devolver
>    qué tipos de numeros debo aceptar
>
>    Después de mis respuestas, recién ahí proponé el código.


**Resultado obtenido**:
1. ¿Qué mensajes exactos querés que devuelva `clasificar_numero` en cada caso?  
   (Por ejemplo: positivo, negativo, cero, par, impar, etc.)

2. ¿Qué tipos de números debe aceptar la función?  
   (Solo `int`, o también `float`.)

3. Si recibe un valor fuera de esos tipos permitidos, ¿cómo querés que se comporte?  
   (Por ejemplo: devolver un mensaje de error o lanzar una excepción.)

>   quiero que unicamente devuelva "positivo", "negativo", "cerro" o "invalido"
>
>   debe aceptar unicamente valores int
>
>   valores fuera de esos tipos debe devolver el texto "error"

Voy a revisar rápidamente el archivo de condicionales y sus tests para implementar `clasificar_numero` con exactamente las reglas que definiste (`int` válido, `"error"` para tipo inválido, y mensajes exactos).

Read [](file:///home/javirulo/LPyL/tp-2-introducci-n-a-python-athegemann-1/src/condicionales.py)

Read [](file:///home/javirulo/LPyL/tp-2-introducci-n-a-python-athegemann-1/tests/test_condicionales.py)

Ya tengo el contexto: voy a implementar solo `clasificar_numero` con tus textos exactos, dejando el resto del archivo sin cambios. Después te muestro el código final y cómo se comporta en cada caso.

Generating patch (19 lines) in [](file:///home/javirulo/LPyL/tp-2-introducci-n-a-python-athegemann-1/src/condicionales.py)


```

```
Perfecto. Con tus reglas, la función queda así:

```python
def clasificar_numero(n: int) -> str:
    """
    Retorna "positivo", "negativo" o "cerro" según corresponda.
    Si el valor no es int, retorna "error".
    """
    if type(n) is not int:
        return "error"
    if n > 0:
        return "positivo"
    if n < 0:
        return "negativo"
    return "cerro"
```

Comportamiento:

- `5` -> `"positivo"`
- `-2` -> `"negativo"`
- `0` -> `"cerro"`
- `"7"` -> `"error"`
- `3.14` -> `"error"`
- `True` -> `"error"` (porque se valida `type(n) is int`)

**¿Lo usaste tal cual o lo modificaste?**
Modifique un typo ("cerro" en vez de "cero")


---

### 3 - listas.py

**Herramienta**: GPT-5.4

**Prompt usado**:
> Estoy resolviendo un ejercicio de listas en Python con estas reglas:
>
>    la funcion debe llamarse suma_lista
>    se le debe pasar un dato lista
>    debe devolver un numero entero que sea la suma de todos los elementos de la lista
>    ¿Podés revisar mi lógica como verificador cognitivo?
>
>    enumerá casos borde que debería testear,
>    decime errores típicos,
>    proponé 3 tests con entradas y salidas esperadas
>    escribime el codigo en python para la funcion


**Resultado obtenido**:
Perfecto, te lo reviso como verificador cognitivo.

1. Casos borde que conviene testear
1. Lista vacía: debería devolver 0.
2. Lista con un solo elemento: debería devolver ese mismo valor.
3. Lista con enteros negativos y positivos mezclados: valida que la suma combine signos bien.
4. Lista con todos ceros: debería devolver 0.
5. Lista con valores grandes: para confirmar que no hay errores de lógica.
6. Lista con tipos no esperados (por ejemplo strings o float): definir si querés error o conversión.

2. Errores típicos en este ejercicio
1. Inicializar mal el acumulador (por ejemplo en None o "").
2. Olvidar retornar el acumulador al final.
3. Usar mal el rango y saltear elementos.
4. Sobrescribir la lista en vez de acumular en una variable aparte.
5. Devolver dentro del loop y cortar antes de tiempo.
6. Asumir que siempre habrá elementos (falla en lista vacía).

3. Tres tests concretos (entrada y salida esperada)
1. Entrada: [1, 2, 3, 4] -> Salida esperada: 10
2. Entrada: [] -> Salida esperada: 0
3. Entrada: [-5, 10, -2] -> Salida esperada: 3

4. Implementación en Python
~~~python
def suma_lista(lista: list[int]) -> int:
    """Devuelve la suma de todos los elementos enteros de una lista."""
    total = 0
    for elemento in lista:
        total += elemento
    return total
~~~

Si querés, en el siguiente paso te doy una versión con validación estricta de tipos para que devuelva error cuando haya elementos no enteros.


**¿Lo usaste tal cual o lo modificaste?**
Lo utilicé tal cual.


---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> Generá 8 ejemplos de strings en Python que tengan palabras sueltas, como por ejemplo "hola mundo hola"
> Para cada ejemplo, mostráme el texto y mostrame un diccionario en python que tenga cada palabra y la cantidad de veces que aparece en el texto, por ejemplo: {"hola": 2, "mundo":1}
> Luego extraé una regla general para implementar contar_palabras(texto).

**Resultado obtenido**:
Acá van 8 ejemplos simples de textos y su diccionario de frecuencias de palabras.

1. Texto: `"hola mundo hola"`
   Diccionario: `{"hola": 2, "mundo": 1}`

2. Texto: `"python es divertido python"`
   Diccionario: `{"python": 2, "es": 1, "divertido": 1}`

3. Texto: `"perro gato perro pez"`
   Diccionario: `{"perro": 2, "gato": 1, "pez": 1}`

4. Texto: `"uno dos tres dos uno"`
   Diccionario: `{"uno": 2, "dos": 2, "tres": 1}`

5. Texto: `"manzana pera manzana banana pera"`
   Diccionario: `{"manzana": 2, "pera": 2, "banana": 1}`

6. Texto: `"rojo azul verde azul rojo rojo"`
   Diccionario: `{"rojo": 3, "azul": 2, "verde": 1}`

7. Texto: `"casa auto casa mesa auto"`
   Diccionario: `{"casa": 2, "auto": 2, "mesa": 1}`

8. Texto: `"sol luna sol estrella luna sol"`
   Diccionario: `{"sol": 3, "luna": 2, "estrella": 1}`

Regla general para implementar `contar_palabras(texto)`:

1. Separar el texto en palabras.
2. Recorrer palabra por palabra.
3. Para cada palabra:
   - si ya está en el diccionario, sumar 1
   - si no está, agregarla con valor 1
4. Devolver el diccionario final

En forma más concreta, la lógica sería:

- crear un diccionario vacío
- hacer `texto.split()` para obtener las palabras
- contar apariciones acumulando en el diccionario

Si querés, te puedo escribir enseguida la función `contar_palabras(texto)` en Python.


**¿Lo usaste tal cual o lo modificaste?**
Utilice la funcion tal cual, que luego de pedirsela fue:
```python
def contar_palabras(texto: str) -> dict:
    """
    Retorna un diccionario con la frecuencia de cada palabra.
    Ejemplo: contar_palabras("hola mundo hola") -> {"hola": 2, "mundo": 1}
    Las palabras deben ser comparadas en minúsculas.
    """
    conteo = {}
    for palabra in texto.lower().split():
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo
```


---

### 5 - loops.py

**Herramienta**: GPT-5.4

**Prompt usado**:
> Como hago para crear una lista en python?

**Resultado obtenido**:
En Python, una lista se crea con corchetes.

Ejemplos:

- Lista vacía: []
- Lista con elementos: [1, 2, 3]
- Lista de textos: ["hola", "mundo"]

También podés crearla así:

- usando list(): list()
- a partir de un rango: list(range(5))  -> [0, 1, 2, 3, 4]

Si querés, te muestro cómo agregar, eliminar y recorrer elementos de una lista.
> Como puedo llenar esta lista con numeros utilizando un loop?
Hay varias formas de llenar una lista con números usando un loop:

**Forma 1: Agregar con append()**
```python
lista = []
for i in range(5):
    lista.append(i)
# resultado: [0, 1, 2, 3, 4]
```

**Forma 2: Comprensión de listas (más concisa)**
```python
lista = [i for i in range(5)]
# resultado: [0, 1, 2, 3, 4]
```

**Forma 3: Con números personalizados**
```python
lista = []
for i in range(1, 11):  # del 1 al 10
    lista.append(i * 2)
# resultado: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

**Forma 4: Llenar una lista existente**
```python
lista = [0] * 5  # [0, 0, 0, 0, 0]
for i in range(len(lista)):
    lista[i] = i + 1
# resultado: [1, 2, 3, 4, 5]
```

La opción más idiomática en Python es la comprensión de listas (forma 2).

¿Querés que te muestre algún caso específico?
> Como puedo hacer para que los numeros sean una secuencia desde 1 hasta un numero N inclusive
Para crear una secuencia desde 1 hasta N inclusive, usa `range(1, N+1)`:

**Con append:**
```python
N = 10
lista = []
for i in range(1, N + 1):
    lista.append(i)
# resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Con comprensión (recomendado):**
```python
N = 10
lista = [i for i in range(1, N + 1)]
# resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Explicación del range:**
- `range(1, N + 1)` genera números desde 1 hasta N (inclusive)
- el segundo argumento es exclusivo, por eso sumamos 1

Si N = 5:
- `range(1, 6)` genera: 1, 2, 3, 4, 5

Eso es todo lo que necesitás.

**¿Lo usaste tal cual o lo modificaste?**
Utilice tal cual el ejemplo de append.

---

### 6 - funciones.py

**Herramienta**: GPT-6.4

**Prompt usado**:
> Necesito una función aplicar_funcion(lista: list, func) -> list en Python 2.13.
>Quiero comparar enfoques y elegir uno simple y performante para un TP:
>
>    nueva lista que cada elemento sea func(elemento)
>    alguna manera de implementar la funcion a cada elemento y guardarlo nuevamente
>    alguna otra alternativa que corra con solo una funcion y aplique a toda la lista
>    
>    Analizá pros/contras (performance + simplicidad + edge cases como puntuación).
>    Luego recomendá UNO y escribí el código con docstring, dejando claro qué casos NO cubre (por ejemplo, "hola," vs "hola").


**Resultado obtenido**:
Voy a revisar el módulo de funciones para ajustar `aplicar_funcion` con una solución simple y eficiente, y dejar explícitos los límites de lo que cubre.

Read [](file:///home/javirulo/LPyL/tp-2-introducci-n-a-python-athegemann-1/src/funciones.py)

Read [](file:///home/javirulo/LPyL/tp-2-introducci-n-a-python-athegemann-1/tests/test_funciones.py)

Ya tengo el contexto y voy a implementar `aplicar_funcion` con el enfoque que mejor equilibra simplicidad y rendimiento para este TP: una comprensión de listas.

Generating patch (15 lines) in [](file:///home/javirulo/LPyL/tp-2-introducci-n-a-python-athegemann-1/src/funciones.py)


```

```
Elegí y dejé implementada la opción más equilibrada para este TP en funciones.py: comprensión de listas.

Comparación rápida de enfoques:

1. `for` con `append`
- Pros: muy explícito, fácil de entender para principiantes.
- Contras: más verboso.
- Performance: buena, pero normalmente un poco peor que una comprensión de listas.

2. Comprensión de listas
- Pros: simple, idiomática en Python, normalmente la opción más clara cuando querés construir una nueva lista.
- Contras: menos didáctica si recién estás aprendiendo bucles.
- Performance: suele ser la mejor o muy cercana a la mejor para este caso.

3. `map(func, lista)`
- Pros: concisa.
- Contras: devuelve un iterador, así que para obtener lista hay que envolverlo en `list(...)`; a veces es menos legible si la función no es trivial.
- Performance: puede ser competitiva, pero para este caso no aporta una ventaja clara frente a la comprensión.

Recomendación:
- Para este TP, usar comprensión de listas.
- Es simple, performante y expresa exactamente “aplicar una función a cada elemento y devolver una nueva lista”.

La función quedó así:

    def aplicar_funcion(lista: list, func) -> list:
        """
        Aplica func a cada elemento de la lista y retorna una nueva lista.

        No normaliza ni limpia los elementos antes de aplicar la función:
        por ejemplo, "hola," y "hola" se tratan como valores distintos.
        """
        return [func(elemento) for elemento in lista]

Casos que no cubre:
- No limpia texto ni quita puntuación.
- No convierte tipos automáticamente.
- Si `func` falla con un elemento, la excepción se propaga.
- Si la lista está vacía, devuelve `[]`.

Si querés, también te puedo escribir la versión con `for` explícito para comparar lado a lado con esta.

Made changes.


**¿Lo usaste tal cual o lo modificaste?**
Lo utilicé tal cual.

---

### 7 - operaciones.py

**Herramienta**: GPT-5.4

**Prompt usado**:
>Tengo que implementar capitalizar_palabras(texto: str) -> str para un TP.
>    Compará 3 enfoques:
>    A) utilizar alguna funcion que capitalice cada palabra de un string directamente,
>    B) crear una lista con las palabras y capitalizar la primer letra de cada palabra, luego recomponer la lista a un string
>    C) capitalizar cada caracter que siga despues de un espacio.
>    Elegí el más adecuado para principiantes, justificá, y escribí el código final.


**Resultado obtenido**:
Voy a comparar los 3 enfoques para que veas cuál es mejor para aprender:

**Enfoque A: Función directa**
```python
def capitalizar_palabras(texto: str) -> str:
    return texto.title()
```
- Pros: muy conciso
- Contras: es "magia", no aprendes cómo funciona, no es flexible

**Enfoque B: Lista + manipulación + recomposición (RECOMENDADO)**
```python
def capitalizar_palabras(texto: str) -> str:
    palabras = texto.split()
    capitalizadas = []
    for palabra in palabras:
        capitalizadas.append(palabra.capitalize())
    return " ".join(capitalizadas)
```
- Pros: didáctico, verás cada paso, aprendes split/join, fácil de modificar
- Contras: un poco más de código (pero educativo)

**Enfoque C: Iteración por caracteres**
```python
def capitalizar_palabras(texto: str) -> str:
    resultado = ""
    capitalizar_siguiente = True
    for char in texto:
        if char == " ":
            resultado += char
            capitalizar_siguiente = True
        elif capitalizar_siguiente:
            resultado += char.upper()
            capitalizar_siguiente = False
        else:
            resultado += char.lower()
    return resultado
```
- Pros: enseña lógica de estado
- Contras: complejo para principiantes, fácil para equivocarse

**Elección: Enfoque B**

Justificación:
- Equilibra claridad con educación
- Enseña conceptos fundamentales: listas, strings, métodos útiles
- Código legible y fácil de debuggear
- Flexible para cambios futuros

Código final:

```python
def capitalizar_palabras(texto: str) -> str:
    """
    Retorna el texto con la primera letra de cada palabra en mayúscula.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    palabras = texto.split()
    capitalizadas = []
    for palabra in palabras:
        capitalizadas.append(palabra.capitalize())
    return " ".join(capitalizadas)
```

Alternativa compacta (con comprensión):
```python
def capitalizar_palabras(texto: str) -> str:
    """
    Retorna el texto con la primera letra de cada palabra en mayúscula.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    return " ".join(palabra.capitalize() for palabra in texto.split())
```

¿Querés que implemente esto en operaciones.py?

**¿Lo usaste tal cual o lo modificaste?**
Utilice tal cual la primer opcion que me dio (Codigo final, no la alternativa)

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
Que la IA te puede dar muchas alternativas sobre como realizar la misma acción, y la diferencia con los prompts es mas que nada la explicación que le dan al usuario.
- ¿En qué casos la IA fue útil y en cuáles no?
No le encontre mucho sentido al modo de prompting de Interaccion Invertida, ya que directamente podrias hacerle esas preguntas en el mismo mensaje en vez de tener que volver a escribirle y gastando tokens. Diria lo mismo del metodo de refinamiento de preguntas pero en ese comprendo que las distintas explicaciones sirven para enseñar al usuario el por qué de las cosas.
- ¿Qué harías diferente la próxima vez?
No se responder esta pregunta.