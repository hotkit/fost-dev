from configuration import *


for v in range(59, 68):
    if v not in BOOST_VERSIONS and v != 60:
        BOOST_VERSIONS.append(v)

## (1, 62, 0) is already in [configure.py](./configure.py)
BOOST += [(1, 63, 0), (1, 64 ,0), (1, 65, 0), (1, 66, 0), (1, 67, 0)]
