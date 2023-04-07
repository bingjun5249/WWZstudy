import numpy as np
import awkward as ak
import glob

# Combine all channel before drawing combined channel

com_list = ['even','odd']
channel_list = ['4e','3e1m','2e2m','1e3m','4m']
proc_list = ['WWZ','ZZ','ttbarZ','WZZ','ZZZ','WZ','ZG','Z','ttbar','tWZ']
data_list = ['Fist', 'Second', 'Third','Fourth','Fifth','Sixth','Seventh','Eighth','Nineth','Tenth']


def Load(proc_list):
	First = np.load(proc_list[0],allow_pickle=True)[()]
	Second = np.load(proc_list[1],allow_pickle=True)[()]
	Third = np.load(proc_list[2],allow_pickle=True)[()]
	Fourth = np.load(proc_list[3],allow_pickle=True)[()]
	Fifth = np.load(proc_list[4],allow_pickle=True)[()]
	Sixth = np.load(proc_list[5],allow_pickle=True)[()]
	Seventh = np.load(proc_list[6],allow_pickle=True)[()]
	Eighth = np.load(proc_list[7],allow_pickle=True)[()]
	Nineth = np.load(proc_list[8],allow_pickle=True)[()]
	Tenth = np.load(proc_list[9],allow_pickle=True)[()]


	process_list = [First, Second, Third, Fourth, Fifth,Sixth,Seventh,Eighth,Nineth,Tenth]
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
			di_z1w1_mass = arrays['di_z1w1_mass']
			di_z1w2_mass = arrays['di_z1w2_mass']
			di_z2w1_mass = arrays['di_z2w1_mass']
			di_z2w2_mass = arrays['di_z2w2_mass']
			wleps_mass = arrays['wleps_mass']

			tri_121_mass = arrays['tri_121_mass']
			tri_122_mass = arrays['tri_122_mass']
			tri_212_mass = arrays['tri_211_mass']
			
			fourlep_pt = arrays['fourlep_pt']
			fourlep_mass = arrays['fourlep_mass']

			MET_MET = arrays['MET_MET']
			MET_phi = arrays['MET_phi']
			MT2 = arrays['MT2']
			HT = arrays['HT']

			jet_pt = arrays['Jet_pt']
			jet_btag = arrays['Jet_btag']

			Channel_info = arrays['Channel']
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
				histo['di_z1w1_mass'] = di_z1w1_mass
				histo['di_z1w2_mass'] = di_z1w2_mass
				histo['di_z2w1_mass'] = di_z2w1_mass
				histo['di_z2w2_mass'] = di_z2w2_mass
				histo['wleps_mass'] = wleps_mass

				histo['tri_121_mass'] = tri_121_mass
				histo['tri_122_mass'] = tri_122_mass
				histo['tri_212_mass'] = tri_212_mass

				histo['fourlep_pt'] = fourlep_pt
				histo['fourlep_mass'] = fourlep_mass

				histo['MET_MET'] = MET_MET
				histo['MET_phi'] = MET_phi
				histo['MT2'] = MT2
				histo['HT'] = HT
	
				histo['Jet_pt'] = jet_pt
				histo['Jet_btag'] = jet_btag

				histo['Channel'] = Channel_info

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
				histo['di_z1w1_mass'] = np.concatenate([histo['di_z1w1_mass'], di_z1w1_mass])
				histo['di_z1w2_mass'] = np.concatenate([histo['di_z1w2_mass'], di_z1w2_mass])
				histo['di_z2w1_mass'] = np.concatenate([histo['di_z2w1_mass'], di_z2w1_mass])
				histo['di_z2w2_mass'] = np.concatenate([histo['di_z2w2_mass'], di_z2w2_mass])
				histo['wleps_mass'] = np.concatenate([histo['wleps_mass'], wleps_mass])

				histo['tri_121_mass'] = np.concatenate([histo['tri_121_mass'], tri_121_mass])
				histo['tri_122_mass'] = np.concatenate([histo['tri_122_mass'], tri_122_mass])
				histo['tri_212_mass'] = np.concatenate([histo['tri_212_mass'], tri_212_mass])

				histo['fourlep_pt'] = np.concatenate([histo['fourlep_pt'], fourlep_pt])
				histo['fourlep_mass'] = np.concatenate([histo['fourlep_mass'], fourlep_mass])

				histo['MET_MET'] = np.concatenate([histo['MET_MET'], MET_MET])
				histo['MET_phi'] = np.concatenate([histo['MET_phi'], MET_phi])
				histo['MT2'] = np.concatenate([histo['MT2'], MT2])
				histo['HT'] = np.concatenate([histo['HT'], HT])

				histo['Jet_pt'] = np.concatenate([histo['Jet_pt'], jet_pt])
				histo['Jet_btag'] = np.concatenate([histo['Jet_btag'], jet_btag])

				histo['Channel'] = np.concatenate([histo['Channel'], Channel_info])
		except KeyError:
			print("empty")

	return histo

def Events(process, histo):

	for p in range(len(process)):
		if len(histo[p]) == 0:
			print("Number of {0} Events : 0".format(process[p]))
		else:
			print("Number of {0} Events : {1}".format(process[p], len(histo[p]['fstlep_pt'])))

for i in proc_list:
	print(i+' process...')
	for j in channel_list:
		eeee = '/home/bjpark/WWZ/BASELINE/combine/data/'+i+'/'+j+'/*.npy'
		#eeem = '/home/bjpark/WWZ/BASELINE/combine/data/'+i+'/'+j+'/*.npy'
		#eemm = '/home/bjpark/WWZ/BASELINE/combine/data/'+i+'/'+j+'/*.npy'
		#emmm = '/home/bjpark/WWZ/BASELINE/combine/data/'+i+'/'+j+'/*.npy'
		#mmmm = '/home/bjpark/WWZ/BASELINE/combine/data/'+i+'/'+j+'/*.npy'

		eeee_proc_list = glob.glob(eeee)
		#eeem_proc_list = glob.glob(eeem)
		#eemm_proc_list = glob.glob(eemm)
		#emmm_proc_list = glob.glob(emmm)
		#mmmm_proc_list = glob.glob(mmmm)

		eeee_list = Load(eeee_proc_list)
		#eeem_list = Load(eeem_proc_list)
		#eemm_list = Load(eemm_proc_list)
		#emmm_list = Load(emmm_proc_list)
		#mmmm_list = Load(mmmm_proc_list)


		eeee = Loop(eeee_list)
		outname1 = "combine_"+j+".npy"
		np.save('/home/bjpark/WWZ/BASELINE/combine/data/newVari/'+i+'/{0}'.format(outname1), eeee)
		#eeem = Loop(eeem_list)
		#outname2 = "combine_3e1m.npy"
		#np.save('/home/bjpark/WWZ/DRAW/baseline/npy/combine/proc/'+i+'/{0}'.format(outname2), outname2)
		#eemm = Loop(eemm_list)
		#outname3 = "combine_2e2m.npy"
		#np.save('/home/bjpark/WWZ/DRAW/baseline/npy/combine/proc/'+i+'/{0}'.format(outname3), outname3)
		#emmm = Loop(emmm_list)
		#outname4 = "combine_1e3m.npy"
		#np.save('/home/bjpark/WWZ/DRAW/baseline/npy/combine/proc/'+i+'/{0}'.format(outname4), outname4)
		#mmmm = Loop(mmmm_list)
		#outname5 = "combine_4m.npy"
		#np.save('/home/bjpark/WWZ/DRAW/baseline/npy/combine/proc/'+i+'/{0}'.format(outname5), outname5)

		#Events(proc_list, histo)


print("END")

	
