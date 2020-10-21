Name:           gio-qt
Version:        0.0.9
Release:        3%{?dist}
Summary:        Gio wrapper for Qt applications 
License:        LGPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core) >= 5.6.3
BuildRequires:  glibmm24-devel
BuildRequires:  cmake >= 3.12.4
BuildRequires:  doxygen
BuildRequires:  qt5-doctools 
# for test
BuildRequires:  pkgconfig(Qt5Test)


%description
This package provides a GIO wrapper class for Qt.


%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?isa}
Requires:       glibmm24-devel%{?isa}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
# fix doc path
sed -i 's|qt5/doc|doc/qt5|' CMakeLists.txt

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
# make test will not work here, manually run tests
%{_target_platform}/test/tst_dgiosettings
%{_target_platform}/test/tst_simplefileinfo
%{_target_platform}/test/tst_matchgioenum

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_qt5_docdir}/%{name}.qch


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0.0.9-2
- change to fit new cmake macros

* Tue Jun 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0.0.9-1
- Initial Build, code mostly taken from copr: cheeselee/deepin-20-testing
- Add tests

