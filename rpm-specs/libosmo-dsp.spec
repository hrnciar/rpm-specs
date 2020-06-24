Name:             libosmo-dsp
URL:              http://osmocom.org/projects/libosmo-dsp
Version:          0.3
Release:          13%{?dist}
License:          GPLv2+
BuildRequires:    autoconf, automake, libtool, fftw-devel, doxygen, graphviz
Summary:          A library with SDR DSP primitives
Source0:          http://cgit.osmocom.org/libosmo-dsp/snapshot/%{name}-%{version}.tar.bz2

%description
A library with SDR DSP primitives.

%package devel
Summary:          Development files for libosmo-dsp
Requires:         %{name} = %{version}-%{release}

%description devel
Development files for libosmo-dsp.

%package doc
Summary:          Documentation files for libosmo-dsp
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%description doc
Documentation files for libosmo-dsp.

%prep
%setup -q

%build
# Fix pkg-config version, related to rhbz#1692517, it could be dropped
# when fixed upstream
test -x ./git-version-gen && echo %{version}-%{release} > .tarball-version 2>/dev/null

autoreconf -fi
%configure --disable-static
make CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# remove libtool
rm -f %{buildroot}%{_libdir}/*.la

# fix docs location
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/libosmodsp %{buildroot}%{_docdir}/%{name}/html

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/osmocom
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%files doc
%{_docdir}/%{name}/html

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3-11
- Updated URL

* Wed Mar 27 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3-10
- Fixed version in pkg-config file
  Related: rhbz#1692517

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct  8 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3-1
- Initial release
