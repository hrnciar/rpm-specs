Name:           paris-traceroute
Version:        0.93
Release:        3%{?dist}
Summary:        A network diagnosis and measurement tool

License:        LGPLv3
URL:            https://github.com/libparistraceroute/libparistraceroute
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf

%description
Paris Traceroute is a fundamental upgrade to the standard Traceroute tool
that exists on all of the major operating systems. Standard Traceroute was
not designed to take into account the presence of load balancing routers,
which are widely deployed in today’s Internet, both at the core and at its
edges. As a result, standard Traceroute is not aware that there are often
multiple paths between a source and a destination in the Internet: the
paths will split at a load balancing router at one point along the route
and then reconverge some hops later. Standard traceroute is incapable of
furnishing this information to its users and instead reports what it states
to be a single path but is instead a confusing mixture of pieces of multiple
paths. Paris Traceroute is aware of the multiple paths and can report on any
single one of them accurately, as well as on all of them. 

%package -n libparistraceroute
Summary:        Library files for %{name}

%description -n libparistraceroute
Library files for programs using libparistraceroute.

%package -n libparistraceroute-devel
Summary:        Development files for %{name}
Requires:       libparistraceroute = %{version}-%{release}

%description -n libparistraceroute-devel
Development files for programs using libparistraceroute.

%prep
%autosetup -n libparistraceroute-%{version}

%build
./autogen.sh
%configure --enable-shared --disable-static
%make_build CFLAGS="${RPM_OPT_FLAGS} -fcommon"

%install
%make_install
# Rename ping to paris-ping to avaoid name clash with the standard tool
mv %{buildroot}%{_bindir}/ping %{buildroot}%{_bindir}/paris-ping 
rm %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS README.md TODO
%license COPYING LICENSE
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}
%{_bindir}/paris-ping

%files -n libparistraceroute
%{_libdir}/*.so.*

%files -n libparistraceroute-devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/paristraceroute

%changelog
* Tue Mar 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.93-3
- Fix FTBFS (rhbz#1799849)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.93-1
- Update to latest upstream release 0.93 (rhbz#1584015)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.92-7
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.92-3
- Man page path fixed (rhbz#910640)

* Sun Oct 21 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.92-2
- Minor changes

* Fri Mar 30 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.92-1
- Initial package for Fedora
