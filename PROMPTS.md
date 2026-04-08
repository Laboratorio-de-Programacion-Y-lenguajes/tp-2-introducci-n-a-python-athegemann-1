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
> Actuá como tutor de Python 3.13. Dame una receta paso a paso para: crear una funcion llamada crear_saludo, enviar como parametro el nombre de una persona, devolver un string con el formato "Hola, " y el nombre de la persona. No uses librerías externas. Mostrá la función con docstring.


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

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


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
