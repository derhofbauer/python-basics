#!/usr/bin/python3

import tkinter as tk
import time

# Fenster erstellen
window = tk.Tk()
window.title("Snake")

# Canvas erstellen, damit wir in das Fenster zeichnen koennen
virtual_pixel = 25
canvas_width = 15 * virtual_pixel
canvas_height = 15 * virtual_pixel

canvas = tk.Canvas(
    window,
    width = canvas_width,
    height = canvas_height
)
canvas.pack() # erstelltes Canvas an window dran haengen

# Spiel Arena definieren
arena_padding = 1 * virtual_pixel
canvas.create_rectangle(
    1 + arena_padding,
    1 + arena_padding,
    canvas_width - arena_padding,
    canvas_height - arena_padding
)

# Schlange zeichnen
snake = [
    [4, 7],
    [3, 7],
    [2, 7]
]
rectangles = []
direction = "r"

# Hauptlogik des Spiels
crash = False

while crash is False:
    head = snake[0]

    # um die Elemente in dem Canvas Element jedes mal
    # neu zeichnen zu koennen, muessen wir sie loeschen
    for rec in rectangles:
        canvas.delete(rec)

    # zeichnen der einzelnen Elemente der Schlange
    for pixel in snake:
        m = virtual_pixel
        color = "#bada55"

        if pixel == head: # Kopf der Schlange anders einfaerben
            color = "#6F8233"

        rectangle = canvas.create_rectangle(
            pixel[0] * m,
            pixel[1] * m,
            pixel[0] * m + m,
            pixel[1] * m + m,
            fill=color,
            outline="#ff0000"
        )
        # speichern des gezeichneten Rechtecks,
        # damit wir es im naechsten Durchlauf der
        # while-Schleife loeschen koennen
        rectangles.append(rectangle)
    # Ende for-Schleife

    # Fenster neu zeichnen
    window.update()

    # Schlange nach vorne schieben
    if direction == "r":
        new_head = [
            head[0] + 1,
            head[1]
        ]
        snake.insert(0, new_head)
        snake.pop()
    
    # 800 Millisekunden warten, damit die Snake eine
    # smoothe Bewegung macht
    time.sleep(0.8)

# Ende while-Schleife

# tkinter Fenster starten
window.mainloop()