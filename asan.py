from configuration import Mode, MODES

MODES['clang']['asan'] = Mode(env=[
    'CXXFLAGS="-fsanitize=address -fno-omit-frame-pointer -fno-common"',
    'LDFLAGS="-fsanitize=address"'])
