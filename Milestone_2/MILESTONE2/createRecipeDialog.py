# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class CreateRecipe
###########################################################################

class CreateRecipe ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Create Recipe"), pos = wx.DefaultPosition, size = wx.Size( 350,100 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.createrecipe_name_label = wx.StaticText( self, wx.ID_ANY, _(u"Recipe Name:"), wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.createrecipe_name_label.Wrap( -1 )

        bSizer8.Add( self.createrecipe_name_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.createrecipe_name_field = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.createrecipe_name_field, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.createrecipe_save_button = wx.Button( self, wx.ID_ANY, _(u"Save"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.createrecipe_save_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.SetSizer( bSizer8 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.createrecipe_save_button.Bind( wx.EVT_BUTTON, self.save_recipe )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def save_recipe( self, event ):
        event.Skip()


