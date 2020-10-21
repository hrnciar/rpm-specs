# Force out of source build
%undefine __cmake_in_source_build

#
Name:           airtsp
Version:        1.01.7
Release:        6%{?dist}

Summary:        C++ Simulated Airline Travel Solution Provider Library

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
a C++ library, of an Airline Schedule Management System. It is intended
to be used in simulated environments only: it is not designed to work
in the real-world of Airline IT operations.

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: http://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for Airline Schedule Management, mainly for simulation purpose.

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
BuildRequires:  tex(latex), tex(sectsty.sty), tex(tocloft.sty), tex(xtab.sty)
BuildRequires:  texlive-epstopdf
BuildRequires:  doxygen
BuildRequires:  ghostscript
BuildRequires:  graphviz

%description    doc
This package contains HTML pages, as well as a PDF reference manual,
for %{name}. All that documentation is generated thanks to Doxygen
(https://doxygen.org). The content is the same as what can be browsed
online (https://%{name}.org).


%prep
%autosetup -n %{name}-%{name}-%{version}


%build
%cmake
%cmake_build

%install
%cmake_install

# Remove the Doxygen installer
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/html/installdox

# Remove additional documentation files (those files are already available
# in the project top directory)
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}

%check
#ctest


%files
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING
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
%doc %{_docdir}/%{name}/html
%license COPYING


%changelog
* Sun Aug 09 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.7-6
- Removed the work around for document directory

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.7-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.7-3
- Rebuilt for SOCI 4.0.1-alpha2

* Wed Jun 03 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.7-2
- Rebuilt for Boost 1.73

* Sun May 31 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.7-1
- Upstream update

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.01.6-2
- Rebuilt for Python 3.9

* Thu Feb 06 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.6-1
- Fixed the pkg-config issue

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.01.5-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.5-1
- CMake support files updated for Python 3.8

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.01.4-2
- Rebuilt for Boost 1.69

* Thu Jan 17 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.4-1
- Upstream update

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Jonathan Wakely <jwakely@redhat.com> - .3-9
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.01.3-7
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.01.3-4
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.01.3-1
- Fixed a compatibility issue with C++11 with std::istringstream.
BZ #1307310

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.01.2-9
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.01.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 1.01.2-7
- Rebuilt for Boost 1.60

* Sun Aug 30 2015 Jonathan Wakely <jwakely@redhat.com> 1.01.2-6
- Patched and rebuilt for Boost 1.59

* Sat Aug 29 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.2-5
- Mass rebuild

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.01.2-3
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 13 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.2-1
- Aligned on StdAir for the CMake helper files.

* Sat Apr 18 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.1-2
- On Fedora 22+, ZeroMQ v2 is no longer the default.

* Mon Aug 12 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.1-1
- Took into account feedback from review request (BZ#972431):
  airtsp-config now supports multilib (32 and 64bit versions).
- Upstream update

* Mon Jul 29 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.01.0-3
- Fixed the docdir issue, following the F20 System Wide Change
- Rebuild for boost 1.54.0

* Wed Jun 12 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.01.0-2
- Added a dependency on graphviz and texlive-utils (epstopdf), so as
  build the documentation with figures

* Sat Jun 08 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.01.0-1
- Renamed the package, from AirSched to AirTSP, due to trademark issue
  with Plancor

* Wed Oct 26 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.2-1
- Upstream update

* Sat Aug 20 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.1-1
- Upstream update
- Took into account the feedback from various review requests (bugs #732205,
  #728649, #732218)

* Sat Aug 20 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.1.0-1
- First RPM release

