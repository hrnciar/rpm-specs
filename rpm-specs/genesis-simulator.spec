# Upstream has been informed of incorrect FSF addresses
# https://github.com/genesis-sim/genesis-2.4/issues/4


%global commit 374cdbc7971ccffa0a0fe270ce9904e30c0802dc
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global realname genesis
%global instdir %{_datadir}/%{name}

Name:       %{realname}-simulator
Summary:    A general purpose simulation platform
Version:    2.4
Release:    6.20181209git374cdbc%{?dist}
Url:        http://www.genesis-sim.org/GENESIS/
Source0:    https://github.com/genesis-sim/%{realname}-%{version}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Fix for format-security issues. Sent upstream:
# https://github.com/genesis-sim/genesis-2.4/pull/2
Patch0:     0001-Update-for-Wformat-security.patch
# Update scripts to use python3. Also sent upstream
# https://github.com/genesis-sim/genesis-2.4/pull/3
Patch1:     0001-Update-scripts-to-use-python3.patch

# GPL and LGPL: Genesis
# MIT: param library
# Public Domain: Scripts
License:    GPLv2+ and LGPLv2+ and MIT and Public Domain

BuildRequires: gcc
BuildRequires: bison
BuildRequires: flex
BuildRequires: flex-devel
BuildRequires: ncurses-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: netcdf-devel
BuildRequires: git

%description
GENESIS (short for GEneral NEural SImulation System) is a general
purpose simulation platform that was developed to support the
simulation of neural systems ranging from subcellular components and
biochemical reactions to complex models of single neurons, simulations
of large networks, and systems-level models. As such, GENESIS, and its
version for parallel and networked computers (PGENESIS) was the first
broad scale modeling system in computational biology to encourage
modelers to develop and share model features and components. Most
current GENESIS applications involve realistic simulations of
biological neural systems. Although the software can also model more
abstract networks, other simulators are more suitable for
backpropagation and similar connectionist modeling.

%package devel
Summary: Static library and tools for building genesis extensions
%description devel
%{summary}.

%package doc
BuildArch: noarch
Summary: Documentation for %{name}
%description doc
%{summary}.

%ifarch x86_64
%global extraflags -DLONGWORDS
%endif

%prep
%autosetup -n %{realname}-%{version}-%{commit}/%{realname} -p2 -S git

# Correct spurious perms
find Doc -type f -exec chmod -x '{}' \;
# Correct shebang for perl scripts
find Scripts/purkinje/perl -exec sed -i 's|#!/usr/local/bin/perl -w|#!/usr/bin/perl -w|' '{}' \;

# Correct executable perms
find Scripts -type f -exec chmod -x '{}' \;
find Tutorials -type f -exec chmod -x '{}' \;

# file-not-utf8
pushd Scripts/burster
# Convert to utf-8
for file in README README.txt; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done
popd

# Remove the binaries they ship
rm -rf ../%{realname}-binaries

# Remove unrelated programs
rm -rf ./src/contrib

# Remove bundled netcdf
rm -rf ./src/diskio/interface/netcdf/netcdf-3.4
# Do not use bundled netcdflib
sed -i 's/netcdflib.o: netcdflib/netcdflib.o:/' ./src/diskio/interface/netcdf/Makefile

# Set up Makefile for Linux installation
cp src/Makefile.dist src/Makefile
cat >>src/Makefile <<EOF
MACHINE=Linux
OS=BSD
XLIB=%{_libdir}
CC=gcc
CPP=cpp -P
CFLAGS=%{optflags} %{?extraflags}
LD=ld
RANLIB=ranlib
AR=ar
YACC=bison -y
LEX=flex -l
LEXLIB=-lfl
LIBS=\$(LEXLIB) -lm -lnetcdf
TERMCAP=-lncurses
TERMOPT=-DTERMIO -DDONT_USE_SIGIO
NETCDFOBJ = \
        \$(DISKIODIR)/interface/\$(NETCDFSUBDIR)/netcdflib.o
EOF

%build
make -C src %{?_smp_mflags} genesis

%install
make -C src install INSTALLDIR=%{buildroot}%{_libdir}/genesis
rm -r %{buildroot}%{_libdir}/genesis/{src,man}
rm -v %{buildroot}%{_libdir}/genesis/.*simrc
chmod -x %{buildroot}%{_libdir}/genesis/startup/*

mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/genesis/genesis %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_includedir}
mv %{buildroot}%{_libdir}/genesis/include %{buildroot}%{_includedir}/genesis

mv %{buildroot}%{_libdir}/genesis/bin/convert %{buildroot}%{_bindir}/genesis-convert
install -D man/man1/convert.1 %{buildroot}%{_mandir}/man1/genesis-convert.1
cp src/libsh %{buildroot}%{_libdir}/genesis/lib

find %{buildroot}%{_libdir}/genesis/startup/ -name '*simrc' -exec \
    sed -i 's|%{buildroot}||g' {} \;

# Fix permission for man
chmod -x %{buildroot}%{_mandir}/man1/%{realname}-convert.1*

# Remove docs from libdir
rm -rf %{buildroot}%{_libdir}/%{realname}/Doc
rm -rf %{buildroot}%{_libdir}/%{realname}/Hyperdoc
rm -rf %{buildroot}%{_libdir}/%{realname}/Tutorials
rm -rf %{buildroot}%{_libdir}/%{realname}/Scripts

# add emacs mode

%files
%{_bindir}/%{realname}
%{_bindir}/%{realname}-convert
%license GPLicense LGPLicense
%doc AUTHORS COPYRIGHT CONTACTING.GENESIS ChangeLog
%exclude %{_libdir}/%{realname}/lib
%exclude %{_libdir}/%{realname}/*make
%{_libdir}/%{realname}
%{_mandir}/man1/*

%files devel
%license GPLicense LGPLicense
%{_includedir}/%{realname}/
%{_libdir}/%{realname}/lib
%{_libdir}/%{realname}/*make

%files doc
%license GPLicense LGPLicense
%doc Doc Hyperdoc Tutorials Scripts

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6.20181209git374cdbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5.20181209git374cdbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4.20181209git374cdbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 2.4-3.20181209git374cdbc
- Rebuild for netcdf 4.6.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2.20181209git374cdbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4-1.20181209git374cdbc
- Add all licenses
- Add gcc to BR
- Add checkout date in timestamp
- Initial build for Fedora repos
- Use latest git commit
