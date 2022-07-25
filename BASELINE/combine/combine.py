import numpy as np
import awkward as ak
import glob

# Combine all channel before drawing combined channel

data_list = ['WWZ','ZZ','ttbarZ']#,'ttbar']

def Load(proc_list):
	num1 = np.load(proc_list[0],allow_pickle=True)[()]
	num2 = np.load(proc_list[1],allow_pickle=True)[()]
	num3 = np.load(proc_list[2],allow_pickle=True)[()]
	num4 = np.load(proc_list[3],allow_pickle=True)[()]
	num5 = np.load(proc_list[4],allow_pickle=True)[()]

	process_list = [num1,num2,num3,num4,num5]
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
			
			dilep_mass = arrays['dilep_mass']
			wleps_mass = arrays['wleps_mass']

			MET_MET = arrays['MET_MET']
			MET_phi = arrays['MET_phi']
			MT2 = arrays['MT2']

			jet_pt = arrays['Jet_pt']
			jet_btag = arrays['Jet_btag']
	
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

				histo['dilep_mass'] = dilep_mass
				histo['wleps_mass'] = wleps_mass

				histo['MET_MET'] = MET_MET
				histo['MET_phi'] = MET_phi
				histo['MT2'] = MT2
	
				histo['jet_pt'] = jet_pt
				histo['jet_btag'] = jet_btag

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

				histo['dilep_mass'] = np.concatenate([histo['dilep_mass'], dilep_mass])
				histo['wleps_mass'] = np.concatenate([histo['wleps_mass'], wleps_mass])

				histo['MET_MET'] = np.concatenate([histo['MET_MET'], MET_MET])
				histo['MET_phi'] = np.concatenate([histo['MET_phi'], MET_phi])
				histo['MT2'] = np.concatenate([histo['MT2'], MT2])

				histo['jet_pt'] = np.concatenate([histo['jet_pt'], jet_pt])
				histo['jet_btag'] = np.concatenate([histo['jet_btag'], jet_btag])
		except KeyError:
			print("empty")
	return histo



WWZ = '/home/bjpark/WWZ/BASELINE/combine/data/WWZ/*.npy'
ZZ = '/home/bjpark/WWZ/BASELINE/combine/data/ZZ/*.npy'
ttbarZ = '/home/bjpark/WWZ/BASELINE/combine/data/ttbarZ/*.npy'
#ttbar = '/home/bjpark/WWZ/BASELINE/combine/data/ttbar/*.npy'

WWZ_proc_list = glob.glob(WWZ)
ZZ_proc_list = glob.glob(ZZ)
ttbarZ_proc_list = glob.glob(ttbarZ)
#ttbar_proc_list = glob.glob(ttbar)

WWZ_list = Load(WWZ_proc_list)
ZZ_list = Load(ZZ_proc_list)
ttbarZ_list = Load(ttbarZ_proc_list)
#ttbar_list = Load(ttbar_proc_list)

WWZ = Loop(WWZ_list)
ZZ = Loop(ZZ_list)
ttbarZ = Loop(ttbarZ_list)
#ttbar = Loop(ttbar_list)

print("Number of WWZ Events : {0}\n".format(len(WWZ['dilep_mass'])))
print("Number of ZZ Events : {0}\n".format(len(ZZ['dilep_mass'])))
print("Number of ttbarZ Events : {0}\n".format(len(ttbarZ['dilep_mass'])))
#print("Number of ttbar Events : {0}\n".format(len(ttbar['dilep_mass'])))

combine = {}
combine['WWZ'] = WWZ
combine['ZZ'] = ZZ
combine['ttbarZ'] = ttbarZ
#combine['ttbar'] = ttbar

outname = "combine.npy"
np.save('/home/bjpark/WWZ/DRAW/baseline/npy/{0}'.format(outname), combine)

print("END")

	
