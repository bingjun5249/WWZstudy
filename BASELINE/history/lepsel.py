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
	
	# Lepton channel cut

	Electrons_mask = ak.num(Electron) == e_num
	Muon_mask = ak.num(Muon) == (4 - e_num)

	channel_mask = Electrons_mask & Muon_mask	
	
	# Apply masks
	
	Electron_channel = Electron[channel_mask]
	Muon_channel = Muon[channel_mask]
	MET_channel = MET[channel_mask]

	result = [Electron_channel, Muon_channel, MET_channel]

	return result
'''
def Classify_leptons(particles, e_num):

	Electron = particles[0]
	Muon = particles[1]

	if e_num == 4:
		Leptons = ak.zip({
			"lep1" : Electron[0],
			"lep2" : Electron[1],
			"lep3" : Electron[2],
			"lep4" : Electron[3]
		})
	elif e_num == 3:
		Leptons = ak.zip({
			"lep1" : Electron[0],
			"lep2" : Electron[1],
			"lep3" : Electron[2],
			"lep4" : Muon[3]
		})
	elif e_num == 2:
		Leptons = ak.zip({
			"lep1" : Electron[0],
			"lep2" : Electron[1],
			"lep3" : Muon[2],
			"lep4" : Muon[3]
		})
	elif e_num == 1:
		Leptons = ak.zip({
			"lep1" : Electron[0],
			"lep2" : Muon[1],
			"lep3" : Muon[2],
			"lep4" : Muon[3]
		})
	else:
		Leptons = ak.zip({
			"lep1" : Muon[0],
			"lep2" : Muon[1],
			"lep3" : Muon[2],
			"lep4" : Muon[3]
		})

	return Leptons


def OSSF_Z_selection(particles, builder, e_num):

	index = 1

	Electron = particles[0]
	Muon = particles[1]
	MET = particles[2]


	# Make ossf+Z mask

	for lepton in Leptons:
		builder.begin_list()
		nlep = len(lepton)
		
		for i in range(nlep):
			for j in range(i+1, nlep):
				if lepton[i].F == lepton[j].F != 0:
					index += 1
					continue
				if lepton[i].Charge + lepton[i].Charge != 0:
					index += 1
					continue
				if abs((lepton[i].mass + lepton[i].mass) - 91.1876) > 10:
					index += 1
					continue
				else:
'''
					


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
		"Charge" : arrays[b"Electron.Charge"]
		})

		Muon = ak.zip({

		"PT" : arrays[b"MuonTight.PT"],
		"Eta" : arrays[b"MuonTight.Eta"],
		"Phi" : arrays[b"MuonTight.Phi"],
		"Charge" : arrays[b"MuonTight.Charge"]
		})

		MET = ak.zip({

		"MET" : arrays[b"PuppiMissingET.MET"],
		"Phi" : arrays[b"PuppiMissingET.Phi"],
		})

		particles = [Electron, Muon, MET]

		print("-----> Defined variables : {0}".format(len(Electron)))


		# Lepton selection
		
		lep_sel = Lepton_selection(particles, e_num)

		print("-----> Lepton selection done. : {0}".format(len(lep_sel[0].PT)))

		count += len(lep_sel[0].PT)
		print(count)


		try:

			# Output variables
			
			electron = lep_sel[0]
			leptons = vector.obj(pt=electron.PT, phi=electron.Phi, eta=electron.Eta, mass=0)
			print(leptons)

			# Flatten and convert to numpy

			lep_pt = ak.to_numpy(ak.flatten(leptons.pt))
			lep_eta = ak.to_numpy(ak.flatten(leptons.eta))
			lep_phi = ak.to_numpy(ak.flatten(leptons.phi))
	
			# Output histo
	
			if len(histo) == 0:
				histo['lep_pt'] = lep_pt
				histo['lep_phi'] = lep_phi
				histo['lep_eta'] = lep_eta
			
			else:
				histo['lep_pt'] = np.concatenate([histo['lep_pt'], lep_pt])
				histo['lep_phi'] = np.concatenate([histo['lep_phi'], lep_phi])
				histo['lep_eta'] = np.concatenate([histo['lep_eta'], lep_eta])
				
		except ValueError:
			print("empty")
	
	return histo


dataset = ["Original"]#,"Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Nineth","Tenth"]
datatype = ["WWZ"]#["signal","WG","ZG","WW","WZ","ZZ","WWW","WWZ","WZZ","ZZZ","ttbarG"]
channeltype = ["4e","3e1m","2e2m","1e3m","4m"]

e_num = 4
for channel in channeltype:
	print(e_num)
	for counter in dataset:
        	for process in datatype:
                	dir_path = "/x6/spool/dylee/workspace/SM//Storage/"+counter+"_data/root/"+process+"/"+counter+"/*.root"
	                file_list = glob.glob(dir_path)
        	        flist = []
	                for f in file_list:
        	                flist.append(f+':Delphes')
	                print("Now working on <"+channel+"> channel <"+counter+"> and <"+process+"> process...")
        	        histo = Selection(file_list, e_num)
#                	outname = dir_path.split("/")[-3]+"_"+dir_path.split("/")[-2]+"_"+channel+".npy"
#	                np.save('/home/bjpark/WWZ/BASELINE/data/{0}/{1}/{2}'.format(channel,process,outname), histo, allow_pickle=True)
	e_num -= 1

print("End Process....")
print("--- %s seconds ---" % (time.time() - start_time))
















