
class PaletteExplorer:
	def __init__(self, myop):
		self.MyOp 					= myop
		self.PaletteWindowCOMP 		= op('window_palette')
		self.SelectContainer 		= op('container_palette_widget/container_body/container_selected_palette')
		self.LastSelectedToxPath 	= tdu.Dependency(None)
		pass

	def PaletteWindow(self, state):

		if state:
			self.PaletteWindowCOMP.par.winopen.pulse()

		else:
			self.PaletteWindowCOMP.par.winclose.pulse()

		pass
	
	def FindToxToLoad(self, info):
		row 			= info.get('row')
		lister 			= info.get('ownerComp').parent(2)
		folderDAT 		= info.get('ownerComp').parent(3).op('folder1')
		folderRowIndex 	= (row+1) + ((lister.digits - 1) * self.SelectContainer.par.Numrows)

		TOXPath 		= folderDAT[ folderRowIndex, 'path']

		self.LastSelectedToxPath.val = TOXPath