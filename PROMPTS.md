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
> Necesito crear un saludo personalizado. Se que tengo que pedirle al usuario su nombre, edad y ciudad. Necesito el codigo de python y una secuencia completa de pasos, incluyendo los pasos que no tuve en cuenta y descartando los innecesarios.

**Resultado obtenido**:
Para crear un saludo personalizado, necesitas 3 datos de entrada: nombre, edad y ciudad. Con eso, el programa puede construir el mensaje final.

```python
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa tu ciudad: ")

print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}.")
```

Secuencia completa de pasos:

1. Pedir al usuario su nombre.
2. Pedir al usuario su edad.
3. Convertir la edad a número entero, porque `input()` siempre devuelve texto.
4. Pedir al usuario su ciudad.
5. Construir el saludo usando esos tres datos.
6. Mostrar el saludo en pantalla.

Pasos que no son necesarios para este caso:

1. Crear funciones, porque el ejercicio es muy simple.
2. Usar condicionales, porque no hay decisiones que tomar.
3. Usar bucles, porque solo se pide un saludo una vez.
4. Importar módulos, porque no hace falta ninguna librería externa.

Si quieres, también te lo puedo escribir con un estilo más básico, como para un ejercicio de introducción, o más prolijo usando una función.

**¿Lo usaste tal cual o lo modificaste?**
Lo modifique para que aplique a la funcion, pidiendo las variables que me decia. El print lo utilicé tal cual.

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
