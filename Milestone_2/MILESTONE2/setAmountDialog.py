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
## Class change_amount
###########################################################################

class change_amount ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Set Servings"), pos = wx.DefaultPosition, size = wx.Size( 298,85 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

        self.set_amount_label = wx.StaticText( self, wx.ID_ANY, _(u"Set Amount:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.set_amount_label.Wrap( -1 )

        bSizer22.Add( self.set_amount_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.set_amount_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.set_amount_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.set_amount_save = wx.Button( self, wx.ID_ANY, _(u"Save"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.set_amount_save, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.SetSizer( bSizer22 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.set_amount_save.Bind( wx.EVT_BUTTON, self.amount_save )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def amount_save( self, event ):
        event.Skip()


