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
#%%
cwd = os.path.dirname(__file__)

c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample00\Vicon Motion Systems')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'pyCGM2 lower limb CGM24 Walking01.c3d')

# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample01')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'Eb015pr.c3d')

# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample05')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'vicon512.c3d')

# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample00\Codamotion')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'codamotion_gaitwands_19970212.c3d')

# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample10')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'TYPE-4a.c3d')

# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample28')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'type1.c3d')

acq = ba.open_c3d(src_c3d_path)

fp_output = ba.get_fp_output(acq, None)
wc_output = ba.get_fp_wrench(acq, 0.0)

f_lab_btk = wc_output[0]['FORCE']
f_lab_manual = fp_output[0]['F_COP_LAB']
diff_f_lab = f_lab_btk-f_lab_manual

m_cop_btk = wc_output[0]['MOMENT']*0.001
m_cop_manual = fp_output[0]['M_COP_LAB']
diff_m_cop = m_cop_btk-m_cop_manual

cop_lab_btk = wc_output[0]['POS']*0.001
cop_lab_manual = fp_output[0]['COP_LAB']
diff_cop_lab = cop_lab_btk-cop_lab_manual
