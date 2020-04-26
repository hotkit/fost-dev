from configuration import BOOST, MODES, platform


platform('focal')
__import__('gcc-10')
del MODES['gcc']
try:
    BOOST.remove((1,70,0))
except ValueError:
    pass

