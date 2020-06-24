Name:           qcint
Version:        3.0.20
Release:        2%{?dist}
Summary:        An optimized libcint branch for X86 platform

License:        GPLv3+
URL:            https://github.com/sunqm/qcint
Source0:        https://github.com/sunqm/qcint/archive/v%{version}/qcint-%{version}.tar.gz

# This package uses AVX/AVX2/AVX-512 extensions
ExclusiveArch:  x86_64
# qcint is a drop-in replacement of libcint with architecture dependent optimizations
Conflicts:      libcint

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openblas-devel 
BuildRequires:  cmake 
BuildRequires:  python2-devel 
BuildRequires:  numpy 

%description    
Qcint is a branch of the libcint library.  It provides exactly the
same APIs as libcint. However, the code is optimized using AVX
instructions. On x86_64 platform, qcint can be 5 ~ 50% faster than
libcint. Please refer to libcint for more details of the features.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      libcint-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
mkdir build
cd build
export CFLAGS="%{optflags} -Wl,--as-needed"
%cmake -DENABLE_EXAMPLE=1 -DWITH_F12=1 -DWITH_COULOMB_ERF=1 -DWITH_RANGE_COULOMB=1 -DQUICK_TEST=1 -DBLAS_LIBRARIES=%{_libdir}/libopenblaso.so ..
make %{?_smp_mflags} VERBOSE=1

%install
make -C build install DESTDIR=%{buildroot}

%check

%ldconfig_scriptlets

%files
%doc README.md ChangeLog
%license LICENSE
%{_libdir}/libcint.so.*

%files devel
%{_includedir}/cint.h
%{_libdir}/libcint.so

%changelog
* Sat May 23 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-2
- Add conflicts with libcint-devel to qcint-devel package.

* Thu May 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-1
- Update to 3.0.20, no changes from 3.0.19.

* Sun Feb 02 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-3
- Use OpenBLAS instead of ATLAS.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-1
- Update to 3.0.19.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.2-1
- Update to version 3.0.2.

* Tue Sep 26 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.1-1
- Update to version 3.0.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Matt Chan <talcite@gmail.com> - 1.8.6-1
- Initial build
