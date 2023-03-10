import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep
import scipy
from scipy.stats import poisson
import ROOT

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
"WWZ" : 79440,
"Z" : 0,
"WZ" : 0,
"ZZ" : 152,
"ZG" : 0,
"WZZ" : 73,
"ZZZ" : 61,
"ttbar" : 0,
"ttbarZ" : 1220,
"tWZ" : 108,
}

com_histo = {'lumi':[], 'sig':[], 'pvalue':[]}

def GetPvalue(nbkg, ntotal):
	x = np.arange(ntotal)
	bkg = nbkg
	y =poisson(bkg).pmf(x)
	p_value = 1 - y.sum()
	return p_value

idx_com = 0

for lumi in range(137000, 10010000, 500000):


	# Combine
	com_Yield = {

	"WWZ" : Dict['WWZ']*lumi*xsecDict['WWZ'] / EventDict['WWZ'],
	"Z" : Dict['Z']*lumi*xsecDict['Z'] / EventDict['Z'],
	"WZ" : Dict['WZ']*lumi*xsecDict['WZ'] / EventDict['WZ'],
	"ZZ" : Dict['ZZ']*lumi*xsecDict['ZZ'] / EventDict['ZZ'],
	"ZG" : Dict['ZG']*lumi*xsecDict['ZG'] / EventDict['ZG'],
	"WZZ" : Dict['WZZ']*lumi*xsecDict['WZZ'] / EventDict['WZZ'],
	"ZZZ" : Dict['ZZZ']*lumi*xsecDict['ZZZ'] / EventDict['ZZZ'],
	"ttbar" : Dict['ttbar']*lumi*xsecDict['ttbar'] / EventDict['ttbar'],
	"ttbarZ" : Dict['ttbarZ']*lumi*xsecDict['ttbarZ'] / EventDict['ttbarZ'],
	"tWZ" : Dict['tWZ']*lumi*xsecDict['tWZ'] / EventDict['tWZ'],

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

df = pd.DataFrame(com_histo)
df.to_csv('result.csv')
