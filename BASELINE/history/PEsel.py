import uproot
import awkward as ak
import numpy as np
import glob
from numba import jit
from tqdm import tqdm
import vector
import time

start_time = time.time()

branches = ['Electron.PT', 'Electron.Eta', 'Electron.Phi', 'Electron.Charge', 'MuonTight.PT', 'MuonTight.Eta', 'MuonTight.Phi', 'MuonTight.Charge', 'PuppiMissingET.MET', 'PuppiMissingET.Phi']

def Lepton_selection(particles, e_num):
	
	Electron = particles[0]
	Muon = particles[1]
	MET = particles[2]

	# PT, Eta selection

	Muon_mask = (Muon.PT > 20) & (np.abs(Muon.Eta) < 2.5)
	PE_Muon = Muon[Muon_mask]

	Electron_mask = (Electron.PT > 20) & (np.abs(Electron.Eta) < 2.5)
	PE_Electron = Electron[Electron_mask]

	# Lepton number selection

	Electrons_num_mask = (ak.num(PE_Electron) == e_num)
	Muon_num_mask = (ak.num(PE_Muon) == (4 - e_num))

	channel_mask = Electrons_num_mask & Muon_num_mask


	# Apply masks
		
	Electron_lepsel = PE_Electron[channel_mask]
	Muon_lepsel = PE_Muon[channel_mask]
	MET_lepsel = MET[channel_mask]
	

	result = [Electron_lepsel, Muon_lepsel, MET_lepsel]

	return result

	

def Classify_leptons(particles, e_num):

	Electron = particles[0]
	Muon = particles[1]

	if e_num == 4:
		Leptons = ak.zip({
			"lep1" : Electron[:,0],
			"lep2" : Electron[:,1],
			"lep3" : Electron[:,2],
			"lep4" : Electron[:,3]
		})
	elif e_num == 3:
		Leptons = ak.zip({
			"lep1" : Electron[:,0],
			"lep2" : Electron[:,1],
			"lep3" : Electron[:,2],
			"lep4" : Muon[:,0]
		})
	elif e_num == 2:
		Leptons = ak.zip({
			"lep1" : Electron[:,0],
			"lep2" : Electron[:,1],
			"lep3" : Muon[:,0],
			"lep4" : Muon[:,1]
		})
	elif e_num == 1:
		Leptons = ak.zip({
			"lep1" : Electron[:,0],
			"lep2" : Muon[:,0],
			"lep3" : Muon[:,1],
			"lep4" : Muon[:,2]
		})
	else:
		Leptons = ak.zip({
			"lep1" : Muon[:,0],
			"lep2" : Muon[:,1],
			"lep3" : Muon[:,2],
			"lep4" : Muon[:,3]
		})

	return Leptons



def Selection(file_list, e_num):

	# Define array
	histo = {}

	count = 0

	for arrays in tqdm(uproot.iterate(flist,branches)):

		raw_data = len(arrays)
		print("\n > Number of Events : {0} < ".format(raw_data))

		Electron = ak.zip({

		"PT" : arrays[b"Electron.PT"],
		"Eta" : arrays[b"Electron.Eta"],
		"Phi" : arrays[b"Electron.Phi"],
		"Charge" : arrays[b"Electron.Charge"],
		"F" : 1*abs(arrays[b"Electron.Charge"])
		})

		Muon = ak.zip({

		"PT" : arrays[b"MuonTight.PT"],
		"Eta" : arrays[b"MuonTight.Eta"],
		"Phi" : arrays[b"MuonTight.Phi"],
		"Charge" : arrays[b"MuonTight.Charge"],
		"F" : 2*abs(arrays[b"MuonTight.Charge"])
		})

		MET = ak.zip({

		"MET" : arrays[b"PuppiMissingET.MET"],
		"Phi" : arrays[b"PuppiMissingET.Phi"],
		})

		particles = [Electron, Muon, MET]

		print("-----> Defined variables : {0}".format(len(Electron)))


		## Lepton selection

		# Lepton number selection
		
		lep_sel = Lepton_selection(particles, e_num)

		print("-----> Lepton selection done. : {0}".format(len(lep_sel[0].PT)))


		# Classify leptons

		classi_lep = Classify_leptons(lep_sel, e_num)



		count += len(lep_sel[0].PT)
		print(count)
		


		try:

			# Output variables
	
			fst_lep = vector.obj(pt=classi_lep.lep1.PT, phi=classi_lep.lep1.Phi, eta=classi_lep.lep1.Eta, mass=0)
			snd_lep = vector.obj(pt=classi_lep.lep2.PT, phi=classi_lep.lep2.Phi, eta=classi_lep.lep2.Eta, mass=0)
			trd_lep = vector.obj(pt=classi_lep.lep3.PT, phi=classi_lep.lep3.Phi, eta=classi_lep.lep3.Eta, mass=0)
			frt_lep = vector.obj(pt=classi_lep.lep4.PT, phi=classi_lep.lep4.Phi, eta=classi_lep.lep4.Eta, mass=0)
			

			#print(leptons)		

			#print(leptons.pt)
			#print(leptons.phi)
			#print(leptons.eta)

			# Flatten and convert to numpy

			fstlep_pt = ak.to_numpy(fst_lep.pt)
			fstlep_phi = ak.to_numpy(fst_lep.phi)
			fstlep_eta = ak.to_numpy(fst_lep.eta)

			sndlep_pt = ak.to_numpy(snd_lep.pt)
			sndlep_phi = ak.to_numpy(snd_lep.phi)
			sndlep_eta = ak.to_numpy(snd_lep.eta)

			trdlep_pt = ak.to_numpy(trd_lep.pt)
			trdlep_phi = ak.to_numpy(trd_lep.phi)
			trdlep_eta = ak.to_numpy(trd_lep.eta)

			frtlep_pt = ak.to_numpy(frt_lep.pt)
			frtlep_phi = ak.to_numpy(frt_lep.phi)
			frtlep_eta = ak.to_numpy(frt_lep.eta)

			#lep_pt = ak.to_numpy(ak.flatten(leptons.pt))
			#lep_eta = ak.to_numpy(ak.flatten(leptons.eta))
			#lep_phi = ak.to_numpy(ak.flatten(leptons.phi))
			#print("O")
	
			# Output histo
	
			if len(histo) == 0:
				histo['fstlep_pt'] = fstlep_pt
				histo['fstlep_phi'] = fstlep_phi
				histo['fstlep_eta'] = fstlep_eta

				histo['sndlep_pt'] = sndlep_pt
				histo['sndlep_phi'] = sndlep_phi
				histo['sndlep_eta'] = sndlep_eta

				histo['trdlep_pt'] = trdlep_pt
				histo['trdlep_phi'] = trdlep_phi
				histo['trdlep_eta'] = trdlep_eta

				histo['frtlep_pt'] = frtlep_pt
				histo['frtlep_phi'] = frtlep_phi
				histo['frtlep_eta'] = frtlep_eta
			
			else:
				histo['fstlep_pt'] = np.concatenate([histo['fstlep_pt'], fstlep_pt])
				histo['fstlep_phi'] = np.concatenate([histo['fstlep_phi'], fstlep_phi])
				histo['fstlep_eta'] = np.concatenate([histo['fstlep_eta'], fstlep_eta])
				
				histo['sndlep_pt'] = np.concatenate([histo['sndlep_pt'], sndlep_pt])
				histo['sndlep_phi'] = np.concatenate([histo['sndlep_phi'], sndlep_phi])
				histo['sndlep_eta'] = np.concatenate([histo['sndlep_eta'], sndlep_eta])
				
				histo['trdlep_pt'] = np.concatenate([histo['trdlep_pt'], trdlep_pt])
				histo['trdlep_phi'] = np.concatenate([histo['trdlep_phi'], trdlep_phi])
				histo['trdlep_eta'] = np.concatenate([histo['trdlep_eta'], trdlep_eta])
				
				histo['frtlep_pt'] = np.concatenate([histo['frtlep_pt'], frtlep_pt])
				histo['frtlep_phi'] = np.concatenate([histo['frtlep_phi'], frtlep_phi])
				histo['frtlep_eta'] = np.concatenate([histo['frtlep_eta'], frtlep_eta])
				
		except ValueError:
			print("empty")
		
	return histo


# dataset = ["Original"]#,"Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Nineth","Tenth"]
datatype = ["WWZ", "ZZ_L", "ttbarZ"]#["signal","WG","ZG","WW","WZ","ZZ","WWW","WWZ","WZZ","ZZZ","ttbarG"]
channeltype = ["4e","3e1m","2e2m","1e3m","4m"]

for process in datatype:
	e_num = 4
	print(e_num)
	for channel in channeltype:
		dir_path = "/x6/spool/bjpark/condor/condorplace/"+process+"/makeroot/rootOut/*.root"
		file_list = glob.glob(dir_path)
		flist = []
		for f in file_list:
			flist.append(f+':Delphes')
		print("Now working on <"+channel+"> channel <"+process+"> process...")
		histo = Selection(file_list, e_num)
		outname = dir_path.split("/")[-4]+"_"+channel+".npy"
		np.save('/home/bjpark/WWZ/BASELINE/data/{0}/{1}/{2}'.format(channel,process,outname), histo, allow_pickle=True)
		e_num -= 1

print("End Process....")
print("--- %s seconds ---" % (time.time() - start_time))
















