# Fost development #

This project is intended to help run tests and do development of the library collection.

It contains a location where the Boost library builds can be kept and scripts for cloning and testing the libraries.

The main command is `./dev`. It takes a number of options that control what is going to be done and how it is done. The general form of the command is:

    ./dev libraries options platform actions

## Libraries ##

The only option supported right now is `fost` which is the collection of Fost libraries that have been moved to git so far.

## Options ##

* allboost -- Test against all of the supported Boost libraries.
* mfc -- Include the MFC build variants. You will need the full compiler for this, the Express ones won't work.

## Platform ##

The platform that you are running the tests on. For Ubuntu the release code name is used (i.e. `precise` etc.). For Windows use `windows` and for Mac use `snowleopard`.

## Actions ##

* clone -- Pull all libraries from GitHub and make sure that the right versions of the sub-modules are in use. If a library is already present then it just makes sure that the sub-module is checked out at the correct revision.
* push -- Push all projects back up to GitHub. If no libraries are included then it just pushes the `fost-dev` code.
* stable -- Merge the develop branches into master and push back to GitHub.
* test -- Build the projects and run all of their tests.
