#
%global mydocs __tmp_docdir
#
Name:           airinv
Version:        1.00.4
Release:        3%{?dist}

Summary:        C++ Simulated Airline Inventory Management System library
License:        LGPLv2+
URL:            https://github.com/airsim/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  readline-devel
BuildRequires:  zeromq-devel
BuildRequires:  cppzmq-devel
BuildRequires:  sevmgr-devel
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  stdair-devel
BuildRequires:  airrac-devel
BuildRequires:  rmol-devel
BuildRequires:  sevmgr-devel


%description
%{name} is a C++ library of airline inventory management classes and
functions, mainly targeting simulation purposes.

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for Airline Inventory Management, mainly for simulation purpose.

%package        devel
Summary:        Header files, libraries and development helper tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files, shared libraries and
development helper tools for %{name}. If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

%package        doc
Summary:        HTML documentation for the %{name} library
BuildArch:      noarch
BuildRequires:  tex(latex)
BuildRequires:  texlive-epstopdf
BuildRequires:  doxygen
BuildRequires:  ghostscript

%description    doc
This package contains HTML pages, as well as a PDF reference manual,
for %{name}. All that documentation is generated thanks to Doxygen
(https://doxygen.org). The content is the same as what can be browsed
online (https://%{name}.org).


%prep
%autosetup -n %{name}-%{name}-%{version} 


%build
%cmake .
%make_build

%install
%make_install

mkdir -p %{mydocs}
mv $RPM_BUILD_ROOT%{_docdir}/%{name}/html %{mydocs}
rm -f %{mydocs}/html/installdox

# Remove additional documentation files (those files are already available
# in the project top directory)
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/{NEWS,README,AUTHORS}

%check
ctest


%files
%doc AUTHORS ChangeLog COPYING NEWS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}_parseInventory
%{_bindir}/AirInvClient
%{_bindir}/AirInvServer
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}_parseInventory.1.*
%{_mandir}/man1/AirInvClient.1.*
%{_mandir}/man1/AirInvServer.1.*

%files devel
%{_includedir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/CMake
%{_mandir}/man1/%{name}-config.1.*
%{_mandir}/man3/%{name}-library.3.*

%files doc
%doc %{mydocs}/html
%doc COPYING


%changelog
* Sat Jun 06 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.4-3
- Rebuilt for SOCI 4.0.1-alpha2

* Wed Jun 03 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.4-2
- Rebuilt for Boost 1.73

* Sun May 31 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.4-1
- Upstream update

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.00.3-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.3-5
- Rebuild for SOCI 4.0.0-rc2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.00.3-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.00.3-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.3-1
- CMake support files updated for Python 3.8

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.00.2-4
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.00.2-2
- Rebuilt for Boost 1.69

* Wed Jan 16 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.2-1
- Upstream update

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-19
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-17
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.00.1-14
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.00.1-11
- Rebuild for readline 7.x

* Wed May 18 2016 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-10
- Rebuilt for linker errors in boost (#1331983)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-8
- Rebuilt for Boost 1.60

* Sun Aug 30 2015 Jonathan Wakely <jwakely@redhat.com> 1.00.1-7
- Patched and rebuilt for Boost 1.59

* Sat Aug 29 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-6
- Mass rebuild

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.00.1-4
- rebuild for Boost 1.58

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 1.00.1-3
- rebuilt for new zeromq 4.1.2

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-1
- Removed the dependency on ZeroMQ (only AirInv is dependent on it, not StdAir)

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 1.00.0-13
- Rebuilt for GCC 5 C++11 ABI change

* Sun Feb 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.00.0-12
- BR: zeromq2-devel (Work around RHBZ#1190463; Fix boost-1.57 FTBFS).
- BR: /usr/bin/epstopdf.

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 1.00.0-11
- Rebuild for boost 1.57.0
- Cmake should look for zmq.h, not zmq.hpp (stdair-1.00.1-cmake.patch)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 1.00.0-8
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.00.0-7
- rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-5
- Fixed the docdir issue, following the F20 System Wide Change
- Rebuild for boost 1.54.0

* Wed May 22 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-4
- Rebuild for Soci-3.2.1

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-2
- Rebuild for Boost-1.53.0

* Tue Dec 25 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.00.0-1
- Upstream update

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 0.1.2-5
- Rebuilt for new boost

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 04 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.2-1
- Upstream update. Took into account review request (#750099)

* Sun Oct 30 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.1-1
- First RPM release

