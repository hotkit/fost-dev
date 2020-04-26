from configuration import Mode, MODES

MODES['gcc-10'] = {'': Mode(
    env=[
        '''CC=gcc-10''',
        '''CXX=g++-10''',
    ],
    cmake=[
        '''-DBOOST_TOOLSET=gcc-10''',
    ],
    suffix='-gcc-10',
)}
