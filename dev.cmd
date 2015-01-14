@echo off

call git pull origin master

call git submodule init
call git submodule sync --recursive
call git submodule update --init --recursive

python dev.py %*
