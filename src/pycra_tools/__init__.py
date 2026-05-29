"""Package to read Ticra Tools field and coupling data stored in .cut, .grd and .h5 file formats"""

# This allows user to just write "from pycra import GridFile" without having to dig through subscripts
from ._version import __version__

from .fields.gridfile import readgrid
from .fields.cutfile import readcut
from .coupling.cutfile import readcut_coupling

# # just uncommented to see what happens
#__version__ = "0.0.1"
#__author__ = "Roland Albers"
#__email__ = "roland.albers@unibe.ch"
#__all__ = ['gridfile', 'cutfile', 'utils']

