import os
import sys
if sys.path[0] != os.getcwd():
    sys.path.insert(0, os.getcwd())
lib_local_path = os.path.normpath(r'C:\WORKSPACE\DEV\mocaplib')
if os.path.exists(lib_local_path):
    if sys.path[1] != lib_local_path:
        sys.path.insert(1, lib_local_path)
from mocaplib import btkapp as ba
import numpy as np
from scipy.spatial.transform import Rotation as R
#%%
cwd = os.path.dirname(__file__)

c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample00\Vicon Motion Systems')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'pyCGM2 lower limb CGM24 Walking01.c3d')
trc_path = os.path.join(cwd, 'Test02_result.trc')
mot_path = os.path.join(cwd, 'Test02_result.mot')

acq = ba.open_c3d(src_c3d_path)
dict_pts = ba.get_dict_points(acq, tgt_types=['Marker'])
mkr_names = [x for x in list(dict_pts['LABELS']) if len(x)<=4]
axes_src = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
axes_tgt = [[0, -1, 0], [0, 0, 1], [-1, 0, 0]]
rot_ret = R.align_vectors(a=axes_src, b=axes_tgt)
rot_obj = rot_ret[0]
trf = rot_obj.as_matrix()

ba.export_trc(acq, trc_path, rot_mat=trf, filt_fc=20.0, tgt_mkr_names=mkr_names)
ret = ba.export_mot(acq, mot_path, rot_mat=trf, filt_fc=20.0, threshold=15.0)
