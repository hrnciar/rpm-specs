%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:		luckybackup
Version:	0.4.9
Release:	7%{?dist}
Summary:	A powerful, fast and reliable backup and sync tool

License:	GPLv3+
URL:		http://luckybackup.sourceforge.net/index.html
Source0:	http://downloads.sourceforge.net/project/%{name}/%{version}/source/%{name}-%{version}.tar.gz
Source1:	%{name}.policy

BuildRequires:	qt-devel
Buildrequires:	desktop-file-utils
Buildrequires:	gcc-c++
Requires:	polkit

%description
luckyBackup is an application that backs-up and/or synchronizes any 
directories with the power of rsync.

It is simple to use, fast (transfers over only changes made and not all data), 
safe (keeps your data safe by checking all declared directories before 
proceeding in any data manipulation ), reliable and fully customizable.

%prep
%setup -q
sed -i 's,/usr/share/doc/luckybackup,%{_pkgdocdir},' luckybackup.pro
sed -i 's,/usr/share/doc/luckybackup/license/gpl.html,%{_pkgdocdir}/license/gpl.html,' src/global.h
sed -i 's,/usr/share/doc/luckybackup/manual/index.html,%{_pkgdocdir}/manual/index.html,' src/global.h
sed -i 's,su-to-root -X -c,/usr/bin/pkexec,' menu/%{name}-gnome-su.desktop
sed -i '/Fedora users/d' manual/index.html
chmod a-x manual/index.html

%build
%{qmake_qt4}
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
INSTALL_ROOT=%{buildroot} \
  make install DESTDIR=%{buildroot}
install -m 0755 -d %{buildroot}%{_datadir}/polkit-1/actions/
install -m 0644 -p %{SOURCE1} %{buildroot}%{_datadir}/polkit-1/actions/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-kde-su.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gnome-su.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc readme/README readme/changelog
%license license/gpl.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*
%{_datadir}/polkit-1/actions/%{name}.policy
%{_datadir}/%{name}
%{_datadir}/man/man8/*.8.*
%{_datadir}/menu
%{_datadir}/pixmaps/%{name}*
%{_docdir}/%{name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Michael J Gruber <mjg@fedoraproject.org> - 0.4.9-3
- Adjust to new guidelines (BR gcc)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Michael J Gruber <mjg@fedoraproject.org> - 0.4.9-1
- new version (with bugfixes)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Michael J Gruber <mjg@fedoraproject.org> - 0.4.8-9
- replace beesu by pkexec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Michael J Gruber <mjg@fedoraproject.org> - 0.4.8-7
- fix F24 FTBFS

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.4.8-6
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.8-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 - Michael J Gruber <mjg@fedoraproject.org> 0.4.8-1
- luckybackup 0.4.8

* Mon Nov 11 2013 - Michael J Gruber <mjg@fedoraproject.org> 0.4.7-5
- follow F20 unversioned docdir change (bug #993914)
- spec cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 15 2012 Michael J Gruber <mjg@fedoraproject.org> 0.4.7-1
- luckybackup 0.4.7
- fix spurious x bits on html manual

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 15 2011 Michael J Gruber <mjg@fedoraproject.org> 0.4.6-1
- luckybackup 0.4.6

* Thu Mar 10 2011 Michael J Gruber <mjg@fedoraproject.org> 0.4.5-1
- luckybackup 0.4.5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 01 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.4.4-1
- luckybackup 0.4.4 bugfix release

* Sun Sep 05 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.4.3-1
- luckybackup 0.4.3 bugfix release

* Sun Aug 29 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.4.2-1
- luckybackup 0.4.2 bugfix release

* Thu Jun 17 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.4.1-1
- luckybackup 0.4.1 bugfix release

* Wed May 19 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.4.0-1
- luckybackup 0.4.0 fixes and improvements

* Sun Mar 07 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.3.5-3
- replace consolekit solution to default (upstream) behavior user and root
- fixes bug #570804
- added Requires beesu

* Mon Feb 15 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.3.5-2
- Added missing files
- Fixes Bug 565428

* Mon Jan 11 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.3.5-1
- update to source 0.3.5
- removed luckybackup.desktop

* Thu Nov 26 2009 Thomas Janssen <thomasj@fedoraproject.org> 0.3.3-1
- Initial Fedora release
