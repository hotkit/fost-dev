from configuration import MODES

MODES['clang']['werror'] = (['CXXFLAGS="-Wall -Wpedantic -Werror"'], [])
MODES['gcc']['werror'] = (['CXXFLAGS="-Wall -Wpedantic -Werror"'], [])
