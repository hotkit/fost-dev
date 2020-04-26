from configuration import MODES, platform


platform('focal')
__import__('gcc-10')
del MODES['gcc']
