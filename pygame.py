import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CV Game 2024 - Mi CV interactivo")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fuentes
font = pygame.font.Font(None, 36)

# Datos del CV
projects = [
    {"title": "Proyecto 1: Web Scraping con IA", "description": "Desarrollo de una herramienta de web scraping utilizando GPT-3."},
    {"title": "Proyecto 2: Juego 2D en Python", "description": "Un juego simple desarrollado con Pygame."},
    {"title": "Proyecto 3: App móvil con Flutter", "description": "Aplicación móvil para seguimiento de hábitos."}
]

experience = [
    {"company": "Empresa 1", "role": "Desarrollador Python", "duration": "2019-2021"},
    {"company": "Empresa 2", "role": "Ingeniero de Software", "duration": "2021-2023"},
]

# Función para mostrar texto en la pantalla
def draw_text(text, x, y, color=WHITE):
    screen.blit(font.render(text, True, color), (x, y))

# Bucle principal del juego
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(BLACK)

        # Dibuja la sección de proyectos
        draw_text("Proyectos:", 50, 50)
        for i, project in enumerate(projects):
            draw_text(f"{project['title']}", 50, 100 + i * 60)
            draw_text(f"{project['description']}", 70, 130 + i * 60)

        # Dibuja la sección de experiencia laboral
        draw_text("Experiencia Laboral:", 50, 350)
        for i, exp in enumerate(experience):
            draw_text(f"{exp['company']} - {exp['role']}", 50, 400 + i * 60)
            draw_text(f"Duración: {exp['duration']}", 70, 430 + i * 60)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
