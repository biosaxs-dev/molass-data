"""
make_tutorial_data4.py

SAMPLE4 is simulated (molass-library#379): three overlapping species, each a folded core with a disordered
Gaussian-chain tail (Pedersen 1997, item 25) with different tail share, on the geometry, error and scatter of the
real data set it replaces (molass_data 0.5.0 and before: 20220210). The truth is in ``ssd.simulation_truth``.

Run from any folder with molass-library >= the commit of #379 importable:

    python make_tutorial_data4.py
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../molass-library')))
from molass import get_version

assert get_version() >= '1.2.3', "Incompatible molass version"

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(HERE, '..', 'molass_data', 'SAMPLE4')

from molass.Testing import simulate_sample4_like
from molass.DataObjects import SecSaxsData as SSD

ssd = simulate_sample4_like("tails3", noise=1.0, seed=0)
if os.path.isdir(FOLDER):
    for name in os.listdir(FOLDER):
        os.remove(os.path.join(FOLDER, name))
ssd.export(FOLDER, 'PREFIX4_', fmt='%.8e')

import matplotlib.pyplot as plt
check_ssd = SSD(FOLDER)
check_ssd.plot_compact()
plt.show()
