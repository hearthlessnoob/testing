import arcade
import random

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000




class Balle1:
    #initiate la classe balle
    def __init__(self, x, y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = 10
        self.change_y = 10
        self.rayon = rayon
        self.color = color
    #faire la balle bouger
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.y < self.rayon:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1
    #dessiner la balle
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Balle2:
    #initiate la classe balle
    def __init__(self, x, y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = -10
        self.change_y = -10
        self.rayon = rayon
        self.color = color
    #faire la balle bouger
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.y < self.rayon:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1
    #dessiner la balle
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)
class Balle3:
    #initiate la classe balle
    def __init__(self, x, y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = -10
        self.change_y = 10
        self.rayon = rayon
        self.color = color
    #faire la balle bouger
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.y < self.rayon:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1
    #dessiner la balle
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Balle4:
    #initiate la classe balle
    def __init__(self, x, y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = 10
        self.change_y = -10
        self.rayon = rayon
        self.color = color
    #faire la balle bouger
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.y < self.rayon:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1
    #dessiner la balle
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


class Rectangle1:
    #initiate la classe rectangle
    def __init__(self, x, y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = 10
        self.change_y = 10
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle
    #faire bouger le rectangle
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.width/2:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width/2:
            self.change_x *= -1
        if self.y < self.height/2:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height/2:
            self.change_y *= -1
    #dessiner le rectangle
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

class Rectangle2:
    #initiate la classe rectangle
    def __init__(self, x, y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = -10
        self.change_y = -10
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle
    #faire bouger le rectangle
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.width/2:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width/2:
            self.change_x *= -1
        if self.y < self.height/2:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height/2:
            self.change_y *= -1
    #dessiner le rectangle
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)
class Rectangle3:
    #initiate la classe rectangle
    def __init__(self, x, y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = -10
        self.change_y = 10
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle
    #faire bouger le rectangle
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.width/2:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width/2:
            self.change_x *= -1
        if self.y < self.height/2:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height/2:
            self.change_y *= -1
    #dessiner le rectangle
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

class Rectangle4:
    #initiate la classe rectangle
    def __init__(self, x, y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = 10
        self.change_y = -10
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle
    #faire bouger le rectangle
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.width/2:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width/2:
            self.change_x *= -1
        if self.y < self.height/2:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height/2:
            self.change_y *= -1
    #dessiner le rectangle
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

class MyGame(arcade.Window):
    #ouvrir la fenetre
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.balles = []
        self.rectangles = []
    #changer le background color
    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
    #dessiner les formes
    def on_draw(self):
        arcade.start_render()
        for balle in self.balles:
            balle.draw()
        for rectangle in self.rectangles:
            rectangle.draw()
    #faire bouger les formes
    def on_update(self, x, y, modifiers, delta_time):
        for balle in self.balles:
            balle.update()
        for rectangle in self.rectangles:
            rectangle.update()
        if self.mouse1_held:
            balle1 = Balle1(x, y, 30, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
            balle2 = Balle2(x, y, 30, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
            balle3 = Balle3(x, y, 30, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
            balle4 = Balle4(x, y, 30, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
            self.balles.append(balle1)
            self.balles.append(balle2)
            self.balles.append(balle3)
            self.balles.append(balle4)
        elif self.mouse2_held:
            rectangle1 = Rectangle1(x, y, 50, 50,
                                    (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), 0)
            rectangle2 = Rectangle2(x, y, 50, 50,
                                    (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), 0)
            rectangle3 = Rectangle3(x, y, 50, 50,
                                    (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), 0)
            rectangle4 = Rectangle4(x, y, 50, 50,
                                    (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), 0)
            self.rectangles.append(rectangle1)
            self.rectangles.append(rectangle2)
            self.rectangles.append(rectangle3)
            self.rectangles.append(rectangle4)
    #savoir si on doit creer un cercle ou un rectangle
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse1_held = True
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.mouse2_held = True


    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse1_held = False
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse2_held = False


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


if __name__ == "__main__":
    main()
