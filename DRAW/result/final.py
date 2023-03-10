import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep
import scipy
from scipy.stats import poisson
#import ROOT

EventDict = {
"WWZ" : 10000000/5,
"Z" : 10200000/5,
"WZ" : 10000000/5,
"ZZ" : 10000000/5,
"ZG" : 10100000/5,
"WZZ" : 10100000/5,
"ZZZ" : 10100000/5,
"ttbar" : 10000000/5,
"ttbarZ" : 10100000/5,
"tWZ" : 10100000/5,
}

xsecDict = {
"WWZ" : 0.0003051,
"Z" : 44870,
"WZ" : 26.16,
"ZZ" : 0.04655,
"ZG" : 72.19,
"WZZ" : 0.02785,
"ZZZ" : 0.009669,
"ttbar" : 40.288,
"ttbarZ" : 0.002151,
"tWZ" : 0.09813,
}


Dict ={
"WWZ" : 74311,
"Z" : 0,
"WZ" : 0,
"ZZ" : 222,
"ZG" : 0,
"WZZ" : 58,
"ZZZ" : 103,
"ttbar" : 0,
"ttbarZ" : 1349,
"tWZ" : 108,
}
'''
com_histo = {'lumi':[], 'sig':[], 'pvalue':[]}

def GetPvalue(nbkg, ntotal):
	x = np.arange(ntotal)
	bkg = nbkg
	y =poisson(bkg).pmf(x)
	p_value = 1 - y.sum()
	return p_value

idx_com = 0

for lumi in range(0, 6010000, 10000):


	# Combine
	com_Yield = {

	"WWZ" : eee_Yield['WWZ']+eem_Yield['WWZ']+emm_Yield['WWZ']+mmm_Yield['WWZ'],
	"Z" : eee_Yield['Z']+eem_Yield['Z']+emm_Yield['Z']+mmm_Yield['Z'],
	"WZ" : eee_Yield['WZ']+eem_Yield['WZ']+emm_Yield['WZ']+mmm_Yield['WZ'],
	"ZZ" : eee_Yield['ZZ']+eem_Yield['ZZ']+emm_Yield['ZZ']+mmm_Yield['ZZ'],
	"ZG" : eee_Yield['ZG']+eem_Yield['ZG']+emm_Yield['ZG']+mmm_Yield['ZG'],
	"WZZ" : eee_Yield['WZZ']+eem_Yield['WZZ']+emm_Yield['WZZ']+mmm_Yield['WZZ'],
	"ZZZ" : eee_Yield['ZZZ']+eem_Yield['ZZZ']+emm_Yield['ZZZ']+mmm_Yield['ZZZ'],
	"ttbar" : eee_Yield['ttbar']+eem_Yield['ttbar']+emm_Yield['ttbar']+mmm_Yield['ttbar'],
	"ttbarZ" : eee_Yield['ttbarZ']+eem_Yield['ttbarZ']+emm_Yield['ttbarZ']+mmm_Yield['ttbarZ'],
	"tWZ" : eee_Yield['tWZ']+eem_Yield['tWZ']+emm_Yield['tWZ']+mmm_Yield['tWZ'],

	}

	# com Significance
	com_total_bkg = (com_Yield['Z'] + com_Yield['ZG'] + com_Yield['ZZ'] + com_Yield['WZ'] + com_Yield['WZZ'] + com_Yield['ttbar'] + com_Yield['ttbarZ'] + com_Yield['tWZ'] + com_Yield['ZZZ'])

	com_signal = com_Yield['WWZ']

	com_pvalue = GetPvalue(com_total_bkg, com_total_bkg + com_signal)

	com_sig = ROOT.Math.gaussian_quantile_c(com_pvalue,1)

	com_histo['lumi'].append(lumi/1000)
	com_histo['pvalue'].append(com_pvalue)
	com_histo['sig'].append(com_sig)
	
	if com_sig >= 5:
		if idx_com == 1:
			continue
		print(lumi/1000)
		idx_com += 1

'''
infile = '/home/bjpark/WWZ/DRAW/result/result.csv'
df = pd.read_csv(infile)
com_histo = df


plt.figure(figsize=(10,8))
plt.style.use(hep.style.CMS)
plt.plot(com_histo['lumi'], com_histo['sig'], label='combined channel',color='red', linewidth=1)

plt.axhline(5, 0, 10000, color='black', linestyle='-', linewidth=1, label='5 $\sigma$ line')

plt.legend(fontsize=17, loc='lower right')
plt.xlim(137,6000)
plt.ylim(0,6.5)
plt.xlabel("Luminosity [$fb^{-1}$]", fontsize=20, loc='center')
plt.ylabel("Expected Significance", fontsize=20, loc='center')

plt.savefig("result.png")
plt.show()

