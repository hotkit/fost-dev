# Fost development #

This project is intended to help run tests and do development of the library collection.

It contains a location where the Boost library builds can be kept and scripts for cloning and testing the libraries.

The main command is `./dev`. It takes a number of options that control what is going to be done and how it is done. The general form of the command is:

    ./dev libraries options platform actions

## Libraries ##

Most of the libraries are still only in the `fost` collection, but fost-aws has also been split out to `aws`.

## Options ##

* allboost -- Test against all of the supported Boost libraries.
* mfc -- Include the MFC build variants. You will need the full compiler for this, the Express ones won't work.

## Platform ##

The platform that you are running the tests on. For Ubuntu you should find that the correct platform is chosen for you, but if you get an import error you may be using a version that the `dev` system doesn't know about.

For 32 bit Windows the `windows` option should also be selected for you. For Mac use `snowleopard`.

## Actions ##

* `latest` -- Update the submodules to their latest verisons using the origin master or develop branches as appropriate. These changes are then checked in.
* `pull` -- Pull all libraries from GitHub and make sure that the right versions of the sub-modules are in use. If a library is already present then it just makes sure that the sub-module is checked out at the correct revision.
* `push` -- Push all projects back up to GitHub. If no libraries are included then it just pushes the `fost-dev` code. It assumes that all of the project checkouts are on a tracked branch.
* `stable` -- Merge the develop branches into master. Follow with `push` to send to GitHub.
* `test` -- Build the projects and run all of their tests.

## Examples ##

Get latest code and run all builds and tests on Ubuntu Saucy

    ./dev fost pull test

Push the current versions of all checked out libraries to GitHub.

    ./dev fost push

Merge the `develop` branches to master and then push to GitHub.

    ./dev fost stable push

Fetch the current version of fost-aws, update to the latest libraries, test then push (if all of the tests pass).

    ./dev aws pull latest test push
