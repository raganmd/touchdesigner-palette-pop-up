
class PaletteExplorer:
	def __init__(self, myop):
		self.MyOp = myop
		self.PaletteWindowCOMP = op('window_palette')
		pass

	def PaletteWindow(self, state):

		if state:
			self.PaletteWindowCOMP.par.winopen.pulse()

		else:
			self.PaletteWindowCOMP.par.winclose.pulse()

		pass