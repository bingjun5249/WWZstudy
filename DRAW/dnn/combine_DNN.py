import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import awkward as ak
import pandas as pd
import os
import math

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--trial', type=str,default='0',help="--trial TRIAL NUMBER")
parser.add_argument('--thr', type=float,default=0,help="--thr THRESHOLD")

args = parser.parse_args()

trial = args.trial
thr = args.thr

com_list = ['total']

## Details
lumi = 3000000

EventDict = {
"WWZ" : 10000000/5,
"ZZ" : 10000000/5,
"ttbarZ" : 10000000/5,
"WZZ" : 10100000/5,
"ZZZ" : 10100000/5,
"WZ" : 10000000/5,
"ZG" : 10100000/5,
"Z" : 10200000/5,
"tWZ" : 10100000/5,
"ttbar" : 10000000/5,
}

xsecDict = {
"WWZ" : 0.0003051,
"ZZ" : 0.04655,
"ttbarZ" : 0.002151,
"WZZ" : 0.02785,
"ZZZ" : 0.009669,
"WZ" : 26.16,
"ZG" : 72.19,
"Z" : 44870,
"tWZ" : 0.09813,
"ttbar" : 40.288,
}

def LepZ1_PT(stk_lepPT, WWZ_lepPT, weight, color, label, order, com):

	rng_max = 150
	rng_min = 0
	
	stk = []
	for i in range(len(stk_lepPT)):
		lepPT = stk_lepPT[i]
		stk.append(np.clip(lepPT, rng_min, rng_max))
	
	stk_lepPT = stk

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.yscale('log')
	plt.ylim(10**-3,10**2)
	plt.hist(stk_lepPT, range=(rng_min,rng_max), bins=30, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_lepPT, range=(rng_min,rng_max), bins=30, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_lepPT, range=(rng_min,rng_max), bins=30, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("3000 $fb^{-1}$ (14 TeV)", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(rng_min,rng_max)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("$p^{Z1}_{T}$ [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield", fontsize=20, loc='top')
	plt.legend(fontsize=12, loc='upper right')
	plt.savefig("" + order + "_Lep_PT")
	#plt.show()
	plt.close()
	
def LepZ2_PT(stk_lepPT, WWZ_lepPT, weight, color, label, order, com):

	rng_max = 150
	rng_min = 0
	
	stk = []
	for i in range(len(stk_lepPT)):
		lepPT = stk_lepPT[i]
		stk.append(np.clip(lepPT, rng_min, rng_max))
	
	stk_lepPT = stk

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_lepPT, range=(rng_min,rng_max), bins=30, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_lepPT, range=(rng_min,rng_max), bins=30, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_lepPT, range=(rng_min,rng_max), bins=30, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("3000 $fb^{-1}$ (14 TeV)", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(rng_min,rng_max)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("$p^{Z2}_{T}$ [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield", fontsize=20, loc='top')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("" + order + "_Lep_PT")
	#plt.show()
	plt.close()
	
def LepW1_PT(stk_lepPT, WWZ_lepPT, weight, color, label, order, com):

	rng_max = 150
	rng_min = 0
	
	stk = []
	for i in range(len(stk_lepPT)):
		lepPT = stk_lepPT[i]
		stk.append(np.clip(lepPT, rng_min, rng_max))
	
	stk_lepPT = stk

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_lepPT, range=(rng_min,rng_max), bins=30, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_lepPT, range=(rng_min,rng_max), bins=30, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_lepPT, range=(rng_min,rng_max), bins=30, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("3000 $fb^{-1}$ (14 TeV)", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(rng_min,rng_max)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("$p^{l1}_{T}$ [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield", fontsize=20, loc='top')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("" + order + "_Lep_PT")
	#plt.show()
	plt.close()
	
def LepW2_PT(stk_lepPT, WWZ_lepPT, weight, color, label, order, com):

	rng_max = 150
	rng_min = 0
	
	stk = []
	for i in range(len(stk_lepPT)):
		lepPT = stk_lepPT[i]
		stk.append(np.clip(lepPT, rng_min, rng_max))
	
	stk_lepPT = stk

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_lepPT, range=(rng_min,rng_max), bins=30, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_lepPT, range=(rng_min,rng_max), bins=30, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_lepPT, range=(rng_min,rng_max), bins=30, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("3000 $fb^{-1}$ (14 TeV)", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(rng_min,rng_max)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("$p^{l2}_{T}$ [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield", fontsize=20, loc='top')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("" + order + "_Lep_PT")
	#plt.show()
	plt.close()
	
def Lep_Eta(stk_lepEta, WWZ_lepEta, weight, color, label, order, com):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_lepEta, range=(-4,4), bins=64, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_lepEta, range=(-4,4), bins=64, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_lepEta, range=(-4,4), bins=64, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(-4,4)
	plt.xlabel("" + order + " Lepton $\eta$",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("" + order + "_Lep_Eta")
	#plt.show()
	plt.close()

def Fourlep_PT(stk_FlepPT, WWZ_FlepPT, weight, color, label, com):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_FlepPT, range=(0,300), bins=30, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_FlepPT, range=(0,300), bins=30, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_FlepPT, range=(0,300), bins=30, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("3000 $fb^{-1}$ (14 TeV)", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,300)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("$p^{4l}_{T}$ [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield", fontsize=20, loc='top')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("Fourlep_Pt")
	#plt.show()
	plt.close()
	
def Fourlep_mass(stk_Flep_mass, WWZ_Flep_mass, weight, color, label, com):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_Flep_mass, range=(0,1500), bins=150, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_Flep_mass, range=(0,1500), bins=150, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_Flep_mass, range=(0,1500), bins=150, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,1500)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("$m_{4l}$ [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield | 10 GeV", fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("Fourlep_mass")
	#plt.show()
	plt.close()
	
def Dilep_mass(stk_dilep_mass, WWZ_dilep_mass, weight, color, label, com):

	rng_max = 111
	rng_min = 71
	
	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.yscale('log')
	plt.ylim(10**-3,10**2)
	plt.hist(stk_dilep_mass, range=(rng_min,rng_max), bins=40, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_dilep_mass, range=(rng_min,rng_max), bins=40, weights=weight, color=color, label=label,  stacked=True)
	plt.hist(WWZ_dilep_mass, range=(rng_min,rng_max), bins=40, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("3000 $fb^{-1}$ (14 TeV)", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(rng_min,rng_max)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("$M^{Z}_{ll} [GeV]$",fontsize=25, loc='right')
	plt.ylabel("Expected Yield", fontsize=20, loc='top')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("Dilep_mass")
	#plt.show()
	plt.close()
	
def MET(stk_MET, WWZ_MET, weight, color, label, com):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.yscale('log')
	plt.ylim(10**-3,10**2)
	plt.hist(stk_MET, range=(0,500), bins=50, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_MET, range=(0,500), bins=50, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_MET, range=(0,500), bins=50, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("3000 $fb^{-1}$ (14 TeV)", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,500)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("MET [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield", fontsize=20, loc='top')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("MET")
	#plt.show()
	plt.close()

def MT2(stk_MT2, WWZ_MT2, wight, color, label, com):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_MT2, range=(0,100), bins=100, weights=weight,  color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_MT2, range=(0,100), bins=100, weights=weight,  color=color, label=label, stacked=True)
	plt.hist(WWZ_MT2, range=(0,100), bins=100, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("3000 $fb^{-1}$ (14 TeV)", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,100)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("$M_{T2}$ [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield", fontsize=20, loc='top')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("MT2")
	#plt.show()
	plt.close()

def W_leptons_mass(stk_wleps_mass, WWZ_wleps_mass, weight, color, label, com):

	rng_max = 150
	rng_min = 0
	
	stk = []
	for i in range(len(stk_wleps_mass)):
		wlep_m = stk_wleps_mass[i]
		stk.append(np.clip(wlep_m, rng_min, rng_max))
	
	stk_wleps_mass = stk

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.yscale('log')
	plt.ylim(10**-3,10**2)
	plt.hist(stk_wleps_mass, range=(rng_min,rng_max), bins=50, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_wleps_mass, range=(rng_min,rng_max), bins=50, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_wleps_mass, range=(rng_min,rng_max), bins=50, weights=scales["WWZ"], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("3000 $fb^{-1}$ (14 TeV)", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(rng_min,rng_max)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("$M_{ll}$ [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield", fontsize=20, loc='top')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("wleps_mass")
	#plt.show()
	plt.close()

def Jet_PT(stk_jet_pt, WWZ_jet_pt, weight, color, label, com):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_jet_pt, range=(0,1500), bins=30, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_jet_pt, range=(0,1500), bins=30, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_jet_pt, range=(0,1500), bins=30, weights=scales["WWZ"], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,1500)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("Leading Jet $p_{T}$ [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield | 50 GeV", fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("Jet_pt")
	#plt.show()
	plt.close()
	
def Jet_BTag(stk_jet_btag, WWZ_jet_btag, color, label, com):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_jet_btag, range=(0,64), bins=64, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_jet_btag, range=(0,64), bins=64, color=color, label=label, stacked=True)
	plt.hist(WWZ_jet_btag, range=(0,64), bins=64, color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,64)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("BTag Score",fontsize=25, loc='right')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("Jet_btag")
	#plt.show()
	plt.close()
	
def HT(stk_HT, WWZ_HT, weight, color, label, com):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.yscale('log')
	plt.ylim(10**-3,10**2)
	plt.hist(stk_HT, range=(0,2000), bins=40, weights=weight, color=blk, histtype='step', linewidth=0.5, stacked=True)
	plt.hist(stk_HT, range=(0,2000), bins=40, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_HT, range=(0,2000), bins=40, weights=scales["WWZ"], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	if com == 'even':
		plt.title("($ee/\mu\mu$ channel)", fontsize=13, loc='left')
	elif com == 'odd':
		plt.title("($e\mu$ channel)", fontsize=13, loc='left')
	else:
		plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,2000)
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	plt.xlabel("$H_{T}$ [GeV]",fontsize=25, loc='right')
	plt.ylabel("Expected Yield | 40 GeV", fontsize=18, loc='top')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("HT")
	#plt.show()
	plt.close()
	
## Start drawing

 	
for com in com_list:
	os.chdir('/home/bjpark/WWZ/DRAW/DNN/png/')

	# Data load
	infile = '/home/bjpark/WWZ/ML/DNN/storage/run_files/total/trial'+trial+'/total_prediction.csv'
	df = pd.read_csv(infile)
	cut_df = df[df['prediction'] >= thr]
	idx = cut_df.iloc[:,[0]].values.flatten()

	testset = '/home/bjpark/WWZ/ML/DNN/storage/run_files/total/trial'+trial+'/total_testset.h5'
	test_df = pd.read_hdf(testset)
	after = test_df.iloc[idx]
	


	WWZ = after[after['xsec'] == xsecDict['WWZ']]
	Z = after[after['xsec'] == xsecDict['Z']]
	WZ = after[after['xsec'] == xsecDict['WZ']]
	ZZ = after[after['xsec'] == xsecDict['ZZ']]
	ZG = after[after['xsec'] == xsecDict['ZG']]
	WZZ = after[after['xsec'] == xsecDict['WZZ']]
	ZZZ = after[after['xsec'] == xsecDict['ZZZ']]
	ttbar = after[after['xsec'] == xsecDict['ttbar']]
	ttbarZ = after[after['xsec'] == xsecDict['ttbarZ']]
	tWZ = after[after['xsec'] == xsecDict['tWZ']]

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

	if com == 'even':
		print("-----> ee/mm channel")
	elif com == 'odd':
		print("-----> em channel")
	else:
		print("-----> total")

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



	sig_yield = Yield['WWZ']
	back_yield = (Yield['ZZ']+Yield['ttbarZ']+Yield['tWZ']+Yield['WZZ']+Yield['ZZZ']+Yield['WZ']+Yield['ZG']+Yield['Z']+Yield['ttbar'])
#	sig = math.sqrt(2 * (sig_yield + back_yield) * math.log(1 + (sig_yield / back_yield)) - sig_yield)
	sig = Yield['WWZ']/math.sqrt(Yield['ZZ']+Yield['ttbarZ']+Yield['tWZ']+Yield['WZZ']+Yield['ZZZ']+Yield['WZ']+Yield['ZG']+Yield['Z']+Yield['ttbar'])

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
	print("total expected yield: {0}".format(back_yield))

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
	stk_wleps_mass = bkg_stack(bkg_vari, 11)

	stk_MET = bkg_stack(bkg_vari, 12)
	stk_MT2 = bkg_stack(bkg_vari, 13)

	stk_jet_pt = bkg_stack(bkg_vari, 14)
#	stk_jet_btag = bkg_stack(bkg_vari, 15)

	stk_HT = bkg_stack(bkg_vari, 16)
	'''
	stk_fstlepPT = [ttbarZ['fstlep_pt'], ZZ['fstlep_pt']]#, ttbar['fstlep_pt']]
	stk_fstlepEta = [ttbarZ['fstlep_eta'], ZZ['fstlep_eta']]#, ttbar['fstlep_eta']]

	stk_sndlepPT = [ttbarZ['sndlep_pt'], ZZ['sndlep_pt']]#, ttbar['sndlep_pt']]
	stk_sndlepEta = [ttbarZ['sndlep_eta'], ZZ['sndlep_eta']]#, ttbar['sndlep_eta']]

	stk_trdlepPT = [ttbarZ['trdlep_pt'], ZZ['trdlep_pt']]#, ttbar['trdlep_pt']]
	stk_trdlepEta = [ttbarZ['trdlep_eta'], ZZ['trdlep_eta']]#, ttbar['trdlep_eta']]

	stk_frtlepPT = [ttbarZ['frtlep_pt'], ZZ['frtlep_pt']]#, ttbar['frtlep_pt']]
	stk_frtlepEta = [ttbarZ['frtlep_eta'], ZZ['frtlep_eta']]#, ttbar['frtlep_eta']]

	stk_dilep_mass = [ttbarZ['dilep_mass'], ZZ['dilep_mass']]#, ttbar['dilep_mass']]
	stk_wleps_mass = [ttbarZ['wleps_mass'], ZZ['wleps_mass']]

	stk_MET = [ttbarZ['MET_MET'], ZZ['MET_MET']]#, ttbar_MET]
	stk_MT2 = [ttbarZ['MT2'], ZZ['MT2']]#, ttbar_MT2]

	stk_jet_pt = [ttbarZ['jet_pt'], ZZ['jet_pt']]
	stk_jet_btag = [ttbarZ['jet_btag'], ZZ['jet_btag']]
	'''

	#weight
	#weight = [scales['ZZ'], scales["ttbarZ"], scales['tWZ'], scales['WZZ'], scales['ZZZ'], scales['WZ'], scales['Z'], scales['ZG'], scales["ttbar"]]
	weight = [scales['ttbar'], scales['ZG'], scales['Z'], scales['ZZZ'], scales['WZZ'], scales['WZ'], scales['tWZ'], scales['ttbarZ'], scales['ZZ']]

	# color
	#color = ['royalblue','gold','aqua','c','g','orange','coral','darkslategrey','midnightblue']
	color = ['midnightblue','darkslategrey','coral','g','c','orange','aqua','royalblue','gold']
	blk = ['black','black','black','black','black','black','black','black','black']

	# label
	#label = ['ZZ', '$t\overline{t}+Z$', 'tWZ', 'WZZ', 'ZZZ', 'WZ', '$Z\gamma$', 'Z', '$t\overline{t}$']
	label = ['$t\overline{t}$','$Z\gamma$','Z','ZZZ','WZZ','WZ','tWZ','$t\overline{t}+Z$','ZZ']

	#WWZ['HT'] = np.array(WWZ['HT'], dtype=np.float64)
	print("\n\n")

	# fst Lepton PT

	LepZ1_PT(stk_fstlepPT, WWZ['fstlep_pt'], weight, color, label, '1st', com)

	# fst Lepton Eta
	Lep_Eta(stk_fstlepEta, WWZ['fstlep_eta'], weight, color, label, '1st', com)

	# snd Lepton PT
	LepZ2_PT(stk_sndlepPT, WWZ['trdlep_pt'], weight, color, label, '2nd', com)

	# snd Lepton Eta
	Lep_Eta(stk_sndlepEta, WWZ['sndlep_eta'], weight, color, label, '2nd', com)

	# trd Lepton PT
	LepW1_PT(stk_trdlepPT, WWZ['trdlep_pt'], weight, color, label, '3rd', com)

	# trd Lepton Eta
	Lep_Eta(stk_trdlepEta, WWZ['trdlep_eta'], weight, color, label, '3rd', com)

	# frt Lepton PT
	LepW2_PT(stk_frtlepPT, WWZ['frtlep_pt'], weight, color, label, '4th', com)

	# frt Lepton Eta
	Lep_Eta(stk_frtlepEta, WWZ['frtlep_eta'], weight, color, label, '4th', com)

	# four Lepton PT
	Fourlep_PT(stk_fourlepPT, WWZ['fourlep_pt'], weight, color, label, com)

	# four Lepton PT
	Fourlep_mass(stk_fourlep_mass, WWZ['fourlep_mass'], weight, color, label, com)

	# Di-lepton mass
	Dilep_mass(stk_dilep_mass, WWZ['dilep_mass'], weight, color, label, com)

	# W leptons mass
	W_leptons_mass(stk_wleps_mass, WWZ['wleps_mass'], weight, color, label, com)

	# MET
	MET(stk_MET, WWZ['MET_MET'], weight, color, label, com)

	# MT2
	MT2(stk_MT2, WWZ['MT2'], weight, color, label, com)

	# Jet PT
	Jet_PT(stk_jet_pt, WWZ['jet_pt'], weight, color, label, com)

	# Jet BTag
	#Jet_BTag(stk_jet_btag, WWZ['jet_btag'], color, label, com)

	# HT
	HT(stk_HT, WWZ['HT'], weight, color, label, com)
