import numpy as np
import awkward as ak
import glob

# Combine all channel before drawing combined channel

com_list = ['even','odd']
channel_list = ['4e','3e1m','2e2m','1e3m','4m']
data_list = ['WWZ','ZZ','ttbarZ','WZZ','ZZZ','WZ','ZG','Z','ttbar','tWZ']

def Load_even(proc_list):
	First = np.load(proc_list[0],allow_pickle=True)[()]
	Second = np.load(proc_list[1],allow_pickle=True)[()]
	Third = np.load(proc_list[2],allow_pickle=True)[()]

	process_list = [First, Second, Third]
	return process_list

def Load_odd(proc_list):
	First = np.load(proc_list[0],allow_pickle=True)[()]
	Second = np.load(proc_list[1],allow_pickle=True)[()]

	process_list = [First, Second]
	return process_list

def Loop(file_list):

	histo = {}

	for arrays in file_list:
		try:
			fstlep_pt = arrays['fstlep_pt']
			fstlep_eta = arrays['fstlep_eta']
			fstlep_phi = arrays['fstlep_phi']

			sndlep_pt = arrays['sndlep_pt']
			sndlep_eta = arrays['sndlep_eta']
			sndlep_phi = arrays['sndlep_phi']

			trdlep_pt = arrays['trdlep_pt']
			trdlep_eta = arrays['trdlep_eta']
			trdlep_phi = arrays['trdlep_phi']

			frtlep_pt = arrays['frtlep_pt']
			frtlep_eta = arrays['frtlep_eta']
			frtlep_phi = arrays['frtlep_phi']

			fourlep_pt = arrays['fourlep_pt']
			fourlep_mass = arrays['fourlep_mass']
			
			dilep_mass = arrays['dilep_mass']
			wleps_mass = arrays['wleps_mass']

			MET_MET = arrays['MET_MET']
			MET_phi = arrays['MET_phi']
			MT2 = arrays['MT2']

			jet_pt = arrays['Jet_pt']
			jet_btag = arrays['Jet_btag']

			HT = arrays['HT']
	
			if len(histo) == 0:
				histo['fstlep_pt'] = fstlep_pt
				histo['fstlep_eta'] = fstlep_eta
				histo['fstlep_phi'] = fstlep_phi

				histo['sndlep_pt'] = sndlep_pt
				histo['sndlep_eta'] = sndlep_eta
				histo['sndlep_phi'] = sndlep_phi

				histo['trdlep_pt'] = trdlep_pt
				histo['trdlep_eta'] = trdlep_eta
				histo['trdlep_phi'] = trdlep_phi

				histo['frtlep_pt'] = frtlep_pt
				histo['frtlep_eta'] = frtlep_eta
				histo['frtlep_phi'] = frtlep_phi

				histo['fourlep_pt'] = fourlep_pt
				histo['fourlep_mass'] = fourlep_mass

				histo['dilep_mass'] = dilep_mass
				histo['wleps_mass'] = wleps_mass

				histo['MET_MET'] = MET_MET
				histo['MET_phi'] = MET_phi
				histo['MT2'] = MT2
	
				histo['jet_pt'] = jet_pt
				histo['jet_btag'] = jet_btag

				histo['HT'] = HT

			else:
				histo['fstlep_pt'] = np.concatenate([histo['fstlep_pt'], fstlep_pt])
				histo['fstlep_eta'] = np.concatenate([histo['fstlep_eta'], fstlep_eta])
				histo['fstlep_phi'] = np.concatenate([histo['fstlep_phi'], fstlep_phi])

				histo['sndlep_pt'] = np.concatenate([histo['sndlep_pt'], sndlep_pt])
				histo['sndlep_eta'] = np.concatenate([histo['sndlep_eta'], sndlep_eta])
				histo['sndlep_phi'] = np.concatenate([histo['sndlep_phi'], sndlep_phi])

				histo['trdlep_pt'] = np.concatenate([histo['trdlep_pt'], trdlep_pt])
				histo['trdlep_eta'] = np.concatenate([histo['trdlep_eta'], trdlep_eta])
				histo['trdlep_phi'] = np.concatenate([histo['trdlep_phi'], trdlep_phi])

				histo['frtlep_pt'] = np.concatenate([histo['frtlep_pt'], frtlep_pt])
				histo['frtlep_eta'] = np.concatenate([histo['frtlep_eta'], frtlep_eta])
				histo['frtlep_phi'] = np.concatenate([histo['frtlep_phi'], frtlep_phi])

				histo['fourlep_pt'] = np.concatenate([histo['fourlep_pt'], fourlep_pt])
				histo['fourlep_mass'] = np.concatenate([histo['fourlep_mass'], fourlep_mass])

				histo['dilep_mass'] = np.concatenate([histo['dilep_mass'], dilep_mass])
				histo['wleps_mass'] = np.concatenate([histo['wleps_mass'], wleps_mass])

				histo['MET_MET'] = np.concatenate([histo['MET_MET'], MET_MET])
				histo['MET_phi'] = np.concatenate([histo['MET_phi'], MET_phi])
				histo['MT2'] = np.concatenate([histo['MT2'], MT2])

				histo['jet_pt'] = np.concatenate([histo['jet_pt'], jet_pt])
				histo['jet_btag'] = np.concatenate([histo['jet_btag'], jet_btag])

				histo['HT'] = np.concatenate([histo['HT'], HT])
		except KeyError:
			print("empty")

	return histo

def Events(process, histo):

	for p in range(len(process)):
		if len(histo[p]) == 0:
			print("Number of {0} Events : 0".format(process[p]))
		else:
			print("Number of {0} Events : {1}".format(process[p], len(histo[p]['dilep_mass'])))

for com in com_list:

	WWZ = '/home/bjpark/WWZ/BASELINE/combine/data/WWZ/'+com+'/*.npy'
	ZZ = '/home/bjpark/WWZ/BASELINE/combine/data/ZZ/'+com+'/*.npy'
	ttbarZ = '/home/bjpark/WWZ/BASELINE/combine/data/ttbarZ/'+com+'/*.npy'
	tWZ = '/home/bjpark/WWZ/BASELINE/combine/data/tWZ/'+com+'/*.npy'
	Z = '/home/bjpark/WWZ/BASELINE/combine/data/Z/'+com+'/*.npy'
	ZG = '/home/bjpark/WWZ/BASELINE/combine/data/ZG/'+com+'/*.npy'
	WZ = '/home/bjpark/WWZ/BASELINE/combine/data/WZ/'+com+'/*.npy'
	WZZ = '/home/bjpark/WWZ/BASELINE/combine/data/WZZ/'+com+'/*.npy'
	ZZZ = '/home/bjpark/WWZ/BASELINE/combine/data/ZZZ/'+com+'/*.npy'
	ttbar = '/home/bjpark/WWZ/BASELINE/combine/data/ttbar/'+com+'/*.npy'


	WWZ_proc_list = glob.glob(WWZ)
	ZZ_proc_list = glob.glob(ZZ)
	ttbarZ_proc_list = glob.glob(ttbarZ)
	WZZ_proc_list = glob.glob(WZZ)
	ZZZ_proc_list = glob.glob(ZZZ)
	WZ_proc_list = glob.glob(WZ)
	ZG_proc_list = glob.glob(ZG)
	Z_proc_list = glob.glob(Z)
	tWZ_proc_list = glob.glob(tWZ)
	ttbar_proc_list = glob.glob(ttbar)

	if com == 'even':
		WWZ_list = Load_even(WWZ_proc_list)
		ZZ_list = Load_even(ZZ_proc_list)
		ttbarZ_list = Load_even(ttbarZ_proc_list)
		WZZ_list = Load_even(WZZ_proc_list)
		ZZZ_list = Load_even(ZZZ_proc_list)
		WZ_list = Load_even(WZ_proc_list)
		ZG_list = Load_even(ZG_proc_list)
		Z_list = Load_even(Z_proc_list)
		tWZ_list = Load_even(tWZ_proc_list)
		ttbar_list = Load_even(ttbar_proc_list)
	else:
		WWZ_list = Load_odd(WWZ_proc_list)
		ZZ_list = Load_odd(ZZ_proc_list)
		ttbarZ_list = Load_odd(ttbarZ_proc_list)
		WZZ_list = Load_odd(WZZ_proc_list)
		ZZZ_list = Load_odd(ZZZ_proc_list)
		WZ_list = Load_odd(WZ_proc_list)
		ZG_list = Load_odd(ZG_proc_list)
		Z_list = Load_odd(Z_proc_list)
		tWZ_list = Load_odd(tWZ_proc_list)
		ttbar_list = Load_odd(ttbar_proc_list)
	histo = []


	WWZ = Loop(WWZ_list)
	histo.append(WWZ)
	ZZ = Loop(ZZ_list)
	histo.append(ZZ)
	ttbarZ = Loop(ttbarZ_list)
	histo.append(ttbarZ)
	WZZ = Loop(WZZ_list)
	histo.append(WZZ)
	ZZZ = Loop(ZZZ_list)
	histo.append(ZZZ)
	WZ = Loop(WZ_list)
	histo.append(WZ)
	ZG = Loop(ZG_list)
	histo.append(ZG)
	Z = Loop(Z_list)
	histo.append(Z)
	ttbar = Loop(ttbar_list)
	histo.append(ttbar)
	tWZ = Loop(tWZ_list)
	histo.append(tWZ)

	Events(data_list, histo)
	'''
	print("Number of ZZ Events : {0}\n".format(len(ZZ['dilep_mass'])))
	print("Number of ttbarZ Events : {0}\n".format(len(ttbarZ['dilep_mass'])))
	print("Number of WZZ Events : {0}\n".format(len(WZZ['dilep_mass'])))
	print("Number of ZZZ Events : {0}\n".format(len(ZZZ['dilep_mass'])))
	print("Number of WZ Events : {0}\n".format(len(WZ['dilep_mass'])))
	print("Number of ZG Events : {0}\n".format(len(ZG['dilep_mass'])))
	print("Number of Z Events : {0}\n".format(len(Z['dilep_mass'])))
	print("Number of tWZ Events : {0}\n".format(len(tWZ['dilep_mass'])))
	print("Number of ttbar Events : {0}\n".format(len(ttbar['dilep_mass'])))

	'''
	combine = {}
	combine['WWZ'] = WWZ
	combine['ZZ'] = ZZ
	combine['ttbarZ'] = ttbarZ
	combine['WZZ'] = WZZ
	combine['ZZZ'] = ZZZ
	combine['WZ'] = WZ
	combine['ZG'] = ZG
	combine['Z'] = Z
	combine['ttbar'] = ttbar
	combine['tWZ'] = tWZ

	outname = "combine_"+com+".npy"
	np.save('/home/bjpark/WWZ/DRAW/baseline/npy/combine/{0}'.format(outname), combine)

print("END")

	
