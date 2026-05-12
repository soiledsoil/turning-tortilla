import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import pygame


def rbg_to_hex (rgb):
    # Convertion line taken from
    # https://stackoverflow.com/questions/3380726/converting-an-rgb-color-tuple-to-a-hexidecimal-string
    hex_value = '#%02x%02x%02x' % (rgb)
    return (hex_value)

# Drag and drop code taken and modified from 
# https://pythonguides.com/python-tkinter-drag-and-drop/
file_path = ""

def drop_file(event):
    """Handles the dropped file path."""
    global file_path
    file_path = event.data  # File path as a string
    label.config(text=f"Dropped file:\n{file_path}")

# Creation of the tkinter window
root = TkinterDnD.Tk()
root.geometry("500x300")
root.title("File Drag and Drop")

# Label/Graphic creation
label = tk.Label(root, text="Drag & Drop a file here then close the window",
                  bg="lightgray", width=50, height=10)
label.pack(pady=50)


label.drop_target_register(DND_FILES)
label.dnd_bind("<<Drop>>", drop_file)

root.mainloop()

def main():
    # Pygame Setup
    pygame.init()
    pygame.font.init()
    pygame.display.init()
    pygame.display.set_caption("Eyedropper Color picker")
    clock = pygame.time.Clock()
    dt = 0
    mouse_press = pygame.MOUSEBUTTONUP
    font = pygame.font.Font(None, size=20)

    # Color vars
    rgba_value = ()
    hex_value = ""
    rgb_text = ""
    hex_text = ""

    # Image Loader
    user_file = pygame.image.load(file_path)
    image_x = user_file.get_width() + 500
    image_y = user_file.get_height() + 100

    resolution = ([image_x,image_y])
    screen = pygame.display.set_mode(size=resolution, flags=pygame.SCALED|
                                     pygame.FULLSCREEN)

    screen.fill("Grey")
    screen.blit(user_file, dest=(50,50))

    rgb_text = font.render(str(rgba_value),antialias=True, color="White")
    screen.blit(rgb_text, ((screen.width/2) + 200, 50))

    hex_text = font.render(hex_value,antialias=True, color="White")
    screen.blit(hex_text, ((screen.width/2) + 200, screen.height/2))


    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                rgba_value = screen.get_at(mouse_pos)
                rgba_value = rgba_value[0:3]
                hex_value = rbg_to_hex(rgba_value)

                rgb_text = font.render(str(rgba_value),
                                       antialias=True, color="White")
                hex_text = font.render(hex_value,
                                       antialias=True, color="White")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Render & Display
        screen.blit(rgb_text, ((screen.width/2) + 200, 50))
        screen.blit(hex_text, ((screen.width/2) + 200, screen.height/2))
        pygame.display.flip()
        dt = clock.tick(24)


    pygame.quit()

if __name__ == "__main__":
    main()