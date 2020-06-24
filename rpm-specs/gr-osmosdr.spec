%global git_commit f3905d3510dfb3851f946f097a9e2ddaa5fb333b
%global git_date 20191112

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

# git clone git://git.osmocom.org/gr-osmosdr
# cd %%{name}
# git archive --format=tar --prefix=%%{name}-%%{version}/ %%{git_commit} | \
# bzip2 > ../%%{name}-%%{version}-%%{git_suffix}.tar.bz2

%{?filter_setup:
%filter_provides_in %{python3_sitearch}/osmosdr/.*\.so$
%filter_setup
}

Name:             gr-osmosdr
URL:              http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
Version:          0.1.4
Release:          24.%{git_suffix}%{?dist}
License:          GPLv3+
BuildRequires:    cmake, gcc-c++, python3-devel, gnuradio-devel, boost-devel
BuildRequires:    doxygen, graphviz, swig, rtl-sdr-devel, uhd-devel
BuildRequires:    hackrf-devel, gr-fcdproplus-devel, gmp-devel
BuildRequires:    gr-iqbal-devel
BuildRequires:    airspyone_host-devel, SoapySDR-devel, python3-mako
BuildRequires:    log4cpp-devel, orc-devel
Summary:          Common software API for various radio hardware
#Source0:          %%{name}-%%{version}-%%{git_suffix}.tar.bz2
# IMHO not the official source, but gnuradio-3.8 fixed, not yet upstreamed
Source0:          https://github.com/igorauad/gr-osmosdr/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
Patch0:           gr-osmosdr-0.1.1-pkgconfig-fix.patch
Patch1:           gr-osmosdr-0.1.4-gnuradio38-blocks-fix.patch
Patch2:           gr-osmosdr-boost173.patch

%description
Primarily gr-osmosdr supports the OsmoSDR hardware, but it also
offers a wrapper functionality for FunCube Dongle,  Ettus UHD
and rtl-sdr radios. By using gr-osmosdr source you can take
advantage of a common software api in your application(s)
independent of the underlying radio hardware.

%package devel
Summary:          Development files for gr-osmosdr
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-osmosdr.

%package doc
Summary:        Documentation files for gr-osmosdr
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation files for gr-osmosdr.

%prep
%setup -q -n %{name}-%{git_commit}

%patch0 -p1 -b .pkgconfig-fix
%patch1 -p1 -b .gnuradio38-blocks-fix
%patch2 -p1 -b .boost173

# TODO fix the lib location nicer way
sed -i 's|/lib/|/%{_lib}/|g' CMakeLists.txt

%build
mkdir build
cd build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name} ..
# parallel build is broken
make

%install
cd build
make install DESTDIR=%{buildroot}

# fix docs
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/gnuradio/* %{buildroot}%{_docdir}/%{name}
rmdir %{buildroot}%{_docdir}/gnuradio

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%doc AUTHORS COPYING
%{_bindir}/*
%{_libdir}/*.so.*
%{python3_sitearch}/*
%{_datadir}/gnuradio/grc/blocks/*

%files devel
%{_includedir}/osmosdr
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/osmosdr/*.cmake

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Wed Jun 03 2020 Jonathan Wakely <jwakely@redhat.com> - 0.1.4-24.20191112gitf3905d35
- Rebuilt and patched for Boost 1.73.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-23.20191112gitf3905d35
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-22.20191112gitf3905d35
- Rebuilt for new gnuradio

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-21.20191112gitf3905d35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-20.20191112gitf3905d35
- Re-enabled gr-iqbal support

* Mon Nov 11 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-19.20191112gitf3905d35
- New version
- Switched to Python 3
  Resolves: rhbz#1738958

* Mon Aug 12 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-18.20170221git2a2236cc
- Rebuilt for new uhd

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-17.20170221git2a2236cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-16.20170221git2a2236cc
- Rebuilt for new gnuradio

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-15.20170221git2a2236cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  9 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-14.20170221git2a2236cc
- Rebuilt for new gnuradio and UHD
  Resolves: rhbz#1625012

* Mon Dec 10 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-13.20170221git2a2236cc
- Rebuilt for new gnuradio

* Fri Aug 31 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-12.20170221git2a2236cc
- Added support for SoapySDR
  Resolves: rhbz#1624000

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-11.20170221git2a2236cc
- Disabled parallel build
  Resolves: rhbz#1604317

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-10.20170221git2a2236cc
- Rebuilt for new gnuradio
- Fixed python macros
- Added requirement for C++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9.20170221git2a2236cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-8.20170221git2a2236cc
- Added support for Airspy
- Rebuilt for new gnuradio

* Tue Feb  6 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-7.20170221git2a2236cc
- Rebuilt for new boost

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6.20170221git2a2236cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5.20170221git2a2236cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 0.1.4-4.20170221git2a2236cc
- Rebuilt for Boost 1.64

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1.4-3.20170221git2a2236cc
- Rebuild due to bug in RPM (RHBZ #1468476)

* Wed May 24 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-2.20170221git2a2236cc
- Rebuilt for new gnuradio

* Tue Feb 21 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-1.20170221git2a2236cc
- New version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-24.20141023git42c66fdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-23.20141023git42c66fdd
- Rebuilt for new uhd

* Fri Sep 16 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-22.20141023git42c66fdd
- Rebuilt for new gnuradio

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-21.20141023git42c66fdd
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-20.20141023git42c66fdd
- Rebuilt for new gnuradio

* Tue May 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-19.20141023git42c66fdd
- Rebuilt for new uhd

* Wed Feb 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-18.20141023git42c66fdd
- Rebuilt for new gnuradio

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-17.20141023git42c66fdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0.1.3-16.20141023git42c66fdd
- Rebuilt for Boost 1.60

* Mon Jan 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-15.20141023git42c66fdd
- Rebuilt for new gnuradio

* Tue Dec 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-14.20141023git42c66fdd
- Rebuilt for new gnuradio

* Thu Nov  5 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-13.20141023git42c66fdd
- Rebuilt for new gnuradio

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.1.3-12.20141023git42c66fdd
- Rebuilt for Boost 1.59

* Thu Aug 13 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-11.20141023git42c66fdd
- Rebuilt for new gnuradio

* Tue Aug  4 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-10.20141023git42c66fdd
- Rebuilt for new boost

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-9.20141023git42c66fdd
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Tue Jul 28 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-8.20141023git42c66fdd
- Rebuilt for new gnuradio

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.1.3-7.20141023git42c66fdd
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-6.20141023git42c66fdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-5.20141023git42c66fdd
- Rebuilt for new gnuradio

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.3-4.20141023git42c66fdd
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-3.20141023git42c66fdd
- Rebuilt for new gnuradio

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 0.1.3-2.20141023git42c66fdd
- Rebuild for boost 1.57.0

* Thu Oct 23 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-1.20141023git42c66fdd
- New version
- Added gr-fcdproplus (FUNcube Dongle Pro+) support
- Added gr-iqbal support

* Wed Sep 24 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-17.20130729git9dfe3a63
- Added hackrf support

* Tue Sep  2 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-16.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-15.20130729git9dfe3a63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-14.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-13.20130729git9dfe3a63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 0.1.1-12.20130729git9dfe3a63
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.1.1-11.20130729git9dfe3a63
- rebuild for boost 1.55.0

* Mon May  5 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-10.20130729git9dfe3a63
- Enabled UHD support
  Resolves: rhbz#1093954

* Tue Mar 11 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-9.20130729git9dfe3a63
- Fixed pkgconfig version string

* Tue Mar 11 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-8.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Mon Jan  6 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-7.20130729git9dfe3a63
- Dummy release bump due to http://fedorahosted.org/rel-eng/ticket/5823

* Mon Dec  2 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-6.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Mon Nov 18 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-5.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Mon Sep  2 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-4.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Tue Aug  6 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-3.20130729git9dfe3a63
- Used unversioned doc directory
  Resolves: rhbz#993807

* Mon Jul 29 2013 Petr Machata <pmachata@redhat.com> - 0.1.1-2.20130729git9dfe3a63
- Rebuild for boost 1.54.0

* Mon Jul 29 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-1.20130729git9dfe3a63
- New version
- Dropped doxygen-fix and docdir-override patches (upstreamed)

* Tue May 28 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.1-3.20130403gite85c68d9
- Rebuilt for new gnuradio

* Tue Apr  9 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.1-2.20130403gite85c68d9
- Packaged doxygen docs and examples
- Various improvements according to comments in the merge review

* Wed Apr  3 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.1-1.20130403gite85c68d9
- Initial version
