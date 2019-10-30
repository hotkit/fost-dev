from configuration import Mode, MODES

MODES['clang']['werror'] = Mode(env=['CXXFLAGS="-Werror"'])
MODES['gcc']['werror'] = Mode(env=['CXXFLAGS="-Werror"'])
