%global commit 7ad249625eb42ab4b9ed9697c2f72aaed551a5f4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20201010
%global fedora_soname 2.0
Name:           liquid-dsp
Version:        1.3.2
Release:        3.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:        Digital Signal Processing Library for Software-Defined Radios

License:        MIT
URL:            http://liquidsdr.org/
Source0:        https://github.com/jgaeddert/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# upstream autotools files not in the tarball
Source1:        config.h.in
# set soname ourselves as upstream doesn't
Patch0:         soname-version.patch
# Patch configure.ac for ppc64
Patch1:         ppc64-configureac.patch
# fixes ppc64 altivec, other 64-bit problems. Patch by Dan Horák.
# https://github.com/jgaeddert/liquid-dsp/pull/136
Patch3:         ppc64.patch
BuildRequires:  gcc
BuildRequires:  fftw-devel fftw-libs-single
BuildRequires:  autoconf automake libtool

%description
Digital signal processing library for software-defined radios

%package -n %{name}-devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-devel
Digital signal processing library for software-defined radios

%prep
%autosetup -p1 -n %{name}-%{commit}
cp %{SOURCE1} .
autoreconf -f -i
%build
%configure --exec_prefix=/ --enable-simdoverride
%make_build

%check
make check

%install
%make_install
pushd ${RPM_BUILD_ROOT}/%{_libdir} > /dev/null 2>&1
rm libliquid.a
ln -s libliquid.so.2.0 libliquid.so
chmod a+x libliquid.so.%{fedora_soname}
popd > /dev/null 2>&1

%ldconfig_scriptlets
%files
%license LICENSE
%{_libdir}/libliquid.so.%{fedora_soname}


%files -n %{name}-devel
%{_includedir}/liquid/
%{_libdir}/libliquid.so


%changelog
* Mon Oct 12 2020 Matt Domsch <matt@domsch.com> 1.3.2-3.20201010git7ad2496
- Upstream removed the exit() calls https://github.com/jgaeddert/liquid-dsp/issues/134
- invoke autoreconf at build time, as upstream doesn't package what we need
- Add BR: fftw-devel
- Remove BR: gcovr and --enable-coverage. It was keeping the exit call in the library,
  and we aren't looking at the coverage results anyhow.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr  7 2020 Matt Domsch <matt@domsch.com> 1.3.2-1
- upstream 1.3.2
- upstream constantly changes the ABI in backwards-incompatible ways without versioning
  with sonames themselves. Add a fedora_soname.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6.20180806git9658d81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5.20180806git9658d81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4.20180806git9658d81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug  15 2018 Matt Domsch <matt@domsch.com> 1.3.1-3.20180806git9658d81
- apply patch fixing ppc64, armv7hl build failures

* Tue Aug  14 2018 Matt Domsch <matt@domsch.com> 1.3.1-2.20180806git9658d81
- remove -faltivec from ppc64le build gcc args

* Tue Aug  7 2018 Matt Domsch <matt@domsch.com> 1.3.1-1.20180806git9658d81
- Initial Fedora packaging
