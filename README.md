# Tutorial Data for Molass Library

To use this package, install and use as follows.

```
pip install molass_data
```

```
from molass_data import SAMPLE1     # contains the folder path
from molass_data import SAMPLE2     # contains the folder path
from molass_data import SAMPLE3     # contains the folder path
from molass_data import SAMPLE4     # contains the folder path
from molass_data import SAMPLE5     # contains the folder path
```

`SAMPLE1`, `SAMPLE2`, `SAMPLE3` and `SAMPLE5` are measured data sets. **`SAMPLE4` is simulated**: three overlapping
species, each a folded core with a disordered Gaussian-chain tail (Pedersen 1997), with the photon-counting noise
of Sedlak et al. (2017), on the geometry of a measured data set. The truth is known and the data can be regenerated with
`molass.Testing.simulate_sample4_like("tails3", scale=30.0)` (`scripts/make_tutorial_data4.py`).

## Changes

### 0.6.1

- `SAMPLE4`: the noise is now the published photon-counting model of Sedlak et al. (J. Appl. Cryst. 50 (2017) 621-630,
  about 30 counts at the strongest frame and the first q point) and the stated error is that model's standard error.
  Version 0.6.0 used a stated error and scatter taken from a measured data set; no measured error is used any more.
  The species (peaks, areas, Rg) and the geometry (q grid, frames, UV/XR mapping, intensity) are unchanged, so
  results computed from `SAMPLE4` 0.6.0 change through the noise only; for example the number of components
  that scores best in a rigorous decomposition is not stable under a change of noise.

### 0.6.0

- `SAMPLE4` is replaced by a simulated data set with the same name and file layout. Results computed from
  `SAMPLE4` with earlier versions (0.5.0 and before: a measured data set) therefore change.
- `SAMPLE6` (`20191006_proteins5`) is removed from this package.