@echo off

pushd %1\Boost
call install.cmd %2 0 ../../Boost
popd

FOR %%d IN (debug debug-mfc release release-mfc) DO (
    title Building %1 %%d with Boost 1.%2
    rmdir /s /q %1\dist
    call %1\%3\compile.cmd all %%d toolset=msvc
    IF ERRORLEVEL 1 (
        echo Failed %1 %%d with Boost 1.%2
        copy
        GOTO end
    )
)
:end
