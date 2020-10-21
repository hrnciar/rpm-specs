Name:		callgit
Version:	2.0
Release:	25%{dist}
Summary:	A tool for Ham Radio Operators to look up call-signs on the web
License:	GPLv3
URL:		http://www.hamsoftware.org/
Source0:	http://www.hamsoftware.org/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:    Ham_Icon-1-48.png

BuildRequires: qt-devel
BuildRequires: desktop-file-utils

%description
This program allows you to search for another Ham's name and address
without having a web browser up. It is very simple.

%prep
%setup -q -n %{name}

%build
%{qmake_qt4}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
install -Dpm 755 callgit %{buildroot}/%{_bindir}/%{name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/Ham_Icon-1-48.png 

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/Ham_Icon-1-48.png

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.0-15
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0-13
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 25 2010 Jens Maucher <jensm@fedoraproject.org> - 2.0-5
- Changed desktop-file

* Sat Feb 27 2010 Jens Maucher <jensm@fedoraproject.org> - 2.0-4
- Added Icon

* Sat Feb 20 2010 Jens Maucher <jensm@fedoraproject.org> - 2.0-3
- Changed desktop-file

* Fri Feb 19 2010 Jens Maucher <jensm@fedoraproject.org> - 2.0-2
- Added desktop-file
- Corrected misspellings

* Sat Feb 12 2010 Jens Maucher <jensm@fedoraproject.org> - 2.0-1
- Initial spec file
