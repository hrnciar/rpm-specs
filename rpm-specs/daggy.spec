%undefine __cmake_in_source_build
%global _vpath_srcdir src

Name:           daggy
Version:        2.0.2
Release:        2%{?dist}
Summary:        Data Aggregation Utility

License:        MIT
URL:            https://github.com/synacker/daggy
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  gcc-c++
BuildRequires:  mustache-devel
BuildRequires:  libssh2-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  cmake


%description
Server-less remote or local data aggregation and 
streaming.

Daggy main goals are simplicity and ease-of-use. 

Daggy is server-less, cross-platform solution and 
don't require installation on remote servers. 
Aggregation and streaming work under SSH transport protocol 
or via local processes execution.

Daggy can be helpful for developers, QA, DevOps and 
engineers for debug, analyze and control 
distributed network systems, for example, 
based on micro-service architecture.

%package devel
Summary: Development files for %{name}

%description devel
%{summary}

%prep
%autosetup
sed -i 's|kainjow/mustache.hpp|mustache.hpp|' src/Daggy/Precompiled.h

%build
%cmake -DVERSION=%{version} src
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/libDaggyCore.so

%post
daggy --version

%files devel
%{_includedir}/DaggyCore

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Mikhail Milovidov <milovidovmikhail@gmail.com> - 2.0.2-1
- Update up to 2.0.2 version

* Tue Apr 07 2020 Mikhail Milovidov <milovidovmikhail@gmail.com> - 2.0.1-1
- Update up to 2.0.1 version. Fix typos in description

* Sun Apr 05 2020 Mikhail Milovidov <milovidovmikhail@gmail.com>
- Update to 2.0.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Benjamin Kircher <bkircher@0xadd.de> - 1.1.3-3
- Rebuild for botan2-2.13

* Fri Oct 18 2019 Richard Shaw <hobbes1069@gmail.com> - 1.1.3-2
- Rebuild for yaml-cpp 0.6.3.

* Thu Jul 25 2019 Mikhail Milovidov <milovidovmikhail@gmail.com> - 1.1.3-1
- Update to 1.2.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Mikhail Milovidov <milovidovmikhail@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Fri Jun 21 2019 Mikhail Milovidov <milovidovmikhail@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Sun Jun 16 20:04:20 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue Mar 19 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sat Mar 16 2019 Mikhail Milovidov <milovidovmikhail@gmail.com> - 1.0.0-1
- Initial rpm release
