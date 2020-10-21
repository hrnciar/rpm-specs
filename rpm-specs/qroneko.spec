Name:		qroneko
Version:	0.5.4
Release:	22%{?dist}
Summary:	A qt front end to crontab
License:	GPLv2+ 
URL:		http://qroneko.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		qroneko-0.5.4-CronModel.cpp.patch
Patch1:		qroneko-0.5.4-ExecuteList.cpp.patch

BuildRequires:	qt-devel,desktop-file-utils


%description
qroneko is a scheduling utility which uses crontab as the back-end.
Features and highlights:
 * Smart "Cron Time" Setting.
 * Lists expected execute time.
 * Enables to edit crontab by text

%prep
%setup -q
%patch0 -p0
%patch1 -p0


%build
%{_qt4_qmake} -project -o qroneko.pro
%{qmake_qt4} qroneko.pro
make %{?_smp_mflags}

%install
install -pd $RPM_BUILD_ROOT/%{_bindir}
install -p %{name} $RPM_BUILD_ROOT/%{_bindir}

#menu-entries
install -pdm 755 $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
install -pd $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -p %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps


%files
%{_bindir}/qroneko
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/qroneko*.desktop
%doc README



%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.5.4-13
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.4-11
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.5.4-4
- Fixed buildroot,timestamp and desktop file issues

* Tue Aug 31 2010 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.5.4-3
- Fixed build requirement and add Desktop file and add patch for x86_64 system

* Fri Aug 27 2010 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.5.4-2
- Add doc and fixed LICENSE and URL issue 

* Fri Aug 13 2010 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.5.4-1
- Initial Build
