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

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Search:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        bSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, _(u"Select Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer2, 0, 0, 0 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

        self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid1.CreateGrid( 5, 5 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer1.Add( self.m_grid1, 0, wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button2.Bind( wx.EVT_BUTTON, self.open_filter_dialog )
        self.m_button3.Bind( wx.EVT_BUTTON, self.on_search )
        self.m_grid1.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_cell_click )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def open_filter_dialog( self, event ):
        event.Skip()

    def on_search( self, event ):
        event.Skip()

    def on_cell_click( self, event ):
        event.Skip()


