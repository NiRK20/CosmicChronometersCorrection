import numpy as np
import src.modelos as modelos

def chi2Hz(theta, modelo, dados):
    corr = modelos.MODELOS[modelo]["Corr"]
    flat = modelos.MODELOS[modelo]["Flat"]
    h0, wm, wl, f = modelos.free_par(theta, corr, flat)
    z = dados["z"]
    hz = dados["Hz"]
    
    Ez = wm*(1+z)**3 + (1-wm-wl)*(1+z)**2 + wl

    if np.any(Ez<0):
        return np.inf
        
    Hzm = h0*np.sqrt(Ez)
    dhz = hz-Hzm
    inv_covCorr = dados["inv_cov"]/f**2

    return np.dot(np.dot(dhz.T, inv_covCorr), dhz)
    
def lnprob(theta, modelo, dados):
    ndata = len(dados["z"])
    corr = modelos.MODELOS[modelo]["Corr"]
    flat = modelos.MODELOS[modelo]["Flat"]
    _, _, _, f = modelos.free_par(theta, corr, flat)
    chi2 = chi2Hz(theta, modelo, dados)
    return -0.5*chi2 - ndata*np.log(f)

def deltaBIC(samples, n, k):
    params = samples.getParams()
    if hasattr(params, 'chi2'):
        chi2min = np.min(params.chi2)
    elif hasattr(params, 'minuslogpost'):
        chi2min = 2 * np.min(params.minuslogpost)
    else:
        print("Aviso: Chi2 não encontrado nas amostras.")
        return 0

    BIC = chi2min + k*np.log(n)

    return BIC, chi2min