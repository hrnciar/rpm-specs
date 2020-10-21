Summary:       Libraries to move files to a trash-folder on delete
Name:          libtrash
Version:       3.6
Release:       1%{dist} 
License:       GPLv2+
URL:           http://pages.stern.nyu.edu/~marriaga/software/libtrash
Source:        http://pages.stern.nyu.edu/~marriaga/software/libtrash/%{name}-%{version}.tgz
Patch0:        libtrash-3.2-defaults.patch
Patch1:        libtrash-3.2-makefile.patch
Patch2:        libtrash-3.3-license.patch

BuildRequires: gcc
BuildRequires: perl-interpreter
BuildRequires: perl(English)
BuildRequires: python3

%description
Libtrash is the shared library which, when preloaded, implements a trash
can under GNU/Linux. Through the interception of function calls which 
might lead to accidental data loss libtrash effectively ensures that your 
data remains protected from your own mistakes.

%package devel
Summary: Libraries to move files to a trash-folder on delete
License: GPLv2+
Requires: libtrash = %{version}-%{release}

%description devel
This package contains the libtrash.so dynamic library which, when preloaded,
implements a trash can under GNU/Linux.

%prep
%autosetup -p1

# enforce use of python3 during the build
sed -e 's|print \(.*\)$|print(\1)|' -i scripts/get_symbol_versions.py
sed -e 's|python|python3|' -i src/Makefile

%build
# -D_REENTRANT: keep up to date with src/Makefile
make CFLAGS="$RPM_OPT_FLAGS -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_sysconfdir}}

make install INSTLIBDIR=$RPM_BUILD_ROOT%{_libdir} SYSCONFFILE=$RPM_BUILD_ROOT%{_sysconfdir}/libtrash.conf

rm -f $RPM_BUILD_ROOT/%{_libdir}/libattr.so.3
ln -sf libtrash.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libtrash.so.3

%ldconfig_scriptlets

%files
%doc README.md TODO COPYING CHANGE.LOG config.txt 
%attr(644, root, root) %{_sysconfdir}/libtrash.conf
%config(noreplace) %{_sysconfdir}/libtrash.conf
%{_libdir}/libtrash.so.*

%files devel
%{_libdir}/libtrash.so

%changelog
* Thu Aug 06 2020 Kamil Dudka <kdudka@redhat.com> - 3.6-1
- update to new upstream release

* Tue Aug 04 2020 Kamil Dudka <kdudka@redhat.com> - 3.5-1
- use `readelf -s -W` to avoid truncation of long symbol names (#1864057)
- update to new upstream release

* Tue Aug 04 2020 Kamil Dudka <kdudka@redhat.com> - 3.3-17
- require perl(English) for build (#1864057)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com> - 3.3-10
- enforce use of python3 during the build
- add explicit BR for the gcc compiler

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 08 2016 Kamil Dudka <kdudka@redhat.com> - 3.3-5
- update FSF addresss in the license file to silence rpmlint

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Kamil Dudka <kdudka@redhat.com> - 3.3-1
- update to new upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Kamil Dudka <kdudka@redhat.com> - 3.2-14
- avoid symbol clashes when loading audacious plug-ins (#1096443)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 22 2009 Zdenek Prikryl <zprikryl@redhat.com> 3.2-7
- Fixed usage of RPM_OPT_FLAGS

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Zdenek Prikryl <zprikryl@redhat.com> 3.2-5
- Fixed permissions on config file

* Wed Jul 09 2008 Zdenek Prikryl <zprikryl@redhat.com> 3.2-4
- Added documentation to devel package
- Minor spec clean up

* Wed Jul 02 2008 Zdenek Prikryl <zprikryl@redhat.com> 3.2-3
- Create devel package

* Tue Jul 01 2008 Zdenek Prikryl <zprikryl@redhat.com> 3.2-2
- Package for Fedora 10

* Thu Mar 06 2008 Zdenek Prikryl <zprikryl@redhat.com> 3.2-1
- Package for Fedora 9

