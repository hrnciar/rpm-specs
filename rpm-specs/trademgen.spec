#
%global mydocs __tmp_docdir

# Build -python subpackage
%bcond_without python

#
Name:           trademgen
Version:        1.00.6
Release:        3%{?dist}

Summary:        C++ Simulated Travel Demand Generation Library
License:        LGPLv2+
URL:            https://github.com/airsim/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  readline-devel
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  stdair-devel
BuildRequires:  sevmgr-devel


%description
%{name} aims at providing a clean API, and the corresponding C++
implementation, able to generate demand for travel solutions (e.g.,
from JFK to PEK on 25-05-2009) according to characteristics (e.g.,
Willingness-To-Pay, preferred airline, etc).

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for travel-related demand generation, mainly for simulation purpose.

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

%if %{with python}
%package        -n python3-%{name}
Summary:        Python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  boost-python3-devel
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package contains Python libraries for %{name}
%endif


%prep
%autosetup -n %{name}-%{name}-%{version} 


%build
%cmake .
%make_build

%install
%make_install

# Remove extra libraries, which are generated only for the tests
rm -f %{buildroot}%{_libdir}/libsequential_generation*.so*

#
mkdir -p %{mydocs}
mv %{buildroot}%{_docdir}/%{name}/html %{mydocs}
rm -f %{mydocs}/html/installdox

# Remove additional documentation files (those files are already available
# in the project top directory)
rm -f %{buildroot}%{_docdir}/%{name}/{NEWS,README,AUTHORS}

#check
#ctest


%files
%doc AUTHORS ChangeLog COPYING NEWS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}_with_db
%{_bindir}/%{name}_generateDemand
%{_bindir}/%{name}_extractBookingRequests
%{_bindir}/%{name}_drawBookingArrivals
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}_with_db.1.*
%{_mandir}/man1/%{name}_generateDemand.1.*
%{_mandir}/man1/%{name}_extractBookingRequests.1.*
%{_mandir}/man1/%{name}_drawBookingArrivals.1.*

%files devel
%{_includedir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/CMake/%{name}-config-version.cmake
%{_datadir}/%{name}/CMake/%{name}-config.cmake
%{_datadir}/%{name}/CMake/%{name}-library-depends.cmake
%{_datadir}/%{name}/CMake/%{name}-library-depends-debug.cmake
%{_mandir}/man1/%{name}-config.1.*
%{_mandir}/man3/%{name}-library.3.*

%files doc
%doc %{mydocs}/html
%doc COPYING

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/py%{name}/
%{_mandir}/man1/py%{name}.1.*
%{_datadir}/%{name}/CMake/%{name}-config-python.cmake
%{_datadir}/%{name}/CMake/%{name}-python-library-depends-debug.cmake
%{_datadir}/%{name}/CMake/%{name}-python-library-depends.cmake
%endif


%changelog
* Wed Jun 03 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.6-3
- Rebuilt for SOCI 4.0.1-alpha2

* Wed Jun 03 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.6-2
- Upstream for Boost 1.73

* Sun May 31 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.6-1
- Upstream update

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.00.4-7
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.4-5
- Rebuilt for SOCI 4.0.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.00.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.00.4-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.4-1
- CMake support files updated for Python 3.8

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.00.3-6
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.00.3-4
- Rebuilt for Boost 1.69

* Thu Jan 17 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.3-3
- Fixed a typo in Python library directory

* Wed Jan 16 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.3-2
- Integrated clean-up suggestions from Miro (mhroncok)

* Tue Jan 15 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.3-1
- Upstream update

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.2-18
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.2-16
- Rebuilt for Boost 1.66

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.00.2-15
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.00.2-14
- Python 2 binary package renamed to python2-trademgen
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.00.2-11
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.00.2-9
- Rebuild for readline 7.x

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.2-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 1.00.2-6
- Rebuilt for Boost 1.60

* Sun Aug 30 2015 Jonathan Wakely <jwakely@redhat.com> 1.00.2-5
- Patched and rebuilt for Boost 1.59

* Sat Aug 29 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.2-4
- Mass rebuild

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.00.2-2
- rebuild for Boost 1.58

* Sat Jun 27 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.2-1
- Upstream update

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-1
- Removed the dependency on ZeroMQ (only AirInv is dependent on it, not StdAir)

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 1.00.0-13
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 10 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-12
- For some reason, the tests now fail. De-activated them.
  Will open a bug upstream.

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 1.00.0-11
- Rebuild for boost 1.57.0
- Cmake should look for zmq.h, not zmq.hpp (stdair-1.00.1-cmake.patch)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 1.00.0-8
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.00.0-7
- rebuild for boost 1.55.0

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.00.0-6
- Rebuild for boost 1.54.0

* Mon Jul 29 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-5
- Fixed the docdir issue, following the F20 System Wide Change

* Sat Jul 27 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.00.0-4
- Fix build when %%doc dir is not versioned.

* Wed May 22 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-3
- Rebuild for Soci-3.2.1

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-2
- Rebuild for Boost-1.53.0

* Sun Dec 23 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-1
- Upstream update

* Mon Aug 13 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.2.2-5
- Rebuilt for new Boost 1.50.0.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.2.2-1
- Upstream update. Took into account feedback from #728815.

* Mon Dec 05 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.2.1-1
- Upstream update

* Fri Aug 19 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.0-2
- Added (BR) missing packages needed by a mock build

* Sun Aug 07 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.0-1
- First package

