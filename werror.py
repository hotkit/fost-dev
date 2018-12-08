from configuration import MODES

MODES['clang']['werror'] = (['CXXFLAGS="-Wall -Wextra -Wpedantic -Werror"'], [])
MODES['gcc']['werror'] = (['CXXFLAGS="-Wall -Wextra -Wpedantic -Werror"'], [])
