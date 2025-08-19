"""
make_tutorial_data4.py
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

DATA3 = os.path.join(DATA_ROOT_FOLDER, "20220210")

import matplotlib.pyplot as plt
from molass.DataObjects import SecSaxsData as SSD
ssd = SSD(DATA3)
ssd.plot_compact()
plt.show()

ssd.export('SAMPLE4', 'PREFIX4_', fmt='%.8e')

check_ssd = SSD('SAMPLE4')
check_ssd.plot_compact()
plt.show()
