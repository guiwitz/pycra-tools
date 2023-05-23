import graspy_readgrd as gr
import matplotlib.pyplot as plt
import os

os.chdir('/storage/basin/work/AWS/aws_grasp/AWS_12_22/complete_rot_far/ps_1/scan_angle_1')
test = gr.gridfile(["farfield_54.grd", "farfield_89.grd", "farfield_183.grd"])
print(test.data)