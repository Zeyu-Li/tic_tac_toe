# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 206)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tic Tac Toe", pos = wx.DefaultPosition, size = wx.Size( 500,525 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		self.matrix = [[None,None,None],[None,None,None],[None,None,None]]

		gSizer2 = wx.GridSizer( 4, 3, 0, 0 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,90 ), 0 )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button1.SetFont( wx.Font( 28, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,90 ), 0 )
		self.m_button2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button2.SetFont( wx.Font( 28, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,90 ), 0 )
		self.m_button3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button3.SetFont( wx.Font( 28, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,90 ), 0 )
		self.m_button4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button4.SetFont( wx.Font( 28, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,90 ), 0 )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button5.SetFont( wx.Font( 28, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,90 ), 0 )
		self.m_button6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button6.SetFont( wx.Font( 28, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,90 ), 0 )
		self.m_button7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button7.SetFont( wx.Font( 28, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,90 ), 0 )
		self.m_button8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button8.SetFont( wx.Font( 28, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,90 ), 0 )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button9.SetFont( wx.Font( 28, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_button9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		# bottom
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Winner: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 20, 74, 90, 90, False, "Arial" ) )
		gSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_LEFT_DOWN, self.Cross1 )
		self.m_button1.Bind( wx.EVT_RIGHT_DOWN, self.Knots1 )
		self.m_button2.Bind( wx.EVT_LEFT_DOWN, self.Cross2 )
		self.m_button2.Bind( wx.EVT_RIGHT_DOWN, self.Knots2 )
		self.m_button3.Bind( wx.EVT_LEFT_DOWN, self.Cross3 )
		self.m_button3.Bind( wx.EVT_RIGHT_DOWN, self.Knots3 )
		self.m_button4.Bind( wx.EVT_LEFT_DOWN, self.Cross4 )
		self.m_button4.Bind( wx.EVT_RIGHT_DOWN, self.Knots4 )
		self.m_button5.Bind( wx.EVT_LEFT_DOWN, self.Cross5 )
		self.m_button5.Bind( wx.EVT_RIGHT_DOWN, self.Knots5 )
		self.m_button6.Bind( wx.EVT_LEFT_DOWN, self.Cross6 )
		self.m_button6.Bind( wx.EVT_RIGHT_DOWN, self.Knots6 )
		self.m_button7.Bind( wx.EVT_LEFT_DOWN, self.Cross7 )
		self.m_button7.Bind( wx.EVT_RIGHT_DOWN, self.Knots7 )
		self.m_button8.Bind( wx.EVT_LEFT_DOWN, self.Cross8 )
		self.m_button8.Bind( wx.EVT_RIGHT_DOWN, self.Knots8 )
		self.m_button9.Bind( wx.EVT_LEFT_DOWN, self.Cross9 )
		self.m_button9.Bind( wx.EVT_RIGHT_DOWN, self.Knots9 )
		self.m_button11.Bind( wx.EVT_BUTTON, self.reset )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Cross1( self, event ):
		self.m_button1.SetLabel("X")
		self.matrix[0][0] = 1
		self.test()
	def Knots1( self, event ):
		self.m_button1.SetLabel("O")
		self.matrix[0][0] = 0
		self.test()
	def Cross2( self, event ):
		self.m_button2.SetLabel("X")
		self.matrix[0][1] = 1
		self.test()
	def Knots2( self, event ):
		self.m_button2.SetLabel("O")
		self.matrix[0][1] = 0
		self.test()
	def Cross3( self, event ):
		self.m_button3.SetLabel("X")
		self.matrix[0][2] = 1
		self.test()
	def Knots3( self, event ):
		self.m_button3.SetLabel("O")
		self.matrix[0][2] = 0
		self.test()
	def Cross4( self, event ):
		self.m_button4.SetLabel("X")
		self.matrix[1][0] = 1
		self.test()
	def Knots4( self, event ):
		self.m_button4.SetLabel("O")
		self.matrix[1][0] = 0
		self.test()
	def Cross5( self, event ):
		self.m_button5.SetLabel("X")
		self.matrix[1][1] = 1
		self.test()
	def Knots5( self, event ):
		self.m_button5.SetLabel("O")
		self.matrix[1][1] = 0
		self.test()
	def Cross6( self, event ):
		self.m_button6.SetLabel("X")
		self.matrix[1][2] = 1
		self.test()
	def Knots6( self, event ):
		self.m_button6.SetLabel("O")
		self.matrix[1][2] = 0
		self.test()
	def Cross7( self, event ):
		self.m_button7.SetLabel("X")
		self.matrix[2][0] = 1
		self.test()
	def Knots7( self, event ):
		self.m_button7.SetLabel("O")
		self.matrix[2][0] = 0
		self.test()
	def Cross8( self, event ):
		self.m_button8.SetLabel("X")
		self.matrix[2][1] = 1
		self.test()
	def Knots8( self, event ):
		self.m_button8.SetLabel("O")
		self.matrix[2][1] = 0
		self.test()
	def Cross9( self, event ):
		self.m_button9.SetLabel("X")
		self.matrix[2][2] = 1
		self.test()
	def Knots9( self, event ):
		self.m_button9.SetLabel("O")
		self.matrix[2][2] = 0
		self.test()

	def reset(self, event):
		self.matrix = [[None,None,None],[None,None,None],[None,None,None]]
		self.m_button1.SetLabel("")
		self.m_button2.SetLabel("")
		self.m_button3.SetLabel("")
		self.m_button4.SetLabel("")
		self.m_button5.SetLabel("")
		self.m_button6.SetLabel("")
		self.m_button7.SetLabel("")
		self.m_button8.SetLabel("")
		self.m_button9.SetLabel("")
		self.m_staticText2.SetLabel("Winner: ")

	def test(self):

		# horizontal


		for i in range(3):
			hor = []
			hor.append(self.matrix[i][i])

			col = []

			# rows
			if(len(set(self.matrix[i]))==1) and self.matrix[i][0] != None and self.matrix[i][1] != None and self.matrix[i][2] != None:
				if self.matrix[i][i] == 1:
					self.m_staticText2.SetLabel("Winner: X")
				else: 
					self.m_staticText2.SetLabel("Winner: O")
			for j in range(3):

				col.append(self.matrix[j][i])
				if(len(set(col))==1) and self.matrix[0][j] != None and self.matrix[1][j] != None and self.matrix[2][j] != None:
					if col[0] == 1:
						self.m_staticText2.SetLabel("Winner: X")
					else: 
						self.m_staticText2.SetLabel("Winner: O")


		if(len(set(hor))==1) and self.matrix[0][0] != None and self.matrix[1][1] != None and self.matrix[2][2] != None:
			if self.matrix[0][0] == 1:
				self.m_staticText2.SetLabel("Winner: X")
			else: 
				self.m_staticText2.SetLabel("Winner: O")

		if(len(set([self.matrix[2][0], self.matrix[1][1], self.matrix[0][2]]))==1) and self.matrix[2][0] != None and self.matrix[1][1] != None and self.matrix[0][2] != None:
			if self.matrix[2][0] == 1:
				self.m_staticText2.SetLabel("Winner: X")
			else: 
				self.m_staticText2.SetLabel("Winner: O")

	def Cal( self, event ):
		event.Skip()


class MainApp(wx.App):
	def OnInit(self):
		mainFrame=MyFrame1(None)
		mainFrame.Show(True)
		return True
	

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

if __name__ == '__main__':
	app = MainApp()
	app.MainLoop()
