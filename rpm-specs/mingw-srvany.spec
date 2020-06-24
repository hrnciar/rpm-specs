%{?mingw_package_header}

# Only build the 32 bit package.
%global mingw_build_win32 1
%global mingw_build_win64 0

%global gitdate 20150115
%global commit fd659e77cdd9da484fdc9dcbe0605c62ec26fa30
%global shortcommit fd659e77

Name:		mingw-srvany
Version:	1.0
Release:	24.%{gitdate}git%{shortcommit}%{?dist}
Summary:	Utility for creating services for Windows

License:	GPLv2+
BuildArch:	noarch

URL:		http://github.com/rwmjones/rhsrvany
Source0:	https://github.com/rwmjones/rhsrvany/archive/%{commit}/rhsrvany-%{commit}.tar.gz
Source1:	COPYING

# Needed because we build from the git version, using autoreconf.
BuildRequires:	automake autoconf libtool

BuildRequires:	mingw32-filesystem
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-gcc-c++


%description
Utility for creating a service from any MinGW Windows binary


%package -n mingw32-srvany
Summary:	Utility for creating services for Windows


%description -n mingw32-srvany
Utility for creating a service from any MinGW Windows binary


%{?mingw_debug_package}


%prep
%setup -q -n rhsrvany-%{commit}
cp %{SOURCE1} .


%build
autoreconf -i
%{mingw32_configure}
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install


%files -n mingw32-srvany
%doc COPYING
%{mingw32_bindir}/rhsrvany.exe


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24.20150115gitfd659e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23.20150115gitfd659e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22.20150115gitfd659e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21.20150115gitfd659e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20.20150115gitfd659e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19.20150115gitfd659e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18.20150115gitfd659e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17.20150115gitfd659e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-16.20150115gitfd659e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar  4 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0-15
- Update to 20150115.
- Includes fix for out of bounds array read (RHBZ#1187226).
- Set macros so we only build the 32 bit target.

* Tue Jul  8 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0-14
- Various packaging fixes (RHBZ#1117291).
- Put git version into release tag.
  https://fedoraproject.org/wiki/Packaging:NamingGuidelines#Release_Tag

* Tue Jul  8 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0-13
- Switch to upstream version instead of fork.
- There is no documentation upstream, but include a COPYING file.
- The program is called 'rhsrvany.exe' (not srvany, which is a MSFT program).
- Run rpmlint and fix problems.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.0-8
- Renamed the source package to mingw-srvany (#801031)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0-7
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 3 2010 Andrew Beekhof <andrew@beekhof.net> - 1.0-4
- Fixed the license tag

* Mon Oct 25 2010 Andrew Beekhof <andrew@beekhof.net> - 1.0-3
- Incorporate feedback from Fedora review

* Mon Sep 13 2010 Andrew Beekhof <andrew@beekhof.net> - 1.0-1
- Initial build.
