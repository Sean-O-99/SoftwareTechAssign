# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

delete_recipe_item_ID = 6000

###########################################################################
## Class RecipeBuilder
###########################################################################

class RecipeBuilder ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Recipe View"), pos = wx.DefaultPosition, size = wx.Size( 778,636 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.recipebuilder_name_label = wx.StaticText( self, wx.ID_ANY, _(u"Name:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.recipebuilder_name_label.Wrap( -1 )

        bSizer11.Add( self.recipebuilder_name_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.recipebuilder_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.recipebuilder_name, 0, wx.ALL, 5 )

        self.recipebuilder_save_button = wx.Button( self, wx.ID_ANY, _(u"Save"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.recipebuilder_save_button, 0, wx.ALL, 5 )


        bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.recipebuilder_delete_button = wx.Button( self, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.recipebuilder_delete_button, 0, wx.ALL, 5 )


        bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        self.recipe_summary = wx.StaticText( self, wx.ID_ANY, _(u"Nutrient Summary for:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.recipe_summary.Wrap( -1 )

        bSizer21.Add( self.recipe_summary, 0, wx.ALL, 5 )

        self.recipe_summary_value = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.recipe_summary_value.Wrap( -1 )

        bSizer21.Add( self.recipe_summary_value, 0, wx.ALL, 5 )


        bSizer13.Add( bSizer21, 0, wx.EXPAND, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.caloric_value_label = wx.StaticText( self, wx.ID_ANY, _(u"Caloric Value:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.caloric_value_label.Wrap( -1 )

        bSizer14.Add( self.caloric_value_label, 0, wx.ALL, 5 )

        self.caloric_value_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.caloric_value_total.Wrap( -1 )

        bSizer14.Add( self.caloric_value_total, 0, wx.ALL, 5 )

        self.carbs_label = wx.StaticText( self, wx.ID_ANY, _(u"Carbohydrates:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.carbs_label.Wrap( -1 )

        bSizer14.Add( self.carbs_label, 0, wx.ALL, 5 )

        self.carbs_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.carbs_total.Wrap( -1 )

        bSizer14.Add( self.carbs_total, 0, wx.ALL, 5 )

        self.protein_label = wx.StaticText( self, wx.ID_ANY, _(u"Protein:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.protein_label.Wrap( -1 )

        bSizer14.Add( self.protein_label, 0, wx.ALL, 5 )

        self.protein_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.protein_total.Wrap( -1 )

        bSizer14.Add( self.protein_total, 0, wx.ALL, 5 )

        self.sugars_label = wx.StaticText( self, wx.ID_ANY, _(u"Sugars:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sugars_label.Wrap( -1 )

        bSizer14.Add( self.sugars_label, 0, wx.ALL, 5 )

        self.sugars_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sugars_total.Wrap( -1 )

        bSizer14.Add( self.sugars_total, 0, wx.ALL, 5 )

        self.fiber_label = wx.StaticText( self, wx.ID_ANY, _(u"Dietary Fiber:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fiber_label.Wrap( -1 )

        bSizer14.Add( self.fiber_label, 0, wx.ALL, 5 )

        self.fiber_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fiber_total.Wrap( -1 )

        bSizer14.Add( self.fiber_total, 0, wx.ALL, 5 )

        self.cholesterol_label = wx.StaticText( self, wx.ID_ANY, _(u"Cholesterol:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cholesterol_label.Wrap( -1 )

        bSizer14.Add( self.cholesterol_label, 0, wx.ALL, 5 )

        self.cholesterol_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cholesterol_total.Wrap( -1 )

        bSizer14.Add( self.cholesterol_total, 0, wx.ALL, 5 )


        bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        self.fats_label = wx.StaticText( self, wx.ID_ANY, _(u"Fats"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fats_label.Wrap( -1 )

        bSizer15.Add( self.fats_label, 0, wx.ALL, 5 )

        self.fats_sat_label = wx.StaticText( self, wx.ID_ANY, _(u"Saturated: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fats_sat_label.Wrap( -1 )

        bSizer15.Add( self.fats_sat_label, 0, wx.ALL, 5 )

        self.fats_sat_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fats_sat_total.Wrap( -1 )

        bSizer15.Add( self.fats_sat_total, 0, wx.ALL, 5 )

        self.fats_mono_label = wx.StaticText( self, wx.ID_ANY, _(u"Monounsaturated:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fats_mono_label.Wrap( -1 )

        bSizer15.Add( self.fats_mono_label, 0, wx.ALL, 5 )

        self.fats_mono_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fats_mono_total.Wrap( -1 )

        bSizer15.Add( self.fats_mono_total, 0, wx.ALL, 5 )

        self.fats_poly_label = wx.StaticText( self, wx.ID_ANY, _(u"Polyunsaturated:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fats_poly_label.Wrap( -1 )

        bSizer15.Add( self.fats_poly_label, 0, wx.ALL, 5 )

        self.fats_poly_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fats_poly_total.Wrap( -1 )

        bSizer15.Add( self.fats_poly_total, 0, wx.ALL, 5 )


        bSizer13.Add( bSizer15, 0, wx.EXPAND, 5 )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        self.vitamins_label = wx.StaticText( self, wx.ID_ANY, _(u"Vitamins"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.vitamins_label.Wrap( -1 )

        bSizer16.Add( self.vitamins_label, 0, wx.ALL, 5 )

        self.A_label = wx.StaticText( self, wx.ID_ANY, _(u"A:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.A_label.Wrap( -1 )

        bSizer16.Add( self.A_label, 0, wx.ALL, 5 )

        self.A_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.A_total.Wrap( -1 )

        bSizer16.Add( self.A_total, 0, wx.ALL, 5 )

        self.B_label = wx.StaticText( self, wx.ID_ANY, _(u"B-1:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.B_label.Wrap( -1 )

        bSizer16.Add( self.B_label, 0, wx.ALL, 5 )

        self.B_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.B_total.Wrap( -1 )

        bSizer16.Add( self.B_total, 0, wx.ALL, 5 )

        self.b_11_label = wx.StaticText( self, wx.ID_ANY, _(u"B-11:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_11_label.Wrap( -1 )

        bSizer16.Add( self.b_11_label, 0, wx.ALL, 5 )

        self.b_11_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_11_total.Wrap( -1 )

        bSizer16.Add( self.b_11_total, 0, wx.ALL, 5 )

        self.b_12_label = wx.StaticText( self, wx.ID_ANY, _(u"B-12:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_12_label.Wrap( -1 )

        bSizer16.Add( self.b_12_label, 0, wx.ALL, 5 )

        self.b_12_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_12_total.Wrap( -1 )

        bSizer16.Add( self.b_12_total, 0, wx.ALL, 5 )

        self.b_2_label = wx.StaticText( self, wx.ID_ANY, _(u"B-2:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_2_label.Wrap( -1 )

        bSizer16.Add( self.b_2_label, 0, wx.ALL, 5 )

        self.b_2_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_2_total.Wrap( -1 )

        bSizer16.Add( self.b_2_total, 0, wx.ALL, 5 )

        self.b_3_label = wx.StaticText( self, wx.ID_ANY, _(u"B-3:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_3_label.Wrap( -1 )

        bSizer16.Add( self.b_3_label, 0, wx.ALL, 5 )

        self.b_3_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_3_total.Wrap( -1 )

        bSizer16.Add( self.b_3_total, 0, wx.ALL, 5 )

        self.b_5_label = wx.StaticText( self, wx.ID_ANY, _(u"B-5:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_5_label.Wrap( -1 )

        bSizer16.Add( self.b_5_label, 0, wx.ALL, 5 )

        self.b_5_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_5_total.Wrap( -1 )

        bSizer16.Add( self.b_5_total, 0, wx.ALL, 5 )

        self.b_6_label = wx.StaticText( self, wx.ID_ANY, _(u"B-6:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_6_label.Wrap( -1 )

        bSizer16.Add( self.b_6_label, 0, wx.ALL, 5 )

        self.b_6_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.b_6_total.Wrap( -1 )

        bSizer16.Add( self.b_6_total, 0, wx.ALL, 5 )

        self.c_label = wx.StaticText( self, wx.ID_ANY, _(u"C:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.c_label.Wrap( -1 )

        bSizer16.Add( self.c_label, 0, wx.ALL, 5 )

        self.c_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.c_total.Wrap( -1 )

        bSizer16.Add( self.c_total, 0, wx.ALL, 5 )

        self.D_label = wx.StaticText( self, wx.ID_ANY, _(u"D:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.D_label.Wrap( -1 )

        bSizer16.Add( self.D_label, 0, wx.ALL, 5 )

        self.D_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.D_total.Wrap( -1 )

        bSizer16.Add( self.D_total, 0, wx.ALL, 5 )

        self.E_label = wx.StaticText( self, wx.ID_ANY, _(u"E:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.E_label.Wrap( -1 )

        bSizer16.Add( self.E_label, 0, wx.ALL, 5 )

        self.E_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.E_total.Wrap( -1 )

        bSizer16.Add( self.E_total, 0, wx.ALL, 5 )

        self.K_label = wx.StaticText( self, wx.ID_ANY, _(u"K:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.K_label.Wrap( -1 )

        bSizer16.Add( self.K_label, 0, wx.ALL, 5 )

        self.K_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.K_total.Wrap( -1 )

        bSizer16.Add( self.K_total, 0, wx.ALL, 5 )


        bSizer13.Add( bSizer16, 0, wx.EXPAND, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        self.calcium_label = wx.StaticText( self, wx.ID_ANY, _(u"Calcium:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.calcium_label.Wrap( -1 )

        bSizer17.Add( self.calcium_label, 0, wx.ALL, 5 )

        self.calcium_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.calcium_total.Wrap( -1 )

        bSizer17.Add( self.calcium_total, 0, wx.ALL, 5 )

        self.copper_label = wx.StaticText( self, wx.ID_ANY, _(u"Copper:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.copper_label.Wrap( -1 )

        bSizer17.Add( self.copper_label, 0, wx.ALL, 5 )

        self.copper_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.copper_total.Wrap( -1 )

        bSizer17.Add( self.copper_total, 0, wx.ALL, 5 )

        self.iron_label = wx.StaticText( self, wx.ID_ANY, _(u"Iron:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.iron_label.Wrap( -1 )

        bSizer17.Add( self.iron_label, 0, wx.ALL, 5 )

        self.iron_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.iron_total.Wrap( -1 )

        bSizer17.Add( self.iron_total, 0, wx.ALL, 5 )

        self.magnesium_label = wx.StaticText( self, wx.ID_ANY, _(u"Magnesium:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.magnesium_label.Wrap( -1 )

        bSizer17.Add( self.magnesium_label, 0, wx.ALL, 5 )

        self.magnesium_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.magnesium_total.Wrap( -1 )

        bSizer17.Add( self.magnesium_total, 0, wx.ALL, 5 )

        self.manganese_label = wx.StaticText( self, wx.ID_ANY, _(u"Manganese:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.manganese_label.Wrap( -1 )

        bSizer17.Add( self.manganese_label, 0, wx.ALL, 5 )

        self.manganese_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.manganese_total.Wrap( -1 )

        bSizer17.Add( self.manganese_total, 0, wx.ALL, 5 )

        self.phosphorus_label = wx.StaticText( self, wx.ID_ANY, _(u"Phosphorus:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.phosphorus_label.Wrap( -1 )

        bSizer17.Add( self.phosphorus_label, 0, wx.ALL, 5 )

        self.phosphorus_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.phosphorus_total.Wrap( -1 )

        bSizer17.Add( self.phosphorus_total, 0, wx.ALL, 5 )

        self.potassium_label = wx.StaticText( self, wx.ID_ANY, _(u"Potassium:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.potassium_label.Wrap( -1 )

        bSizer17.Add( self.potassium_label, 0, wx.ALL, 5 )

        self.potassium_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.potassium_total.Wrap( -1 )

        bSizer17.Add( self.potassium_total, 0, wx.ALL, 5 )


        bSizer13.Add( bSizer17, 0, wx.EXPAND, 5 )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

        self.selenium_label = wx.StaticText( self, wx.ID_ANY, _(u"Selenium:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.selenium_label.Wrap( -1 )

        bSizer18.Add( self.selenium_label, 0, wx.ALL, 5 )

        self.selenium_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.selenium_total.Wrap( -1 )

        bSizer18.Add( self.selenium_total, 0, wx.ALL, 5 )

        self.zinc_label = wx.StaticText( self, wx.ID_ANY, _(u"Zinc:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.zinc_label.Wrap( -1 )

        bSizer18.Add( self.zinc_label, 0, wx.ALL, 5 )

        self.zinc_total = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.zinc_total.Wrap( -1 )

        bSizer18.Add( self.zinc_total, 0, wx.ALL, 5 )


        bSizer13.Add( bSizer18, 0, wx.EXPAND, 5 )


        bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )


        bSizer9.Add( bSizer10, 0, wx.EXPAND, 5 )

        self.recipebuilder_added_items_list = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.recipebuilder_added_items_list.CreateGrid( 5, 36 )
        self.recipebuilder_added_items_list.EnableEditing( True )
        self.recipebuilder_added_items_list.EnableGridLines( True )
        self.recipebuilder_added_items_list.EnableDragGridSize( False )
        self.recipebuilder_added_items_list.SetMargins( 0, 0 )

        # Columns
        self.recipebuilder_added_items_list.EnableDragColMove( False )
        self.recipebuilder_added_items_list.EnableDragColSize( True )
        self.recipebuilder_added_items_list.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.recipebuilder_added_items_list.EnableDragRowSize( True )
        self.recipebuilder_added_items_list.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.recipebuilder_added_items_list.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer9.Add( self.recipebuilder_added_items_list, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()
        self.recipebuilder_popup_menu = wx.Menu()
        self.menu_change_amount = wx.MenuItem( self.recipebuilder_popup_menu, wx.ID_ANY, _(u"Change Food Amount"), wx.EmptyString, wx.ITEM_NORMAL )
        self.recipebuilder_popup_menu.Append( self.menu_change_amount )

        self.menu_remove_item = wx.MenuItem( self.recipebuilder_popup_menu, delete_recipe_item_ID, _(u"Remove Item"), wx.EmptyString, wx.ITEM_NORMAL )
        self.recipebuilder_popup_menu.Append( self.menu_remove_item )

        self.Bind( wx.EVT_RIGHT_DOWN, self.RecipeBuilderOnContextMenu )


        self.Centre( wx.BOTH )

        # Connect Events
        self.recipebuilder_save_button.Bind( wx.EVT_BUTTON, self.recipebuilder_save )
        self.recipebuilder_delete_button.Bind( wx.EVT_BUTTON, self.recipebuilder_delete )
        self.recipebuilder_added_items_list.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.cell_menu )
        self.Bind( wx.EVT_MENU, self.change_amount, id = self.menu_change_amount.GetId() )
        self.Bind( wx.EVT_MENU, self.remove_item, id = self.menu_remove_item.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def recipebuilder_save( self, event ):
        event.Skip()

    def recipebuilder_delete( self, event ):
        event.Skip()

    def cell_menu( self, event ):
        event.Skip()

    def change_amount( self, event ):
        event.Skip()

    def remove_item( self, event ):
        event.Skip()

    def RecipeBuilderOnContextMenu( self, event ):
        self.PopupMenu( self.recipebuilder_popup_menu, event.GetPosition() )


