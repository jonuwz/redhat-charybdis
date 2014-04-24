name=charybdis-3.4.2.tar.gz
ttps://github.com/atheme/charybdis/archive/%{name}-%{version}.tar.gz
[[ -e "/usr/src/packages/SOURCES/$name" ]] || wget -O /usr/src/packages/SOURCES/$name "https://github.com/atheme/charybdis/archive/$name"
find SPECS SOURCES -type f -exec /bin/cp -f {} /usr/src/packages/{} \;
echo "Now run :"
echo "    rpmbuild -ba /usr/src/packages/SPECS/charybdis.spec"
echo
