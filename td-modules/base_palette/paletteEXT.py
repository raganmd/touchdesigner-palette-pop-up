
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
		self.MouseClickDAT.par.active = True
		self.PlacementWindow(True)

		return TOXPath
	
	def GetCurrentNetworkLocation(self):
		currentPane = ui.panes[ui.panes.current]
		networkPath = currentPane.owner
		return networkPath

	def CreatePaletteTOX(self):
		self.MouseClickDAT.par.active = False
		self.PlacementWindow(False)
		networkPath = self.GetCurrentNetworkLocation()

		paletteTOX = op(networkPath).loadTox(self.LastSelectedToxPath.val)

		targetOp 	= paletteTOX.findChildren(type=COMP, depth=1)[0]
		copyOp 		= networkPath.copy(targetOp)
		copyOp.nodeX = 200

		paletteTOX.destroy()

		pass