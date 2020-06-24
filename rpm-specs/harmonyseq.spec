Name:          harmonyseq
Summary:       A MIDI sequencer
Version:       0.16
Release:       30%{?dist}
License:       GPLv3+
URL:           http://harmonyseq.wordpress.com/
Source:        http://launchpad.net/harmonyseq/stable/0.16/+download/harmonySEQ-%{version}.tar.gz
# add missing includes
Patch0:        harmonySEQ-includes.patch
# gcc7 fixes
Patch1:        harmonySEQ-gcc7.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: gtkmm24-devel 
BuildRequires: glibmm24-devel
BuildRequires: alsa-lib-devel 
BuildRequires: liblo-devel
BuildRequires: desktop-file-utils
BuildRequires: autoconf automake gettext-devel

%description
%{name} is a live loop-based MIDI software sequencer intended to aid music 
composers and performers.

%prep
%setup -q -n harmonySEQ-%{version}
%patch0 -p1 -b .includes
%patch1 -p1 -b .gcc7
sed -i -e 's|-O3|%{optflags}|' src/Makefile.am \
  configure.ac 

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%check

%install
make install DESTDIR="%{buildroot}"

%find_lang harmonySEQ
desktop-file-install                                    \
--remove-mime-type="text/x-harmonyseq"                  \
--add-mime-type="text/x-harmonyseq"                     \
--delete-original                                       \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}/%{_datadir}/applications/%{name}.desktop

%files -f harmonySEQ.lang
%doc LICENSE CHANGELOG README examples
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/gnome/*/mimetypes/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.16-25
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 18 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.16-21 
- gcc7 fixes
- added missing includes due to glibmm library change
- include examples in doc

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.16-17
- Rebuilt for GCC 5 C++11 ABI change

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.16-16
- update mime scriptlets

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 01 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.16-14
- Fix FTBS BZ#909783

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.16-12
- Unversioned doc dir change

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.16-9
- Update license to GPLv3+

* Sat Oct 27 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.16-8
- Add missing BR

* Thu Oct 25 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.16-7
- Initial package
