import awkward as ak
import numpy as np
import glob
from numba import jit
#from tqdm import tqdm
import time


ch_list = ['4e','3e1m','2e2m','1e3m','4m']
proc_list = ['WWZ','ZZ','ttbarZ','WZZ','ZZZ','WZ','ZG','Z','tWZ','ttbar']


## Data load

def Load(process):
	Original = np.load(process[0],allow_pickle=True)[()]

	process_list = [Original]
	return process_list

def Events(process, histo):

        for p in range(len(process)):
                if len(histo[p]) == 0:
                        print("Number of {0} Events : 0".format(process[p]))
                else:
                        print("Number of {0} Events : {1}".format(process[p], len(histo[p]['fstlep_pt'])))

## Variables

def Loop(file_list):

	# Define array
	histo = {}

	for arrays in file_list:
		if len(arrays) == 0: continue
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


			# Output histo
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



for channel in ch_list:

	# Data path
	WWZ = '/home/bjpark/WWZ/BASELINE/data/' + channel + '/WWZ/*.npy'
	ZZ = '/home/bjpark/WWZ/BASELINE/data/' + channel + '/ZZ_L/*.npy'
	ttbarZ = '/home/bjpark/WWZ/BASELINE/data/' + channel + '/ttbarZ/*.npy'
	WZZ = '/home/bjpark/WWZ/BASELINE/data/' + channel + '/WZZToinclusive/*.npy'
	ZZZ = '/home/bjpark/WWZ/BASELINE/data/' + channel + '/ZZZToinclusive/*.npy'
	WZ = '/home/bjpark/WWZ/BASELINE/data/' + channel + '/WZ/*.npy'
	ZG = '/home/bjpark/WWZ/BASELINE/data/' + channel + '/ZGToinclusive/*.npy'
	Z = '/home/bjpark/WWZ/BASELINE/data/' + channel + '/ZToallall/*.npy'
	tWZ = '/home/bjpark/WWZ/BASELINE/data/' + channel + '/tWZToinclusive/*.npy'
	ttbar = '/home/bjpark/WWZ/BASELINE/data/' + channel + '/ttbar/*.npy'

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


	# Data load & Make array
	WWZ_list = Load(WWZ_proc_list)
	ZZ_list = Load(ZZ_proc_list)
	ttbarZ_list = Load(ttbarZ_proc_list)
	WZZ_list = Load(WZZ_proc_list)
	ZZZ_list = Load(ZZZ_proc_list)
	WZ_list = Load(WZ_proc_list)
	ZG_list = Load(ZG_proc_list)
	Z_list = Load(Z_proc_list)
	tWZ_list = Load(tWZ_proc_list)
	ttbar_list = Load(ttbar_proc_list)


	# Variables

	WWZ = Loop(WWZ_list)
	ZZ = Loop(ZZ_list)
	ttbarZ = Loop(ttbarZ_list)
	WZZ = Loop(WZZ_list)
	ZZZ = Loop(ZZZ_list)
	WZ = Loop(WZ_list)
	ZG = Loop(ZG_list)
	Z = Loop(Z_list)
	tWZ = Loop(tWZ_list)
	ttbar = Loop(ttbar_list)

	histo = []

	histo.append(WWZ)
	histo.append(ZZ)
	histo.append(ttbarZ)
	histo.append(WZZ)
	histo.append(ZZZ)
	histo.append(WZ)
	histo.append(ZG)
	histo.append(Z)
	histo.append(tWZ)
	histo.append(ttbar)

	print("\n###" + channel + " channel###")
	Events(proc_list, histo)

	
	lep_ch ={}
	lep_ch['WWZ'] = WWZ
	lep_ch['ZZ'] = ZZ
	lep_ch['ttbarZ'] = ttbarZ
	lep_ch['WZZ'] = WZZ
	lep_ch['ZZZ'] = ZZZ
	lep_ch['WZ'] = WZ
	lep_ch['ZG'] = ZG
	lep_ch['Z'] = Z
	lep_ch['tWZ'] = tWZ
	lep_ch['ttbar'] = ttbar


	outname = "" + channel + "_channel.npy"
	np.save('/home/bjpark/WWZ/DRAW/baseline/npy/{0}/{1}'.format(channel,outname), lep_ch)


print("END")






