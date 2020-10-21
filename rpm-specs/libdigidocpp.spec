Name:           libdigidocpp

Version:        3.14.4
Release:        1%{?dist}

Summary:        Library offers creating, signing and verification of digitally signed documents
License:        LGPLv2+
URL:            https://github.com/open-eid/libdigidocpp
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz


%if 0%{?el7}
BuildRequires: cmake3
%else
BuildRequires: cmake
%endif
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(openssl)
BuildRequires:  xml-security-c-devel
BuildRequires:  xsd
%if 0%{?fedora} >= 30
BuildRequires:  minizip-compat-devel
%else
BuildRequires:  pkgconfig(minizip)
%endif
# Provide xxd
BuildRequires:  vim-common

# Dynamically loaded libraries
Requires:       opensc%{?_isa}

%description
Libdigidocpp library offers creating, signing and verification of digitally
signed documents, according to XAdES and XML-DSIG standards. Documentation
http://open-eid.github.io/libdigidocpp


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation provided by upstream.

%prep
%setup -q

# it contains non UTF-8 files, but they do not worth the process of
# unpackaging and fixing the encoding
rm -rf doc/sample_files.zip

# Remove bundled minizip
rm -rf src/minizip

%build

%if 0%{?el7}
%{cmake3} . \
 -DCMAKE_INSTALL_SYSCONFDIR=/etc \
 -DSWIG_EXECUTABLE=SWIG_EXECUTABLE-NOTFOUND
%else
%{cmake} . \
 -DCMAKE_INSTALL_SYSCONFDIR=/etc \
 -DSWIG_EXECUTABLE=SWIG_EXECUTABLE-NOTFOUND
%endif

%if ((0%{?el} >= 9) || (0%{?fedora} >= 33))
%cmake_build
%else
%make_build
%endif

%install

%if ((0%{?el} >= 9) || (0%{?fedora} >= 33))
%cmake_install
%else
%make_install
%endif

%if 0%{?fedora} <= 28 || 0%{?el7}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%doc AUTHORS README.md CONTRIBUTING.md RELEASE-NOTES.md
%license COPYING LICENSE.LGPL
%{_libdir}/*.so.*
%dir %{_sysconfdir}/digidocpp
%config(noreplace) %{_sysconfdir}/digidocpp/digidocpp.conf
%{_sysconfdir}/digidocpp/798.p12
%{_sysconfdir}/digidocpp/schema/
%{_bindir}/digidoc-*
%{_mandir}/man1/digidoc-tool.1.*

%files devel
%doc AUTHORS README.md CONTRIBUTING.md RELEASE-NOTES.md
%license COPYING
%{_includedir}/digidocpp/
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/*.so

%files doc
%doc AUTHORS README.md CONTRIBUTING.md RELEASE-NOTES.md doc/*
%license COPYING


%changelog
* Sun Sep 27 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 3.14.4-2
- Fix attempting to package missing docs breaking the build

* Sun Sep 27 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 3.14.4-1
- Upstream release 3.14.4

* Sun Sep 27 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 3.14.3-4
- Fixing the build for F33

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 3.14.3-1
- Upstream release 3.14.3 

* Fri Jan 31 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 3.14.2-2
- Switch to tarball with git submodules checked out

* Fri Jan 31 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 3.14.2-1
- Upstream release 3.14.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Dmitri Smirnov <dmitri@smirnov.ee> - 3.14.1-1
- Upstream release 3.14.1
- Removed percentage sign from package changelog causing rpmlint warning

* Sun Sep 08 2019 Dmitri Smirnov <dmitri@smirnov.ee> - 3.14.0-3
- Fix changelog notes

* Sun Sep 08 2019 Dmitri Smirnov <dmitri@smirnov.ee> - 3.14.0-2
- Upstream release 3.14.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 2019 Dmitri Smirnov <dmitri@smirnov.ee> - 3.13.9-1
- Upstream release 3.13.9

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 3.13.8-1
- Update to 3.13.8

* Fri Nov 16 2018 Pete Walter <pwalter@fedoraproject.org> - 3.13.7-1
- Update to 3.13.7

* Fri Nov 16 2018 Pete Walter <pwalter@fedoraproject.org> - 3.13.6-9
- Rebuild for xml-security-c 2.0

* Tue Aug 28 2018 Patrik Novotný <panovotn@redhat.com> - 3.13.6-8
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.6-6
- moved BuildRequires:  gcc-c++ outside any macro scope

* Wed Jul 11 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.6-5
- moved BuildRequires: gcc and BuildRequires:  gcc-c++ inside 0%%{?fedora} > 28 macro scope

* Wed Jul 11 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.6-4
- moved BuildRequires: gcc and BuildRequires:  gcc-c++ outside el7 macro scope

* Tue Jul 10 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.6-3
- /sbin/ldconfig scripts no longer needed on >F28 because glibc has filetrigger marcos which makes execution /sbin/ldconfig obsolete
- Removed uneeded Requires: openssl-devel xml-security-c-devel xsd in devel package

* Mon Jun 25 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 3.13.6-2
- Provide tarball consistent with the upstream

* Wed Jun 13 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 3.13.6-1
- 3.13.6 release

* Tue May 01 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.5-2
- removed rm -rf src/openssl
- removed UTF-8 conversion scripts for AUTHORS and COPYING files

* Mon Apr 30 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.5-1
- 3.13.5 release

* Wed Feb 28 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.2-4
- added macros for cmake 3 in EPEL 7

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.13.2-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Germano Massullo <germano.massullo@gmail.com> - 3.13.2-1
- 3.13.2 release
- Removed opensslv1.1 patch because no longer necessary
- Adjusted docs file names
- Removed Requires: libdigidoc-devel and BuildRequires: libdigidoc-devel because libdigidoc uses OpenSSL 1.0 that conflicts with OpenSSL 1.1.  libdigidocpp should then use online SiVa validator for ddoc files (libdigidoc was used to handle such kind of files)
- updated summary and description
- replaced make %%{?_smp_mflags} with %%make_build (see package review #1519747)
- replaced make install DESTDIR=%%{buildroot} with %%make_install (see package review #1519747)
- removed line %%clean and rm -rf %%{buildroot} (see package review #1519747)
- license file attached to %%license macro, instead of %%doc macro (see package review #1519747)
- replaced lines Requires: %%{name} = %%{version}-%%{release} with Requires: %%{name}%%{?_isa} = %%{version}-%%{release} (see package review #1519747)
- UTF-8 AUTHORS version of AUTHORS file (see package review #1519747)
- Replaced BuildRequires: openssl-devel and BuildRequires: minizip-devel with BuildRequires: pkgconfig(openssl) and BuildRequires: pkgconfig(minizip) (see package review #1519747)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 24 2017 Mihkel Vain <mihkel@fedoraproject.org> - 3.12.3-1
- New upstream release
- Add openssl v1.1 support via libdigidocpp-opensslv1.1.patch
- Remove bundled openssl

* Sun Feb 19 2017 Mihkel Vain <mihkel@fedoraproject.org> - 3.12.2-3
- Remove bundled minizip

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 10 2016 Mihkel Vain <mihkel@fedoraproject.org> - 3.12.2-1
- New upstream release

* Thu May 19 2016 Mihkel Vain <mihkel@fedoraproject.org> - 3.12.1-1
- New upstream release

* Tue Feb 02 2016 Mihkel Vain <mihkel@fedoraproject.org> - 3.12.0-1
- New upstream release

* Tue Sep 22 2015 Mihkel Vain <mihkel@fedoraproject.org> - 3.11.1.1306-1
- New upstream release

* Mon Jul 13 2015 Mihkel Vain <mihkel@fedoraproject.org> - 3.11.0.1296-1
- New upstream release
- Spec file cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Mihkel Vain <mihkel@fedoraproject.org> - 3.10.0-2
- Rebuild for gcc5

* Sat Mar 28 2015 Mihkel Vain <mihkel@fedoraproject.org> - 3.10.0-1
- New upstream release
- Project moved to github

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0.1237-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul  3 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.9.0.1237-1
- New upstream release
- Create a separate sub-package for docs

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0.1208-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.0.1208-3
- Fix typo: ppython-digidoc -> python-digidoc

* Wed Apr 30 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.0.1208-2
- Use cmake macro
- Obsolete old subpackages

* Thu Apr 24 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.0.1208-1
- First package based on new source code from RIA

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.3.0-19
- Perl 5.18 rebuild

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 0.3.0-18
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 0.3.0-15
- Perl 5.16 rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-14
- Rebuilt for c++ ABI breakage

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 0.3.0-13
- build against php 5.4.0
- add %%check for php extension
- %%config flag for digidoc.ini

* Thu Jan 19 2012 Ralf CorsÃ©pius <corsepiu@fedoraproject.org> - 0.3.0-12
- Add libdigidocpp-0.3.0-gcc47.patch (Fix mass rebuild FTBFS).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 0.3.0-10
- RPM 4.9 dependency filtering added

* Mon Jun 20 2011 Petr Sabata <contyk@redhat.com> - 0.3.0-9
- Perl mass rebuild
- Removing now obsolete Buildroot and defattr

* Fri Apr 15 2011 Kalev Lember <kalev@smartlink.ee> - 0.3.0-8
- Rebuilt for lib11 0.2.8 soname bump

* Wed Mar 16 2011 Antti Andreimann <Antti.Andreimann@mail.ee> 0.3.0-7
- Rebuilt with xml-security-c 1.6.0

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 0.3.0-6
- Cleaned up php conditionals not needed in current Fedora releases

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 0.3.0-5
- Rebuilt with xerces-c 3.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 20 2010 Kalev Lember <kalev@smartlink.ee> - 0.3.0-3
- Updated descriptions for bindings subpackages, thanks to Sander Lepik.

* Tue Oct 12 2010 Kalev Lember <kalev@smartlink.ee> - 0.3.0-2
- Remove bundled minizip in prep

* Mon Oct 11 2010 Kalev Lember <kalev@smartlink.ee> - 0.3.0-1
- Update to 0.3.0
- Renamed binding subpackages to use <language>-digidoc naming scheme
- Filter shared object provides in private directories
- Added missing defattr lines
- Marked digidocpp.conf as noreplace

* Thu Jul 01 2010 Antti Andreimann <Antti.Andreimann@mail.ee> - 0.2.0-0.7.svn2811
- Added language bindings for Python, Perl and PHP

* Mon Mar 29 2010 Kalev Lember <kalev@smartlink.ee> - 0.2.0-0.6.svn2681
- Spec file clean up
- Updated summary
- Removed BR: pkcs11-helper-devel
- Removed libdigidoc++ obsoletes/provides
- Removed R: pkgconfig which is now automatically picked up by rpm
- Added AUTHORS and COPYING docs
- Cleaned up nightly build changelog entries

* Sat Feb 13 2010 Kalev Lember <kalev@smartlink.ee> - 0.2.0-0.4.svn2528
- rebuilt with new xerces-c 3.0 (F13)

* Thu Jan 21 2010 Kalev Lember <kalev@smartlink.ee> - 0.2.0-0.2.svn2454
- rebuilt with new libp11

* Sun Jun 14 2009 Kalev Lember <kalev@smartlink.ee> - 0.0.12-0.1.svn712
- Initial RPM release.
