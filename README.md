redhat-charybdis
=======

This builds a charybdis-3.4.2-1.rpm suitable for RedHat 6.5

Why ?

1. Irc is cool

Usage
=======

    git clone https://github.com/jonuwz/redhat-charybdis.git
    cd redhat-charybdis
    mkdir -p /usr/src/packages/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
    yum -y install rpm-build flex bison openssl-devel

    ./build.sh


