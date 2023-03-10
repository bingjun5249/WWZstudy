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

lumi = 3000000

EventDict = {
"WWZ" : 10000000,
"ZZ" : 10000000,
"ttbarZ" : 10000000,
"WZZ" : 10100000,
"ZZZ" : 10100000,
"WZ" : 10000000,
"ZG" : 10100000,
"Z" : 10200000,
"tWZ" : 10100000,
"ttbar" : 10000000
}

xsecDict = {
"WWZ" : 0.002151,
"WZZ" : 0.02785,
"ZZZ" : 0.009669,
"WZ" : 26.16,
"ZG" : 72.19,
"Z" : 44870,
"tWZ" : 0.09813,
"ttbar" : 40.288,
"ZZ" : 0.04642,
"ttbarZ" : 0.002149,
}

#def denominator(
#num_bkg = ((len(ZZ_MET1)+len(ZZ_MT21)) * lumi * xsecDict["ZZ"] / EventDict["ZZ"]) + ((len(ttbarZ_MET1)+len(ttbarZ_MT21)) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"])


def Calculate(fn):

	infile = '/home/bjpark/WWZ/DRAW/baseline/npy/cut_archive/history/MET_HT_cut/combine_even.npy'

	load = np.load(infile,allow_pickle=True)[()]

	WWZ = load['WWZ']
	Z = load['Z']
	WZ = load['WZ']
	ZZ = load['ZZ']
	ZG = load['ZG']
	WZZ = load['WZZ']
	ZZZ = load['ZZZ']
	ttbar = load['ttbar']
	ttbarZ = load['ttbarZ']
	tWZ = load['tWZ']
	
	bkg_vari = ['fstlep_pt','fstlep_eta','sndlep_pt','sndlep_eta','trdlep_pt','trdlep_eta','frtlep_pt','frtlep_eta','fourlep_pt','fourlep_mass','dilep_mass','wleps_mass','MET_MET','MT2','jet_pt','jet_btag','HT']


	if len(WZZ) == 0:
		for i in range(len(bkg_vari)):
			WZZ[''+bkg_vari[i]] = []
	if len(ZZZ) == 0:
		for i in range(len(bkg_vari)):
			ZZZ[''+bkg_vari[i]] = []
	if len(WZ) == 0:
		for i in range(len(bkg_vari)):
			WZ[''+bkg_vari[i]] = []
	if len(ZG) == 0:
		for i in range(len(bkg_vari)):
			ZG[''+bkg_vari[i]] = []
	if len(Z) == 0:
		for i in range(len(bkg_vari)):
			Z[''+bkg_vari[i]] = []
	if len(ttbar) == 0:
		for i in range(len(bkg_vari)):
			ttbar[''+bkg_vari[i]] = []


	WWZ_MET = WWZ['MET_MET']
	Z_MET = Z['MET_MET']
	WZ_MET = WZ['MET_MET']
	ZZ_MET = ZZ['MET_MET']
	ZG_MET = ZG['MET_MET']
	WZZ_MET = WZZ['MET_MET']
	ZZZ_MET = ZZZ['MET_MET']
	ttbar_MET = ttbar['MET_MET']
	ttbarZ_MET = ttbarZ['MET_MET']
	tWZ_MET = tWZ['MET_MET']

	MET = [WWZ_MET,Z_MET,WZ_MET,ZZ_MET,ZG_MET,WZZ_MET,ZZZ_MET,ttbar_MET,ttbarZ_MET,tWZ_MET]

	
	WWZ_MT2 = WWZ['MT2']
	Z_MT2 = Z['MT2']
	WZ_MT2 = WZ['MT2']
	ZZ_MT2 = ZZ['MT2']
	ZG_MT2 = ZG['MT2']
	WZZ_MT2 = WZZ['MT2']
	ZZZ_MT2 = ZZZ['MT2']
	ttbar_MT2 = ttbar['MT2']
	ttbarZ_MT2 = ttbarZ['MT2']
	tWZ_MT2 = tWZ['MT2']

	MT2 = [WWZ_MT2,Z_MT2,WZ_MT2,ZZ_MT2,ZG_MT2,WZZ_MT2,ZZZ_MT2,ttbar_MT2,ttbarZ_MT2,tWZ_MT2]

	WWZ_pt4l = WWZ['fourlep_pt']
	Z_pt4l = Z['fourlep_pt']
	WZ_pt4l = WZ['fourlep_pt']
	ZZ_pt4l = ZZ['fourlep_pt']
	ZG_pt4l = ZG['fourlep_pt']
	WZZ_pt4l = WZZ['fourlep_pt']
	ZZZ_pt4l = ZZZ['fourlep_pt']
	ttbar_pt4l = ttbar['fourlep_pt']
	ttbarZ_pt4l = ttbarZ['fourlep_pt']
	tWZ_pt4l = tWZ['fourlep_pt']

	pt4l = [WWZ_pt4l,Z_pt4l,WZ_pt4l,ZZ_pt4l,ZG_pt4l,WZZ_pt4l,ZZZ_pt4l,ttbar_pt4l,ttbarZ_pt4l,tWZ_pt4l]

	WWZ_HT = WWZ['HT']
	Z_HT = Z['HT']
	WZ_HT = WZ['HT']
	ZZ_HT = ZZ['HT']
	ZG_HT = ZG['HT']
	WZZ_HT = WZZ['HT']
	ZZZ_HT = ZZZ['HT']
	ttbar_HT = ttbar['HT']
	ttbarZ_HT = ttbarZ['HT']
	tWZ_HT = tWZ['HT']

	HT = [WWZ_HT,Z_HT,WZ_HT,ZZ_HT,ZG_HT,WZZ_HT,ZZZ_HT,ttbar_HT,ttbarZ_HT,tWZ_HT]

	WWZ_dlm = WWZ['dilep_mass']
	Z_dlm = Z['dilep_mass']
	WZ_dlm = WZ['dilep_mass']
	ZZ_dlm = ZZ['dilep_mass']
	ZG_dlm = ZG['dilep_mass']
	WZZ_dlm = WZZ['dilep_mass']
	ZZZ_dlm = ZZZ['dilep_mass']
	ttbar_dlm = ttbar['dilep_mass']
	ttbarZ_dlm = ttbarZ['dilep_mass']
	tWZ_dlm = tWZ['dilep_mass']

	dlm = [WWZ_dlm,Z_dlm,WZ_dlm,ZZ_dlm,ZG_dlm,WZZ_dlm,ZZZ_dlm,ttbar_dlm,ttbarZ_dlm,tWZ_dlm]
	WWZ_wleps_mass = WWZ['wleps_mass']
	ZZ_wleps_mass = ZZ['wleps_mass']
	ttbarZ_wleps_mass = ttbarZ['wleps_mass']

	WWZ_dilep_mass = WWZ['dilep_mass']
	ZZ_dilep_mass = ZZ['dilep_mass']
	ttbarZ_dilep_mass = ttbarZ['dilep_mass']
	
	sig_list = []
	idx_list = []

		
	Yield = {
			"WWZ" : len(WWZ['fstlep_pt']) * lumi * xsecDict["WWZ"] / EventDict["WWZ"],
			"ZZ" : len(ZZ['fstlep_pt']) * lumi * xsecDict["ZZ"] / EventDict["ZZ"],
			"ttbarZ" : len(ttbarZ['fstlep_pt']) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"],
			"WZZ" : len(WZZ['fstlep_pt']) * lumi * xsecDict["WZZ"] / EventDict["WZZ"],
			"ZZZ" : len(ZZZ['fstlep_pt']) * lumi * xsecDict["ZZZ"] / EventDict["ZZZ"],
			"WZ" : len(WZ['fstlep_pt']) * lumi * xsecDict["WZ"] / EventDict["WZ"],
			"ZG" : len(ZG['fstlep_pt']) * lumi * xsecDict["ZG"] / EventDict["ZG"],
			"Z" : len(Z['fstlep_pt']) * lumi * xsecDict["Z"] / EventDict["Z"],
			"tWZ" : len(tWZ['fstlep_pt']) * lumi * xsecDict["tWZ"] / EventDict["tWZ"],
			"ttbar" : len(ttbar['fstlep_pt']) * lumi * xsecDict["ttbar"] / EventDict["ttbar"],

		}

	# MET
	if fn == 1:

		print("MET significance calculation")
		for i in range(mini, maxi+1):
	
			WWZ_mask = WWZ_MET > i
			ZZ_mask = ZZ_MET > i
			ttbarZ_mask = ttbarZ_MET > i
			#Z_mask = Z_MET > i
			WZ_mask = WZ_MET > i
			#ZG_mask = ZG_MET > i
			WZZ_mask = WZZ_MET > i
			ZZZ_mask = ZZZ_MET > i
			ttbar_mask = ttbar_MET > i
			tWZ_mask = tWZ_MET > i

			WWZ_MET = WWZ_MET[WWZ_mask]
			ZZ_MET = ZZ_MET[ZZ_mask]
			ttbarZ_MET = ttbarZ_MET[ttbarZ_mask]
			#Z_MET = Z_MET[Z_mask]
			WZ_MET = WZ_MET[WZ_mask]
			#ZG_MET = ZG_MET[ZG_mask]
			WZZ_MET = WZZ_MET[WZZ_mask]
			ZZZ_MET = ZZZ_MET[ZZZ_mask]
			ttbar_MET = ttbar_MET[ttbar_mask]
			tWZ_MET = tWZ_MET[tWZ_mask]
	
			Yield = {
					"WWZ" : len(WWZ_MET) * lumi * xsecDict["WWZ"] / EventDict["WWZ"],
					"ZZ" : len(ZZ_MET) * lumi * xsecDict["ZZ"] / EventDict["ZZ"],
					"ttbarZ" : len(ttbarZ_MET) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"],
					"WZZ" : len(WZZ_MET) * lumi * xsecDict["WZZ"] / EventDict["WZZ"],
					"ZZZ" : len(ZZZ_MET) * lumi * xsecDict["ZZZ"] / EventDict["ZZZ"],
					"WZ" : len(WZ_MET) * lumi * xsecDict["WZ"] / EventDict["WZ"],
					"ZG" : len(ZG_MET) * lumi * xsecDict["ZG"] / EventDict["ZG"],
					"Z" : len(Z_MET) * lumi * xsecDict["Z"] / EventDict["Z"],
					"tWZ" : len(tWZ_MET) * lumi * xsecDict["tWZ"] / EventDict["tWZ"],
					"ttbar" : len(ttbar_MET) * lumi * xsecDict["ttbar"] / EventDict["ttbar"]

			}

			# Calculate Significance

			num_sig = Yield['WWZ']
			num_bkg = Yield['ZZ']+Yield['Z']+Yield['WZ']+Yield['ZG']+Yield['WZZ']+Yield['ZZZ']+Yield['ttbar']+Yield['ttbarZ']+Yield['tWZ']
	
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
			WWZ_mask1 = (WWZ_dlm > 91-i)
			ZZ_mask1 = (ZZ_dlm > 91-i)
			ttbarZ_mask1 = (ttbarZ_dlm > 91-i)
#			Z_mask1 = (Z_dlm > 91-i)
			WZ_mask1 = (WZ_dlm > 91-i)
			ZG_mask1 = (ZG_dlm > 91-i)
			WZZ_mask1 = (WZZ_dlm > 91-i)
			ZZZ_mask1 = (ZZZ_dlm > 91-i)
			tWZ_mask1 = (tWZ_dlm > 91-i)
			ttbar_mask1 = (ttbar_dlm > 91-i)

			WWZ_dilep1 = WWZ_dlm[WWZ_mask1]
			ZZ_dilep1 = ZZ_dlm[ZZ_mask1]
			ttbarZ_dilep1 = ttbarZ_dlm[ttbarZ_mask1]
#			Z_dilep1 = Z_dlm[Z_mask1]
			WZ_dilep1 = WZ_dlm[WZ_mask1]
			ZG_dilep1 = ZG_dlm[ZG_mask1]
			WZZ_dilep1 = WZZ_dlm[WZZ_mask1]
			ZZZ_dilep1 = ZZZ_dlm[ZZZ_mask1]
			tWZ_dilep1 = tWZ_dlm[tWZ_mask1]
			ttbar_dilep1 = ttbar_dlm[ttbar_mask1]
		

			for j in range(mini, maxi+1):
			
				idxelem_list = []
		
				# upper cut	
				WWZ_mask2 = (WWZ_dilep1 < 91+j)
				ZZ_mask2 = (ZZ_dilep1 < 91+j)
				ttbarZ_mask2 = (ttbarZ_dilep1 < 91+j)
	#			Z_mask2 = (Z_dilep1 < 91+j)
				WZ_mask2 = (WZ_dilep1 < 91+j)
				ZG_mask2 = (ZG_dilep1 < 91+j)
				WZZ_mask2 = (WZZ_dilep1 < 91+j)
				ZZZ_mask2 = (ZZZ_dilep1 < 91+j)
				tWZ_mask2 = (tWZ_dilep1 < 91+j)
				ttbar_mask2 = (ttbar_dilep1 < 91+j)

				WWZ_dilep2 = WWZ_dilep1[WWZ_mask2]
				ZZ_dilep2 = ZZ_dilep1[ZZ_mask2]
				ttbarZ_dilep2 = ttbarZ_dilep1[ttbarZ_mask2]
	#			Z_dilep2 = Z_dilep1[Z_mask2]
				WZ_dilep2 = WZ_dilep1[WZ_mask2]
				ZG_dilep2 = ZG_dilep1[ZG_mask2]
				WZZ_dilep2 = WZZ_dilep1[WZZ_mask2]
				ZZZ_dilep2 = ZZZ_dilep1[ZZZ_mask2]
				tWZ_dilep2 = tWZ_dilep1[tWZ_mask2]
				ttbar_dilep2 = ttbar_dilep1[ttbar_mask2]

				Yield = {
						"WWZ" : len(WWZ_dilep2) * lumi * xsecDict["WWZ"] / EventDict["WWZ"],
						"ZZ" : len(ZZ_dilep2) * lumi * xsecDict["ZZ"] / EventDict["ZZ"],
						"ttbarZ" : len(ttbarZ_dilep2) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"],
						"WZ" : len(WZ_dilep2) * lumi * xsecDict["WZ"] / EventDict["WZ"],
				#		"Z" : len(Z_dilep2) * lumi * xsecDict["Z"] / EventDict["Z"],
						"ZG" : len(ZG_dilep2) * lumi * xsecDict["ZG"] / EventDict["ZG"],
						"WZZ" : len(WZZ_dilep2) * lumi * xsecDict["WZZ"] / EventDict["WZZ"],
						"ZZZ" : len(ZZZ_dilep2) * lumi * xsecDict["ZZZ"] / EventDict["ZZZ"],
						"ttbar" : len(ttbar_dilep2) * lumi * xsecDict["ttbar"] / EventDict["ttbar"],
						"tWZ" : len(tWZ_dilep2) * lumi * xsecDict["tWZ"] / EventDict["tWZ"],
				}
			
		
				# Calculate Significance
			
				num_sig = Yield['WWZ']
				num_bkg = Yield['ZZ']+Yield['WZ']+Yield['ZG']+Yield['WZZ']+Yield['ZZZ']+Yield['ttbar']+Yield['ttbarZ']+Yield['tWZ']
		
				significance = num_sig/math.sqrt(num_sig + num_bkg)
				print(significance)
		
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


	elif fn == 7:
		# MET & pt4l significance	

		sig_list = []

		idx_list = []
		
		for i in range(mini, maxi+1):

			input_list = []
			
			idxrow_list = []

			WWZ_mask = WWZ_MET > i
			ZZ_mask = ZZ_MET > i
			ttbarZ_mask = ttbarZ_MET > i
			#Z_mask = Z_MET > i
			WZ_mask = WZ_MET > i
			ZG_mask = ZG_MET > i
			WZZ_mask = WZZ_MET > i
			ZZZ_mask = ZZZ_MET > i
			ttbar_mask = ttbar_MET > i
			tWZ_mask = tWZ_MET > i

			WWZ_MET = WWZ_MET[WWZ_mask]
			ZZ_MET = ZZ_MET[ZZ_mask]
			ttbarZ_MET = ttbarZ_MET[ttbarZ_mask]
			#Z_MET = Z_MET[Z_mask]
			WZ_MET = WZ_MET[WZ_mask]
			ZG_MET = ZG_MET[ZG_mask]
			WZZ_MET = WZZ_MET[WZZ_mask]
			ZZZ_MET = ZZZ_MET[ZZZ_mask]
			ttbar_MET = ttbar_MET[ttbar_mask]
			tWZ_MET = tWZ_MET[tWZ_mask]
	

			for j in range(mini, maxi+1):
				idxelem_list = []
		
				WWZ_mask = WWZ_pt4l > j
				ZZ_mask = ZZ_pt4l > j
				ttbarZ_mask = ttbarZ_pt4l > j
				#Z_mask = Z_pt4l > j
				WZ_mask = WZ_pt4l > j
				ZG_mask = ZG_pt4l > j
				WZZ_mask = WZZ_pt4l > j
				ZZZ_mask = ZZZ_pt4l > j
				ttbar_mask = ttbar_pt4l > j
				tWZ_mask = tWZ_pt4l > j

				WWZ_pt4l = WWZ_pt4l[WWZ_mask]
				ZZ_pt4l = ZZ_pt4l[ZZ_mask]
				ttbarZ_pt4l = ttbarZ_pt4l[ttbarZ_mask]
				#Z_pt4l = Z_pt4l[Z_mask]
				WZ_pt4l = WZ_pt4l[WZ_mask]
				ZG_pt4l = ZG_pt4l[ZG_mask]
				WZZ_pt4l = WZZ_pt4l[WZZ_mask]
				ZZZ_pt4l = ZZZ_pt4l[ZZZ_mask]
				ttbar_pt4l = ttbar_pt4l[ttbar_mask]
				tWZ_pt4l = tWZ_pt4l[tWZ_mask]
	
		
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
		print("Maximum value at MET cut {0} GeV, pt4l cut {1} GeV: {2}".format(below_idx, above_idx, maxsig))
		print("--------------------------")
	
		#plt.figure(figsize=(8,8))
		#plt.style.use(hep.style.CMS)
		bins = np.linspace(0,50,100)
		plt.matshow(sig_list, cmap='jet')
		plt.xlabel("pt4l cut [GeV]", fontsize=10, loc='center')
		plt.ylabel("MET cut [GeV]", fontsize=10, loc='center')
		cbar=plt.colorbar()#label='Significance')
		cbar.set_label('Significance',loc='center')
		plt.savefig("sig_MET_pt4l")
		plt.show()
		plt.close()


	# fourlep_pt
	if fn == 8:

		print("pt_4l significance calculation")
		for i in range(mini, maxi+1):
	
			WWZ_mask = WWZ_pt4l > i
			ZZ_mask = ZZ_pt4l > i
			ttbarZ_mask = ttbarZ_pt4l > i
			#Z_mask = Z_pt4l > i
			WZ_mask = WZ_pt4l > i
			#ZG_mask = ZG_pt4l > i
			WZZ_mask = WZZ_pt4l > i
			ZZZ_mask = ZZZ_pt4l > i
			#ttbar_mask = ttbar_pt4l > i
			tWZ_mask = tWZ_pt4l > i

			WWZ_pt4l = WWZ_pt4l[WWZ_mask]
			ZZ_pt4l = ZZ_pt4l[ZZ_mask]
			ttbarZ_pt4l = ttbarZ_pt4l[ttbarZ_mask]
			#Z_pt4l = Z_pt4l[Z_mask]
			WZ_pt4l = WZ_pt4l[WZ_mask]
			#ZG_pt4l = ZG_pt4l[ZG_mask]
			WZZ_pt4l = WZZ_pt4l[WZZ_mask]
			ZZZ_pt4l = ZZZ_pt4l[ZZZ_mask]
			#ttbar_pt4l = ttbar_pt4l[ttbar_mask]
			tWZ_pt4l = tWZ_pt4l[tWZ_mask]
	
			Yield = {
					"WWZ" : len(WWZ_pt4l) * lumi * xsecDict["WWZ"] / EventDict["WWZ"],
					"ZZ" : len(ZZ_pt4l) * lumi * xsecDict["ZZ"] / EventDict["ZZ"],
					"ttbarZ" : len(ttbarZ_pt4l) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"],
					"WZZ" : len(WZZ_pt4l) * lumi * xsecDict["WZZ"] / EventDict["WZZ"],
					"ZZZ" : len(ZZZ_pt4l) * lumi * xsecDict["ZZZ"] / EventDict["ZZZ"],
					"WZ" : len(WZ_pt4l) * lumi * xsecDict["WZ"] / EventDict["WZ"],
					"ZG" : len(ZG_pt4l) * lumi * xsecDict["ZG"] / EventDict["ZG"],
					"Z" : len(Z_pt4l) * lumi * xsecDict["Z"] / EventDict["Z"],
					"tWZ" : len(tWZ_pt4l) * lumi * xsecDict["tWZ"] / EventDict["tWZ"],
					"ttbar" : len(ttbar_pt4l) * lumi * xsecDict["ttbar"] / EventDict["ttbar"]

			}

			# Calculate Significance

			num_sig = Yield['WWZ']
			num_bkg = Yield['ZZ']+Yield['Z']+Yield['WZ']+Yield['ZG']+Yield['WZZ']+Yield['ZZZ']+Yield['ttbar']+Yield['ttbarZ']+Yield['tWZ']
	
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
		plt.savefig("sig_pt4l")
		#plt.show()
		plt.close()
	
	if fn == 9:

		print("H_T significance calculation")
		for i in range(mini, maxi+1):
	
			WWZ_mask = WWZ_HT > i
			ZZ_mask = ZZ_HT > i
			ttbarZ_mask = ttbarZ_HT > i
			#Z_mask = Z_HT > i
			WZ_mask = WZ_HT > i
			#ZG_mask = ZG_HT > i
			WZZ_mask = WZZ_HT > i
			ZZZ_mask = ZZZ_HT > i
			ttbar_mask = ttbar_HT > i
			tWZ_mask = tWZ_HT > i

			WWZ_HT = WWZ_HT[WWZ_mask]
			ZZ_HT = ZZ_HT[ZZ_mask]
			ttbarZ_HT = ttbarZ_HT[ttbarZ_mask]
			#Z_HT = Z_HT[Z_mask]
			WZ_HT = WZ_HT[WZ_mask]
			#ZG_HT = ZG_HT[ZG_mask]
			WZZ_HT = WZZ_HT[WZZ_mask]
			ZZZ_HT = ZZZ_HT[ZZZ_mask]
			ttbar_HT = ttbar_HT[ttbar_mask]
			tWZ_HT = tWZ_HT[tWZ_mask]
	
			Yield = {
					"WWZ" : len(WWZ_HT) * lumi * xsecDict["WWZ"] / EventDict["WWZ"],
					"ZZ" : len(ZZ_HT) * lumi * xsecDict["ZZ"] / EventDict["ZZ"],
					"ttbarZ" : len(ttbarZ_HT) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"],
					"WZZ" : len(WZZ_HT) * lumi * xsecDict["WZZ"] / EventDict["WZZ"],
					"ZZZ" : len(ZZZ_HT) * lumi * xsecDict["ZZZ"] / EventDict["ZZZ"],
					"WZ" : len(WZ_HT) * lumi * xsecDict["WZ"] / EventDict["WZ"],
					"ZG" : len(ZG_HT) * lumi * xsecDict["ZG"] / EventDict["ZG"],
					"Z" : len(Z_HT) * lumi * xsecDict["Z"] / EventDict["Z"],
					"tWZ" : len(tWZ_HT) * lumi * xsecDict["tWZ"] / EventDict["tWZ"],
					"ttbar" : len(ttbar_HT) * lumi * xsecDict["ttbar"] / EventDict["ttbar"]

			}

			# Calculate Significance

			num_sig = Yield['WWZ']
			num_bkg = Yield['ZZ']+Yield['Z']+Yield['WZ']+Yield['ZG']+Yield['WZZ']+Yield['ZZZ']+Yield['ttbar']+Yield['ttbarZ']+Yield['tWZ']
	
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
		plt.xlabel("$H_{T}$ [GeV]", fontsize=20, loc='center')
		plt.ylabel("Expected Significance", fontsize=20, loc='center')
		plt.savefig("sig_HT")
		#plt.show()
		plt.close()

Calculate(fn)
