Name: libparserutils
Version: 0.2.4
Release: 2%{?dist}
Summary: A library for building efficient parsers

License: MIT
URL: http://www.netsurf-browser.org/projects/libparserutils/
Source: http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz

BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: netsurf-buildsystem
BuildRequires: pkgconfig(check)

%description
LibParserUtils is a library for building efficient parsers, written in
C. It was developed as part of the NetSurf project.

Features:
* No mandatory dependencies (iconv() implementation optional for
  enhanced charset support)
* A number of built-in character set converters
* Mapping of character set names to/from MIB enum values
* UTF-8 and UTF-16 (host endian) support functions
* Various simple data structures (resizeable buffer, stack, vector)
* A UTF-8 input stream
* Simple C API
* Portable

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%global make_vars COMPONENT_TYPE=lib-shared PREFIX=/usr LIBDIR=%{_lib} DOXYCONF=build/Doxyfile Q=
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="$RPM_LD_FLAGS"

%prep
%autosetup -n %{name}-%{version} -p1

sed -i -e s@-Werror@@ Makefile

%build
make %{?_smp_mflags} %{make_vars} %{build_vars}
make %{?_smp_mflags} docs %{make_vars}

%install
make install DESTDIR=%{buildroot} %{make_vars}

%check
make %{?_smp_mflags} test %{make_vars} %{build_vars}

%files
%doc README
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/parserutils
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license COPYING
%doc build/docs/html

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 David Tardon <dtardon@redhat.com> - 0.2.4-1
- new upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 18 2016 David Tardon <dtardon@redhat.com> - 0.2.3-1
- new upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 David Tardon <dtardon@redhat.com> - 0.2.1-1
- new upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 David Tardon <dtardon@redhat.com> - 0.2.0-1
- new upstream release

* Mon Jan 13 2014 David Tardon <dtardon@redhat.com> - 0.1.2-3
- fix libparserutils.pc

* Tue Jan 07 2014 David Tardon <dtardon@redhat.com> - 0.1.2-2
- build with correct flags

* Wed Dec 25 2013 David Tardon <dtardon@redhat.com> - 0.1.2-1
- initial import
