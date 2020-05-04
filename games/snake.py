#!/usr/bin/python3

import tkinter as tk
import time
import random

# Fenster erstellen
window = tk.Tk()
window.title("Snake")

# Canvas erstellen, damit wir in das Fenster zeichnen koennen
virtual_pixel = 25
canvas_virtual_width = 15
canvas_virtual_height = 15
canvas_width = canvas_virtual_width * virtual_pixel
canvas_height = canvas_virtual_height * virtual_pixel

canvas = tk.Canvas(
    window,
    width=canvas_width,
    height=canvas_height
)
canvas.pack()  # erstelltes Canvas an window dran haengen

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

# Futter Koordinaten vorbereiten
food = []
food_pixel = False

# Steuerung
def key_pressed(event):
    print(event.char)
    global direction
    if event.char == 'w' and direction != 'b':
        direction = 't'
    elif event.char == 'd' and direction != 'l':
        direction = 'r'
    elif event.char == 's' and direction != 't':
        direction = 'b'
    elif event.char == 'a' and direction != 'r':
        direction = 'l'
    return direction

window.bind('<Key>', key_pressed)

# Hauptlogik des Spiels
#
# die crash-Variable dient uns als Ausschalter
crash = False

# Game-Loop
while crash is False:
    head = snake[0]

    # Futter Koordinaten berechnen
    if len(food) == 0:
        while True:
            rand_x = random.randint(1, canvas_virtual_width)
            rand_y = random.randint(1, canvas_virtual_height)

            is_valid_coordinates = True
            for pixel in snake:
                if (pixel[0] == rand_x) and (pixel[1] == rand_y):
                    is_valid_coordinates = False

            if is_valid_coordinates is True:
                food = [
                    rand_x,
                    rand_y
                ]

                m = virtual_pixel
                food_pixel = canvas.create_rectangle(
                    food[0] * m,
                    food[1] * m,
                    food[0] * m + m,
                    food[1] * m + m,
                    fill='red'
                )
                break

    # um die Elemente in dem Canvas Element jedes mal
    # neu zeichnen zu koennen, muessen wir sie loeschen
    for rec in rectangles:
        canvas.delete(rec)
    rectangles = []

    # zeichnen der einzelnen Elemente der Schlange
    for pixel in snake:
        m = virtual_pixel
        color = "#bada55"

        if pixel == head:  # Kopf der Schlange anders einfaerben
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
    #
    # head[0] ist die x-Koordinate vom aktuellen Kopf, head[1] die y-Koordinate. Diese Koordinaten verwenden wir um den
    # "neuen" Kopf zu berechnen.
    new_head = []
    if direction == "r":
        new_head = [
            head[0] + 1,
            head[1]
        ]
    elif direction == "b":
        new_head = [
            head[0],
            head[1] + 1
        ]
    elif direction == "l":
        new_head = [
            head[0] - 1,
            head[1]
        ]
    elif direction == "t":
        new_head = [
            head[0],
            head[1] - 1
        ]
    # das ganze else könnten wir uns eigentlich sparen, weil direction nie einen anderen Wert als t, b, l oder t annehmen können sollte
    else:
        print('Dieser Fall sollte nicht auftreten! Wenn diese Zeile ausgegeben wird, dann ist estwas schlimmes passiert.')

    # Wenn die Schlange sich selbst berührt, ist das Spiel auch vorbei
    for pixel in snake:
        if (pixel[0] == new_head[0]) and (pixel[1] == new_head[1]):
            print('game over')
            crash = True

    # neu berechneten Kopf an die Schlange dran hängen
    snake.insert(0, new_head)
    # letztes Element der Schlange abschneiden. Dadurch entsteht die Illusion einer Bewebung
    snake.pop()

    # Hilfsvariablen berechnen
    right_border = (canvas_width - arena_padding) / virtual_pixel
    bottom_border = (canvas_height - arena_padding) / virtual_pixel
    left_border = arena_padding / virtual_pixel
    top_border = arena_padding / virtual_pixel

    # Wenn die Schlange am Rand anläuft, ist das Spiel vorbei
    if (new_head[0] >= right_border) or (new_head[0] < left_border) or (new_head[1] >= bottom_border) or (new_head[1] < top_border):
        print('game over')
        crash = True

    # 800 Millisekunden warten, damit die Snake eine
    # "smoothe" Bewegung macht
    time.sleep(0.15)

# Ende while-Schleife

# tkinter Fenster starten
window.mainloop()
