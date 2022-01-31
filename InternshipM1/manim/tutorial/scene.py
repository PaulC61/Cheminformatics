from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5) 

        self.add(circle, square, triangle)
        self.wait(1)

class SomeAnimations(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        self.play(ApplyMethod(square.set_fill, WHITE))
        self.wait(1)

        self.play(ApplyMethod(square.shift, UP), run_time = 4)
        self.wait(1)