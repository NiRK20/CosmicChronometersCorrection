import numpy as np
import pandas as pd

def load_chronometers(data_file, cov_file):
    zHz, Hzi, errHz = np.genfromtxt(data_file, comments='#', usecols=(0,1,2), unpack=True)
    zmod, imf, slib, sps, spsooo = np.genfromtxt(cov_file, comments='#', usecols=(0,1,2,3,4), unpack=True)
    
    cov_mat_diag = np.zeros((len(zHz), len(zHz)), dtype='float64') 

    # Erros estatísticos
    for i in range(len(zHz)):
        cov_mat_diag[i,i] = errHz[i]**2
    
    # Erros sistemáticos
    imf_intp = np.interp(zHz, zmod, imf)/100
    spsooo_intp = np.interp(zHz, zmod, spsooo)/100
    
    cov_mat_imf = np.zeros((len(zHz), len(zHz)), dtype='float64')
    cov_mat_spsooo = np.zeros((len(zHz), len(zHz)), dtype='float64')
    
    for i in range(len(zHz)):
        for j in range(len(zHz)):
            cov_mat_imf[i,j] = Hzi[i] * imf_intp[i] * Hzi[j] * imf_intp[j]
            cov_mat_spsooo[i,j] = Hzi[i] * spsooo_intp[i] * Hzi[j] * spsooo_intp[j]
            
    # Matriz de covariância total
    cov_mat = cov_mat_spsooo+cov_mat_imf+cov_mat_diag
    inv_cov_mat = np.linalg.inv(cov_mat)

    return {
        "z": zHz,
        "Hz": Hzi,
        "inv_cov": inv_cov_mat
    }