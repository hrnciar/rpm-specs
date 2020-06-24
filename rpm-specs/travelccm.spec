#
%global mydocs __tmp_docdir
#
Name:           travelccm
%global sfname  travel-ccm
Version:        1.00.5
Release:        3%{?dist}

Summary:        C++ Travel Customer Choice Model (CCM) Library

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
%{name} aims at providing a clean API, and the corresponding
C++ implementation, for choosing one item among a set of travel
solutions, given demand-related characteristics (e.g.,
Willingness-To-Pay, preferred airline, preferred cabin, etc.).

The %{name} C++ library implements some simple Customer Choice Models
(CCM), as referenced in the literature (PhD dissertations at MIT, for
instance: https://dspace.mit.edu).

The %{name} C++ library exposes a simple, clean and object-oriented,
API. For instance, the choose() method takes, as input, both a
structure representing the travel request (e.g., "from Washington, DC,
US, to Beijing, China, on the 25th of May") and a list of travel
solutions (as provided by the Airline Travel Solution Provider (AirTSP)
project: https://github.com/airsim/airtsp), and yields, as output, the
chosen item.

The output can then be used by other systems, for instance to book the
corresponding travel or to visualize it on a map and calendar and to
share it with others.

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for Customer-Choice Modeling (CCM), mainly for simulation purpose.

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
(http://doxygen.org). The content is the same as what can be browsed
online (http://%{name}.org).


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
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*

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
* Sat Jun 06 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.5-3
- Rebuilt for SOCI 4.0.1-alpha2

* Wed Jun 03 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.5-2
- Rebuilt for Boost 1.73

* Sun May 31 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.5-1
- Upstream update

* Sun Feb 16 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.4-7
- Removed the python-abi problematic line

* Sun Feb 16 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.4-6
- Fixed Python3 macro expansion issue

* Sun Feb 16 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.4-5
- BZ#41324726 - fixed the FTBFS issue on armv7hl

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.00.4-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.4-1
- CMake support files updated for Python 3.8

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.00.3-2
- Rebuilt for Boost 1.69

* Thu Jan 17 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.3-1
- Upstream update

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.2-15
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.2-13
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.00.2-10
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.00.2-8
- Rebuild for readline 7.x

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

* Sun Jun 21 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.2-1
- Removed the dependency on ZeroMQ (only AirInv is dependent on it, not StdAir)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.00.1-10
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.00.1-9
- Rebuild for boost 1.57.0
- Cmake should look for zmq.h, not zmq.hpp (stdair-1.00.1-cmake.patch)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.00.1-6
- rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 1.00.1-4
- Rebuild for boost 1.54.0

* Wed May 22 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-3
- Rebuild for Soci-3.2.1

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-2
- Rebuild for Boost-1.53.0

* Sun Dec 23 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-1
- Upstream update

* Mon Aug 13 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.5.3-4
- Rebuilt for new Boost 1.50.0.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.5.3-1
- Upstream update

* Sun Nov 20 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.5.2-2
- Rebuild for the new Boost-1.48.0

* Wed Nov 02 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.5.2-1
- Rebuilt for the new soci-3.1.0 and stdair-0.44.0 packages

* Sat Sep 24 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.5.0-2
- Integrated feedback from review requests: #732218, #728649 and #702987

* Sat Aug 20 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.5.0-1
- Upstream integration

* Mon Aug 23 2010 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.4.0-1
- Initial RPM release

