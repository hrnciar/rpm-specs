Name:           libarcus-lulzbot
Version:        3.6.21
Release:        8%{?dist}
Summary:        Communication library between Cura components, Lulzbot fork
License:        LGPLv3+
URL:            https://code.alephobjects.com/source/arcus
# git clone https://code.alephobjects.com/source/arcus.git
# cd arcus
# git checkout v3.6.21
## CANNOT use git archive here, because we need to scrape the hash for version
# cd ..
# mv arcus libarcus-lulzbot-3.6.21
# tar cvfz libarcus-lulzbot-3.6.21.tar.gz libarcus-lulzbot-3.6.21
Source0:        %{name}-%{version}.tar.gz

# Gonna make this our fork
Patch2:         libArcus-3.6.12-lulzbot.patch
Patch3:         libarcus-lulzbot-3.6.12-find-sip.patch

BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-protobuf
BuildRequires:  python3-sip-devel
BuildRequires:  /usr/bin/sip
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

%description
Arcus library contains C++ code and Python 3 bindings for creating a socket in
a thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code. This is the Lulzbot fork.

%package        devel

# The cmake scripts are BSD
License:        LGPLv3+ and BSD

Summary:        Development files for libarcus, Lulzbot fork
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Arcus library contains C++ code and Python 3 bindings for creating a socket in
a thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code. This is the Lulzbot fork.

Development files.

%package -n     python3-arcus-lulzbot
Summary:        Python 3 libArcus bindings, Lulzbot fork
%if 0%{?fedora} >= 31
Requires:       python3-pyqt5-sip
%else
Requires:       python3-sip
%endif
%{?python_provide:%python_provide python3-arcus-lulzbot}

%description -n python3-arcus-lulzbot
Arcus Python 3 bindings for creating a socket in a thread and using this
socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code. This is the Lulzbot fork.

%prep
%setup -q -n libarcus-lulzbot-%{version}
%patch2 -p1 -b .lulzbot
%patch3 -p1 -b .sipfix

%build
%cmake -DBUILD_EXAMPLES:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=ON .
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_libdir}/cmake/Arcus-lulzbot/ArcusConfig.cmake %{buildroot}%{_libdir}/cmake/Arcus-lulzbot/Arcus-lulzbotConfig.cmake

%files
%license LICENSE
%doc README.md TODO.md
%{_libdir}/libArcus-lulzbot.so.*

%files devel
%license LICENSE cmake/COPYING-CMAKE-SCRIPTS
%doc examples/example.cpp examples/example.proto
%{_libdir}/libArcus-lulzbot.so
%{_includedir}/Arcus-lulzbot
# Own the dir not to depend on cmake:
%{_libdir}/cmake

%files -n python3-arcus-lulzbot
%license LICENSE
%doc README.md TODO.md
%doc examples/example.py
%{python3_sitearch}/Arcus-lulzbot.so

%changelog
* Wed Sep 23 2020 Adrian Reber <adrian@lisas.de> - 3.6.21-8
- Rebuilt for protobuf 3.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 3.6.21-6
- Rebuilt for protobuf 3.12

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.21-5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 3.6.21-3
- Rebuild for protobuf 3.11

* Wed Nov 13 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.21-2
- fix python3-sip dependency issue in f31+

* Mon Oct 21 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.21-1
- update to 3.6.21

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.18-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.18-1
- update to 3.6.18

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.12-3
- add lulzbot fork info to subpackage summaries

* Wed Jul 10 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.12-2
- fix python_provide to refer to this fork
- fix license tag in -devel

* Fri Jun 28 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.12-1
- initial package (based on libarcus package)
