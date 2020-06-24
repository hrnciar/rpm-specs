#
%global mydocs __tmp_docdir

# Build -python subpackage
%bcond_without python

#
Name:           rmol
Version:        1.00.6
Release:        3%{?dist}

Summary:        C++ library of Revenue Management and Optimisation classes and functions

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
BuildRequires:  airrac-devel

%description
%{name} is a C++ library of Revenue Management and Optimisation classes 
and functions. Typically, that library may be used by service providers
(e.g., airlines offering flight seats, hotels offering rooms, rental car
companies offering rental days, broadcasting company offering advertisement 
slots, theaters offering seats, etc.) to help in optimizing their revenues
from seat capacities.
Most of the algorithms implemented are public and documented in the
following book:
The Theory and practice of Revenue Management, by Kalyan T. Talluri and
Garrett J. van Ryzin, Kluwer Academic Publishers, 2004, ISBN 1-4020-7701-7

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for Airline Revenue Management (RM), mainly for simulation purpose.

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
online (https://%{name}.net).

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

mkdir -p %{mydocs}
mv %{buildroot}%{_docdir}/%{name}/html %{mydocs}
rm -f %{mydocs}/html/installdox

# Remove additional documentation files (those files are already available
# in the project top directory)
rm -f %{buildroot}%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}

%check
ctest

%if %{with python}
%post -n python3-%{name}
ln -s -f %{python3_sitearch}/py%{name}/py%{name} %{_bindir}/py%{name}

%postun -n python3-%{name}
rm -f %{_bindir}/py%{name}
%endif


%files
%doc AUTHORS ChangeLog COPYING NEWS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}_drawBPC
%{_bindir}/%{name}_extractBPC
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}_drawBPC.1.*
%{_mandir}/man1/%{name}_extractBPC.1.*

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
* Sat Jun 06 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.6-3
- Rebuilt for SOCI 4.0.1-alpha2

* Wed Jun 03 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.6-2
- Rebuilt for Boost 1.73

* Sun May 31 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.6-1
- Upstream update

* Sun May 31 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.5-1
- Upstream update

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.00.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.4-1
- Upstream update

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.00.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.00.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.3-1
- CMake support files updated for Python 3.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.00.2-3
- Rebuilt for Boost 1.69

* Thu Jan 17 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.2-2
- Added the delivery of pyrmol

* Wed Jan 16 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.2-1
- Upstream update

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-17
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-15
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.00.1-12
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.00.1-9
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-7
- Rebuilt for Boost 1.60

* Sun Aug 30 2015 Jonathan Wakely <jwakely@redhat.com> 1.00.1-6
- Patched and rebuilt for Boost 1.59

* Sat Aug 29 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-5
- Mass rebuild

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.00.1-3
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-1
- Removed the dependency on ZeroMQ (only AirInv is dependent on it, not StdAir)

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 1.00.0-12
- Rebuilt for GCC 5 C++11 ABI change

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 1.00.0-11
- Rebuild for boost 1.57.0
- Cmake should look for zmq.h, not zmq.hpp (stdair-1.00.1-cmake.patch)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 15 2014 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-9
- Rebuild for ARM architecture.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.00.0-7
- rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.00.0-5
- Rebuild for boost 1.54.0

* Mon Jul 29 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-4
- Fixed the docdir issue, following the F20 System Wide Change
- Rebuild for Boost-1.54.0

* Wed May 22 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-3
- Rebuild for Soci-3.2.1

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-2
- Rebuild for Boost-1.53.0

* Tue Dec 25 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-1
- Upstream update

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 0.25.3-6
- Rebuild for new boost

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.3-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.25.3-1
- Upstream integration

* Sun Nov 20 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.25.2-2
- Rebuild for the new Boost-1.48.0

* Wed Nov 02 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.25.2-1
- Upstream integration

* Sat Oct 29 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.25.0-2
- Fixed the doc sub-package (no)arch for EPEL

* Sun Oct 23 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.25.0-1
- Upstream integration

* Sat Jul 23 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.23.1-5
- Rebuild for Boost-1.47.0-2

* Mon Apr 25 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.23.1-4
- Rebuild for Boost-1.46.1-2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.23.1-2
- rebuild for new boost

* Tue Sep 07 2010 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.23.1-1
- Upstream integration
- Fixed bug #631080 (https://bugzilla.redhat.com/show_bug.cgi?id=631080)

* Wed Jul 28 2010 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.23.0-3
- Added a patch to fix Rawhide build error

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> 0.23.0-2
- Rebuild for Boost soname bump

* Tue Sep 15 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.23.0-1
- Upstream integration

* Mon May 11 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.22.0-1
- Upstream integration

* Sun May 10 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.21.0-3
- Removed dependencies on specific versions (for EL 5)

* Sat May 09 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.21.0-2
- Removed dependencies on specific versions (for EL 5)

* Mon May 04 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.21.0-1
- Upstream integration

* Sun May 03 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.20.0-3
- Added dependency on libicu for Boost 1.37 (Fedora 11)

* Sun May 03 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.20.0-2
- Added dependency on libicu-devel for Boost 1.37 (Fedora 11)

* Sun May 03 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.20.0-1
- Upstream integration

* Wed Mar 25 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.19.0-1
- RPM release for Fedora 10

* Wed Mar  4 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.18.0-1
- Second RPM release
