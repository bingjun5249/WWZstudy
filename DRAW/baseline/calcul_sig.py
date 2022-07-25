import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import awkward as ak

import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--fn', type=int,default=1,help='--fn FUNCTION')
parser.add_argument('--minimum', type=int,default=100,help='--min GeV')
parser.add_argument('--maximum', type=int,default=110,help='--max GeV')
args = parser.parse_args()

mini = args.minimum
maxi = args.maximum
fn = args.fn

sig_list = []
idx_list = []

lumi = 3000000

EventDict = {
"WWZ" : 100000,
"ZZ" : 100000,
"ttbarZ" : 100000,
}

xsecDict = {
"WWZ" : 0.0003067,
"ZZ" : 0.04642,
"ttbarZ" : 0.002149,
}




def Calculate(fn):

	infile = '/home/bjpark/WWZ/DRAW/baseline/npy/combine.npy'

	load = np.load(infile,allow_pickle=True)[()]

	WWZ = load['WWZ']
	ZZ = load['ZZ']
	ttbarZ = load['ttbarZ']
	
	WWZ_MET = WWZ['MET_MET']
	ZZ_MET = ZZ['MET_MET']
	ttbarZ_MET = ttbarZ['MET_MET']
	
	WWZ_MT2 = WWZ['MT2']
	ZZ_MT2 = ZZ['MT2']
	ttbarZ_MT2 = ttbarZ['MT2']

	WWZ_wleps_mass = WWZ['wleps_mass']
	ZZ_wleps_mass = ZZ['wleps_mass']
	ttbarZ_wleps_mass = ttbarZ['wleps_mass']

	WWZ_dilep_mass = WWZ['dilep_mass']
	ZZ_dilep_mass = ZZ['dilep_mass']
	ttbarZ_dilep_mass = ttbarZ['dilep_mass']
	
		

	# MET
	if fn == 1:
		for i in range(mini, maxi+1):
	
			WWZ_mask = (WWZ_MET > i)
			ZZ_mask = (ZZ_MET > i)
			ttbarZ_mask = (ttbarZ_MET > i)
		
			WWZ_MET = WWZ_MET[WWZ_mask]
			ZZ_MET = ZZ_MET[ZZ_mask]
			ttbarZ_MET = ttbarZ_MET[ttbarZ_mask]
	
			# Calculate Significance
	
			num_sig = len(WWZ_MET) * lumi * xsecDict["WWZ"] / EventDict["WWZ"]
			num_bkg = (len(ZZ_MET) * lumi * xsecDict["ZZ"] / EventDict["ZZ"]) + (len(ttbarZ_MET) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"])
	
			significance = num_sig/math.sqrt(num_sig + num_bkg)
	
			sig_list.append(significance)
			idx_list.append(i)
		
			print("Significance over {0} GeV : {1}".format(i, significance))
	
	
		print("--------------------------")
		print("Maximum value : {0} GeV, {1}".format(idx_list[sig_list.index(max(sig_list))], max(sig_list)))
		print("--------------------------")
	
		plt.figure(figsize=(8,8))
		plt.style.use(hep.style.CMS)
		bins = np.linspace(0,50,100)
		plt.plot(idx_list, sig_list)
		plt.xlabel("$E^{miss}_{T}$ [GeV]", fontsize=20, loc='center')
		plt.ylabel("Expected Significance", fontsize=20, loc='center')
		plt.savefig("sig_MET")
		#plt.show()
		plt.close()
	
	elif fn == 2:
		print(len(WWZ_MT2))
		# MT2
	
		sig_list = []
		idx_list = []
	
		for i in range(mini, maxi+1):
	
			WWZ_mask = (WWZ_MT2 > i)
			ZZ_mask = (ZZ_MT2 > i)
			ttbarZ_mask = (ttbarZ_MT2 > i)
	
			WWZ_MT2 = WWZ_MT2[WWZ_mask]
			ZZ_MT2 = ZZ_MT2[ZZ_mask]
			ttbarZ_MT2 = ttbarZ_MT2[ttbarZ_mask]

			# Calculate Significance
		
			num_sig = len(WWZ_MT2) * lumi * xsecDict["WWZ"] / EventDict["WWZ"]
			num_bkg = (len(ZZ_MT2) * lumi * xsecDict["ZZ"] / EventDict["ZZ"]) + (len(ttbarZ_MT2) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"])
	
			significance = num_sig/math.sqrt(num_sig + num_bkg)
	
			sig_list.append(significance)
			idx_list.append(i)
			
			print("Significance over {0} GeV : {1}".format(i, significance))
	
	
		print("--------------------------")
		print("Maximum value : {0} GeV, {1}".format(idx_list[sig_list.index(max(sig_list))], max(sig_list)))
		print("--------------------------")
	
		plt.figure(figsize=(8,8))
		plt.style.use(hep.style.CMS)
		bins = np.linspace(0,50,100)
		plt.plot(idx_list, sig_list)
		plt.xlabel("$M_{T2}$ [GeV]", fontsize=20, loc='center')
		plt.ylabel("Expected Significance", fontsize=20, loc='center')
		plt.savefig("sig_MT2")
		#plt.show()
		plt.close()
		
	
	
	######
	
	elif fn == 3:
		# b tag score
	
		sig_list = []
		idx_list = []
	
		for i in range(mini, maxi+1):
	
			WWZ_jet_btag = WWZ['jet_btag']
			ZZ_jet_btag = ZZ['jet_btag']
			ttbarZ_jet_btag = ttbarZ['jet_btag']
	
			WWZ_mask = (WWZ_jet_btag <= i)
			ZZ_mask = (ZZ_jet_btag <= i)
			ttbarZ_mask = (ttbarZ_jet_btag <= i)
	
			WWZ_jet_btag = WWZ_jet_btag[WWZ_mask]
			ZZ_jet_btag = ZZ_jet_btag[ZZ_mask]
			ttbarZ_jet_btag = ttbarZ_jet_btag[ttbarZ_mask]
			
			# Calculate Significance
	
			num_sig = len(WWZ_jet_btag) * lumi * xsecDict["WWZ"] / EventDict["WWZ"]
			num_bkg = (len(ZZ_jet_btag) * lumi * xsecDict["ZZ"] / EventDict["ZZ"]) + (len(ttbarZ_jet_btag) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"])
	
			significance = num_sig/math.sqrt(num_sig + num_bkg)
	
			sig_list.append(significance)
			idx_list.append(i)
		
			print("Significance : score {0}, {1}".format(i, significance))
	
	
		print("--------------------------")
		print("Maximum value : score {0}, {1}".format(idx_list[sig_list.index(max(sig_list))], max(sig_list)))
		print("--------------------------")
	
		plt.figure(figsize=(8,8))
		plt.style.use(hep.style.CMS)
		bins = np.linspace(0,50,100)
		plt.plot(idx_list, sig_list)
		plt.xlabel("B Tag score", fontsize=20, loc='center')
		plt.ylabel("Expected Significance", fontsize=20, loc='center')
		plt.savefig("sig_btag")
		#plt.show()
		plt.close()
	
	
	######
	
	elif fn == 4:
		# Non-Z leptons invariant mass
		
		sig_list = []

		idx_list = []
		
		for i in range(mini, maxi+1):

			input_list = []
			
			idxrow_list = []

			if (91 - i) < 0:
				i = 91
	
			# lower cut
			WWZ_mask1 = (WWZ_wleps_mass <= 91-i)
			ZZ_mask1 = (ZZ_wleps_mass <= 91-i)
			ttbarZ_mask1 = (ttbarZ_wleps_mass <= 91-i)

			WWZ_wleps1 = WWZ_wleps_mass[WWZ_mask1]
			ZZ_wleps1 = ZZ_wleps_mass[ZZ_mask1]
			ttbarZ_wleps1 = ttbarZ_wleps_mass[ttbarZ_mask1]
		

			for j in range(mini, maxi+1):
			
				idxelem_list = []
		
				# upper cut	
				WWZ_mask2 = (WWZ_wleps_mass >= (91 + j))
				ZZ_mask2 = (ZZ_wleps_mass >= (91 + j))
				ttbarZ_mask2 = (ttbarZ_wleps_mass >= (91 + j))
		

				WWZ_wleps2 = WWZ_wleps_mass[WWZ_mask2]
				ZZ_wleps2 = ZZ_wleps_mass[ZZ_mask2]
				ttbarZ_wleps2 = ttbarZ_wleps_mass[ttbarZ_mask2]
		
				# Calculate Significance
			
				num_sig = (len(WWZ_wleps1)+len(WWZ_wleps2)) * lumi * xsecDict["WWZ"] / EventDict["WWZ"]
				num_bkg = ((len(ZZ_wleps1)+len(ZZ_wleps2)) * lumi * xsecDict["ZZ"] / EventDict["ZZ"]) + ((len(ttbarZ_wleps1)+len(ttbarZ_wleps2)) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"])
		
				significance = num_sig/math.sqrt(num_sig + num_bkg)
		
				input_list.append(significance)
				idxelem_list.append(i)
				idxelem_list.append(j)
				idxrow_list.append(idxelem_list)

			sig_list.append(input_list)
			idx_list.append(idxrow_list)
		
		maxsig = max(map(max, sig_list))
		newidx_list = ak.flatten(idx_list)
		target_idx = newidx_list[np.argmax(sig_list)]

		below_idx = target_idx[0]
		above_idx = target_idx[1]

		print("--------------------------")
		print("Maximum value at lower point {0} GeV, upper point {1} GeV: {2}".format(91 - below_idx, 91 + above_idx, maxsig))
		print("--------------------------")
	
		#plt.figure(figsize=(8,8))
		#plt.style.use(hep.style.CMS)
		bins = np.linspace(0,50,100)
		plt.matshow(sig_list, cmap='jet')
		plt.xlabel("Upper Z mass cut [GeV]", fontsize=10, loc='center')
		plt.ylabel("Lower Z mass cut [GeV]", fontsize=10, loc='center')
		cbar=plt.colorbar()#label='Significance')
		cbar.set_label('Significance',loc='center')
		plt.savefig("sig_nonZleps")
		plt.show()
		plt.close()


	elif fn == 5:
		# MET & MT2 significance	

		sig_list = []

		idx_list = []
		
		for i in range(mini, maxi+1):

			input_list = []
			
			idxrow_list = []

	
			WWZ_mask1 = (WWZ_MET >= i)
			ZZ_mask1 = (ZZ_MET >= i)
			ttbarZ_mask1 = (ttbarZ_MET >= i)

			WWZ_MET1 = WWZ_MET[WWZ_mask1]
			ZZ_MET1 = ZZ_MET[ZZ_mask1]
			ttbarZ_MET1 = ttbarZ_MET[ttbarZ_mask1]
		

			for j in range(mini, maxi+1):
				idxelem_list = []
		
				WWZ_mask2 = (WWZ_MT2 >= j)
				ZZ_mask2 = (ZZ_MT2 >= j)
				ttbarZ_mask2 = (ttbarZ_MT2 >= j)
		

				WWZ_MT21 = WWZ_MT2[WWZ_mask2]
				ZZ_MT21 = ZZ_MT2[ZZ_mask2]
				ttbarZ_MT21 = ttbarZ_MT2[ttbarZ_mask2]
		
				# Calculate Significance
			
				num_sig = (len(WWZ_MET1)+len(WWZ_MT21)) * lumi * xsecDict["WWZ"] / EventDict["WWZ"]
				num_bkg = ((len(ZZ_MET1)+len(ZZ_MT21)) * lumi * xsecDict["ZZ"] / EventDict["ZZ"]) + ((len(ttbarZ_MET1)+len(ttbarZ_MT21)) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"])
		
				significance = num_sig/math.sqrt(num_sig + num_bkg)

				input_list.append(significance)
				idxelem_list.append(i)
				idxelem_list.append(j)
				idxrow_list.append(idxelem_list)

			sig_list.append(input_list)
			idx_list.append(idxrow_list)
		
		maxsig = max(map(max, sig_list))
		newidx_list = ak.flatten(idx_list)
		target_idx = newidx_list[np.argmax(sig_list)]

		below_idx = target_idx[0]
		above_idx = target_idx[1]

		print("--------------------------")
		print("Maximum value at MET cut {0} GeV, MT2 cut {1} GeV: {2}".format(below_idx, above_idx, maxsig))
		print("--------------------------")
	
		#plt.figure(figsize=(8,8))
		#plt.style.use(hep.style.CMS)
		bins = np.linspace(0,50,100)
		plt.matshow(sig_list, cmap='jet')
		plt.xlabel("MT2 cut [GeV]", fontsize=10, loc='center')
		plt.ylabel("MET cut [GeV]", fontsize=10, loc='center')
		cbar=plt.colorbar()#label='Significance')
		cbar.set_label('Significance',loc='center')
		plt.savefig("sig_MET_MT2")
		plt.show()
		plt.close()


	elif fn == 6:
		# Di-lepton invariant mass
		
		sig_list = []

		idx_list = []
		
		for i in range(mini, maxi+1):

			input_list = []
			
			idxrow_list = []

			if (91 - i) < 0:
				i = 91
	
			# lower cut
			WWZ_mask1 = (WWZ_dilep_mass >= 91-i)
			ZZ_mask1 = (ZZ_dilep_mass >= 91-i)
			ttbarZ_mask1 = (ttbarZ_dilep_mass >= 91-i)

			WWZ_dilep1 = WWZ_dilep_mass[WWZ_mask1]
			ZZ_dilep1 = ZZ_dilep_mass[ZZ_mask1]
			ttbarZ_dilep1 = ttbarZ_dilep_mass[ttbarZ_mask1]
		

			for j in range(mini, maxi+1):
			
				idxelem_list = []
		
				# upper cut	
				WWZ_mask2 = (WWZ_dilep_mass <= (91 + j))
				ZZ_mask2 = (ZZ_dilep_mass <= (91 + j))
				ttbarZ_mask2 = (ttbarZ_dilep_mass <= (91 + j))
		

				WWZ_dilep2 = WWZ_dilep_mass[WWZ_mask2]
				ZZ_dilep2 = ZZ_dilep_mass[ZZ_mask2]
				ttbarZ_dilep2 = ttbarZ_dilep_mass[ttbarZ_mask2]
		
				# Calculate Significance
			
				num_sig = (len(WWZ_dilep1)+len(WWZ_dilep2)) * lumi * xsecDict["WWZ"] / EventDict["WWZ"]
				num_bkg = ((len(ZZ_dilep1)+len(ZZ_dilep2)) * lumi * xsecDict["ZZ"] / EventDict["ZZ"]) + ((len(ttbarZ_dilep1)+len(ttbarZ_dilep2)) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"])
		
				significance = num_sig/math.sqrt(num_sig + num_bkg)
		
				input_list.append(significance)
				idxelem_list.append(i)
				idxelem_list.append(j)
				idxrow_list.append(idxelem_list)

			sig_list.append(input_list)
			idx_list.append(idxrow_list)
		
		maxsig = max(map(max, sig_list))
		newidx_list = ak.flatten(idx_list)
		target_idx = newidx_list[np.argmax(sig_list)]

		below_idx = target_idx[0]
		above_idx = target_idx[1]

		print("--------------------------")
		print("Maximum significance at lower point {0} GeV, upper point {1} GeV: {2}".format(91 - below_idx, 91 + above_idx, maxsig))
		print("--------------------------")
	
		#plt.figure(figsize=(8,8))
		#plt.style.use(hep.style.CMS)
		bins = np.linspace(0,50,100)
		plt.matshow(sig_list, cmap='jet')
		plt.xlabel("Upper Z mass cut [GeV]", fontsize=10, loc='center')
		plt.ylabel("Lower Z mass cut [GeV]", fontsize=10, loc='center')
		cbar=plt.colorbar()#label='Significance')
		cbar.set_label('Significance',loc='center')
		plt.savefig("sig_Dilep")
		plt.show()
		plt.close()



Calculate(fn)
