import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import awkward as ak
import os


## Details
lumi = 3000000

EventDict = {
"WWZ" : 100000,
"ZZ" : 100000,
"ttbarZ" : 100000,
#"ttbar" : 100000,
}

xsecDict = {
"WWZ" : 0.0003067,
"ZZ" : 0.04642,
"ttbarZ" : 0.002149,
#"ttbar" : 40.288,

}

def Lep_PT(stk_lepPT, WWZ_lepPT, weight, color, label, order):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_lepPT, range=(0,300), bins=60, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_lepPT, range=(0,300), bins=60, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,300)
	plt.xlabel("" + order + " Lepton $p_{T}$ [GeV]",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("" + order + "_Lep_PT")
	#plt.show()
	plt.close()
	
def Lep_Eta(stk_lepEta, WWZ_lepEta, weight, color, label, order):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_lepEta, range=(-4,4), bins=64, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_lepEta, range=(-4,4), bins=64, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(-4,4)
	plt.xlabel("" + order + " Lepton $\eta$",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("" + order + "_Lep_Eta")
	#plt.show()
	plt.close()

def Dilep_mass(stk_dilep_mass, WWZ_dilep_mass, weight, color, label):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_dilep_mass, range=(0,300), bins=150, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_dilep_mass, range=(0,300), bins=150, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,300)
	plt.xlabel("$M_{ll} [GeV]$",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("Dilep_mass")
	#plt.show()
	plt.close()
	
def MET(stk_MET, WWZ_MET, weight, color, label):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_MET, range=(0,300), bins=60, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_MET, range=(0,300), bins=60, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,300)
	plt.xlabel("$E_{T}^{miss}$ [GeV]",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("MET")
	#plt.show()
	plt.close()

def MT2(stk_MT2, WWZ_MT2, wight, color, label):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_MT2, range=(0,500), bins=100, weights=weight,  color=color, label=label, stacked=True)
	plt.hist(WWZ_MT2, range=(0,500), bins=100, weights=scales['WWZ'], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,500)
	plt.xlabel("MT2 [GeV]",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("MT2")
	#plt.show()
	plt.close()

def W_leptons_mass(stk_wleps_mass, WWZ_wleps_mass, weight, color, label):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_wleps_mass, range=(0,300), bins=120, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_wleps_mass, range=(0,300), bins=120, weights=scales["WWZ"], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,300)
	plt.xlabel("$M_{l_{W1}l_{W2}}$ [GeV]",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("wleps_mass")
	#plt.show()
	plt.close()

def Jet_PT(stk_jet_pt, WWZ_jet_pt, weight, color, label):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_jet_pt, range=(0,1500), bins=150, weights=weight, color=color, label=label, stacked=True)
	plt.hist(WWZ_jet_pt, range=(0,1500), bins=150, weights=scales["WWZ"], color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,1500)
	plt.xlabel("Leading Jet $p_{T}$ [GeV]",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("Jet_pt")
	#plt.show()
	plt.close()
	
def Jet_BTag(stk_jet_btag, WWZ_jet_btag, color, label):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_jet_btag, range=(0,64), bins=64, color=color, label=label, stacked=True)
	plt.hist(WWZ_jet_btag, range=(0,64), bins=64, color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,64)
	plt.xlabel("BTag Score",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.yscale('log')
	plt.savefig("Jet_btag")
	plt.show()
	plt.close()
	
## Start drawing

 	

os.chdir('/home/bjpark/WWZ/DRAW/baseline/png/combined')

# Data load
infile = '/home/bjpark/WWZ/DRAW/baseline/npy/ossf.npy'

load = np.load(infile,allow_pickle=True)[()]

WWZ = load['WWZ']
ZZ = load['ZZ']
ttbarZ = load['ttbarZ']
#ttbar = load['ttbar']

# Number of events
print("Number of events of WWZ : {0}".format(len(WWZ['fstlep_pt'])))
print("Number of events of ZZ : {0}".format(len(ZZ['fstlep_pt'])))
print("Number of events of ttbarZ : {0}".format(len(ttbarZ['fstlep_pt'])))
#print("Number of events of ttbar : {0}".format(len(ttbar['fstlep_pt'])))

print("\n")

# Normalize
scales = {
	"WWZ" : np.ones(len(WWZ['fstlep_pt'])) * lumi * xsecDict["WWZ"] / EventDict["WWZ"],
	"ZZ" : np.ones(len(ZZ['fstlep_pt'])) * lumi * xsecDict["ZZ"] / EventDict["ZZ"],
	"ttbarZ" : np.ones(len(ttbarZ['fstlep_pt'])) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"],
#	"ttbar" : np.ones(len(ttbar['fstlep_pt'])) * lumi * xsecDict["ttbar"] / EventDict["ttbar"],
}


# Expected Yield
Yield = {
	"WWZ" : len(WWZ['fstlep_pt']) * lumi * xsecDict["WWZ"] / EventDict["WWZ"],
	"ZZ" : len(ZZ['fstlep_pt']) * lumi * xsecDict["ZZ"] / EventDict["ZZ"],
	"ttbarZ" : len(ttbarZ['fstlep_pt']) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"],
#	"ttbar" : len(ttbar['fstlep_pt']) * lumi * xsecDict["ttbar"] / EventDict["ttbar"],

}


print("WWZ expected yield: {0}".format(Yield['WWZ']))
print("ZZ expected yield: {0}".format(Yield['ZZ']))
print("ttbarZ expected yield: {0}".format(Yield['ttbarZ']))
#print("ttbar expected yield: {0}".format(Yield['ttbar']))


# stack
stk_fstlepPT = [ttbarZ['fstlep_pt'], ZZ['fstlep_pt']]#, ttbar['fstlep_pt']]
stk_fstlepEta = [ttbarZ['fstlep_eta'], ZZ['fstlep_eta']]#, ttbar['fstlep_eta']]

stk_sndlepPT = [ttbarZ['sndlep_pt'], ZZ['sndlep_pt']]#, ttbar['sndlep_pt']]
stk_sndlepEta = [ttbarZ['sndlep_eta'], ZZ['sndlep_eta']]#, ttbar['sndlep_eta']]

stk_trdlepPT = [ttbarZ['trdlep_pt'], ZZ['trdlep_pt']]#, ttbar['trdlep_pt']]
stk_trdlepEta = [ttbarZ['trdlep_eta'], ZZ['trdlep_eta']]#, ttbar['trdlep_eta']]

stk_frtlepPT = [ttbarZ['frtlep_pt'], ZZ['frtlep_pt']]#, ttbar['frtlep_pt']]
stk_frtlepEta = [ttbarZ['frtlep_eta'], ZZ['frtlep_eta']]#, ttbar['frtlep_eta']]

stk_dilep_mass = [ttbarZ['dilep_mass'], ZZ['dilep_mass']]#, ttbar['dilep_mass']]
#stk_wleps_mass = [ttbarZ['wleps_mass'], ZZ['wleps_mass']]

#stk_MET = [ttbarZ['MET_MET'], ZZ['MET_MET']]#, ttbar_MET]
#stk_MT2 = [ttbarZ['MT2'], ZZ['MT2']]#, ttbar_MT2]

#stk_jet_pt = [ttbarZ['jet_pt'], ZZ['jet_pt']]
#stk_jet_btag = [ttbarZ['jet_btag'], ZZ['jet_btag']]

#weight
weight = [scales["ttbarZ"], scales["ZZ"]]#, scales["ttbar"]]

# color
color = ['royalblue','gold']#,'midnightblue']

# label
label = ['$t\overline{t}+Z$', 'ZZ']#, '$t\overline{t}$']

print("\n\n")

# fst Lepton PT

Lep_PT(stk_fstlepPT, WWZ['fstlep_pt'], weight, color, label, '1st')

# fst Lepton Eta
Lep_Eta(stk_fstlepEta, WWZ['fstlep_eta'], weight, color, label, '1st')

# snd Lepton PT
Lep_PT(stk_sndlepPT, WWZ['trdlep_pt'], weight, color, label, '2nd')

# snd Lepton Eta
Lep_Eta(stk_sndlepEta, WWZ['sndlep_eta'], weight, color, label, '2nd')

# trd Lepton PT
Lep_PT(stk_trdlepPT, WWZ['trdlep_pt'], weight, color, label, '3rd')

# trd Lepton Eta
Lep_Eta(stk_trdlepEta, WWZ['trdlep_eta'], weight, color, label, '3rd')

# frt Lepton PT
Lep_PT(stk_frtlepPT, WWZ['frtlep_pt'], weight, color, label, '4th')

# frt Lepton Eta
Lep_Eta(stk_frtlepEta, WWZ['frtlep_eta'], weight, color, label, '4th')

# Di-lepton mass
Dilep_mass(stk_dilep_mass, WWZ['dilep_mass'], weight, color, label)

# W leptons mass
#W_leptons_mass(stk_wleps_mass, WWZ['wleps_mass'], weight, color, label)

# MET
#MET(stk_MET, WWZ['MET_MET'], weight, color, label)

# MT2
#MT2(stk_MT2, WWZ['MT2'], weight, color, label)

# Jet PT
#Jet_PT(stk_jet_pt, WWZ['jet_pt'], weight, color, label)

# Jet BTag
#Jet_BTag(stk_jet_btag, WWZ['jet_btag'], color, label)
