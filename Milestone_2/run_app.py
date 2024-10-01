import wx
import wx.grid
import pandas as pd
import re

from template_frame import MyFrame1 as MyFrame1

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

class DataTable (wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GettAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr

class CalcFrame(MyFrame1):
    def __init__(self,parent=None):
        super().__init__(parent)
        columns = ["Food", "Caloric Value", "Fat", "Carbohydrates", "Protein"]
        self.df = pd.read_csv("../Milestone1/Food_Nutrition_Dataset.csv", usecols=columns)
        self.table = DataTable(self.df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.Show(True)
        self.Layout()

    def SearchFunc( self, event ):
        event.Skip()
        keywordValue = self.m_textCtrl1.GetValue()
        keyword = keywordValue.lower()
        searchFood = self.df["Food"]
        index = []

        for food in searchFood:
            if re.search(keyword, food):
                index.append(True)
            else:
                index.append(False)
        dfFiltered = self.df[index]
        self.m_grid1.ClearGrid()
        self.table = DataTable(dfFiltered)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()

if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()