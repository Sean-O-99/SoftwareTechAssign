import wx
from filterDialog import MyDialog1
from all_functions import clear_filters, apply_filters

class FilterDialog(MyDialog1):
    def __init__(self, parent):
        super().__init__(parent)
        self.initialize_dialog()

    def initialize_dialog(self):
        self.m_choice1.SetItems([
            "Caloric Value", "Fat", "Saturated Fats", "Monounsaturated Fats",
            "Polyunsaturated Fats", "Carbohydrates", "Sugars", "Protein",
            "Dietary Fiber", "Cholesterol", "Sodium", "Water", "Vitamin A",
            "Vitamin B1", "Vitamin B11", "Vitamin B12", "Vitamin B2",
            "Vitamin B3", "Vitamin B5", "Vitamin B6", "Vitamin C",
            "Vitamin D", "Vitamin E", "Vitamin K", "Calcium", "Copper",
            "Iron", "Magnesium", "Manganese", "Phosphorus", "Potassium",
            "Selenium", "Zinc", "Nutrition Density"
        ])

        self.m_button4.Bind(wx.EVT_BUTTON, self.clear_filters)

    def clear_filters(self, event):
        filters = clear_filters()

        self.m_choice1.SetSelection(0)
        self.m_textCtrl2.SetValue(filters['min_value'])
        self.m_textCtrl3.SetValue(filters['max_value'])
        self.m_radioBtn1.SetValue(False)
        self.m_radioBtn2.SetValue(False)
        self.m_radioBtn3.SetValue(False)

    def apply_filters(self, event):
        # Gather inputs from the UI
        selected_nutrient = self.m_choice1.GetString(self.m_choice1.GetSelection())
        min_value = self.m_textCtrl2.GetValue()
        max_value = self.m_textCtrl3.GetValue()

        if self.m_radioBtn1.GetValue():
            level = "Low"
        elif self.m_radioBtn2.GetValue():
            level = "Medium"
        elif self.m_radioBtn3.GetValue():
            level = "High"
        else:
            level = None

        # Call the apply_filters function from all_functions.py
        filters = apply_filters(selected_nutrient, min_value, max_value, level)

        # Now set any other needed UI components based on the result
        self.filter_text = f"Nutrient: {filters['selected_nutrient']}, Min: {filters['min_value']}, Max: {filters['max_value']}, Level: {filters['level']}"
        self.selected_nutrient = filters['selected_nutrient']
        self.min_value = filters['min_value']
        self.max_value = filters['max_value']
        self.level = filters['level']

        self.EndModal(wx.ID_OK)

if __name__ == "__main__":
    app = wx.App(False)
    dialog = FilterDialog(None)
    app.MainLoop()
