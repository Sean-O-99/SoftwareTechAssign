import wx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg

from breakdownDialog import MyDialog2

class NutritionalDialog(MyDialog2):
    def __init__(self, parent, food_item, fig):
        super().__init__(parent)
        self.food_item = food_item
        self.fig = fig
        self.initialize_dialog()

    def initialize_dialog(self):
        canvas = FigureCanvasWxAgg(self.m_panel1, -1, self.fig)

        self.SetTitle(F"Nutrition Breakdown: {self.food_item}")