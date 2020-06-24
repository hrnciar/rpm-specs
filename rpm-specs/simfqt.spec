#
%global mydocs __tmp_docdir
#
Name:           simfqt
Version:        1.00.4
Release:        3%{?dist}

Summary:        C++ Simulated Fare Quote System Library

License:        LGPLv2+
URL:            https://github.com/airsim/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  readline-devel
BuildRequires:  stdair-devel

%description
%{name} aims at providing a clean API and a simple implementation, as
a C++ library, of a Travel-oriented fare engine. It corresponds to
the simulated version of the real-world Fare Quote or pricing system.

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for Airline Pricing and Fare Quoting (FQ), mainly for simulation purpose.

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
BuildRequires:  doxygen, ghostscript

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
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}

%check
ctest


%files
%doc AUTHORS ChangeLog COPYING NEWS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}_parseFareRules
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}_parseFareRules.1.*

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

* Sun Feb 16 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.3-5
- Fixed the python3_version expansion issue

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.00.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.3-1
- CMake support files updated for Python 3.8

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.00.2-4
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.00.2-2
- Rebuilt for Boost 1.69

* Thu Jan 17 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.2-1
- Upstream update

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-16
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-14
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.00.1-11
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.00.1-9
- Rebuild for readline 7.x

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-8
- Rebuilt for linker errors in boost (#1331983)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-6
- Rebuilt for Boost 1.60

* Sun Aug 30 2015 Jonathan Wakely <jwakely@redhat.com> - 1.00.1-5
- Patched and rebuilt for Boost 1.59

* Sat Aug 29 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-4
- Mass rebuild

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.00.1-2
- rebuild for Boost 1.58

* Sun Jun 21 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-1
- Removed the dependency on ZeroMQ (only AirInv is dependent on it, not StdAir)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.00.0-11
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 1.00.0-10
- Rebuild for boost 1.57.0
- Cmake should look for zmq.h, not zmq.hpp (stdair-1.00.1-cmake.patch)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.00.0-7
- rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-5
- Fixed the docdir issue, following the F20 System Wide Change

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 1.00.0-4
- Rebuild for boost 1.54.0

* Wed May 22 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-3
- Rebuild for Soci-3.2.1

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-2
- Rebuild for Boost-1.53.0

* Tue Dec 25 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.00.0-1
- Upstream update

* Mon Aug 13 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.1.3-5
- Rebuilt for new Boost 1.50.0.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.3-1
- Upstream update

* Sun Nov 20 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.2-2
- Rebuild for the new Boost-1.48.0

* Sun Oct 30 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.2-1
- Upstream update

* Sun Aug 21 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.1-1
- Upstream update
- Took into account the feedback from various review requests (bugs #732205,
  #728649, #732218)

* Fri Aug 19 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.0-1
- First RPM release

