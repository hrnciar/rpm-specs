%global commit0 f93243b000c52b755c70829768d2ae6bcf7bb91a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global commit1 c137076fdd8bfca3d2bf9cdacda9983dbbec599a
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

%global snapdate 20200806

%global __python %{__python3}

Name:          trellis
Version:       1.0
Release:       0.12.%{snapdate}git%{shortcommit0}%{?dist}
Summary:       Lattice ECP5 FPGA bitstream creation/analysis/programming tools
License:       ISC
URL:           https://github.com/SymbiFlow/prj%{name}
Source0:       https://github.com/SymbiFlow/prj%{name}/archive/%{commit0}/prj%{name}-%{shortcommit0}.tar.gz
Source1:       https://github.com/SymbiFlow/prj%{name}-db/archive/%{commit1}/prj%{name}-db-%{shortcommit1}.tar.gz

# Patches:
Patch1:        pdf-doc-build-de5eec3.patch

BuildRequires: cmake gcc-c++
BuildRequires: python3-devel
BuildRequires: boost-python3-devel
# for building docs:
BuildRequires: python-sphinx-latex
BuildRequires: python3-recommonmark
BuildRequires: latexmk
# for building manpages:
BuildRequires: help2man

Requires:      %{name}-data = %{version}-%{release}

%description
Project Trellis enables a fully open-source flow for ECP5 FPGAs using
Yosys for Verilog synthesis and nextpnr for place and route. Project
Trellis provides the device database and tools for bitstream creation.

%package devel
Summary:       Development files for Project Trellis
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-data = %{version}-%{release}

%description devel
Development files to build packages using Project Trellis

%package data
Summary:       Project Trellis - Lattice ECP5 Bitstream Database
BuildArch:     noarch

%description data
This package contains the bitstream documentation database for
Lattice ECP5 FPGA devices.

%prep
%setup -q -n prj%{name}-%{commit0} -a 1
rm -rf database
mv prj%{name}-db-%{commit1} database
%patch1 -p1
# add "-fPIC -g1" to CMAKE_CXX_FLAGS:
# (NOTE: "-g1" reduces debuginfo verbosity over "-g", which helps on armv7hl)
sed -i '/CMAKE_CXX_FLAGS/s/-O3/-O3 -fPIC -g1/' libtrellis/CMakeLists.txt
# prevent "lib64" false positive (e.g., on i386):
sed -i 's/"lib64"/"lib${LIB_SUFFIX}"/' libtrellis/CMakeLists.txt
# fix shebang lines in Python scripts:
find . -name \*.py -exec sed -i 's|/usr/bin/env python3|/usr/bin/python3|' {} \;
# remove .gitignore files in examples:
find . -name \.gitignore -delete

%build
# building manpages requires in-source build:
%define __cmake_in_source_build 1
# disable LTO to allow building for f33 rawhide (BZ 1865586):
%define _lto_cflags %{nil}
%cmake libtrellis -DCURRENT_GIT_VERSION=%{version}-%{release}
%cmake_build
%make_build -C docs latexpdf
# build manpages:
mkdir man1
for f in ecp*
do
  [ -x $f ] || continue
  LD_PRELOAD=./libtrellis.so \
    help2man --no-discard-stderr --version-string %{version} -N \
             -o man1/$f.1 ./$f
  sed -i '/required but missing/d' man1/$f.1
done

%install
%cmake_install
install -Dpm644 -t %{buildroot}%{_mandir}/man1 man1/*

%check
# nothing to do for now.

%files
%license COPYING
%doc README.md
%doc docs/_build/latex/ProjectTrellis.pdf
%doc examples
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libtrellis.so
%{_datadir}/%{name}/misc
%{_mandir}/man1/ecp*.1*

%files devel
%doc libtrellis/examples
%{_libdir}/%{name}/pytrellis.so
%{_datadir}/%{name}/timing
%{_datadir}/%{name}/util

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/database

%changelog
* Thu Aug 06 2020 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.12.20200806gitf93243b
- Update to newer snapshot.
- Disable LTO for f33 rebuild (BZ 1865586)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.20200127git30ee6f2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.10.20200127git30ee6f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 1.0-0.9.20200127git30ee6f2
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-0.8.20200127git30ee6f2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.7.20200127git30ee6f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.6.20200127git30ee6f2
- Update to newer snapshot.
- Fix Python 3.9 build (BZ #1793496).
- Fix pdf doc build (upstream requires obscure python/sphinx dependency).

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-0.5.20190806git7e97b5b
- Rebuilt for Python 3.8

* Tue Aug 06 2019 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.4.20190806git7e97b5b
- Update to newer snapshot.
- Fix python 3.8 build (BZ #1737016).

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.3.20190327gitf1b1b35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.2.20190327gitf1b1b35
- Update to newer snapshot.
- Fix library suffix mis-detection on i686.

* Wed Mar 20 2019 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.1.20190320git26d6667
- Initial version.
