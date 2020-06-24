# The base of the version (just major and minor without point)
%global base_version 1.10

Name:           libcutl
Version:        %{base_version}.0
Release:        18%{?dist}
Summary:        C++ utility library from Code Synthesis
License:        MIT
URL:            http://www.codesynthesis.com/projects/libcutl/
Source0:        http://www.codesynthesis.com/download/libcutl/%{base_version}/%{name}-%{version}.tar.bz2
Patch0:         libcutl_no_boost_license.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
%if 0%{?fedora} && 0%{?fedora} < 28
# Use the system Boost instead of the internal one
%global external_boost --with-external-boost
BuildRequires: boost-devel
%endif

%if !0%{?external_boost}
Provides: bundled(boost) = 1.54
%endif

# Uses pkgconfig
BuildRequires: pkgconfig
BuildRequires: expat-devel

%description
libcutl is a C++ utility library. It contains a collection of generic and
fairly independent components.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%if 0%{?external_boost:1}
%patch0
rm -rv cutl/details/boost
%endif
rm -rv cutl/details/expat

%build
# Use the system Boost and expat libraries
confopts="--disable-static --with-external-expat %{?external_boost}"
# If building on RHEL 5
%if 0%{?rhel} == 5
# Use the EPEL Boost 1.41 instead of the standard system one
confopts="$confopts CPPFLAGS=-I%{_includedir}/boost141 LDFLAGS=-L%{_libdir}/boost141"
%endif
%configure $confopts
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_datadir}

%ldconfig_scriptlets

%files
%doc LICENSE
%{_libdir}/libcutl-%{base_version}.so

%files devel
%doc NEWS
%{_includedir}/cutl/
%{_libdir}/libcutl.so
%{_libdir}/pkgconfig/libcutl.pc

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.10.0-17
- Some minor fixes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.10.0-13
- use bundled boost on f28+ for now (#1540742)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Rex Dieter <rdieter@fedoraproject.org> 1.10.0-11
- rebuild (boost)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.10.0-8
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.10.0-7
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.10.0-5
- Rebuilt for Boost 1.63

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.10.0-4
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.10.0-2
- Rebuilt for Boost 1.60

* Tue Nov 24 2015 Dave Johansen <davejohansen@gmail.com> 1.10.0-1
- Updated to 1.10.0 (fixes Bugzilla #1278388)

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.9.0-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.9.0-4
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 16 2015 Dave Johansen <davejohansen@gmail.com> 1.9.0-2
- Rebuild for gcc 5.0 C++ ABI change

* Wed Feb 11 2015 Dave Johansen <davejohansen@gmail.com> 1.9.0-1
- Updated to 1.9.0

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.8.1-2
- Rebuild for boost 1.57.0

* Wed Sep 03 2014 Dave Johansen <davejohansen@gmail.com> 1.8.1-1
- Updated to 1.8.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.8.0-3
- Rebuild for boost 1.55.0

* Fri Mar 14 2014 Dave Johansen <davejohansen@gmail.com> 1.8.0-2
- Use system expat library

* Mon Nov 4 2013 Dave Johansen <davejohansen@gmail.com> 1.8.0-1
- Updated to 1.8.0

* Sat Jul 27 2013 Dave Johansen <davejohansen@gmail.com> 1.7.1-3
- Adding support for building on EL5

* Sat Jul 27 2013 pmachata@redhat.com - 1.7.1-2
- Rebuild for boost 1.54.0

* Tue Jul 23 2013 Dave Johansen <davejohansen@gmail.com> 1.7.1-1
- Initial build
