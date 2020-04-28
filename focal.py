from configuration import BOOST, platform, TOOLSET


platform('focal')
TOOLSET['gcc']['env'] = ['''CC=gcc-10''', '''CXX=g++-10''']
TOOLSET['gcc']['cmake'] = ['''-DBOOST_TOOLSET=gcc-10''']
try:
    BOOST.remove((1,70,0))
except ValueError:
    pass
