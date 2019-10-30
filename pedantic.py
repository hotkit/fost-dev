from configuration import Mode, MODES

MODES['clang']['pedantic'] = Mode(
    env=['CXXFLAGS="-Wall -Wextra -Wpedantic -Werror"'])
MODES['gcc']['pedantic'] = Mode(
    env=['CXXFLAGS="-Wall -Wextra -Wpedantic -Werror"'])
