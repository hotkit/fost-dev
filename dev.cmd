@echo off

call git pull origin master

call git submodule init
call git submodule sync
call git submodule update

python dev.py %*
