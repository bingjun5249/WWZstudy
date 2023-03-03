import uproot
import awkward as ak
import numpy as np
import glob
from numba import jit
from tqdm import tqdm
import vector
import time
import argparse
from mt2 import mt2

parser = argparse.ArgumentParser()
parser.add_argument('--enum', type=int,default=4,help="--enum NUMBER_OF_ELECTRON")
args = parser.parse_args()
e_num = args.enum

start_time = time.time()

branches = ['Electron.PT', 'Electron.Eta', 'Electron.Phi', 'Electron.Charge', 'MuonTight.PT', 'MuonTight.Eta', 'MuonTight.Phi', 'MuonTight.Charge', 'PuppiMissingET.MET', 'PuppiMissingET.Phi', 'JetPUPPI.BTag', 'JetPUPPI.PT', 'JetPUPPI.Phi', 'JetPUPPI.Eta', 'ScalarHT.HT']

rawevent = []
events = []

def Lepton_selection(particles, e_num):
	
	Electron = particles[0]
	Muon = particles[1]
	MET = particles[2]
	Jet = particles[3]
	HT = particles[4]

	# PT, Eta selection(Subleading lepton PT cut( > 10 GeV))

	Muon_mask = ((Muon.PT > 10) & (np.abs(Muon.Eta) < 2.5))
	PE_Muon = Muon[Muon_mask]

	Electron_mask = ((Electron.PT > 10) & (np.abs(Electron.Eta) < 2.5))
	PE_Electron = Electron[Electron_mask]

	# Lepton number selection
	
	Electrons_num_mask = (ak.num(PE_Electron) == e_num)
	Muon_num_mask = (ak.num(PE_Muon) == (4 - e_num))

	channel_mask = Electrons_num_mask & Muon_num_mask

	# Apply masks
		
	Electron_lepsel = PE_Electron[channel_mask]
	Muon_lepsel = PE_Muon[channel_mask]
	MET_lepsel = MET[channel_mask]
	Jet_lepsel = Jet[channel_mask]
	HT_lepsel = HT[channel_mask]

	result = [Electron_lepsel, Muon_lepsel, MET_lepsel, Jet_lepsel, HT_lepsel]

	return result

	

def Classify_leptons(fn, particles, e_num, list_arg=None, event=None, case=None):

	# Function 1 : first classify
	if fn == 1:
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
	
	# Function 2 : Z mass classify
	elif fn == 2:
		Electron = particles[0]
		Muon = particles[1]
	
		if e_num == 4:
			lep1=[Electron[event,list_arg[event,case,0]]]
			lep2=[Electron[event,list_arg[event,case,1]]]
			lep3=[Electron[event,list_arg[event,case,2]]]
			lep4=[Electron[event,list_arg[event,case,3]]]
			Leptons = ak.zip({
				"lep1" : lep1,
				"lep2" : lep2,
				"lep3" : lep3,
				"lep4" : lep4
			})
		elif e_num == 3:
			lep1=[Electron[event,list_arg[event,case,0]]]
			lep2=[Electron[event,list_arg[event,case,1]]]
			if (list_arg[event,case,2]>=0):
				lep3=[Electron[event,list_arg[event,case,2]]]
				lep4=[Muon[event,abs(list_arg[event,case,3]) - e_num]]
			else:
				lep3=[Muon[event,abs(list_arg[event,case,2]) - e_num]]
				lep4=[Electron[event,list_arg[event,case,3]]]
			Leptons = ak.zip({
				"lep1" : lep1,
				"lep2" : lep2,
				"lep3" : lep3,
				"lep4" : lep4
			})
		elif e_num == 2:
			if list_arg[event,case,1] > 0:
				lep1=[Electron[event,list_arg[event,case,0]]]
				lep2=[Electron[event,list_arg[event,case,1]]]
				lep3=[Muon[event,abs(list_arg[event,case,2]) - e_num]]
				lep4=[Muon[event,abs(list_arg[event,case,3]) - e_num]]
				Leptons = ak.zip({
					"lep1" : lep1,
					"lep2" : lep2,
					"lep3" : lep3,
					"lep4" : lep4
				})
			elif list_arg[event,case,1] < 0:
				lep1=[Muon[event,abs(list_arg[event,case,0]) - e_num]]
				lep2=[Muon[event,abs(list_arg[event,case,1]) - e_num]]
				lep3=[Electron[event,list_arg[event,case,2]]]
				lep4=[Electron[event,list_arg[event,case,3]]]
				Leptons = ak.zip({
					"lep1" : lep1,
					"lep2" : lep2,
					"lep3" : lep3,
					"lep4" : lep4
				})
		elif e_num == 1:
			lep1=[Muon[event,abs(list_arg[event,case,0]) - e_num]]
			lep2=[Muon[event,abs(list_arg[event,case,1]) - e_num]]
			if (list_arg[event,case,2] >= 0):
				lep3=[Electron[event,list_arg[event,case,2]]]
				lep4=[Muon[event,abs(list_arg[event,case,3]) - e_num]]
			else:
				lep3=[Muon[event,abs(list_arg[event,case,2]) - e_num]]
				lep4=[Electron[event,list_arg[event,case,3]]]
				
			Leptons = ak.zip({
				"lep1" : lep1,
				"lep2" : lep2,
				"lep3" : lep3,
				"lep4" : lep4
			})
		else:
			lep1=[Muon[event,abs(list_arg[event,case,0])]]
			lep2=[Muon[event,abs(list_arg[event,case,1])]]
			lep3=[Muon[event,abs(list_arg[event,case,2])]]
			lep4=[Muon[event,abs(list_arg[event,case,3])]]
			Leptons = ak.zip({
				"lep1" : lep1,
				"lep2" : lep2,
				"lep3" : lep3,
				"lep4" : lep4
			})

	# Function 3 : Compression (After Z mass)
	elif fn == 3:
		lep1 = particles[0]
		lep2 = particles[1]
		lep3 = particles[2]
		lep4 = particles[3]

		lep1 = ak.flatten(lep1, axis=1)
		lep2 = ak.flatten(lep2, axis=1)
		lep3 = ak.flatten(lep3, axis=1)
		lep4 = ak.flatten(lep4, axis=1)

		Leptons = ak.zip({
			"lep1" : lep1,
			"lep2" : lep2,
			"lep3" : lep3,
			"lep4" : lep4
		})
			


	return Leptons


def OSSF_maker(Leptons, builder, e_num):

	idx_list = []

	# Make ossf mask

	for lepton in Leptons:
		builder.begin_list()
		nlep = 4
		
		for i in range(nlep-1):
			for j in range(i+1, nlep):
				for k in range(nlep):
					idx_list.append(k)

				i_str = str(i+1)
				j_str = str(j+1)
				# Opposite sign
				if lepton["lep"+i_str].Charge + lepton["lep"+j_str].Charge != 0:
					idx_list = []
					continue
				# Same flavor
				if (lepton["lep"+i_str].F == lepton["lep"+j_str].F) == 0:	
					idx_list = []
					continue
				else:
					del(idx_list[j])
					del(idx_list[i])

					# electron ossf
					if (e_num == 2) & (lepton["lep"+i_str].F == 1):
						builder.begin_list()
						builder.integer(i)
						builder.integer(j)
						w1_str = str((idx_list[0]+1))
						w2_str = str((idx_list[1]+1))

					#	if lepton["lep"+w1_str].Charge + lepton["lep"+w2_str].Charge != 0:
					#		idx_list = []
					#		continue

						if (lepton["lep"+w1_str].PT > lepton["lep"+w2_str].PT):
							builder.integer(-1*idx_list[0])
							builder.integer(-1*idx_list[1])
							builder.end_list()
						else:
							builder.integer(-1*idx_list[1])
							builder.integer(-1*idx_list[0])
							builder.end_list()

					# muon ossf
					elif (e_num == 2) & (lepton["lep"+i_str].F == 2):
						builder.begin_list()
						builder.integer(-1*i)
						builder.integer(-1*j)
						w1_str = str((idx_list[0]+1))
						w2_str = str((idx_list[1]+1))

					#	if lepton["lep"+w1_str].Charge + lepton["lep"+w2_str].Charge != 0:
					#		idx_list = []
					#		continue

						if (lepton["lep"+w1_str].PT > lepton["lep"+w2_str].PT):
							builder.integer(idx_list[0])
							builder.integer(idx_list[1])
							builder.end_list()
						else:
							builder.integer(-1*idx_list[1])
							builder.integer(-1*idx_list[0])
							builder.end_list()

					else:
						builder.begin_list()
						builder.integer(i)
						builder.integer(j)
						w1_str = str((idx_list[0]+1))
						w2_str = str((idx_list[1]+1))

					#	if lepton["lep"+w1_str].Charge + lepton["lep"+w2_str].Charge != 0:
					#		idx_list = []
					#		continue

						if (lepton["lep"+w1_str].PT > lepton["lep"+w2_str].PT):
							builder.integer(idx_list[0])
							builder.integer(idx_list[1])
							builder.end_list()
						else:
							builder.integer(-1*idx_list[1])
							builder.integer(-1*idx_list[0])
							builder.end_list()

					idx_list = []
		builder.end_list()
	return builder

					
def OSSF(particles, ossf_mask):
	Electron = particles[0]
	Muon = particles[1]
	MET = particles[2]
	Jet = particles[3]
	HT = particles[4]

	# Apply mask
	ossf_Electron = Electron[ossf_mask]
	ossf_Muon = Muon[ossf_mask]
	ossf_MET = MET[ossf_mask]
	ossf_Jet = Jet[ossf_mask]
	ossf_HT = HT[ossf_mask]

	result = [ossf_Electron, ossf_Muon, ossf_MET, ossf_Jet, ossf_HT]
	return result
					
def calMT2(lepton, MET):
	result = []
#	print(lepton.lep3.PT)
#	print(MET.MET)
	
	MET = ak.flatten(MET.MET)
#	met = MET.MET
	
#	print(met)
#	for i in range(len(met)):
#		if bool(ak.all(met[i])) == False:
#			met[i].append(0)
	if lepton.lep3.F[0] == lepton.lep4.F[0]:
		if lepton.lep3.F[0] == 1:	# ee
			vis1_px = np.array(lepton.lep3.PT) * np.cos(np.array(lepton.lep3.Phi))
			vis1_py = np.array(lepton.lep3.PT) * np.sin(np.array(lepton.lep3.Phi))
			vis1_mass = np.array(ak.ones_like(vis1_px)) * 0.0005
			vis2_px = np.array(lepton.lep4.PT) * np.cos(np.array(lepton.lep4.Phi))
			vis2_py = np.array(lepton.lep4.PT) * np.cos(np.array(lepton.lep4.Phi))
			vis2_mass = np.array(ak.ones_like(vis2_px)) * 0.0005
			inv_px = np.array(MET) * np.cos(np.array(MET))
			inv_py = np.array(MET) * np.sin(np.array(MET))
			inv_m1 = np.array(ak.zeros_like(inv_px))
			inv_m2 = np.array(ak.zeros_like(inv_py))
			val = mt2(vis1_px,vis1_py,vis1_mass,vis2_px,vis2_py,vis2_mass,inv_px,inv_py,inv_m1,inv_m2)
			result.append(val)
		elif lepton.lep3.F[0] == 2:	# mm
			vis1_px = np.array(lepton.lep3.PT) * np.cos(np.array(lepton.lep3.Phi))
			vis1_py = np.array(lepton.lep3.PT) * np.sin(np.array(lepton.lep3.Phi))
			vis1_mass = np.array(ak.ones_like(vis1_px)) * 0.1057
			vis2_px = np.array(lepton.lep4.PT) * np.cos(np.array(lepton.lep4.Phi))
			vis2_py = np.array(lepton.lep4.PT) * np.cos(np.array(lepton.lep4.Phi))
			vis2_mass = np.array(ak.ones_like(vis2_px)) * 0.1057
			inv_px = np.array(MET) * np.cos(np.array(MET))
			inv_py = np.array(MET) * np.sin(np.array(MET))
			inv_m1 = np.array(ak.zeros_like(inv_px))
			inv_m2 = np.array(ak.zeros_like(inv_py))
			val = mt2(vis1_px,vis1_py,vis1_mass,vis2_px,vis2_py,vis2_mass,inv_px,inv_py,inv_m1,inv_m2)
			result.append(val)
	else:	# em
		vis1_px = np.array(lepton.lep3.PT) * np.cos(np.array(lepton.lep3.Phi))
		vis1_py = np.array(lepton.lep3.PT) * np.sin(np.array(lepton.lep3.Phi))
		vis1_mass = np.array(ak.ones_like(vis1_px)) * 0.0005
		vis2_px = np.array(lepton.lep4.PT) * np.cos(np.array(lepton.lep4.Phi))
		vis2_py = np.array(lepton.lep4.PT) * np.sin(np.array(lepton.lep4.Phi))
		vis2_mass = np.array(ak.ones_like(vis2_px)) * 0.1057
		inv_px = np.array(MET) * np.cos(np.array(MET))
		inv_py = np.array(MET) * np.sin(np.array(MET))
		inv_m1 = np.array(ak.zeros_like(inv_px))
		inv_m2 = np.array(ak.zeros_like(inv_py))
		val = mt2(vis1_px,vis1_py,vis1_mass,vis2_px,vis2_py,vis2_mass,inv_px,inv_py,inv_m1,inv_m2)
		result.append(val)

	return result

def Zmass_classify(ossf_particles, ossf_idx):

	Z_leptons=[]
	zleading=[]
	zsubleading=[]
	zthird=[]
	zfourth=[]

	for event in range(len(ossf_particles[0])):
		zmass_list = []
		for case in range(len(ossf_idx[event])):

			Zcandidate = Classify_leptons(2, ossf_particles, e_num, ossf_idx, event, case)

			lep1 = vector.obj(pt=Zcandidate.lep1.PT[0], phi=Zcandidate.lep1.Phi[0], eta=Zcandidate.lep1.Eta[0], mass=0)
			lep2 = vector.obj(pt=Zcandidate.lep2.PT[0], phi=Zcandidate.lep2.Phi[0], eta=Zcandidate.lep2.Eta[0], mass=0)
			dilep = lep1 + lep2
			zmass_list.append(abs(dilep.mass - 91.1876))
			
		if len(zmass_list) == 0: continue	
		bestZ_idx = ak.argmin(zmass_list)
			
		Z_quadruple = Classify_leptons(2, ossf_particles, e_num, ossf_idx, event, bestZ_idx)
		zleading.append(Z_quadruple.lep1)
		zsubleading.append(Z_quadruple.lep2)
		zthird.append(Z_quadruple.lep3)
		zfourth.append(Z_quadruple.lep4)	
			
		Z_leptons.append(zleading)
		Z_leptons.append(zsubleading)
		Z_leptons.append(zthird)
		Z_leptons.append(zfourth)

	# Compression

	lep_z = Classify_leptons(3, Z_leptons, e_num)

	return lep_z

def Selection(file_list, e_num):

	# Define array
	histo = {}

	count = 0

	for arrays in tqdm(uproot.iterate(flist,branches)):

	
		raw_data = len(arrays)
		rawevent.append(raw_data)
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
		"Phi" : arrays[b"PuppiMissingET.Phi"]
		})

		Jet = ak.zip({

		"PT" : arrays[b"JetPUPPI.PT"],
		"Eta" : arrays[b"JetPUPPI.Eta"],
		"Phi" : arrays[b"JetPUPPI.Phi"],
		"BTag" : arrays[b"JetPUPPI.BTag"]
		})

		HT = ak.zip({

		"HT" : arrays[b"ScalarHT.HT"]
		})

		particles = [Electron, Muon, MET, Jet, HT]

		print("-----> Defined variables : {0}".format(len(Electron)))



		# Lepton number selection
		
		lep_sel = Lepton_selection(particles, e_num)

		print("-----> Lepton selection done. : {0}".format(len(lep_sel[0].PT)))
		if len(lep_sel[0].PT) == 0: continue

		# Classify leptons

		classi_lep = Classify_leptons(1, lep_sel, e_num)

		# OSSF

		ossf_idx = OSSF_maker(classi_lep,ak.ArrayBuilder(),e_num).snapshot()
		ossf_idx_abs = abs(ossf_idx)

		if e_num == 0 or e_num == 4:
			ossf_mask_1 = ak.num(ossf_idx_abs) > 2
			ossf_mask_2 = ak.num(ossf_idx_abs) < 5
			ossf_mask = ossf_mask_1 & ossf_mask_2
		else:
			ossf_mask = ak.num(ossf_idx_abs) == 2

		ossf_idx = ossf_idx[ossf_mask]
		ossf_idx_abs = ossf_idx_abs[ossf_mask]

		ossf_particles = OSSF(lep_sel,ossf_mask)

		ossf_MET = ossf_particles[2]
		ossf_Jet = ossf_particles[3]
		ossf_HT = ossf_particles[4]

		print("-----> OSSF mask done. : {0}".format(len(ossf_particles[0].PT)))
		if len(ossf_particles[0].PT) == 0: continue

		# Z mass classify & W opposite sign

		lep_z = Zmass_classify(ossf_particles, ossf_idx)

		W_OS_mask = (lep_z.lep3.Charge + lep_z.lep4.Charge == 0)

		lep_Wos = lep_z[W_OS_mask]
		MET_Wos = ossf_MET[W_OS_mask]
		Jet_Wos = ossf_Jet[W_OS_mask]
		HT_Wos = ossf_HT[W_OS_mask]

		print("-----> W OS mask done. : {0}".format(len(lep_Wos.lep1.PT)))
		if len(lep_Wos.lep1.PT) == 0: continue

		# Lepton PT cut

		leadinglep_mask = (lep_Wos.lep1.PT > 25) & (lep_Wos.lep3.PT > 25)
		subleadinglep_mask = (lep_Wos.lep2.PT > 15) & (lep_Wos.lep4.PT > 15)

		lepPT_mask = leadinglep_mask * subleadinglep_mask

		lepPT_lep = lep_Wos[lepPT_mask]
		lepPT_MET = MET_Wos[lepPT_mask]
		lepPT_Jet = Jet_Wos[lepPT_mask]
		lepPT_HT = HT_Wos[lepPT_mask]

		print("-----> Lepton quadraplet define done. : {0}".format(len(lepPT_lep.lep1.PT)))
		if len(lepPT_lep.lep1.PT) == 0: continue

		# Z mass window

		zlep1 = vector.obj(pt=lepPT_lep.lep1.PT, phi=lepPT_lep.lep1.Phi, eta=lepPT_lep.lep1.Eta, mass=0)
		zlep2 = vector.obj(pt=lepPT_lep.lep2.PT, phi=lepPT_lep.lep2.Phi, eta=lepPT_lep.lep2.Eta, mass=0)
		Z = zlep1 + zlep2

		zmass_mask = (abs(Z.mass - 91.1876) < 20)
		zwindow_lep = lepPT_lep

		zwindow_MET = lepPT_MET
		zwindow_Jet = lepPT_Jet
		zwindow_HT = lepPT_HT

		print("-----> Z mass window done. : {0}".format(len(zwindow_lep.lep1.PT)))
		if len(zwindow_lep.lep1.PT) == 0: continue

		# W leptons mass cut

		wlep1 = vector.obj(pt=zwindow_lep.lep3.PT, phi=zwindow_lep.lep3.Phi, eta=zwindow_lep.lep3.Eta, mass=0)
		wlep2 = vector.obj(pt=zwindow_lep.lep4.PT, phi=zwindow_lep.lep4.Phi, eta=zwindow_lep.lep4.Eta, mass=0)
		wleptons = wlep1 + wlep2

#		wlepmask = (abs(wleptons.mass - 91.1876) > 10)
		#wlepmask2 = (wleptons.mass > 5)

		#wlepmask = wlepmask1 * wlepmask2

		wlep_lep = zwindow_lep
		wlep_MET = zwindow_MET
		wlep_Jet = zwindow_Jet
		wlep_HT = zwindow_HT

		print("-----> W leptons mass cut done. : {0}".format(len(wlep_lep.lep1.PT)))
		if len(wlep_lep.lep1.PT) == 0: continue

		# B Tagging score cut
	
		btag_mask = []

		for i in range(len(wlep_Jet['BTag'])):
			btag_idx = 0
			for j in range(len(wlep_Jet['BTag'][i])):
				if wlep_Jet['BTag'][i][j] & 7 > 0:
					btag_mask.append(False)
					break
				else:
					btag_idx += 1
			if btag_idx == len(wlep_Jet['BTag'][i]):
				btag_mask.append(True)

		btag_lep = wlep_lep[btag_mask]
		btag_MET = wlep_MET[btag_mask]
		btag_Jet = wlep_Jet[btag_mask]
		btag_HT = wlep_HT[btag_mask]

		print("-----> B Tagging score mask done. : {0}".format(len(btag_lep.lep1.PT)))
		if len(btag_lep.lep1.PT) == 0: continue

		# MET cut

#		METmask = btag_MET.MET >= 68

		MET_MET = btag_MET
		MET_one_mask = ak.num(MET_MET) > 0

		MET_lep = btag_lep[MET_one_mask]
		MET_Jet = btag_Jet[MET_one_mask]
		MET_MET = MET_MET[MET_one_mask]
		MET_HT = btag_HT[MET_one_mask]


		print("-----> MET mask done. : {0}".format(len(MET_lep.lep1.PT)))
		if len(MET_lep.lep1.PT) == 0: continue

		# MT2 calculation

		mt2 = calMT2(MET_lep, MET_MET)
		mt2 = ak.flatten(mt2)
		mt2 = np.where(mt2<0,0,mt2)

		# MT2 cut

		#print(mt2)
#		MT2mask = mt2 >= 97

		MT2_lep = MET_lep
		MT2_MET = MET_MET
		MT2_Jet = MET_Jet
		MT2_HT = MET_HT

		print("-----> MT2 mask done. : {0}".format(len(MT2_lep.lep1.PT)))
		if len(MT2_lep.lep1.PT) == 0: continue

#		mt2 = calMT2(MT2_lep, MT2_MET)
#		mt2 = ak.flatten(mt2)
#		mt2 = np.where(mt2<0,0,mt2)

		#print(mt2)
		# Event counting
		count += len(MT2_lep.lep1.PT)
		#print(count)

		try:

			# Output variables
	
			fst_lep = vector.obj(pt=MT2_lep.lep1.PT, phi=MT2_lep.lep1.Phi, eta=MT2_lep.lep1.Eta, mass=0)
			snd_lep = vector.obj(pt=MT2_lep.lep2.PT, phi=MT2_lep.lep2.Phi, eta=MT2_lep.lep2.Eta, mass=0)
			trd_lep = vector.obj(pt=MT2_lep.lep3.PT, phi=MT2_lep.lep3.Phi, eta=MT2_lep.lep3.Eta, mass=0)
			frt_lep = vector.obj(pt=MT2_lep.lep4.PT, phi=MT2_lep.lep4.Phi, eta=MT2_lep.lep4.Eta, mass=0)

			dilep = fst_lep + snd_lep
			wleps = trd_lep + frt_lep
			
			fourlep = dilep + wleps

			MET_vec = vector.obj(pt=MT2_MET.MET, phi=MT2_MET.Phi)
			
			Jet_vec = vector.obj(pt=MT2_Jet.PT, phi=MT2_Jet.Phi, eta=MT2_Jet.Eta, mass=0)

			ScalarHT = MT2_HT

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

			fourlep_pt = ak.to_numpy(fourlep.pt)
			fourlep_mass = ak.to_numpy(fourlep.mass)

			dilep_mass = ak.to_numpy(dilep.mass)
			wleps_mass = ak.to_numpy(wleps.mass)

			MET_MET = ak.to_numpy(ak.flatten(MT2_MET.MET))
			MET_phi = ak.to_numpy(ak.flatten(MT2_MET.Phi))
			MT2 = ak.to_numpy(mt2)

			Jet_list = []
			for i in range(len(Jet_vec.pt)): Jet_list.append(Jet_vec.pt[i][0])
			Jet_pt = Jet_list
			Jet_btag = ak.to_numpy(ak.flatten(MT2_Jet['BTag']))

			Scalar_HT = np.array(ak.to_numpy(ak.flatten(ScalarHT)), dtype=np.float64)

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

				histo['fourlep_pt'] = fourlep_pt
				histo['fourlep_mass'] = fourlep_mass

				histo['dilep_mass'] = dilep_mass
				histo['wleps_mass'] = wleps_mass
		
				histo['MET_MET'] = MET_MET
				histo['MET_phi'] = MET_phi
				histo['MT2'] = MT2

				histo['Jet_pt'] = Jet_pt
				histo['Jet_btag'] = Jet_btag

				histo['HT'] = Scalar_HT
			
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

				histo['fourlep_pt'] = np.concatenate([histo['fourlep_pt'], fourlep_pt])
				histo['fourlep_mass'] = np.concatenate([histo['fourlep_mass'], fourlep_mass])

				histo['dilep_mass'] = np.concatenate([histo['dilep_mass'], dilep_mass])
				histo['wleps_mass'] = np.concatenate([histo['wleps_mass'], wleps_mass])

				histo['MET_MET'] = np.concatenate([histo['MET_MET'], MET_MET])
				histo['MET_phi'] = np.concatenate([histo['MET_phi'], MET_phi])
				histo['MT2'] = np.concatenate([histo['MT2'], MT2])

				histo['Jet_pt'] = np.concatenate([histo['Jet_pt'], Jet_pt])
				histo['Jet_btag'] = np.concatenate([histo['Jet_btag'], Jet_btag])
				histo['HT'] = np.concatenate([histo['HT'], Scalar_HT])
		except ValueError:
			print("empty")
	events.append(count)

	return histo


dataset = ["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Nineth","Tenth"]
datatype = ["WWZ", "ZZ_L", "ttbarZ", "WZZToinclusive", "ZZZToinclusive", "ZToallall", "ZGToinclusive", "ttbar", "WZ", "tWZToinclusive"]
channeltype = ["4m","1e3m","2e2m","3e1m","4e"]

#for datagroup in dataset:
for process in datatype:
	dir_path = "/home/bjpark/WWZ/skim/condorOut/x6/spool/bjpark/condor/condorplace/"+process+"/rootOut/*.root"
	file_list = glob.glob(dir_path)
	flist = []
	for f in file_list:
		flist.append(f+':Delphes')
	print("Now working on <"+channeltype[e_num]+"> channel <"+process+"> process...")
	histo = Selection(file_list, e_num)
	outname = dir_path.split("/")[-3]+"_"+channeltype[e_num]+".npy"
	np.save('/home/bjpark/WWZ/BASELINE/data/{0}/{1}/{2}'.format(channeltype[e_num],process,outname), histo, allow_pickle=True)

print("End Process....")
print("--- %s seconds ---" % (time.time() - start_time))
print("\n")


for i in range(len(datatype)):
	print("-----{0} process-----".format(datatype[i]))
	print("{0} channel : {1}".format(channeltype[e_num], events[i]))


