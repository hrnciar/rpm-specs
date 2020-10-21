Name:             gr-iqbal
#URL:              http://cgit.osmocom.org/gr-iqbal/
URL:              https://github.com/osmocom/gr-iqbal
Version:          0.38.1
Release:          2%{?dist}
License:          GPLv3+
BuildRequires:    cmake, gcc-c++, gnuradio-devel, doxygen, graphviz, swig, fftw-devel
BuildRequires:    libosmo-dsp-devel, python3-devel, log4cpp-devel, gmp-devel, orc-devel
Summary:          GNURadio block for suppressing IQ imbalance
Source0:          https://github.com/osmocom/gr-iqbal/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/osmocom/gr-iqbal/pull/3 and also sent to osmocom-sdr@lists.osmocom.org
Patch0:           gr-iqbal-0.38.1-boost-fix.patch

%description
This GNURadio block can suppress IQ imbalance in the RX path of
quadrature receivers.

%package devel
Summary:          Development files for gr-iqbal
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-iqbal.

%package doc
Summary:          Documentation files for gr-iqbal
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%description doc
Documentation files for gr-iqbal.

%prep
%setup -q
%patch0 -p1 -b .boost-fix

%build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build

%install
%cmake_install

# Fix docs location
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/gr-iqbalance %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%doc COPYING AUTHORS
%{_libdir}/*.so.*
%{python3_sitearch}/*
%{_datadir}/gnuradio/grc/blocks/*

%files devel
%{_includedir}/gnuradio/iqbalance
%{_includedir}/gnuradio/swig/*
%{_libdir}/*.so
%{_libdir}/cmake/gnuradio/*.cmake

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.1-2
- Rebuilt for new gnuradio

* Fri Aug  7 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.1-1
- New version
- Fixed FTBFS
  Resolves: rhbz#1863821

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-41
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.37.2-39
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-38
- Rebuilt for new gnuradio

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-36
- Switched to Python 3
  Resolves: rhbz#1738959

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-34
- Rebuilt for new gnuradio

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 0.37.2-33
- Rebuilt for Boost 1.69

* Wed Jan  9 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-32
- Rebuilt for new gnuradio

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-31
- Rebuilt for new gnuradio

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-29
- Rebuilt for new gnuradio
- Disabled parallel build

* Fri Feb  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-28
- Rebuilt for new boost

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.37.2-25
- Rebuilt for Boost 1.64

* Wed May 24 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-24
- Rebuilt for new gnuradio

* Wed Feb 08 2017 Kalev Lember <klember@redhat.com> - 0.37.2-23
- Rebuilt for Boost 1.63

* Fri Sep 16 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-22
- Rebuilt for new gnuradio

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37.2-21
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-20
- Rebuilt for new gnuradio

* Wed Feb 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-19
- Rebuilt for new gnuradio

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0.37.2-17
- Rebuilt for Boost 1.60

* Mon Jan 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-16
- Rebuilt for new gnuradio

* Tue Dec 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-15
- Rebuilt for new gnuradio

* Thu Nov  5 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-14
- Rebuilt for new gnuradio

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.37.2-13
- Rebuilt for Boost 1.59

* Thu Aug 13 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-12
- Rebuilt for new gnuradio

* Tue Aug  4 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-11
- Rebuild for new boost

* Tue Jul 28 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-10
- Rebuilt for new gnuradio

* Thu Jul 23 2015 David Tardon <dtardon@redhat.com> - 0.37.2-9
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-7
- Rebuilt for new gnuradio

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.37.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-5
- Rebuilt for new gnuradio

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 0.37.2-4
- Rebuild for boost 1.57.0

* Thu Oct 23 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-3
- Rebuilt for new gnuradio

* Thu Oct 16 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-2
- Added isa to devel package requirement

* Wed Oct  8 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-1
- Initial release
