%global git_commit 06069c2e201aa2aa1d9da3a52f747952e43d3268
%global git_date 20200807

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:             gr-fcdproplus
URL:              https://github.com/dl1ksv/gr-fcdproplus
Version:          3.8.0
Release:          3.%{git_suffix}%{?dist}
License:          GPLv3+
BuildRequires:    cmake, gcc-c++, gnuradio-devel, dos2unix, hidapi-devel
BuildRequires:    doxygen, graphviz, swig, alsa-lib-devel, libusbx-devel
BuildRequires:    python3-devel, log4cpp-devel, jack-audio-connection-kit-devel
BuildRequires:    portaudio-devel, gmp-devel, orc-devel
Summary:          GNURadio support for FUNcube Dongle Pro+
Source0:          https://github.com/dl1ksv/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
Source1:          10-fcdproplus.rules
# https://github.com/dl1ksv/gr-fcdproplus/pull/20
Patch0:           gr-fcdproplus-3.8.0-boost-fix.patch

%description
GNURadio support for FUNcube Dongle Pro+.

%package devel
Summary:          Development files for gr-fcdproplus
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-fcdproplus.

%package doc
Summary:          Documentation files for gr-fcdproplus
Requires:         %{name} = %{version}-%{release}
# Workaround for rhbz#1814356
#BuildArch:        noarch

%description doc
Documentation files for gr-fcdproplus.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

# Unbundle hidapi
rm -rf lib/hid

%build
# used -Wl,--as-needed to fix unused-direct-shlib-dependency rpmlint warning
export LDFLAGS="-Wl,--as-needed %{?__global_ldflags}"
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build

%install
%cmake_install

# udev rule
install -Dpm 0644 %{S:1} %{buildroot}%{_prefix}/lib/udev/rules.d/10-fcdproplus.rules

%ldconfig_scriptlets

%pre
# sharing group with the rtl-sdr package not to introduce new group
# todo: consolidate also with the uhd package (usrp group) to have one generic
# group e.g. 'sdr' for this class of devices
getent group rtlsdr >/dev/null || \
  %{_sbindir}/groupadd -r rtlsdr >/dev/null 2>&1
exit 0

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%doc COPYING README.md
%{_libdir}/*.so.*
%{python3_sitearch}/*
%{_datadir}/gnuradio/grc/blocks/*
%{_prefix}/lib/udev/rules.d/10-fcdproplus.rules

%files devel
%{_includedir}/fcdproplus
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/*.cmake

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 3.8.0-3.20200807git06069c2e
- Rebuilt for new gnuradio

* Fri Aug  7 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 3.8.0-2.20200807git06069c2e
- Added udev rule for FUNcube Dongle Pro

* Thu Aug  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 3.8.0-1.20200807git06069c2e
- New version
- Fixed FTBFS
  Resolves: rhbz#1863818

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-7.20191111gitf1154db3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-6.20191111gitf1154db3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.7.2-5.20191111gitf1154db3
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.2-4.20191111gitf1154db3
- Rebuilt for new gnuradio

* Tue Mar 17 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.2-3.20191111gitf1154db3
- Made docs arch (workaround for rhbz#1814356)
  Resolves: rhbz#1799468

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2.20191111gitf1154db3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.2-1.20191111gitf1154db3
- New version
- Switched to Python 3
  Resolves: rhbz#1738962

* Fri Sep 13 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.2-0.9.rc1.20180618gite5ff8396
- Added rtlsdr group to the udev rule to support headless server operation

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-0.8.rc1.20180618gite5ff8396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.2-0.7.rc1.20180618gite5ff8396
- Rebuilt for new gnuradio

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 3.7.2-0.6.rc1.20180618gite5ff8396
- Rebuilt for Boost 1.69

* Wed Jan  9 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.2-0.5.rc1.20180618gite5ff8396
- Rebuilt for new gnuradio

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.2-0.4.rc1.20180618gite5ff8396
- Rebuilt for new gnuradio

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-0.3.rc1.20180618gite5ff8396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.2-0.2.rc1.20180618gite5ff8396
- Fixed pkgconfig dependency

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.2-0.1.rc1.20180618gite5ff8396
- New version
- Dropped unbundle-hidapi, doxygen-fix patches, soname-fix (not needed)
- Enabled parallel build

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.32.20140920git1edbe523
- Rebuilt for new gnuradio

* Tue Feb  6 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.31.20140920git1edbe523
- Rebuilt for new boost

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.20140920git1edbe523
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20140920git1edbe523
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0-0.28.20140920git1edbe523
- Rebuilt for Boost 1.64

* Wed May 24 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.27.20140920git1edbe523
- Rebuilt for new gnuradio

* Wed Feb 08 2017 Kalev Lember <klember@redhat.com> - 0-0.26.20140920git1edbe523
- Rebuilt for Boost 1.63

* Fri Sep 16 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.25.20140920git1edbe523
- Rebuilt for new gnuradio

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.24.20140920git1edbe523
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.23.20140920git1edbe523
- Rebuilt for new gnuradio

* Wed Feb 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.22.20140920git1edbe523
- Rebuilt for new gnuradio

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20140920git1edbe523
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0-0.20.20140920git1edbe523
- Rebuilt for Boost 1.60

* Mon Jan 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.19.20140920git1edbe523
- Rebuilt for new gnuradio

* Tue Dec 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.18.20140920git1edbe523
- Rebuilt for new gnuradio

* Thu Nov  5 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.17.20140920git1edbe523
- Rebuilt for new gnuradio

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0-0.16.20140920git1edbe523
- Rebuilt for Boost 1.59

* Thu Aug 13 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.15.20140920git1edbe523
- Rebuilt for new gnuradio

* Tue Aug  4 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.14.20140920git1edbe523
- Rebuilt for new boost

* Tue Jul 28 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.13.20140920git1edbe523
- Rebuilt for new gnuradio

* Thu Jul 23 2015 David Tardon <dtardon@redhat.com> - 0-0.12.20140920git1edbe523
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.20140920git1edbe523
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.10.20140920git1edbe523
- Rebuilt for new gnuradio

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.9.20140920git1edbe523
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.8.20140920git1edbe523
- Rebuilt for new gnuradio

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 0-0.7.20140920git1edbe523
- Rebuild for boost 1.57.0

* Fri Dec 12 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.6.20140920git1edbe523
- Fixed idProduct in udev rule

* Tue Nov  4 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.5.20140920git1edbe523
- Require libusbx instead of libusb

* Thu Oct 23 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.4.20140920git1edbe523
- Rebuilt for new gnuradio

* Fri Oct 10 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.3.20140920git1edbe523
- Used github URL in sources

* Fri Oct 10 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.2.20140920git1edbe523
- Fixed package according to fedora review comments

* Sat Sep 20 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.1.20140920git1edbe523
- Initial release
