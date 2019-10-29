from configuration import MODES

MODES['clang']['asan'] = (['CXXFLAGS="-fsanitize=address -fno-omit-frame-pointer -fno-common" LDFLAGS="-fsanitize=address"'], [])
