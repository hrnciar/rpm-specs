%define src_ver 2.2.1

Name:           kdevelop-pg-qt
Summary:        A parser generator
Version:        2.2.1
Release:        1%{?dist}
# All LGPLv2+, except for bison-generated kdev-pg-parser.{cc.h} which are GPLv2+
License:        LGPLv2+ and GPLv2+ with exception
URL:            http://techbase.kde.org/Development/KDevelop-PG-Qt_Introduction
Source0:        http://download.kde.org/stable/kdevelop-pg-qt/%{version}/src/kdevelop-pg-qt-%{src_ver}.tar.xz

## FTBFS s390x
ExcludeArch: s390x

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

# For AutoReq cmake-filesystem
BuildRequires:  cmake

%description
KDevelop-PG-Qt is a parser generator written in readable source-code and
generating readable source-code. Its syntax was inspired by AntLR. It
implements the visitor-pattern and uses the Qt library. That is why it
is ideal to be used in Qt-/KDE-based applications like KDevelop.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# went noarch->arch, so be careful on upgrades -- rex
Obsoletes: kdevelop-pg-qt-devel < 1.0.0-1

%description devel
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{src_ver}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files 
%doc AUTHORS README
%license COPYING.LIB
%{_bindir}/kdev-pg-qt

%files devel
%{_includedir}/kdevelop-pg-qt/
%{_libdir}/cmake/KDevelop-PG-Qt/


%changelog
* Mon May 25 2020 Marie Loise Nolden <loise@kde.org> - 2.2.1-1
- 2.2.1
- fixes build with Qt 5.14

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-1
- 2.2.0
- fixes FTBFS, ExcludeArch: s390x (#1675229)
- use %%license, %%make_build

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 2.0.0-5
- Rebuilt for AutoReq cmake-filesystem

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 Helio Chissini de Castro <helio@kde.org> - 2.0.0-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Jan Grulich <jgrulich@redhat.com> - 1.90.92-1
- Update to 1.90.92 (beta 2)

* Fri Oct 30 2015 Jan Grulich <jgrulich@redhat.com> - 1.9.90-1
- Update to 1.9.90 (beta 1)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.0-6
- pull in upstream commits, .spec cleanup

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 26 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.0-1
- 1.0.0

* Mon Jan 23 2012 Radek Novacek <rnovacek@redhat.com> 0.9.82-1
- Update to 0.9.82

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 07 2011 Radek Novacek <rnovacek@redhat.com> 0.9.5-1
- Update to 0.9.5

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.9.0-3
- License: LGPLv2+ and GPLv2+ with exception

* Fri Dec 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.9.0-2
- License: GPLv2+

* Mon Dec 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.9.0-1
- first try

