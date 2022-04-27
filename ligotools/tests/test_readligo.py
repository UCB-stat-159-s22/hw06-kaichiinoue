import numpy as np
import os
import fnmatch

from ligotools import readligo as rl

def test_loaddata_H1():
    fn_H1 = 'H-H1_LOSC_4_V2-1126259446-32.hdf5'
    strain_H1, time_H1, channel_dict_H1 = rl.loaddata('data/'+fn_H1, 'H1')
    assert len(strain_H1) == len(time_H1)
    assert len(channel_dict_H1) != 0
    
    
def test_loaddata_time():
    try:
        assert np.isclose(time[0], 1126259446.0)
    except AssertionError as detail:
        msg = "The time value loaded from data is not correct."
        raise AssertionError(detail.__str__() + "\n" +  msg)
    

def test_loaddata_H1H2(): 
    assert strain_H1.shape == strain_L1.shape 
    assert time_H1.shape == time_L1.shape
    assert len(chan_dict_H1) == len(chan_dict_L1) == 13 
    assert chan_dict_H1.keys() == chan_dict_L1.keys()
    

def test_read_hdf5_H1():
    filename = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5(filename)

    assert (strain is not None) & (gpsStart is not None) & (ts is not None) & (shortnameList is not None) & (qmask is not None) & (injmask is not None) & (injnameList is not None) 
