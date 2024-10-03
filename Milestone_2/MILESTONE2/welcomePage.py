# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gSizer1 = wx.GridSizer( 3, 1, 0, 0 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Data Explorer"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        gSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, _(u"This app allows you to explore and analyze a comprehensive dataset of food and nutrition information. You can:\n\nSearch for food items based on specific criteria.\nFilter nutrition data to discover foods that meet your dietary needs.\nVisualize and manage the nutrition breakdown of various food items.\nWhether you're tracking your diet, researching nutritional information, or just curious, this tool helps you access the data you need with ease.\n\nClick \"Get Started\" to begin exploring!"), wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        gSizer1.Add( self.m_richText1, 1, wx.EXPAND|wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, _(u"Get Started"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        self.SetSizer( gSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.on_get_started )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_get_started( self, event ):
        event.Skip()


