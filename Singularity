Bootstrap: debootstrap
MirrorURL: http://us.archive.ubuntu.com/ubuntu
OSVersion: xenial

%labels

    AUTHOR_NAME Zongyang Li
    AUTHOR_EMAIL zli@danforthcenter.org
    APPLICATION_NAME none
    APPLICATION_VERSION none
    APPLICATION_URL none
    SYSTEM_NAME comet
    SYSTEM_SINGULARITY_VERSION 2.3.1
    SYSTEM_URL http://www.sdsc.edu/support/user_guides/comet.html
    VERSION 0.0.5
    LAST_UPDATED 20180122

%setup

%environment

%post -c /bin/bash

    export LC_ALL=C

    apt-get -y install ubuntu-standard
    apt-get -y install ubuntu-server

    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} main"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} universe"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} multiverse"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} restricted"

    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates main"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates universe"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates multiverse"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates restricted"

    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports main"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports universe"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports multiverse"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports restricted"

    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security main"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security universe"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security multiverse"
    add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security restricted"

    apt-get -y update && apt-get -y upgrade
    apt-get install -y matplotlib
    apt-get install -y utm
    apt-get install -y PIL
    apt-get install -y lmfit

    mkdir /cvmfs /oasis /projects /scratch

%files

%runscript

%test
