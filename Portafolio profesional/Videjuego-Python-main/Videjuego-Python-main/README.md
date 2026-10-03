#  Colección de Videojuegos en Python

Una colección de videojuegos clásicos desarrollados en Python para ejecutarse directamente desde la terminal o consola. Este repositorio reúne proyectos enfocados en la lógica de programación, uso de estructuras de control, manejo de excepciones (`try/except`), Programación Orientada a Objetos (POO) y el uso de librerías nativas como `random`.

---

## Juegos Incluidos

### 1. **21 / Blackjack con Mazo Real** (`juego_de_21_(black jack).py`)
- **Descripción:** Implementación del clásico juego de cartas 21.
- **Mecánicas:** Utiliza un mazo interactivo que remueve las cartas tomadas.
- **Modos de Juego:** 1vs1 local (contra otro jugador) o contra la máquina (IA con toma de decisiones automática).

### 2. **Mini RPG de Consola** (`Mini_RPG.py`)
- **Descripción:** Juego de combate por turnos entre el jugador y un enemigo.
- **Mecánicas:** El jugador puede elegir entre **Atacar** (generando daño aleatorio) o **Defender** (recuperando puntos de vida). Gana el primero que reduzca a 0 la vida del oponente.

### 3. **Piedra, Papel o Tijera** (`piedra_papelo_tijera.py`)
- **Descripción:** El juego tradicional adaptado usando Programación Orientada a Objetos (POO).
- **Mecánicas:** Clases independientes para `Jugador`, `Computadora` y la lógica general del `Juego`.

### 4. **Ahorcado** (`juego_ahorcado_pequenio.py`)
- **Descripción:** Juego clásico de adivinanza de palabras por turnos.
- **Mecánicas:** Cuenta con un límite de 6 intentos, validación de caracteres únicos y visualización dinámica del progreso de la palabra.

### 5. **Adivina el Número** (`adivina_el_numero.py` / `ejercios_try.py`)
- **Descripción:** Juego interactivo de adivinanza numérica.
- **Mecánicas:** La máquina genera un número aleatorio entre 1 y 10. Incluye pistas de "muy alto" o "muy bajo" y control de errores por entrada de datos inválidos.

### 6. **Juego del Gato / Tres en Raya** (`Juego_gato.py`)
- **Descripción:** Tablero clásico de 3x3 para jugar en terminal.
- **Mecánicas:** Validación de posiciones (0 al 8), control de casillas ocupadas y alternancia de turnos entre "X" y "O".

---

## 🛠️ Requisitos e Instalación

El proyecto no requiere librerías externas complejas, ya que utiliza la biblioteca estándar de Python (`random`).

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Danielreyesleon/Videjuego-Python.git](https://github.com/Danielreyesleon/Videjuego-Python.git)
   cd Videjuego-Python
python --version
# Para jugar al 21 (Blackjack)
python "juego_de_21_(black jack).py"

# Para jugar al Mini RPG
python Mini_RPG.py

# Para jugar a Piedra, Papel o Tijera
python piedra_papelo_tijera.py

# Para jugar al Ahorcado
python juego_ahorcado_pequenio.py

# Para jugar Adivina el Número
python adivina_el_numero.py
   
