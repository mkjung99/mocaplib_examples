import os
import sys
if sys.path[0] != os.getcwd():
    sys.path.insert(0, os.getcwd())
lib_local_path = os.path.normpath(r'C:\WORKSPACE\DEV\mocaplib')
if os.path.exists(lib_local_path):
    if sys.path[1] != lib_local_path:
        sys.path.insert(1, lib_local_path)
import mocaplib as mcl
from mocaplib import btkapp as ba
import numpy as np
# import logging
#%%
current_f_dir_path = os.path.dirname(__file__)
c3d_sample_dir_path = os.path.join(current_f_dir_path, r'..\Samples_C3D\Sample00\Vicon Motion Systems')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'pyCGM2 lower limb CGM24 Walking01.c3d')
tgt_c3d_path = os.path.splitext(__file__)[0]+'_result.c3d'
tgt_log_path = os.path.splitext(__file__)[0]+'_result.log'

acq = ba.get_acq(src_c3d_path)
pt_names = ba.get_point_names(acq, tgt_types=None)
analog_names = ba.get_analog_names(acq)
dict_events = ba.get_dict_events(acq)
dict_points = ba.get_dict_points(acq, blocked_nan=True, resid=True, tgt_types=None)
dict_analogs = ba.get_dict_analogs(acq)
dict_groups = ba.get_dict_metadata(acq)
