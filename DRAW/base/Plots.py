import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep



class DistPlots:

	def __init__(self, weight, scale):

		self.blk = ['black','black','black','black','black','black','black','black','black']
		#self.color = ['midnightblue','darkslategrey','coral','g','c','orange','aqua','royalblue','gold']
		self.color = ['darkgray', 'powderblue','lightcoral','darkviolet', 'c', 'darkslateblue', 'orange', 'limegreen', 'royalblue']
		self.label = ['$t\overline{t}$','$Z\gamma$','Z','ZZZ','WZZ','WZ','tWZ','$t\overline{t}+Z$','ZZ']

		self.weight = weight
		self.scale = scale


	def PlotDist(self, stk_lepPT, WWZ_lepPT, ch, m, M, b, Xlabel, name):

		stk = []
		for i in range(len(stk_lepPT)):
			lepPT = stk_lepPT[i]
			stk.append(np.clip(lepPT, m, M))	# Stack on the first & last bin
		
		stk_lepPT = stk

		plt.figure(figsize=(8,8))
		plt.style.use(hep.style.CMS)
		bins = np.linspace(0,50,100)
		plt.hist(stk_lepPT, range=(m,M), bins=b, weights=self.weight, color=self.blk, histtype='step', linewidth=0.5, stacked=True)
		plt.hist(stk_lepPT, range=(m,M), bins=b, weights=self.weight, color=self.color, label=self.label, stacked=True)
		plt.hist(WWZ_lepPT, range=(m,M), bins=b, weights=self.scale, color='red', histtype='step', linewidth=2, label='WWZ')
		plt.title("3000 $fb^{-1}$ (14 TeV)", fontsize=13, loc='right')
		if ch == 'even':
			plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
		elif ch == 'odd':
			plt.title("($e\mu$ channel)", fontsize=13, loc='left')
		else:
			plt.title("(combined channel)", fontsize=13, loc='left')
		plt.xlim(m,M)
		plt.xticks(fontsize=16)
		plt.yticks(fontsize=16)
		plt.xlabel(""+Xlabel+ " [GeV]",fontsize=25, loc='right')
		plt.ylabel("Expected Events", fontsize=20, loc='top')
		plt.legend(fontsize=12, loc='upper right', ncol=2)
		plt.yscale('log')
		plt.savefig("" + name )
		#plt.show()
		plt.close()

		
	def Jet_BTag(self, stk_jet_btag, WWZ_jet_btag, color, label, ch):

		plt.figure(figsize=(8,8))
		plt.style.use(hep.style.CMS)
		bins = np.linspace(0,50,100)
		plt.hist(stk_jet_btag, range=(0,64), bins=64, color=self.blk, histtype='step', linewidth=0.5, stacked=True)
		plt.hist(stk_jet_btag, range=(0,64), bins=64, color=color, label=label, stacked=True)
		plt.hist(WWZ_jet_btag, range=(0,64), bins=64, color='red', histtype='step', linewidth=2, label='WWZ')
		plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
		if ch == 'even':
			plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
		elif ch == 'odd':
			plt.title("($e\mu$ channel)", fontsize=13, loc='left')
		else:
			plt.title("(chbined channel)", fontsize=13, loc='left')
		plt.xlim(0,64)
		plt.xticks(fontsize=16)
		plt.yticks(fontsize=16)
		plt.xlabel("BTag Score",fontsize=25, loc='right')
		plt.legend(fontsize=12, loc='upper right')
		plt.yscale('log')
		plt.savefig("Jet_btag")
		#plt.show()
		plt.close()
		
	
		

