#!/usr/bin/env bash
DATAROOT="/netscratch/[your directory]"
DATADIR="$DATAROOT/[experiment]"
ROOTDIR="`dirname \"$0\"`"
ROOTDIR="`readlink -f ${ROOTDIR}`"  # this is the directory that contains this script
sudo userdocker run --rm -it -w $ROOTDIR \  # your container starts in $ROOTDIR
     -v/ds:/ds -v/ds2:/ds2 -v/netscratch:/netscratch \
     [docker image] \
     ./env.sh python [script name].py with \
         parameter=value \
         "$@"  #
