import sys
sys.path.insert(0, '../../molass-library')
sys.path.insert(0, '..')
from molass_data import get_version, get_data_path
print("Library version:", get_version())
print("Tutorial data path:", get_data_path("tutorial_data"))
from molass_data import SAMPLE1, SAMPLE2, SAMPLE3, SAMPLE4, SAMPLE5, SAMPLE6
print("Sample 1 path:", SAMPLE1)
print("Sample 2 path:", SAMPLE2)
print("Sample 3 path:", SAMPLE3)
print("Sample 4 path:", SAMPLE4)
print("Sample 5 path:", SAMPLE5)
print("Sample 6 path:", SAMPLE6)