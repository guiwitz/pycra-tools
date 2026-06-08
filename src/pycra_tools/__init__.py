"""Package to read Ticra Tools field and coupling data stored in .cut, .grd and .h5 file formats"""

# This allows user to just write "from pycra import GridFile" without having to dig through subscripts
from ._version import __version__

from . import torfile
from .fields.gridfile import readgrid
from .fields.cutfile import readcut
from .coupling.cutfile import readcut_coupling

