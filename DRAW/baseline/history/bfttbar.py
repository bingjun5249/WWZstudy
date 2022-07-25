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
}

xsecDict = {
"WWZ" : 0.0003067,
"ZZ" : 0.04642,
"ttbarZ" : 0.002149,

}

def Lep_PT(stk_lepPT, WWZ_lepPT, color, label, order):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_lepPT, range=(0,300), bins=60,  color=color, label=label, stacked=True)
	plt.hist(WWZ_lepPT, range=(0,300), bins=60, color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,300)
	plt.xlabel("" + order + " Lepton $p_{T}$ [GeV]",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.savefig("" + order + "_Lep_PT")
	#plt.show()
	plt.close()
	
def Lep_Eta(stk_lepEta, WWZ_lepEta, color, label, order):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_lepEta, range=(-4,4), bins=64, color=color, label=label, stacked=True)
	plt.hist(WWZ_lepEta, range=(-4,4), bins=64, color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(-4,4)
	plt.xlabel("" + order + " Lepton $\eta$",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.savefig("" + order + "_Lep_Eta")
	#plt.show()
	plt.close()

def Dilep_mass(stk_dilep_mass, WWZ_dilep_mass, color, label):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_dilep_mass, range=(75,100), bins=50, color=color, label=label, stacked=True)
	plt.hist(WWZ_dilep_mass, range=(75,100), bins=50, color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(75,100)
	plt.xlabel("$M_{ll} [GeV]$",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.savefig("Dilep_mass")
	#plt.show()
	plt.close()
	
def MET(stk_MET, WWZ_MET, color, label):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_MET, range=(0,300), bins=60,  color=color, label=label, stacked=True)
	plt.hist(WWZ_MET, range=(0,300), bins=60, color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,300)
	plt.xlabel("$E_{T}^{miss}$ [GeV]",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.savefig("MET")
	#plt.show()
	plt.close()

def MT2(stk_MT2, WWZ_MT2, color, label, weight):

	plt.figure(figsize=(8,8))
	plt.style.use(hep.style.CMS)
	bins = np.linspace(0,50,100)
	plt.hist(stk_MT2, range=(0,300), bins=60, weights=weight,  color=color, label=label, stacked=True)
	plt.hist(WWZ_MT2, range=(0,300), bins=60, color='red', histtype='step', linewidth=2, label='WWZ')
	plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
	plt.title("(combined channel)", fontsize=13, loc='left')
	plt.xlim(0,300)
	plt.xlabel("MT2 [GeV]",fontsize=20, loc='center')
	plt.legend(fontsize=12, loc='upper right')
	plt.savefig("MT2")
	plt.show()
	plt.close()

## Start drawing

 	

os.chdir('/home/bjpark/WWZ/DRAW/baseline/png/combined')

# Data load
infile = '/home/bjpark/WWZ/DRAW/baseline/npy/combine.npy'

lep_sel = np.load(infile,allow_pickle=True)[()]

WWZ = lep_sel['WWZ']
ZZ = lep_sel['ZZ']
ttbarZ = lep_sel['ttbarZ']
ttbar = lep_sel['ttbar']



# fst Lepton PT
WWZ_fst_Lepton_PT = WWZ['fstlep_pt']
ZZ_fst_Lepton_PT = ZZ['fstlep_pt']
ttbarZ_fst_Lepton_PT = ttbarZ['fstlep_pt']
ttbar_fst_Lepton_PT = ttbar['fstlep_pt']


# fst Lepton Eta
WWZ_fst_Lepton_Eta = WWZ['fstlep_eta']
ZZ_fst_Lepton_Eta = ZZ['fstlep_eta']
ttbarZ_fst_Lepton_Eta = ttbarZ['fstlep_eta']
ttbar_fst_Lepton_Eta = ttbar['fstlep_eta']


# fst Lepton Phi
WWZ_fst_Lepton_Phi = WWZ['fstlep_phi']
ZZ_fst_Lepton_Phi = ZZ['fstlep_phi']
ttbarZ_fst_Lepton_Phi = ttbarZ['fstlep_phi']
ttbar_fst_Lepton_Phi = ttbar['fstlep_phi']



# snd Lepton PT
WWZ_snd_Lepton_PT = WWZ['sndlep_pt']
ZZ_snd_Lepton_PT = ZZ['sndlep_pt']
ttbarZ_snd_Lepton_PT = ttbarZ['sndlep_pt']
ttbar_snd_Lepton_PT = ttbar['sndlep_pt']


# snd Lepton Eta
WWZ_snd_Lepton_Eta = WWZ['sndlep_eta']
ZZ_snd_Lepton_Eta = ZZ['sndlep_eta']
ttbarZ_snd_Lepton_Eta = ttbarZ['sndlep_eta']
ttbar_snd_Lepton_Eta = ttbar['sndlep_eta']


# snd Lepton Phi
WWZ_snd_Lepton_Phi = WWZ['sndlep_phi']
ZZ_snd_Lepton_Phi = ZZ['sndlep_phi']
ttbarZ_snd_Lepton_Phi = ttbarZ['sndlep_phi']
ttbar_snd_Lepton_Phi = ttbar['sndlep_phi']



# trd Lepton PT
WWZ_trd_Lepton_PT = WWZ['trdlep_pt']
ZZ_trd_Lepton_PT = ZZ['trdlep_pt']
ttbarZ_trd_Lepton_PT = ttbarZ['trdlep_pt']
ttbar_trd_Lepton_PT = ttbar['trdlep_pt']


# trd Lepton Eta
WWZ_trd_Lepton_Eta = WWZ['trdlep_eta']
ZZ_trd_Lepton_Eta = ZZ['trdlep_eta']
ttbarZ_trd_Lepton_Eta = ttbarZ['trdlep_eta']
ttbar_trd_Lepton_Eta = ttbar['trdlep_eta']


# trd Lepton Phi
WWZ_trd_Lepton_Phi = WWZ['trdlep_phi']
ZZ_trd_Lepton_Phi = ZZ['trdlep_phi']
ttbarZ_trd_Lepton_Phi = ttbarZ['trdlep_phi']
ttbar_trd_Lepton_Phi = ttbar['trdlep_phi']




# frt Lepton PT
WWZ_frt_Lepton_PT = WWZ['frtlep_pt']
ZZ_frt_Lepton_PT = ZZ['frtlep_pt']
ttbarZ_frt_Lepton_PT = ttbarZ['frtlep_pt']
ttbar_frt_Lepton_PT = ttbar['frtlep_pt']


# frt Lepton Eta
WWZ_frt_Lepton_Eta = WWZ['frtlep_eta']
ZZ_frt_Lepton_Eta = ZZ['frtlep_eta']
ttbarZ_frt_Lepton_Eta = ttbarZ['frtlep_eta']
ttbar_frt_Lepton_Eta = ttbar['frtlep_eta']


# frt Lepton Phi
WWZ_frt_Lepton_Phi = WWZ['frtlep_phi']
ZZ_frt_Lepton_Phi = ZZ['frtlep_phi']
ttbarZ_frt_Lepton_Phi = ttbarZ['frtlep_phi']
ttbar_frt_Lepton_Phi = ttbar['frtlep_phi']

# Di lepton mass
WWZ_dilep_mass = WWZ['dilep_mass']
ZZ_dilep_mass = ZZ['dilep_mass']
ttbarZ_dilep_mass = ttbarZ['dilep_mass']
ttbar_dilep_mass = ttbar['dilep_mass']

# MET
WWZ_MET = WWZ['MET_MET']
ZZ_MET = ZZ['MET_MET']
ttbarZ_MET = ttbarZ['MET_MET']
ttbar_MET = ttbar['MET_MET']

# MT2
WWZ_MT2 = WWZ['MT2']
ZZ_MT2 = ZZ['MT2']
ttbarZ_MT2 = ttbarZ['MT2']
ttbar_MT2 = ttbar['MT2']

# Number of events
print("Number of events of WWZ : {0}".format(len(WWZ_fst_Lepton_PT)))
print("Number of events of ZZ : {0}".format(len(ZZ_fst_Lepton_PT)))
print("Number of events of ttbarZ : {0}".format(len(ttbarZ_fst_Lepton_PT)))
print("Number of events of ttbar : {0}".format(len(ttbar_fst_Lepton_PT)))

print("\n")

# Normalize
scales = {
	"WWZ" : np.ones(len(WWZ_fst_Lepton_PT)) * lumi * xsecDict["WWZ"] / EventDict["WWZ"],
	"ZZ" : np.ones(len(ZZ_fst_Lepton_PT)) * lumi * xsecDict["ZZ"] / EventDict["ZZ"],
	"ttbarZ" : np.ones(len(ttbarZ_fst_Lepton_PT)) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"],
	"ttbar" : np.ones(len(ttbar_fst_Lepton_PT)) * lumi * xsecDict["ttbar"] / EventDict["ttbar"],
}


# Expected Yield
Yield = {
	"WWZ" : len(WWZ_fst_Lepton_PT) * lumi * xsecDict["WWZ"] / EventDict["WWZ"],
	"ZZ" : len(ZZ_fst_Lepton_PT) * lumi * xsecDict["ZZ"] / EventDict["ZZ"],
	"ttbarZ" : len(ttbarZ_fst_Lepton_PT) * lumi * xsecDict["ttbarZ"] / EventDict["ttbarZ"],
	"ttbar" : len(ttbar_fst_Lepton_PT) * lumi * xsecDict["ttbar"] / EventDict["ttbar"],

}


print("WWZ expected yield: {0}".format(Yield['WWZ']))
print("ZZ expected yield: {0}".format(Yield['ZZ']))
print("ttbarZ expected yield: {0}".format(Yield['ttbarZ']))
print("ttbar expected yield: {0}".format(Yield['ttbar']))


# stack
stk_fstlepPT = [ZZ['fstlep_pt'], ttbarZ['fstlep_pt'], ttbar['fstlep_pt']]
stk_fstlepEta = [ZZ['fstlep_eta'], ttbarZ['fstlep_eta'], ttbar['fstlep_eta']]

stk_sndlepPT = [ZZ['sndlep_pt'], ttbarZ['sndlep_pt'], ttbar['sndlep_pt']]
stk_sndlepEta = [ZZ['sndlep_eta'], ttbarZ['sndlep_eta'], ttbar['sndlep_eta']]

stk_trdlepPT = [ZZ['trdlep_pt'], ttbarZ['trdlep_pt'], ttbar['trdlep_pt']]
stk_trdlepEta = [ZZ['trdlep_eta'], ttbarZ['trdlep_eta']]

stk_frtlepPT = [ZZ['frtlep_pt'], ttbarZ['frtlep_pt']]
stk_frtlepEta = [ZZ['frtlep_eta'], ttbarZ['frtlep_eta']]

stk_dilep_mass = [ZZ['dilep_mass'], ttbarZ['dilep_mass']]

stk_MET = [ZZ_MET, ttbarZ_MET]
stk_MT2 = [ZZ_MT2, ttbarZ_MT2]

#weight
weight = [scales["ZZ"], scales["ttbarZ"]]

# color
color = ['gold','royalblue']

# label
label = ['ZZ', '$t\overline{t}+Z$']

print("\n\n")

# fst Lepton PT

Lep_PT(stk_fstlepPT, WWZ_fst_Lepton_PT, color, label, '1st')

# fst Lepton Eta
Lep_Eta(stk_fstlepEta, WWZ_fst_Lepton_Eta, color, label, '1st')

# snd Lepton PT
Lep_PT(stk_sndlepPT, WWZ_snd_Lepton_PT, color, label, '2nd')

# snd Lepton Eta
Lep_Eta(stk_sndlepEta, WWZ_snd_Lepton_Eta, color, label, '2nd')

# trd Lepton PT
Lep_PT(stk_trdlepPT, WWZ_trd_Lepton_PT, color, label, '3rd')

# trd Lepton Eta
Lep_Eta(stk_trdlepEta, WWZ_trd_Lepton_Eta, color, label, '3rd')

# frt Lepton PT
Lep_PT(stk_frtlepPT, WWZ_frt_Lepton_PT, color, label, '4th')

# frt Lepton Eta
Lep_Eta(stk_frtlepEta, WWZ_frt_Lepton_Eta, color, label, '4th')

# Di-lepton mass
Dilep_mass(stk_dilep_mass, WWZ_dilep_mass, color, label)

# MET
MET(stk_MET, WWZ_MET, color, label)

# MT2
MT2(stk_MT2, WWZ_MT2, color, label)
