import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import pygame


# Drag and drop code taken from 
# https://pythonguides.com/python-tkinter-drag-and-drop/
file_path = ""

def drop_file(event):
    """Handles the dropped file path."""
    global file_path
    file_path = event.data  # File path as a string
    label.config(text=f"Dropped file:\n{file_path}")


root = TkinterDnD.Tk()
root.geometry("500x300")
root.title("File Drag and Drop")

label = tk.Label(root, text="Drag & Drop a file here then close the window",
                  bg="lightgray", width=50, height=10)
label.pack(pady=50)

label.drop_target_register(DND_FILES)
label.dnd_bind("<<Drop>>", drop_file)

root.mainloop()

def main():
    # Pygame Setup
    pygame.init
    pygame.display.init()
    pygame.display.set_caption("Eyedropper Color picker")
    clock = pygame.time.Clock()
    dt = 0
    mouse_press = pygame.MOUSEBUTTONUP
    user_file = pygame.image.load(file_path)
    image_x = user_file.get_width() + 500
    image_y = user_file.get_height() + 100

    resolution = ([image_x,image_y])
    screen = pygame.display.set_mode(size=resolution, flags=pygame.SCALED|
                                     pygame.FULLSCREEN)

    screen.fill("Grey")
    screen.blit(user_file, dest=(50,50))

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_press = event
                print (mouse_press)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Render & Display
        pygame.display.flip()
        dt = clock.tick(24)


    pygame.quit()

if __name__ == "__main__":
    main()