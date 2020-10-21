%global commit b39a2a502065ec1407417ffacdac2154385bf80f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global snapdate 20200806

Name:		nextpnr
Version:	0
Release:	0.15.%{snapdate}git%{shortcommit}%{?dist}
Summary:	FPGA place and route tool

License:	ISC and BSD and MIT and (MIT or Public Domain)
URL:		https://github.com/YosysHQ/nextpnr
Source0:	https://github.com/YosysHQ/nextpnr/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	libglvnd-devel
BuildRequires:	boost-filesystem
BuildRequires:	boost-thread
BuildRequires:	boost-program-options
BuildRequires:	boost-iostreams
BuildRequires:	qt5-qtconfiguration-devel
BuildRequires:	cmake(QtConfiguration)
BuildRequires:	boost-python3-devel
BuildRequires:	eigen3-devel
# NOTE: remember to update icestorm & trellis before rebuilding nextpnr!!!
BuildRequires:	icestorm >= 0-0.14
BuildRequires:	trellis-devel >= 1.0-0.12

# License: ISC
Provides:	bundled(qtimgui)

# Qt5 enabled fork of QtPropertyBrowser
# License: BSD
Provides:	bundled(QtPropertyBrowser)

# License: MIT
Provides:	bundled(python-console)

# License: (MIT or Public Domain)
Provides:	bundled(imgui) = 1.66-wip


%description
nextpnr aims to be a vendor neutral, timing driven, FOSS FPGA place and
route tool.


%prep
%autosetup -n %{name}-%{commit}
cp 3rdparty/imgui/LICENSE.txt LICENSE-imgui.txt
cp 3rdparty/qtimgui/LICENSE LICENSE-qtimgui.txt
cp 3rdparty/python-console/LICENSE LICENSE-python-console.txt


%build
%cmake . -DARCH=all \
	-DICEBOX_DATADIR=%{_datadir}/icestorm \
	-DTRELLIS_LIBDIR=%{_libdir}/trellis
%cmake_build
# prepare examples doc. directory:
mkdir -p examples/ice40
cp -r ice40/examples/* examples/ice40


%install
%cmake_install


%files
%{_bindir}/nextpnr-generic
%{_bindir}/nextpnr-ice40
%{_bindir}/nextpnr-ecp5
%doc README.md docs examples
%license COPYING
%license LICENSE-imgui.txt
%license LICENSE-qtimgui.txt
%license LICENSE-python-console.txt


%changelog
* Thu Aug 06 2020 Gabriel Somlo <gsomlo@gmail.com> - 0-0.15.20200806gitb39a2a5
- Update to newer snapshot
- Update cmake build commands (fix FTBFS BZ 1864193)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20200129git85f4452
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20200129git85f4452
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Jonathan Wakely <jwakely@redhat.com> - 0-0.12.20200129git85f4452
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-0.11.20200129git85f4452
- Rebuilt for Python 3.9

* Tue Feb 11 2020 Gabriel Somlo <gsomlo@gmail.com> - 0-0.10.20200129git85f4452
- Rebuilt for trellis dependency.

* Wed Jan 29 2020 Gabriel Somlo <gsomlo@gmail.com> - 0-0.9.20200129git85f4452
- Update to newer snapshot.
- Fix Python 3.9 build (BZ #1795549).

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20190821gitc192ba2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Gabriel Somlo <gsomlo@gmail.com> - 0-0.7.20190821gitc192ba2
- Update to newer snapshot
- Spec file: add 'snapdate' variable
- Fix python 3.8 build (BZ #1743893)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.6.20190415gitdb7e850
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20190415gitdb7e850
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Gabriel Somlo <gsomlo@gmail.com> - 0-0.4.20190415gitdb7e850
- Update to newer snapshot

* Mon Apr 01 2019 Gabriel Somlo <gsomlo@gmail.com> - 0-0.3.20190401gitd27ec2c
- Update to snapshot with fast HeAP-based analytical placer
- Package included ice40, ecp5 example projects as documentation

* Thu Mar 21 2019 Lubomir Rintel <lkundrak@v3.sk> - 0-0.2.20190319gitcadbf42
- Enable ecp5

* Tue Mar 19 2019 Lubomir Rintel <lkundrak@v3.sk> - 0-0.1.20190319gitcadbf42
- Initial packaging
