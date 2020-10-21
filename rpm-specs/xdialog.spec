%define real_name Xdialog

Name: xdialog
Summary: X11 drop in replacement for cdialog
Version: 2.3.1
Release: 27%{?dist}
License: GPL+
URL: http://xdialog.free.fr

Source0: http://xdialog.free.fr/%{real_name}-%{version}.tar.bz2
Patch0: xdialog-2.3.1-nostrip.patch
# RHBZ #1037393: Fixes a format string vulnerability (via argv[0])
Patch1: xdialog-2.3.1-secure-fprintf.diff

BuildRequires:  gcc
BuildRequires: gtk+-devel >= 1.2.0
BuildRequires: gtk2-devel >= 2.2.0
BuildRequires: gettext

Provides: %{real_name} = %{version}-%{release}
Obsoletes: %{real_name} < %{version}-%{release}

# there is no need for .desktop file since there is a mandatory argument

%description
Xdialog is designed to be a drop in replacement for the cdialog program.
It converts any terminal based program into a program with an X-windows
interface. The dialogs are easier to see and use and Xdialog adds even
more functionalities (help button+box, treeview, editbox, file selector,
range box, and much more).

%prep
%setup -q -n %{real_name}-%{version}
iconv -f latin1 -t utf8 ChangeLog > ChangeLog.utf8
touch -c -r ChangeLog ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog
%patch0 -p1 -b .nostrip
%patch1 -p0 -b .fprintf
touch -c -r configure.nostrip configure
touch -c -r configure.in.nostrip configure.in

%build
# build both the gtk1 and gtk2 versions. Upstream advises not to use 
# the gtk2 version, however the issues with gtk2 version is with non UTF-8 
# locales which should be rare on fedora, and gtk2 has more features.
%configure
make %{?_smp_mflags}
mv src/Xdialog src/Xdialog-gtk1
make clean
%configure --with-gtk2
make %{?_smp_mflags}
sed -i -e 's:%{_datadir}/doc/Xdialog:%{_datadir}/doc/%{name}:g' doc/Xdialog.1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
install -m0755 src/Xdialog-gtk1 %{buildroot}%{_bindir}

rm -rf __dist_html
mkdir -p __dist_html/html
cp -p doc/*.html doc/*.png __dist_html/html
# there are references to the samples in the documentation.
ln -s ../samples __dist_html/html/samples

%find_lang %{real_name}


%files -f %{real_name}.lang
%doc AUTHORS BUGS ChangeLog README
%doc __dist_html/html/ samples/
%license COPYING
%{_mandir}/man1/Xdialog.1*
%{_bindir}/Xdialog
%{_bindir}/Xdialog-gtk1
%exclude %{_docdir}/%{real_name}-%{version}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.1-22
- fix license file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec  3 2013 Matthieu Saulnier <fantom@fedorapeople.org> - 2.3.1-13
- Remove obsolete Group tag
- Remove obsolete BuildRoot tag
- Remove obsolete cleanup buildroot at the beggining of %%install section
- Remove obsolete %%clean section
- Remove obsolete %%defattr tag in %%files section

* Tue Dec  3 2013 Conrad Meyer <cemeyer@uw.edu> - 2.3.1-12
- Fix fprintf() of untrusted format string (#1037393)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.3.1-7
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jun 29 2008 Patrice Dumas <pertusus@free.fr> 2.3.1-3
- add BR gettext

* Wed Jun 25 2008 Patrice Dumas <pertusus@free.fr> 2.3.1-2
- review request cleanups

* Sat Apr  5 2008 Patrice Dumas <pertusus@free.fr> 2.3.1-1
- submit to fedora.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.1.2-1.2
- Rebuild for Fedora Core 5.

* Tue Feb 22 2005 Dag Wieers <dag@wieers.com> - 2.1.2-1
- Updated to release 2.1.2.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 2.1.1-0
- Initial package. (using DAR)
