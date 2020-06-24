%global git_commit_0 54c86a517edf7933f4ce5e87c8c57d243c85b3ba
%global git_user analogdevicesinc
%global git_snap_date 20170705

%global git_short_commit_0 %(c=%{git_commit_0}; echo ${c:0:7})


# Using a git snapshot becuase the most recent release is very outdated,
# and doesn't support e.g. the PlutoSDR.

Name:          gr-iio
Version:       0.2
Release:       13.%{git_snap_date}git%{git_short_commit_0}%{?dist}
Summary:       GNU Radio interface for IIO

License:       GPLv3+

URL:           https://github.com/%{git_user}/%{name}/

#Source0:       https://github.com/%{git_user}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:        https://github.com/%{git_user}/%{name}/archive/%{git_commit_0}.tar.gz


BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: bison
BuildRequires: flex
BuildRequires: swig
BuildRequires: doxygen
BuildRequires: pkgconfig(gnuradio-runtime)
BuildRequires: pkgconfig(libiio)
BuildRequires: pkgconfig(libad9361)


%description
GNU Radio interface for IIO. Includes source and sink blocks for
Analog Devices ADALM-PLUTO SDR.


%package devel
Summary:       Development package for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.


# NOTE: gnuradio 3.8 is expected to have Python 3 support. When that
# becomes available, Python 3 support should be added to this package.


%prep
%setup -q -n %{name}-%{git_commit_0}

%build
if [ "%{_libdir}" = "%{_prefix}/lib64" ]; then
  %cmake -DUSE_LIB64:BOOL=ON .
else
  %cmake -DUSE_LIB64:BOOL=OFF .
fi

%make_build V=1

%install
%make_install INSTALL='install -p'

mkdir %{buildroot}%{_datarootdir}/%{name}
# The following will result in an rpmlint error, but it is a false alarm,
# because we are moving a file FROM a hardcoded path, where it shouldn't be,
# to the correct location.
mv %{buildroot}/usr/lib/cmake/iio/iioConfig.cmake %{buildroot}%{_datarootdir}/%{name}/


# Remove libtool archives.
find %{buildroot} -name '*.la' -delete


%files
%license COPYING
%{_libdir}/libgnuradio-iio.so.*
%{_datarootdir}/gnuradio/grc/blocks/*.xml

%files devel
%{_libdir}/libgnuradio-iio.so
%{_libdir}/pkgconfig/gnuradio-iio.pc
%{_includedir}/gnuradio/iio
%{_includedir}/swig/iio*.i
%{_datarootdir}/gr-iio

%exclude %{_libdir}/python2*

%changelog
* Tue Apr 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2-13.20170705git54c86a5
- Rebuilt for new gnuradio

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12.20170705git54c86a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11.20170705git54c86a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2-10.20170705git54c86a5
- Rebuilt for new gnuradio

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9.20170705git54c86a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.2-8.20170705git54c86a5
- Rebuilt for Boost 1.69

* Thu Jan 10 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-7.20170705git54c86a5
- Remove Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6.20170705git54c86a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5.20170705git54c86a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.2-4.20170705git54c86a5
- Rebuilt for Boost 1.66

* Thu Sep 21 2017 Eric Smith <brouhaha@fedoraproject.org> 0.2-3.20170705git54c86a5
- Add missing BuildRequires of pkgconfig(libiio).

* Tue Sep 19 2017 Eric Smith <brouhaha@fedoraproject.org> 0.2-2.20170705git54c86a5
- Updated per package review (#1482261) comments.

* Wed Aug 16 2017 Eric Smith <brouhaha@fedoraproject.org> 0.2-1
- Initial version.
