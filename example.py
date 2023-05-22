import graspy_readgrd as gr
import matplotlib.pyplot as plt

test = gr.gridfile('farfield_183.grd')
# maxdB = test.power(test.data)
test.co_cross(test.data)
fig, ax, con = test.plotcont(test.data.co_dB.sel(band=1))
plt.show()