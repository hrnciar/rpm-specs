%global commit 0036426a605933d0c05fcab7441f95d61e679349
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           chck
Version:        0
Release:        9.20161208git%{shortcommit}%{?dist}
Summary:        Collection of C utilities
License:        zlib
URL:            https://github.com/Cloudef/chck
Source0:        https://github.com/Cloudef/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  make

%description
Collection of C utilities taken and cleaned up from my other projects

%package devel
Summary:        Collection of C utilities development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Collection of C utilities taken and cleaned up from my other projects

%prep
%autosetup -n %{name}-%{commit}

%build
%cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
ctest -V -R dl_test
ctest -V %{?_smp_mflags}

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_libdir}/libchck-*.so.0*

%files devel
%{_includedir}/chck/
%{_libdir}/pkgconfig/chck.pc
%{_libdir}/libchck-*.so

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20161208git0036426
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20161208git0036426
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20161208git0036426
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20161208git0036426
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20161208git0036426
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20161208git0036426
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20161208git0036426
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20161208git0036426
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.201612080036426a60
* Tue Sep 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.20160906git55d41fb
- Update to current master

* Sun May 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.20160529git5275403
- Update to current master version

* Fri Apr 08 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.20160408git2efd6cd
- Move unversioned libs to the -devel package
- Improve ownership of folder /usr/include/chck
- Add BuildRequires: make

* Thu Apr 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.20160407git2efd6cd
- Add ownership of folder /usr/include/chck

* Wed Apr 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.20160406git2efd6cd
- Update to current master version

* Sun Feb 14 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0-1.20160214git79d125f
- First Fedora version 
