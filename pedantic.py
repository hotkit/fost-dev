from configuration import MODES

MODES['clang']['pedantic'] = (['CXXFLAGS="-Wall -Wextra -Wpedantic -Werror"'], [])
MODES['gcc']['pedantic'] = (['CXXFLAGS="-Wall -Wextra -Wpedantic -Werror"'], [])
