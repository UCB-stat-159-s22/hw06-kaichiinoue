import matplotlib
matplotlib.use('Agg')
from ligotools import utils
from ligotools import readligo as rl
import pytest
from scipy.interpolate import interp1d
import matplotlib.mlab as mlab
import json
import os
import numpy as np
import matplotlib.pyplot as plt

eventname = 'GW150914' 
tests_path = "ligotools/ligotools/tests/"

def test_whiten():
    assert len(utils.whiten(strain_H1,psd_H1,dt)) == 131072


def reqshift():
    fnjson = "data/BBH_events_v3.json"
    eventname = 'GW150914' 
    events = json.load(open(fnjson,"r"))
    event = events[eventname]
    fs = event['fs'] 
    fband = event['fband'] 
    tevent = event['tevent'] 
    fn_H1 = event['fn_H1']
    strain_H1, time_H1, chan_dict = rl.loaddata('data/'+fn_H1, 'H1')
    dt = time_H1[1] - time_H1[0]
    bb, ab = butter(4, [fband[0]*2./fs, fband[1]*2./fs], btype='band')
    normalization = np.sqrt((fband[1]-fband[0])/(fs/2))
    NFFT = 4*fs
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
    psd_H1 = interp1d(freqs, Pxx_H1)
    strain_H1_whiten = whiten(strain_H1,psd_H1,dt)
    strain_H1_whitenbp = filtfilt(bb, ab, strain_H1_whiten) / normalization
    shift = reqshift(strain_H1_whitenbq,fshift=400,sample_rate=4096)
    assert len(strain) == 131072
    assert max(strain) == 1329.5794826006363


