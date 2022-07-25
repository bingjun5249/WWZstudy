import myModule
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
from matplotlib import gridspec
import mplhep as hep
from mt2 import mt2


def calMt2(tuplelist,channel):
	output = []
	if channel == 'mm':
		for f in tuplelist:
			vis1_px = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_pt'][:,0]) * np.cos(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_phi'][:,0]))
			vis1_py = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_pt'][:,0]) * np.sin(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_phi'][:,0]))
			vis1_mass = np.array(ak.ones_like(vis1_px))*0.1057
			vis2_px = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_pt'][:,1]) * np.cos(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_phi'][:,1]))
			vis2_py = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_pt'][:,1]) * np.sin(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_phi'][:,1]))
			vis2_mass =  np.array(ak.ones_like(vis2_px))*0.1057
			inv_px = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_pt']) * np.cos(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_phi']))
			inv_py = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_pt']) * np.sin(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_phi']))
			inv_m1 = np.array(ak.ones_like(inv_px))
			inv_m2 = np.array(ak.ones_like(inv_px))
			val =  mt2(vis1_mass,vis1_px,vis1_py,vis1_mass,vis2_px,vis2_py,inv_px,inv_py,vis1_mass,vis1_mass)
			output.append(val)

	if channel == 'em':
		for f in tuplelist:
			vis1_px = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_pt'][:,0]) * np.cos(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_phi'][:,0]))
			vis1_py = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_pt'][:,0]) * np.sin(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Muon_phi'][:,0]))
			vis1_mass = np.array(ak.ones_like(vis1_px))*0.1057
			vis2_px = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_pt'][:,0]) * np.cos(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_phi'][:,0]))
			vis2_py = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_pt'][:,0]) * np.sin(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_phi'][:,0]))
			vis2_mass =  np.array(ak.ones_like(vis2_px))*0.0005
			inv_px = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_pt']) * np.cos(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_phi']))
			inv_py = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_pt']) * np.sin(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_phi']))
			inv_m1 = np.array(ak.ones_like(inv_px))
			inv_m2 = np.array(ak.ones_like(inv_px))
			val =  mt2(vis1_mass,vis1_px,vis1_py,vis1_mass,vis2_px,vis2_py,inv_px,inv_py,vis1_mass,vis1_mass)
			output.append(val)
	if channel == 'ee':
		for f in tuplelist:
			vis1_px = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_pt'][:,0]) * np.cos(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_phi'][:,0]))
			vis1_py = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_pt'][:,0]) * np.sin(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_phi'][:,0]))
			vis1_mass = np.array(ak.ones_like(vis1_px))*0.0005
			vis2_px = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_pt'][:,1]) * np.cos(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_phi'][:,1]))
			vis2_py = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_pt'][:,1]) * np.sin(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['Electron_phi'][:,1]))
			vis2_mass =  np.array(ak.ones_like(vis2_px))*0.0005
			inv_px = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_pt']) * np.cos(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_phi']))
			inv_py = np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_pt']) * np.sin(np.array(np.load("./"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]['MET_phi']))
			inv_m1 = np.array(ak.ones_like(inv_px))
			inv_m2 = np.array(ak.ones_like(inv_px))
			val =  mt2(vis1_mass,vis1_px,vis1_py,vis1_mass,vis2_px,vis2_py,inv_px,inv_py,vis1_mass,vis1_mass)
			output.append(val)


	output=np.array(output)
	return output


