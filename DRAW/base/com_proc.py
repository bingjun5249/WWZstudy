import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import awkward as ak
import os
import math


ch_list = ['even','odd','total']

## Details
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
"ttbar" : 10000000,
}

xsecDict = {
"WWZ" : 0.0003051,
"ZZ" : 0.04655,
"ttbarZ" : 0.002151,
"WZZ" : 0.02864,
"ZZZ" : 0.009669,
"WZ" : 26.16,
"ZG" : 72.19,
"Z" : 44710,
"tWZ" : 0.09813,
"ttbar" : 40.288,
}
## Start drawing

 	
for ch in ch_list:
	os.chdir('/home/bjpark/WWZ/DRAW/baseline/png/newVari/'+ch+'/')

	# Data load
	infile = '/home/bjpark/WWZ/DRAW/baseline/npy/combine/proc/combine_'+ch+'.npy'

	load = np.load(infile,allow_pickle=True)[()]

	WWZ = load['WWZ']
	ZZ = load['ZZ']
	ttbarZ = load['ttbarZ']
	WZZ = load['WZZ']
	ZZZ = load['ZZZ']
	WZ = load['WZ']
	ZG = load['ZG']
	Z = load['Z']
	tWZ = load['tWZ']
	ttbar = load['ttbar']

	bkg_vari = ['fstlep_pt','fstlep_eta','sndlep_pt','sndlep_eta','trdlep_pt','trdlep_eta','frtlep_pt','frtlep_eta','fourlep_pt','fourlep_mass','dilep_mass','di_z1w1_mass','di_z1w2_mass','di_z2w1_mass','di_z2w2_mass','wleps_mass','tri_121_mass','tri_122_mass','tri_212_mass','MET_MET','MT2','Jet_pt','HT']

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

	if ch == 'even':
		print("-----> ee/mm channel")
	elif ch == 'odd':
		print("-----> em channel")
	else:
		print("-----> combined channel")

	# Number of events
	print("Number of events of WWZ : {0}".format(len(WWZ['fstlep_pt'])))
	print("Number of events of ZZ : {0}".format(len(ZZ['fstlep_pt'])))
	print("Number of events of ttbarZ : {0}".format(len(ttbarZ['fstlep_pt'])))
	print("Number of events of tWZ : {0}".format(len(tWZ['fstlep_pt'])))
	print("Number of events of WZZ : {0}".format(len(WZZ['fstlep_pt'])))
	print("Number of events of ZZZ : {0}".format(len(ZZZ['fstlep_pt'])))
	print("Number of events of WZ : {0}".format(len(WZ['fstlep_pt'])))
	print("Number of events of ZG : {0}".format(len(ZG['fstlep_pt'])))
	print("Number of events of Z : {0}".format(len(Z['fstlep_pt'])))
	print("Number of events of ttbar : {0}".format(len(ttbar['fstlep_pt'])))

	print("\n")

	# Normalize
	scales = {
		"WWZ" : np.ones(len(WWZ['fstlep_pt'])) * lumi * xsecDict["WWZ"] / EventDict["WWZ"],
		"ZZ" : np.ones(len(ZZ['fstlep_pt'])) * lumi * xsecDict["ZZ"] / EventDict["ZZ"],
		"ttbarZ" : np.ones(len(ttbarZ['fstlep_pt'])) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"],
		"WZZ" : np.ones(len(WZZ['fstlep_pt'])) * lumi * xsecDict["WZZ"] / EventDict["WZZ"],
		"ZZZ" : np.ones(len(ZZZ['fstlep_pt'])) * lumi * xsecDict["ZZZ"] / EventDict["ZZZ"],
		"WZ" : np.ones(len(WZ['fstlep_pt'])) * lumi * xsecDict["WZ"] / EventDict["WZ"],
		"ZG" : np.ones(len(ZG['fstlep_pt'])) * lumi * xsecDict["ZG"] / EventDict["ZG"],
		"Z" : np.ones(len(Z['fstlep_pt'])) * lumi * xsecDict["Z"] / EventDict["Z"],
		"tWZ" : np.ones(len(tWZ['fstlep_pt'])) * lumi * xsecDict["tWZ"] / EventDict["tWZ"],
		"ttbar" : np.ones(len(ttbar['fstlep_pt'])) * lumi * xsecDict["ttbar"] / EventDict["ttbar"],
	}


	# Expected Yield
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


	print("WWZ expected yield: {0}".format(Yield['WWZ']))
	print("ZZ expected yield: {0}".format(Yield['ZZ']))
	print("ttbarZ expected yield: {0}".format(Yield['ttbarZ']))
	print("tWZ expected yield: {0}".format(Yield['tWZ']))
	print("WZZ expected yield: {0}".format(Yield['WZZ']))
	print("ZZZ expected yield: {0}".format(Yield['ZZZ']))
	print("WZ expected yield: {0}".format(Yield['WZ']))
	print("ZG expected yield: {0}".format(Yield['ZG']))
	print("Z expected yield: {0}".format(Yield['Z']))
	print("ttbar expected yield: {0}".format(Yield['ttbar']))

	sig_yield = Yield['WWZ']
	back_yield = (Yield['ZZ']+Yield['ttbarZ']+Yield['tWZ']+Yield['WZZ']+Yield['ZZZ']+Yield['WZ']+Yield['ZG']+Yield['Z']+Yield['ttbar'])
	#	sig = math.sqrt(2 * (sig_yield + back_yield) * math.log(1 + (sig_yield / back_yield)) - sig_yield)
	sig = Yield['WWZ']/math.sqrt(Yield['ZZ']+Yield['ttbarZ']+Yield['tWZ']+Yield['WZZ']+Yield['ZZZ']+Yield['WZ']+Yield['ZG']+Yield['Z']+Yield['ttbar'])

	print("Expected Significance: {0}".format(sig))

	# stack
		

	def bkg_stack(variables, fn):
		bkg_list = []

		bkg_list.append(np.array(ttbar[''+variables[fn]], dtype=np.float64))
		bkg_list.append(np.array(ZG[''+variables[fn]], dtype=np.float64))
		bkg_list.append(np.array(Z[''+variables[fn]], dtype=np.float64))
		bkg_list.append(np.array(ZZZ[''+variables[fn]], dtype=np.float64))
		bkg_list.append(np.array(WZZ[''+variables[fn]], dtype=np.float64))
		bkg_list.append(np.array(WZ[''+variables[fn]], dtype=np.float64))
		bkg_list.append(np.array(tWZ[''+variables[fn]], dtype=np.float64))
		bkg_list.append(np.array(ttbarZ[''+variables[fn]], dtype=np.float64))
		bkg_list.append(np.array(ZZ[''+variables[fn]], dtype=np.float64))

		return bkg_list


	stk_fstlepPT = bkg_stack(bkg_vari, 0)
	stk_fstlepEta = bkg_stack(bkg_vari, 1)

	stk_sndlepPT = bkg_stack(bkg_vari, 2)
	stk_sndlepEta = bkg_stack(bkg_vari, 3)

	stk_trdlepPT = bkg_stack(bkg_vari, 4)
	stk_trdlepEta = bkg_stack(bkg_vari, 5)

	stk_frtlepPT = bkg_stack(bkg_vari, 6)
	stk_frtlepEta = bkg_stack(bkg_vari, 7)

	stk_fourlepPT = bkg_stack(bkg_vari, 8)
	stk_fourlep_mass = bkg_stack(bkg_vari, 9)

	stk_dilep_mass = bkg_stack(bkg_vari, 10)
	stk_di_z1w1_mass = bkg_stack(bkg_vari, 11)
	stk_di_z1w2_mass = bkg_stack(bkg_vari, 12)
	stk_di_z2w1_mass = bkg_stack(bkg_vari, 13)
	stk_di_z2w2_mass = bkg_stack(bkg_vari, 14)
	stk_wleps_mass = bkg_stack(bkg_vari, 15)

	stk_tri_121_mass = bkg_stack(bkg_vari, 16)
	stk_tri_122_mass = bkg_stack(bkg_vari, 17)
	stk_tri_212_mass = bkg_stack(bkg_vari, 18)

	stk_MET = bkg_stack(bkg_vari, 19)
	stk_MT2 = bkg_stack(bkg_vari, 20)

	stk_jet_pt = bkg_stack(bkg_vari, 21)
	#stk_jet_btag = bkg_stack(bkg_vari, 22)

	stk_HT = bkg_stack(bkg_vari, 22)
	

	#weight
	
	weight = [scales['ttbar'], scales['ZG'], scales['Z'], scales['ZZZ'], scales['WZZ'], scales['WZ'], scales['tWZ'], scales['ttbarZ'], scales['ZZ']]

	#WWZ['HT'] = np.array(WWZ['HT'], dtype=np.float64)
	print("\n\n")

	from Plots import DistPlots

	D = DistPlots(weight,scales['WWZ'])

	# D.PlotDist(stack_variable, WWZ['variable'], channel list, minimum, maximum, bins, x label, plot name)

	D.PlotDist(stk_fstlepPT, WWZ['fstlep_pt'], ch, 0, 500, 100, '$p^{Z1}_{T}$', '1stLep_PT')
	D.PlotDist(stk_sndlepPT, WWZ['sndlep_pt'], ch, 0, 500, 100, '$p^{Z2}_{T}$', '2ndLep_PT')
	D.PlotDist(stk_trdlepPT, WWZ['trdlep_pt'], ch, 0, 500, 100, '$p^{W1}_{T}$', '3rdLep_PT')
	D.PlotDist(stk_frtlepPT, WWZ['frtlep_pt'], ch, 0, 500, 100, '$p^{W2}_{T}$', '4thLep_PT')

	D.PlotDist(stk_fstlepEta, WWZ['fstlep_eta'], ch, -4, 4, 64, '$\eta^{Z1}$', '1stLep_Eta') 
	D.PlotDist(stk_sndlepEta, WWZ['sndlep_eta'], ch, -4, 4, 64, '$\eta^{Z2}$', '2ndLep_Eta') 
	D.PlotDist(stk_trdlepEta, WWZ['trdlep_eta'], ch, -4, 4, 64, '$\eta^{W1}$', '3rdLep_Eta') 
	D.PlotDist(stk_frtlepEta, WWZ['frtlep_eta'], ch, -4, 4, 64, '$\eta^{W2}$', '4thLep_Eta') 

	D.PlotDist(stk_dilep_mass, WWZ['dilep_mass'], ch, 71, 111, 40, '$M^{Z}_{ll}$', 'Z1Z2_mass')
	D.PlotDist(stk_di_z1w1_mass, WWZ['di_z1w1_mass'], ch, 0, 500, 100, '$M^{Z1W1}_{ll}$', 'Z1W1_mass')
	D.PlotDist(stk_di_z1w2_mass, WWZ['di_z1w2_mass'], ch, 0, 500, 100, '$M^{Z1W2}_{ll}$', 'Z1W2_mass')
	D.PlotDist(stk_di_z2w1_mass, WWZ['di_z2w1_mass'], ch, 0, 500, 100, '$M^{Z2W1}_{ll}$', 'Z2W1_mass')
	D.PlotDist(stk_di_z2w2_mass, WWZ['di_z2w2_mass'], ch, 0, 500, 100, '$M^{Z2W2}_{ll}$', 'Z2W2_mass')
	D.PlotDist(stk_wleps_mass, WWZ['wleps_mass'], ch, 0, 150, 50, '$M^{W}_{ll}$', 'W1W2_mass')

	D.PlotDist(stk_tri_121_mass, WWZ['tri_121_mass'], ch, 0, 500, 100, '$M^{121}_{lll}$', 'tri_121_mass')
	D.PlotDist(stk_tri_122_mass, WWZ['tri_122_mass'], ch, 0, 500, 100, '$M^{122}_{lll}$', 'tri_122_mass')
	D.PlotDist(stk_tri_212_mass, WWZ['tri_212_mass'], ch, 0, 500, 100, '$M^{212}_{lll}$', 'tri_212_mass')

	D.PlotDist(stk_fourlepPT, WWZ['fourlep_pt'], ch, 0, 300, 30, '$p^{4l}_{T}$', 'Fourlep_Pt')
	D.PlotDist(stk_fourlep_mass, WWZ['fourlep_mass'], ch, 0, 1500, 150, '$M_{4l}$', 'Fourlep_mass')

	D.PlotDist(stk_MET, WWZ['MET_MET'], ch, 0, 500, 50, 'MET', 'MET')
	D.PlotDist(stk_MT2, WWZ['MT2'], ch, 0, 100, 100, '$M_{T2}$', 'MT2')

	D.PlotDist(stk_jet_pt, WWZ['Jet_pt'], ch, 0, 1500, 30, 'Leading Jet $p_{T}$', 'Jet_pt')
	D.PlotDist(stk_HT, WWZ['HT'], ch, 0, 2000, 40, '$H_{T}$', 'HT')

