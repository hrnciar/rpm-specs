Name:           liblouisutdml
Version:        2.9.0
Release:        2%{?dist}
Summary:        Braille transcription library for UTDML documents
License:        LGPLv3+
URL:            http://liblouis.org
Source0:        https://github.com/liblouis/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/liblouis/liblouisutdml/commit/566aa66ac29dd24d88cc39e1c7d1d3c9d9365a75
# Fix MIN_NEXT_LINE value
Patch0:         liblouisutdml-hyphenation.patch

# As of liblouis 3.9.0 the log level constants have been prefixed with LOU_
Patch1:         liblouisutdml-loglevel.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  help2man
BuildRequires:  liblouis-devel >= 3.3
BuildRequires:  libxml2-devel
BuildRequires:  texinfo-tex


# gnulib is a copylib that has been granted an exception from the no-bundled-libraries policy
# http://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Copylibs
Provides: bundled(gnulib)

%description
This is a library intended to provide complete braille transcription services
for UTDML (Unified Tactile Document Markup Language) documents. It translates 
into appropriate braille codes and formats according to its style sheet and 
the specifications in the document.

liblouisutdml is the successor of liblouisxml.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{name} is a braille transcription library for UTDML (Unified Tactile
Document Markup Language) documents. The %{name}-devel package contains
libraries and header files for developing applications that use %{name}.


%package utils
Summary: Utilities that convert various file formats into braille
License: GPLv3+
Requires: antiword
Requires: poppler-utils
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
This package provides the command-line utility file2brl that translates XML
or text files into embosser-ready braille files.


%package doc
Summary: Documentation of the library and the corresponding utilities
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description doc
%{name} is a braille transcription library for UTDML (Unified Tactile
Document Markup Language) documents. This package contains the user and
developer documentation of the library and the command-line utilities
provided by %{name}-utils.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
autoreconf --force --install
libtoolize


%build
%configure --disable-static --disable-java-bindings
make %{?_smp_mflags}
make -C doc liblouisutdml.pdf


%install
%make_install
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{_libdir}/liblouisutdml.la
rm -rf %{buildroot}/%{_defaultdocdir}/liblouisutdml


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog README NEWS
%license COPYING.LIB
%{_libdir}/%{name}.so.*
%{_datadir}/%{name}/


%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%files utils
%license COPYING
%{_bindir}/file2brl
%{_mandir}/man1/file2brl.1*


%files doc
%doc doc/copyright-notice 
%doc doc/%{name}.{html,txt,pdf}
%{_infodir}/%{name}.info.*


%changelog
* Mon Sep 07 2020 Martin Gieseking <martin.gieseking@uos.de> - 2.9.0-2
- Use make_install macro.

* Tue Sep 01 2020 Martin Gieseking <martin.gieseking@uos.de> - 2.9.0-1
- Updated to 2.9.0.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Martin Gieseking <martin.gieseking@uos.de> - 2.8.0-1
- Updated to 2.8.0.
- Dropped patch that resolved a build issue (applied upstream).
- Dropped patch that fixed an issue with ODF headings (applied upstream).
- Included license files with %%license instead of %%doc.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Martin Gieseking <martin.gieseking@uos.de> - 2.7.0-6
- Dropped Java subpackage due to removal of dependencies.
- Added patch to fix build issues introduced with liblouis 3.9.0.

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 2.7.0-5
- Remove obsolete requirements for %%post/%%preun scriptlets

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Martin Gieseking <martin.gieseking@uos.de> - 2.7.0-3
- Rebuilt for liblouis 3.8.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Martin Gieseking <martin.gieseking@uos.de> - 2.7.0-1
- Updated to 2.7.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Martin Gieseking <martin.gieseking@uos.de> 2.5.0-1
- Updated to new release.
- Removed testTranslateString and tripleTrans from utils subpackage (no longer part of liblouisutdml).
- Replaced Requires: java with Requires: java-headless

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Martin Gieseking <martin.gieseking@uos.de> 2.4.0-1
- Updated to new release.

* Sat Mar 23 2013 Martin Gieseking <martin.gieseking@uos.de> 2.3.1-3
- Added missing BR: perl-Carp required to build for f20

* Sat Mar 23 2013 Martin Gieseking <martin.gieseking@uos.de> 2.3.1-2
- Rebuilt with recent autoconf for https://bugzilla.redhat.com/show_bug.cgi?id=925789

* Wed Feb 06 2013 Martin Gieseking <martin.gieseking@uos.de> 2.3.1-1
- Updated to new release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Martin Gieseking <martin.gieseking@uos.de> 2.0.2-1
- Updated to release 2.0.2.
- Dropped patch since the scripts have been removed from the tarball

* Fri May 20 2011 Martin Gieseking <martin.gieseking@uos.de> 1.9.0-2
- Added missing Requires: poppler-utils to -utils package.
- Replaced xml2brl calls with file2brl in helper scripts.
- Dropped rtf2brl because required dependency rtf2xml is not yet available in Fedora.

* Fri May 20 2011 Martin Gieseking <martin.gieseking@uos.de> 1.9.0-1
- Updated to release 1.9.0.

* Mon Apr 04 2011 Martin Gieseking <martin.gieseking@uos.de> 1.7.0-4
- Made -doc subpackage depend on base package.

* Fri Apr 01 2011 Martin Gieseking <martin.gieseking@uos.de> 1.7.0-3
- Dropped buildroot stuff.
- Added Requires: antiword to the -utils package as it's needed by msword2brl.
- Added Requires: jpackage-utils to the -java package.
- Excluded lbu_devonly because it segfaults.
- Moved documentation to -doc subpackage.

* Tue Mar 22 2011 Martin Gieseking <martin.gieseking@uos.de> 1.7.0-2
- Added missing BR: texinfo-tex.
- Added version info to Provides: bundled(gnulib).

* Tue Feb 15 2011 Martin Gieseking <martin.gieseking@uos.de> 1.7.0-1
- Initial Fedora package.
