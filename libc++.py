from configuration import Mode, MODES

## On Ubuntu this requires the libc++ and libc++ ABI packages
## ```
## sudo apt install libc++-dev libc++abi-dev
## ```
## The options specified here require clang 9 or better.
MODES['clang']['libc++'] = Mode(
    env=[
        '''CXXFLAGS="-stdlib=libc++"''',
        '''LDFLAGS="-stdlib=libc++"''',
        '''BOOST_EXTRA_OPTS="cxxflags=-stdlib=libc++ linkflags=-stdlib=libc++"'''
    ],
    cmake=[
        '''-DUSE_TAMARIND_LIBRARY=ON''',
    ],
    boost=[
        (1, 65, 0),
        (1, 65, 1),
        (1, 68, 0),
        (1, 69, 0),
        (1, 70, 0),
        (1, 71, 0),
        (1, 72, 0),
    ],
    suffix='-libc++',
)
