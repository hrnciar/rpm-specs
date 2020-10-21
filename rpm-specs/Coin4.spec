%global commit 6enkw

Name:           Coin4
Version:        4.0.0
Release:        7%{?dist}
Summary:        High-level 3D visualization library

License:        BSD and GPLv3+

URL:            https://bitbucket.org/Coin3D/coin/wiki/Home

Source0:        https://bitbucket.org/Coin3D/coin/downloads/coin-%{version}-src.zip

Patch3:         0003-man3.patch
Patch5:         0005-gcc-4.7.patch
Patch6:         0006-inttypes.patch
Patch11:        0011-Fix-SoCamera-manpage.patch
# Per this thread Coin provides a dummy GLX implementation which causes issues
# when running under Wayland so we patch it out.
# https://forum.freecadweb.org/viewtopic.php?f=8&t=33359#p279513
Patch12:        coin-no_glx.patch


BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

BuildRequires:  boost-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  expat-devel
#BuildRequires:  libXext-devel

%description
Coin3D is a high-level, retained-mode toolkit for effective 3D graphics
development. It is API compatible with Open Inventor 2.1.


%package devel
Summary:        Development files for Coin
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel
Requires:       bzip2-devel
Requires:       fontconfig-devel
Requires:       freetype-devel
Requires:       libGLU-devel
Requires:       pkgconfig
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
Provides:       pkgconfig(Coin)

%description devel
Development package for Coin.


%package doc
Summary:        HTML developer documentation for Coin

%description doc
%{summary}.


%prep
%autosetup -p1 -n coin-%{commit}

# Update doxygen configuration
doxygen -u docs/coin.doxygen.in

#find -name 'Makefile.*' -exec sed -i -e 's,\$(datadir)/Coin,$(datadir)/Coin4,' {} \;

# bogus permissions
find . \( -name '*.h' -o -name '*.cpp' -o -name '*.c' \) -a -executable -exec chmod -x {} \;

# convert sources to utf-8
for a in $(find . -type f -exec file -i {} \; | grep -i iso | sed -e 's,:.*,,'); do \
  /usr/bin/iconv -f ISO-8859-1 -t utf-8 $a > $a~; \
  mv $a~ $a; \
done

# get rid of bundled boost headers
rm -rf include/boost


%build
%cmake -DCOIN_BUILD_DOCUMENTATION=TRUE \
       -DCOIN_BUILD_DOCUMENTATION_MAN=TRUE \
       -DHAVE_MULTIPLE_VERSION=TRUE \
       -DUSE_EXTERNAL_EXPAT=TRUE 

%cmake_build


%install
%cmake_install

cd %{buildroot}%{_mandir}
/usr/bin/rename .3 .3coin4 man3/*
cd - 

mkdir -p %{buildroot}%{_libdir}/Coin4
mkdir -p %{buildroot}%{_bindir}

cat > %{buildroot}%{_libdir}/Coin4/coin-config << EOF
coin-config for Coin4 is here for alternatives compatibility only with Coin2/3.
Use the CMake import targets instead.
EOF

ln -sr %{_libdir}/Coin4/coin-config %{buildroot}%{_bindir}/coin-config
mv %{buildroot}%{_libdir}/pkgconfig/Coin.pc %{buildroot}%{_libdir}/pkgconfig/Coin4.pc
ln -sr %{_libdir}/pkgconfig/Coin4.pc %{buildroot}%{_libdir}/pkgconfig/Coin.pc


%check
%ctest


%ldconfig_scriptlets


%post devel
link=$(readlink -e "%{_bindir}/coin-config")
if [ "$link" = "%{_bindir}/coin-config" ]; then
  rm -f %{_bindir}/coin-config
fi
if [ "$link" = "%{_libdir}/Coin4/coin-config" ]; then
  rm -f %{_bindir}/coin-config
fi

/usr/sbin/alternatives --install "%{_bindir}/coin-config" coin-config \
  "%{_libdir}/Coin4/coin-config" 80 \
  --slave %{_libdir}/pkgconfig/Coin.pc Coin.pc %{_libdir}/pkgconfig/Coin4.pc \
  --slave %{_libdir}/libCoin.so libCoin.so %{_libdir}/libCoin.so.80

%preun devel
if [ $1 = 0 ]; then
  /usr/sbin/alternatives --remove coin-config "%{_libdir}/Coin4/coin-config"
fi


%files
%doc AUTHORS ChangeLog README{,.UNIX} THANKS FAQ*
%license COPYING
%dir %{_datadir}/Coin4
%{_datadir}/Coin4/scxml
%{_libdir}/libCoin.so.*

%files devel
%ghost %{_bindir}/coin-config
%ghost %{_libdir}/libCoin.so
%ghost %{_libdir}/pkgconfig/Coin.pc
%{_includedir}/Coin4/
%{_libdir}/cmake/Coin-%{version}/
%{_libdir}/Coin4/coin-config
%{_libdir}/pkgconfig/Coin4.pc
%dir %{_datadir}/Coin4
%{_datadir}/Coin4/draggerDefaults
%{_datadir}/Coin4/shaders
%{_infodir}/Coin4/
%{_mandir}/man?/*

%files doc
%{_docdir}/Coin4/html/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Richard Shaw <hobbes1069@gmail.com> - 4.0.0-4
- Disable building with glx as it causes crashes in FreeCAD on wayland.

* Tue Sep 17 2019 Richard Shaw <hobbes1069@gmail.com> - 4.0.0-2
- Update spec file per reviewer comments.
- Change package name from Coin4 to coin.

* Tue Sep 03 2019 Richard Shaw <hobbes1069@gmail.com> - 4.0.0-1
- Initial packaging.
