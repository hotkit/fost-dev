from configuration import BOOST, MODES, platform, TOOLSET


platform('focal')
TOOLSET['gcc']['env'] = ['''CC=gcc-10''', '''CXX=g++-10''']
TOOLSET['gcc']['cmake'] = ['''-DBOOST_TOOLSET=gcc-10''']
MODES['gcc'][''].cmake += ['''-DUSE_TAMARIND_LIBRARY=ON''']
try:
    BOOST.remove((1,70,0))
except ValueError:
    pass
