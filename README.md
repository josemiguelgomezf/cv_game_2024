# CV Game 2024 - Mi CV Interactivo

Este proyecto es una versión interactiva de mi CV, desarrollado en un juego 2D usando `pygame`. La idea es mostrar mis proyectos personales y experiencia laboral de una manera entretenida y visual.

## Descripción del Proyecto

El juego presenta una ventana donde se muestra una lista de proyectos en la parte superior y mi experiencia laboral en la parte inferior. Este es solo un punto de partida; puedes expandirlo con más interactividad y contenido.

### Funcionalidades Básicas
- **Proyectos**: Se muestra una lista de proyectos con sus descripciones.
- **Experiencia Laboral**: Se muestra una lista de experiencias laborales con los roles y las duraciones en cada empresa.
- **Interfaz Gráfica**: Utiliza `pygame` para mostrar el contenido de forma visual.

## Requisitos Previos

Asegúrate de tener Python instalado en tu máquina. También necesitas instalar la librería `pygame` para ejecutar el código.

Instala `pygame` utilizando pip:


pip install pygame
Uso del Código
Clona el Repositorio: Si aún no lo has hecho, clona este repositorio en tu máquina local.

Ejecuta el Código: Navega hasta el directorio del proyecto y ejecuta el script en Python.


python cv_game.py
Interacción: Al ejecutar el código, se abrirá una ventana que mostrará mi CV. Puedes cerrar la ventana en cualquier momento haciendo clic en el botón de cierre o presionando Alt + F4.
Explicación del Código
Inicialización y Configuración

import pygame
import sys
pygame: Importa la librería Pygame para manejar la ventana del juego y la visualización del contenido.
sys: Se usa para manejar la salida del programa cuando se cierra la ventana.

pygame.init()
Inicializa todos los módulos de Pygame.
Configuración de la Pantalla

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CV Game 2024 - Mi CV interactivo")
Define las dimensiones de la ventana del juego (800x600 píxeles) y establece el título de la ventana.
Colores y Fuentes

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 36)
Define los colores en formato RGB. BLACK se usa para el fondo y WHITE para el texto.
La fuente del texto se establece con un tamaño de 36 píxeles.
Datos del CV

projects = [
    {"title": "Proyecto 1: Web Scraping con IA", "description": "Desarrollo de una herramienta de web scraping utilizando GPT-3."},
    {"title": "Proyecto 2: Juego 2D en Python", "description": "Un juego simple desarrollado con Pygame."},
    {"title": "Proyecto 3: App móvil con Flutter", "description": "Aplicación móvil para seguimiento de hábitos."}
]

experience = [
    {"company": "Empresa 1", "role": "Desarrollador Python", "duration": "2019-2021"},
    {"company": "Empresa 2", "role": "Ingeniero de Software", "duration": "2021-2023"},
]
projects y experience contienen información sobre mis proyectos personales y experiencia laboral.
Función de Renderizado de Texto

def draw_text(text, x, y, color=WHITE):
    screen.blit(font.render(text, True, color), (x, y))
Función para mostrar texto en la pantalla en una posición específica (x, y) con un color determinado (por defecto WHITE).
Bucle Principal del Juego
python
Copiar código
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(BLACK)
Inicia el bucle principal del juego. Establece el fondo de la pantalla en negro (BLACK).

        # Dibuja la sección de proyectos
        draw_text("Proyectos:", 50, 50)
        for i, project in enumerate(projects):
            draw_text(f"{project['title']}", 50, 100 + i * 60)
            draw_text(f"{project['description']}", 70, 130 + i * 60)
Muestra los títulos y descripciones de los proyectos en la parte superior de la pantalla.

        # Dibuja la sección de experiencia laboral
        draw_text("Experiencia Laboral:", 50, 350)
        for i, exp in enumerate(experience):
            draw_text(f"{exp['company']} - {exp['role']}", 50, 400 + i * 60)
            draw_text(f"Duración: {exp['duration']}", 70, 430 + i * 60)
Muestra la experiencia laboral en la parte inferior de la pantalla.

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)
Maneja los eventos de cierre de la ventana. El contenido de la pantalla se actualiza constantemente con pygame.display.flip().
Ejecución del Programa

if __name__ == "__main__":
    main()
Ejecuta la función main() para iniciar el juego.
Personalización
Este es un punto de partida sencillo para crear tu propio "CV interactivo". Puedes añadir más interactividad, animaciones o incluso convertirlo en un pequeño juego con desafíos que el usuario debe completar para ver más información sobre ti.

Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme.
