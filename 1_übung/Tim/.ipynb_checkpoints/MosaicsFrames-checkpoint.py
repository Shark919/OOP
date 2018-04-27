#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python class for the graphic View of the Mosaic-Functions
# Version 0.3 Veranstaltung: Objektorientierte Programmierung
# Author: Prof. Dr. Margarita Esponda

from javafx.application import Application
from javafx.scene import Scene
from javafx.scene.layout import GridPane
from javafx.scene.canvas import Canvas
from javafx.scene.paint import Color

# Import the Python-functions to be painted
import MosaicFunctions

class MosaicsFrames(Application):
    
    def __init__(self):
        self.size = 400
        self.stone_size = 1
        self.graphics_canvas = []
        self.decide_color_functions = [MosaicFunctions.decide_color_squares, MosaicFunctions.decide_color_diags, MosaicFunctions.decide_color_triangles, MosaicFunctions.decide_color_circle, MosaicFunctions.decide_color_chess, MosaicFunctions.decide_color_illusion_1, MosaicFunctions.decide_color_illusion_2, MosaicFunctions.decide_color_illusion_3, MosaicFunctions.decide_color_own_picture]

    def start(self, stage):
        stage.title = "Mosaiken"
        stage.width = 3 * self.size*self.stone_size
        stage.height = 3 * self.size*self.stone_size + 20

        grid_pane = GridPane()

        for i in range(0, 9):
            self.graphics_canvas.append( Canvas(self.size, self.size) )

        for i in range(0, 9):
            self.draw_Mosaic(self.decide_color_functions[i], i)
            grid_pane.add(self.graphics_canvas[i], i % 3, i//3)

        stage.setScene(Scene(grid_pane, 3 * self.size, 3 * self.size))
        stage.show()

    def draw_Mosaic(self, decide_color_func, i):
        graphic_context = self.graphics_canvas[i].getGraphicsContext2D()

        for x in range(0, self.size):
            for y in range(0, self.size):
                current_color = decide_color_func (x, y, self.size)
                graphic_context.setFill(Color.valueOf(current_color))

                # paint a rectangle with the color in current_color at the (x,y) position
                graphic_context.fillRect(x, y, self.stone_size, self.stone_size)

if __name__ == '__main__':
    Application.launch(MosaicsFrames().class,[])

