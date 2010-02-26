@echo off
for %%t in (fost-base fost-internet fost-aws fost-orm fost-postgres fost-py fost-meta) DO (
    for %%b in (37 38 39 40 41 42) DO (
        call do-build.cmd %%t %%b %%t
        IF ERRORLEVEL 1 (
            copy
            GOTO end
        ) ELSE (
            for %%s in (-rc) DO (
                call do-build.cmd %%t%%s %%b %%t
                IF ERRORLEVEL 1 (
                    copy
                    GOTO end
                )
            )
        )
    )
)
:end
