@echo off
svn up --ignore-externals
test-fost.py %*
