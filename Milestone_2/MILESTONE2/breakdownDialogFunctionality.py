import wx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg

from breakdownDialog import MyDialog2

class NutritionalDialog(MyDialog2):
    def __init__(self, parent, food_item, fig, fat, carbs, prot):
        super().__init__(parent)
        self.food_item = food_item
        self.fig = fig
        self.fat = fat
        self.carbs = carbs
        self.prot = prot
        self.initialize_dialog()


    def initialize_dialog(self):
        canvas = FigureCanvasWxAgg(self.m_panel1, -1, self.fig)

        self.SetTitle(F"Nutrition Breakdown: {self.food_item}")
        carbs_value = str(self.carbs[1])
        prot_value = str(self.prot[1])
        fat_value = str(self.fat[1])
        self.m_staticText91.SetLabel(carbs_value)
        self.m_staticText11.SetLabel(prot_value)
        self.m_staticText13.SetLabel(fat_value)