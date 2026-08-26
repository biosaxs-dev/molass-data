"""
make_tutorial_data5.py
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../molass-library')))
from molass import get_version

assert get_version() >= '0.4.0', "Incompatible molass version"

from molass.Local import get_local_settings
from molass.Global.Options import set_molass_options
set_molass_options(flowchange='auto')
local_settings = get_local_settings()
DATA_ROOT_FOLDER = local_settings['DATA_ROOT_FOLDER']

DATA = os.path.join(DATA_ROOT_FOLDER, "20230706", "BSA002")

import matplotlib.pyplot as plt
from molass.DataObjects import SecSaxsData as SSD
ssd = SSD(DATA)
ssd.plot_compact()
plt.show()

ssd.export('SAMPLE5', 'PREFIX5_', fmt='%.8e')

check_ssd = SSD('SAMPLE5')
check_ssd.plot_compact()
plt.show()
