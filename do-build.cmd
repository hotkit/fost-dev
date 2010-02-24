@echo off
echo Building %1 with Boost 1.%2

pushd %1\Boost
call install.cmd %2 0 ../../Boost
popd

FOR %%d IN (debug debug-mfc release release-mfc) DO (
    call %1\%3\compile.cmd all %%d toolset=msvc
)
