%global commit ed29e639dfaefbe16db182d360af0d03417e7cd8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global realname console_bridge
Name:		console-bridge
Version:	0.3.2
Release:	14%{?dist}
Summary:	Lightweight set of macros used for reporting information in libraries

License:	BSD
URL:		http://ros.org/wiki/console_bridge
Source0:        https://github.com/ros/%{realname}/archive/%{commit}/%{realname}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake

%description
A very lightweight set of macros that can be used for reporting information 
in libraries. The logged information can be forwarded to other systems.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn %{realname}-%{commit}

%build
mkdir build; pushd build
%cmake .. -DUSE_GNU_INSTALL_DIRS=ON
popd
make -C build %{?_smp_mflags}


%install
make -C build install DESTDIR=%{buildroot}

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{realname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{realname}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.3.2-11
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.3.2-8
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.3.2-5
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.3.2-4
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.3.2-2
- Rebuilt for Boost 1.63

* Sun Apr 03 2016 Rich Mattes <richmattes@gmail.com> - 0.3.2-1
- Update to release 0.3.2 (rhbz#1316240)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.2.7-8
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.2.7-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.2.7-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.7-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.2.7-2
- Rebuild for boost 1.57.0

* Sat Aug 23 2014 Rich Mattes <richmattes@gmail.com> - 0.2.7-1
- Update to release 0.2.7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.2.5-2
- Rebuild for boost 1.55.0

* Sat Feb 08 2014 Rich Mattes <richmattes@gmail.com> - 0.2.5-1
- Update to release 0.2.5

* Wed Aug 21 2013 Rich Mattes <richmattes@gmail.com> - 0.2.4-1
- Update to release 0.2.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.1.4-3
- Rebuild for boost 1.54.0

* Tue Apr 09 2013 Rich Mattes <richmattes@gmail.com> - 0.1.4-2
- Add ldconfig calls
- Add patch to create a soversion, set it to 0

* Tue Mar 12 2013 Rich Mattes <richmattes@gmail.com> - 0.1.4-1
- Update to release 0.1.4

* Sun Dec 02 2012 Rich Mattes <richmattes@gmail.com> - 0.1.2-2
- Fixed library path in console_bridge-config.cmake

* Sat Oct 13 2012 Rich Mattes <richmattes@gmail.com> - 0.1.2-1
- Initial package
