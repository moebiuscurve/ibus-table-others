#!/bin/sh
set -e
set -x

autoreconf --verbose --install --force
./configure --enable-maintainer-mode $*
