%global tilp_version 1.18

Name:           libticalcs2
Version:        1.1.9
Release:        10%{?dist}
Summary:        Texas Instruments calculator communication library

License:        GPLv2+
URL:            https://sourceforge.net/projects/tilp/
Source0:        http://sourceforge.net/projects/tilp/files/tilp2-linux/tilp2-%{tilp_version}/%{name}-%{version}.tar.bz2

BuildRequires:  glib2-devel, pkgconfig, libticonv-devel, libticables2-devel, libtifiles2-devel, tfdocgen, gettext
BuildRequires:  autoconf, automake, libtool, gettext-devel

%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc

Summary:        HTML documentation for %{name}
BuildArch:      noarch

%description
The ticalcs library is a library which brings about all the
functions needed to communicate with a Texas Instruments
graphing calculator (or hand-held). Currently, it does not
support some education devices (such as CBL/CBR and others).
This library is able to communicate with handhelds in a fairly
transparent fashion. With this library, the developer does not
have to worry about the packet oriented protocol, the file
management and some other stuff.

%description devel
Include files and libraries for developing applications
to work with libticalcs.

%description doc
HTML documentation for linking and developing applications
using libticalcs2.

%prep
%setup -q
sed -i 's/\r$//' docs/html/style.css
rm po/fr.gmo

# Run auto(re)conf.
autoreconf --force --install

%build
%configure --disable-static
make %{?_smp_mflags}
make -C po fr.gmo

%check
make -C tests check

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libticalcs2.la
rm -rf %{buildroot}%{_docdir}/%{name}/html
rm -f %{buildroot}%{_docdir}/%{name}/COPYING
%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%{_libdir}/libticalcs2.so.*
%doc README AUTHORS ChangeLog
%license COPYING

%files doc
%doc docs/html README AUTHORS ChangeLog
%license COPYING

%files devel
%{_includedir}/tilp2/*.h
%{_libdir}/pkgconfig/ticalcs2.pc
%{_libdir}/libticalcs2.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Ben Rosser <rosser.bjr@gmail.com> - 1.1.9-1
- Updated to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.8-4
- Removed a redundancy in the spec file; only install documentation once.

* Thu Jul 02 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.8-3
- Added a line endings fix for one of the CSS documentation files.
- Removed duplicate include of the localization file.
- Switched the define macro to a global macro.

* Wed Jul 01 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.8-2
- Added missing gettext dependency to build-requires.

* Mon Apr 13 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.8-1
- Bumped release from 0 to 1.
- Added a docs subpackage for HTML documentation.
- Changed spec to run test suite.
- Changed spec to generate localization files using find_lang.

* Sat Apr 20 2013 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.8-0
- Updated to latest upstream version of tilp

* Wed Jul 11 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.7-2
- Added full documentation, built by tfdocgen

* Thu Jul 05 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.7-1
- Moved pkgconfig file and non-versioned *.so  to devel package
- Removed libtool archive from the package
- Package now depends on devel subpackages of other libti* libraries

* Tue Jun 19 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.7-0
- Updated to version 1.1.7
- Added new -devel subpackage for the include files
- Vastly improved spec file

* Sat Jul 30 2011 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.6-0
- Initial version of the package
