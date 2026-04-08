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

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
