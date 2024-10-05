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
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 537,250 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gSizer2 = wx.GridSizer( 4, 1, 0, 0 )

        wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Choose a nutrition:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        wSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

        m_choice1Choices = []
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        wSizer1.Add( self.m_choice1, 0, wx.ALL, 5 )


        gSizer2.Add( wSizer1, 1, wx.EXPAND, 5 )

        wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Range filter:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        wSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"Min:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        wSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        wSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"to"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        wSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Max:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        wSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        wSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )


        gSizer2.Add( wSizer2, 1, wx.EXPAND, 5 )

        wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Level filter:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        wSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, _(u"Low"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

        self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, _(u"Medium"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

        self.m_radioBtn3 = wx.RadioButton( self, wx.ID_ANY, _(u"High"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.m_radioBtn3, 0, wx.ALL, 5 )


        gSizer2.Add( wSizer3, 1, wx.EXPAND, 5 )

        wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.m_button4 = wx.Button( self, wx.ID_ANY, _(u"Clear Filters"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer4.Add( self.m_button4, 1, wx.ALL, 5 )


        wSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button5 = wx.Button( self, wx.ID_ANY, _(u"Apply Filters"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer4.Add( self.m_button5, 1, wx.ALL, 5 )


        gSizer2.Add( wSizer4, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


        self.SetSizer( gSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.onRadioLow )
        self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.onRadioMedium )
        self.m_radioBtn3.Bind( wx.EVT_RADIOBUTTON, self.onRadioHigh )
        self.m_button4.Bind( wx.EVT_BUTTON, self.clear_filters )
        self.m_button5.Bind( wx.EVT_BUTTON, self.apply_filters )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onRadioLow( self, event ):
        event.Skip()

    def onRadioMedium( self, event ):
        event.Skip()

    def onRadioHigh( self, event ):
        event.Skip()

    def clear_filters( self, event ):
        event.Skip()

    def apply_filters( self, event ):
        event.Skip()

