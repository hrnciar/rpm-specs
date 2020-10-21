# git ls-remote git://github.com/bistromath/gr-air-modes.git
%global git_commit 9e2515a56609658f168f0c833a14ca4d2332713e
%global git_date 20200807

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:             gr-air-modes
URL:              http://github.com/bistromath/gr-air-modes
Version:          0
Release:          0.76.%{git_suffix}%{?dist}
License:          GPLv3+
BuildRequires:    cmake, gcc-c++, python3-devel, python3-numpy, python3-scipy, gnuradio-devel
BuildRequires:    sqlite-devel, uhd-devel, boost-devel, doxygen, graphviz
BuildRequires:    swig, python3-zmq, log4cpp-devel, gmp-devel
# TODO: fix this, package not available on ppc64
#BuildRequires:    mpir-devel
BuildRequires:    orc-devel, python3-pyqtgraph
# TODO: check whether qwt is needed
BuildRequires:    qwt5-qt4-devel
Requires:         python3-numpy, python3-scipy, python3-zmq
Requires:         qwt5-qt4
Summary:          SDR receiver for Mode S transponder signals (ADS-B)
Source0:          https://github.com/bistromath/gr-air-modes/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz

%description
Software defined radio receiver for Mode S transponder signals, including
ADS-B reports.

%package devel
Summary:          Development files for gr-air-modes
Requires:         %{name} = %{version}-%{release}

%description devel
Development files for gr-air-modes.

%package doc
Summary:          Documentation files for gr-air-modes
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%description doc
Documentation files for gr-air-modes.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

%build
%cmake -DENABLE_DOXYGEN=on
%cmake_build

%install
%cmake_install

# remove hashbangs
pushd %{buildroot}%{python3_sitearch}/air_modes
for f in *.py
do
  sed -i '/^[ \t]*#!\/usr\/bin\/\(env\|python\)/ d' $f
done
popd

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%{_bindir}/uhd_modes.py
%{_bindir}/modes_gui
%{_bindir}/modes_rx
%{_libdir}/*.so.*
%{python3_sitearch}/*

%files devel
%{_includedir}/gr_air_modes
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/*.cmake


%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.76.20200807git9e2515a5
- Rebuilt for new gnuradio

* Thu Aug  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.75.20200807git9e2515a5
- New version
- Fixed FTBFS
  Resolves: rhbz#1863817

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.74.20191111gita2f2627c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.73.20191111gita2f2627c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-0.72.20191111gita2f2627c
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.71.20191111gita2f2627c
- Rebuilt for new gnuradio

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.70.20191111gita2f2627c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.69.20191111gita2f2627c
- New version
- Switched to Python 3
  Resolves: rhbz#1738963

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.68.20160831git3bad1f5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.67.20160831git3bad1f5d
- Changed unversioned python requirements to explicit python2

* Mon May  6 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.66.20160831git3bad1f5d
- Dropped PyQwt in f31+

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.65.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 0-0.64.20160831git3bad1f5d
- Rebuilt for Boost 1.69

* Wed Jan  9 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.63.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.62.20160831git3bad1f5d
- Added requirement for C++

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.61.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0-0.60.20160831git3bad1f5d
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.59.20160831git3bad1f5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.58.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Tue Feb  6 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.57.20160831git3bad1f5d
- Rebuilt for new boost

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.56.20160831git3bad1f5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.55.20160831git3bad1f5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0-0.54.20160831git3bad1f5d
- Rebuilt for Boost 1.64

* Wed May 24 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.53.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Wed Feb 08 2017 Kalev Lember <klember@redhat.com> - 0-0.52.20160831git3bad1f5d
- Rebuilt for Boost 1.63

* Fri Sep 16 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.51.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Thu Sep  1 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.50.20160831git3bad1f5d
- Fixed traceback in modes_gui
  Related: rhbz#1369923

* Wed Aug 31 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.49.20160831git3bad1f5d
- New version
  Related: rhbz#1369923
- Simplified snapshots updates

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.48.20160106git514414f6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.47.20160106git514414f6
- Rebuilt for new gnuradio

* Wed Feb 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.46.20160106git514414f6
- Rebuilt for new gnuradio

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.45.20160106git514414f6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0-0.44.20160106git514414f6
- Rebuilt for Boost 1.60

* Wed Jan  6 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.43.20160106git514414f6
- New version
  Resolves: rhbz#1295996

* Mon Jan 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.42.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Tue Dec 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.41.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Thu Nov  5 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.40.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0-0.39.20140312gitcc0fa180
- Rebuilt for Boost 1.59

* Thu Aug 13 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.38.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Tue Aug  4 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.37.20140312gitcc0fa180
- Rebuilt for new boost

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.36.20140312gitcc0fa180
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Tue Jul 28 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.35.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0-0.34.20140312gitcc0fa180
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.33.20140312gitcc0fa180
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.32.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.31.20140312gitcc0fa180
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.30.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 0-0.29.20140312gitcc0fa180
- Rebuild for boost 1.57.0

* Thu Oct 23 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.28.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Tue Sep  2 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.27.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.26.20140312gitcc0fa180
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.25.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.24.20140312gitcc0fa180
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 0-0.23.20140312gitcc0fa180
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0-0.22.20140312gitcc0fa180
- rebuild for boost 1.55.0

* Wed Mar 12 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.21.20140312gitcc0fa180
- New version
- Dropped build-fix patch (not needed)

* Tue Mar 11 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.20.20130730git797bef13
- Rebuilt for new gnuradio

* Mon Dec  2 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.19.20130730git797bef13
- Rebuilt for new gnuradio

* Mon Nov 18 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.18.20130730git797bef13
- Rebuilt for new gnuradio

* Mon Sep  2 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.17.20130730git797bef13
- Rebuilt for new gnuradio

* Tue Aug  6 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.16.20130730git797bef13
- Used unversioned doc directory
  Resolves: rhbz#993801

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0-0.15.20130730git797bef13
- Rebuild for boost 1.54.0

* Tue Jul 30 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.14.20130730git797bef13
- New version

* Tue May 28 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.13.20130409gitf25d21f5
- Rebuilt for new gnuradio

* Tue Apr  9 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.12.20130409gitf25d21f5
- Fixed modes_gui build (missed requirements)

* Tue Apr  9 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.11.20130409gitf25d21f5
- New git snapshot
- Dropped add-soname patch (upstreamed)

* Thu Mar 21 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.10.20120905git6c7a7370
- Rebuilt for new gnuradio

* Thu Feb 28 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.9.20120905git6c7a7370
- Rebuilt for new gnuradio

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20120905git6c7a7370
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan  4 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.7.20120905git6c7a7370
- Rebuilt for new gnuradio

* Mon Nov 12 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.6.20120905git6c7a7370
- Added swig build requires

* Fri Oct 26 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.5.20120905git6c7a7370
- Rebuilt for new gnuradio

* Tue Sep 25 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.4.20120905git6c7a7370
- Hardcoded path for sbindir to silent depcheck errors

* Mon Sep 24 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.3.20120905git6c7a7370
- Packaged doxygen generated documentation as doc subpackage

* Wed Sep 19 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.2.20120905git6c7a7370
- Used macro for sbindir

* Wed Sep  5 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.1.20120905git6c7a7370
- Initial version
