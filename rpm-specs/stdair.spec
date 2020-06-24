%global mydocs __tmp_docdir
Name:           stdair
Version:        1.00.10
Release:        3%{?dist}

Summary:        C++ Standard Airline IT Object Library

License:        LGPLv2+
URL:            https://github.com/airsim/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

# For some reason, as of November 2019, it does not compile on ARMv7hl
# See https://koji.fedoraproject.org/koji/taskinfo?taskID=38769808
#ExcludeArch:    armv7hl

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  readline-devel


%description
%{name} aims at providing a clean API, and the corresponding C++
implementation, for the basis of Airline IT and travel distribution
Business Object Model (BOM), that is, to be used by several other open
source projects, such as AirRAC, RMOL, AirInv, AvlCal, AirSched, SimFQT,
SimLFS, SimCRS, TravelCCM, SEvMgr, TraDemGen, DSim, OpenTREP, etc.

Install the %{name} package if you need a library of basic C++ objects
for Airline IT (e.g., schedule management, inventory, revenue management,
revenue accounting), travel distribution, demand generation and customer choice
modeling, mainly for simulation purpose.

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
BuildRequires:  tex(latex)
BuildRequires:  doxygen
BuildRequires:  ghostscript
BuildRequires:  texlive-epstopdf

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

# Fix some permissions
find $RPM_BUILD_ROOT%{_libexecdir}/%{name} -type f -name '*.sh' -exec chmod +x {} \;

mkdir -p %{mydocs}
mv $RPM_BUILD_ROOT%{_docdir}/%{name}/html %{mydocs}
rm -f %{mydocs}/html/installdox

# Remove additional documentation files (those files are already available
# in the project top directory)
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}

%check
ctest

%files
%doc ChangeLog COPYING AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}uicl.so.*
%{_mandir}/man1/%{name}.1.*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*.sh
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/db
%dir %{_datadir}/%{name}/db/data
%dir %{_datadir}/%{name}/samples
%dir %{_datadir}/%{name}/samples/rds01
%dir %{_datadir}/%{name}/samples/HybridForecasting
%dir %{_datadir}/%{name}/samples/IBP_study
%dir %{_datadir}/%{name}/samples/NewQFF
%dir %{_datadir}/%{name}/samples/NewQFF/instance01
%dir %{_datadir}/%{name}/samples/NewQFF/instance02
%dir %{_datadir}/%{name}/samples/OldQFF
%dir %{_datadir}/%{name}/samples/OldQFF/instance01
%dir %{_datadir}/%{name}/samples/OldQFF/instance02
%dir %{_datadir}/%{name}/samples/QForecasting
%{_datadir}/%{name}/db/data/*.sql
%{_datadir}/%{name}/db/data/*.csv
%{_datadir}/%{name}/samples/*.csv
%{_datadir}/%{name}/samples/rds01/*.csv
%{_datadir}/%{name}/samples/HybridForecasting/*.csv
%{_datadir}/%{name}/samples/IBP_study/*.csv
%{_datadir}/%{name}/samples/NewQFF/instance01/*.csv
%{_datadir}/%{name}/samples/NewQFF/instance02/*.csv
%{_datadir}/%{name}/samples/OldQFF/instance01/*.csv
%{_datadir}/%{name}/samples/OldQFF/instance02/*.csv
%{_datadir}/%{name}/samples/QForecasting/*.csv

%files devel
%{_includedir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}uicl.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4
%{_datadir}/%{name}/CMake
%{_mandir}/man1/%{name}-config.1.*
%{_mandir}/man3/%{name}-library.3.*

%files doc
%doc %{mydocs}/html
%doc COPYING


%changelog
* Wed Jun 03 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.10-3
- Rebuilt for SOCI 4.0.1.alpha1

* Wed Jun 03 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.10-2
- Rebuilt for Boost 1.73

* Sun May 31 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.10-1
- Upstream update

* Sun May 31 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.9-1
- Upstream update. No more dependency on Python

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.00.8-6
- Rebuilt for Boost 1.73

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.8-4
- Rebuild for SOCI 4.0.0-rc1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.00.8-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.8-1
- CMake support files updated for Python 3.8

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.00.7-3
- Rebuilt for Boost 1.69

* Thu Jan 17 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.7-2
- Fixed a typo in Python library directory

* Tue Jan 15 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.7-1
- Upstream update

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.6-4
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 1.00.6-2
- Rebuilt for Boost 1.66

* Sun Aug 06 2017 Denis Arnaud <denis_arnaud at users dot sourceforge dot net> - 1.00.6
- Fixed the FTBFS issue related to newer Boost Serialization (from 1.63).
  Ref: StdAir issue #2 on GitHub (http://github.com/airsim/stdair/issues/2)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sat Jul 29 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.00.5-5
- Spec clean up

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.00.5-3
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Feb 26 2017 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.5-1
- Upstream update

* Sat Feb 25 2017 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.2-12
- Attempt to fix the FTBFS issue related to new Boost 1.63 serialization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.00.2-8
- Rebuilt for linker errors in boost (#1331983)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.00.2-6
- Rebuilt for Boost 1.60

* Sat Aug 29 2015 Jonathan Wakely <jwakely@redhat.com> 1.00.2-5
- Patched and rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.00.2-3
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.2-1
- Removed the dependency on ZeroMQ (only AirInv is dependent on it, not StdAir)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.00.1-14
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.00.1-13
- Rebuild for boost 1.57.0
- Cmake should look for zmq.h, not zmq.hpp (stdair-1.00.1-cmake.patch)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-11
- Rebuild for ARM. It seems to work:
  http://arm.koji.fedoraproject.org/koji/taskinfo?taskID=2415169

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.00.1-9
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-7
- Fixed the docdir issue, following the F20 System Wide Change
- Fixed wrong dates in the changelog

* Sat Jul 27 2013 Petr Machata <pmachata@redhat.com> - 1.00.1-6
- Rebuild for boost 1.54.0

* Sun Jun 02 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-5
- Bump the version to be consistent with F19

* Wed May 22 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-4
- Rebuild for Soci-3.2.1

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-3
- Rebuild for Boost-1.53.0

* Wed Jan 02 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-2
- Bump the version to be consistent with F18

* Sun Dec 23 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.1-1
- Upstream update

* Sat Dec 22 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.00.0-1
- Upstream update

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 0.45.1-4
- Rebuild for new boost

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45.1-2
- Rebuilt for c++ ABI breakage

* Sun Jan 15 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.45.1-1
- Upstream update

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 04 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.45.0-1
- Upstream update

* Sun Nov 20 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.44.1-2
- Rebuild for the new Boost-1.48.0

* Sat Nov 05 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.44.1-1
- Upstream update

* Wed Nov 02 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.44.0-1
- Upstream update

* Tue Oct 18 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.43.1-1
- The build framework is now compatible with CMake 2.6 (the exclusive
  dependency on CMake 2.8 has been removed).

* Sat Oct 15 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.43.0-2
- Improved a little the package descriptions

* Sat Oct 15 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.43.0-1
- Upstream update

* Mon Aug 15 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.38.0-1
- Upstream update

* Fri Aug 12 2011 Adam Jackson <ajax@redhat.com> 0.36.2-2
- Rebuild for new boost

* Mon Aug 01 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.36.2-1
- The CMake framework now takes into account compilation flags

* Sun Jul 31 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.36.1-1
- Upstream update

* Sun Jul 31 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.36.0-2
- Took into account review elements (#702987)

* Tue Jul 26 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.36.0-1
- Upstream update

* Thu Jul 07 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.35.0-1
- Upstream update

* Wed Jun 15 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.34.0-1
- Upstream update
- The build system is now CMake (instead of the GNU Autotools)

* Tue Jun  7 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.33.0-1
- Upstream update

* Sun May 22 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.32.0-1
- Upstream update

* Mon May 16 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.31.0-1
- Upstream update

* Fri Apr 29 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.30.0-1
- Upstream update

* Wed Apr 20 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.29.0-1
- Upstream update

* Sun Apr 17 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.28.0-1
- Upstream update

* Tue Apr 12 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.27.0-1
- Upstream update

* Fri Apr 08 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.26.0-1
- Upstream update

* Tue Apr 05 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.25.0-1
- Upstream update

* Fri Apr 01 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.24.0-1
- Upstream update

* Thu Mar 24 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.23.0-1
- Upstream update

* Thu Mar 17 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.22.0-1
- Upstream update

* Sun Mar 13 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.21.0-1
- Upstream update

* Fri Mar  4 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.20.0-1
- Upstream update

* Thu Mar  3 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.19.0-1
- Upstream update

* Thu Mar  3 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.18.0-1
- Upstream update

* Wed Mar  2 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.17.0-1
- Upstream update

* Fri Feb 25 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.16.0-1
- Upstream update

* Tue Feb 22 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.15.0-1
- Upstream update

* Sat Feb 19 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.14.0-1
- Upstream update

* Wed Feb 16 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.13.0-1
- Upstream update

* Sat Feb 12 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.12.0-1
- Upstream update

* Tue Jan 18 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.11.0-1
- Upstream update

* Wed Dec 29 2010 Son Nguyen Kim <nguyenkims@gmail.com> 0.10.0-1
- Upstream update

* Fri Dec 03 2010 Son Nguyen Kim <nguyenkims@gmail.com> 0.9.0-1
- Upstream update

* Sat Nov 06 2010 Son Nguyen Kim <nguyenkims@gmail.com> 0.8.0-1
- Upstream update

* Thu Oct 14 2010 Son Nguyen Kim <nguyenkims@gmail.com> 0.7.0-1
- Upstream update

* Thu Oct 14 2010 Son Nguyen Kim <nguyenkims@gmail.com> 0.6.0-1
- Upstream update

* Thu Sep 16 2010 Son Nguyen Kim <nguyenkims@gmail.com> 0.5.0-1
- Upstream update

* Fri Sep 03 2010 Son Nguyen Kim <nguyenkims@gmail.com> 0.4.0-1
- Replace extracc external ref to dependency

* Sun Aug 29 2010 Son Nguyen Kim <nguyenkims@gmail.com> 0.3.0-1
- Upstream update

* Tue Jul 13 2010 Son Nguyen Kim <nguyenkims@gmail.com> 0.1.0-1
- First RPM release

