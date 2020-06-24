# debuginfo not supported for static libraries, RB #209316
%global debug_package %{nil}

%global srcname kiss_fft

Name:           kiss-fft
Version:        1.3.0
%global srcver %(echo %{version} | sed -e 's/\\.//g')
Release:        10%{?dist}
Summary:        Fast Fourier Transform library

License:        BSD
URL:            https://sourceforge.net/projects/kissfft
Source0:        http://downloads.sourceforge.net/kissfft/%{srcname}%{srcver}.zip
# build static library
Source1:        Makefile.libs
Source2:        README.Fedora
# use the libraries in tests (not intended for upstream)
Patch1:         %{name}-library.patch
# https://sourceforge.net/p/kissfft/code/ci/fbe1bb0bc7b94ec252842b8b7e3f3347ec75d92f/tree/kissfft.hh?diff=effd3ec61a1c4a2141fb04ab9a76d78be0459cce
Patch2:         %{name}-header.patch

# only for benchmark tests (GPLv2+ library)
BuildRequires:  fftw-devel
BuildRequires:  libtool
# for tests
BuildRequires:  numpy
BuildRequires:  python2
%if 0%{?rhel} && 0%{?rhel} <= 6
BuildRequires:  procps
%else
BuildRequires:  procps-ng
%endif

%description
A Fast Fourier Transform based up on the principle, "Keep It Simple, Stupid".
Kiss FFT is a very small, reasonably efficient, mixed radix FFT library that
can use either fixed or floating point data types.


%package devel
Summary:        Fast Fourier Transform library
Provides:       %{name}-static = %{version}-%{release}

%description devel
A Fast Fourier Transform based up on the principle, "Keep It Simple, Stupid".
Kiss FFT is a very small, reasonably efficient, mixed radix FFT library that
can use either fixed or floating point data types.

Header files and static library are provided.


%prep
%setup -q -n %{srcname}%{srcver}
cp -p %{SOURCE2} .
%patch1 -p1
%patch2 -p1
sed -i -e '1s,/usr/bin/env python,/usr/bin/python2,' test/*.py


%build
for type in float double int16 int32; do
    mkdir build_${type}
    pushd build_${type}
    CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" \
    DATATYPE=${type} \
        make %{?_smp_mflags} -f %{SOURCE1} libdir=%{_libdir} srcdir=..
    popd
done


%install
for type in float double int16 int32; do
    pushd build_${type}
    CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" \
    DATATYPE=${type} \
    DESTDIR=%{buildroot} \
        make %{?_smpflags} -f %{SOURCE1} libdir=%{_libdir} srcdir=.. install
    popd
done


%check
while read type suffix; do
    DATATYPE=${type} \
    SUFFIX=${suffix} \
        make -C tools clean all CFLAGS="%{optflags}"

    CFLAGADD="%{optflags}" \
    DATATYPE=${type} \
    SUFFIX=${suffix} \
        make -C test clean test
done << EOF
float _float
double _double
int16_t _int16
int32_t _int32
EOF


%files devel
%license COPYING
%doc CHANGELOG README README.Fedora
%{_includedir}/kissfft/
%{_libdir}/libkiss_fft_*.a
%{_libdir}/libkiss_fftnd_*.a
%{_libdir}/libkiss_fftndr_*.a
%{_libdir}/libkiss_fftr_*.a
%{_libdir}/libkiss_kfc_*.a


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 František Dvořák <valtri@civ.zcu.cz> - 1.3.0-7
- Fix problems with python

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 František Dvořák <valtri@civ.zcu.cz> - 1.3.0-1
- Initial package
