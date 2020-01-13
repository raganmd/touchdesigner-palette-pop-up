
class PaletteExplorer:
	def __init__(self, myop):
		self.MyOp 					= myop
		self.PaletteWindowCOMP 		= op('window_palette')
		self.PlacementWindowCOMP 	= op('window_placement')
		self.SelectContainer 		= op('container_palette_widget/container_body/container_selected_palette')
		self.MouseClickDAT 			= op('chopexec_click')
	
		# last selected TOX info
		self.LastSelectedToxPath 	= tdu.Dependency(None)
		self.LastSelectedToxName 	= tdu.Dependency(None)
		pass

	def PaletteWindow(self, state):

		if state:
			self.PaletteWindowCOMP.par.winopen.pulse()
		else:
			self.PaletteWindowCOMP.par.winclose.pulse()

		pass

	def PlacementWindow(self, state):
		if state:
			self.PlacementWindowCOMP.par.winopen.pulse()
		else:
			self.PlacementWindowCOMP.par.winclose.pulse()

		pass
	
	def FindToxToLoad(self, info):
		row 			= info.get('row')
		TOXPath 	 	= None

		lister 			= info.get('ownerComp').parent(2)
		folderDAT 		= info.get('ownerComp').parent(3).op('folder1')
		folderRowIndex 	= (row+1) + ((lister.digits - 1) * self.SelectContainer.par.Numrows)
		TOXPath 		= folderDAT[ folderRowIndex, 'path']
		TOXName 		= folderDAT[ folderRowIndex, 'name']

		self.LastSelectedToxPath.val = TOXPath
		self.LastSelectedToxName.val = TOXName
		self.PaletteWindow(False)
		return

	def GetCurrentNetworkLocation(self):
		currentPane = ui.panes[ui.panes.current]
		networkPath = currentPane.owner
		return networkPath

	def GetCurrentPane(self):
		return ui.panes[ui.panes.current]

	def CreatePaletteTOX(self):
		networkPath = self.GetCurrentNetworkLocation()

		paletteTOX 		= op(networkPath).loadTox(self.LastSelectedToxPath.val)
		paletteTOX.name = "tempTOX"
		targetOp 		= paletteTOX.findChildren(type=COMP, depth=1)[0]
		
		# place template
		template 		= networkPath.copy(targetOp)
		template.nodeX 	= -1000
		template.nodeY 	= -1000
		# template.expose = False
		print(template)

		# destroy containing op
		paletteTOX.destroy()

		# Use TD's built in op placement toolkit
		self.GetCurrentPane().placeOPs([template])
		pass

	def PlacePaletteTox(self, info):
		self.FindToxToLoad(info)
		self.CreatePaletteTOX()
		
		pass