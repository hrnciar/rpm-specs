%global octpkg ncarray

Name:           octave-%{octpkg}
Version:        1.0.4
Release:        12%{?dist}
Summary:        Access NetCDF files as a multi-dimensional array

License:        GPLv2+
URL:            http://octave.sourceforge.net/ncarray/
Source0:        http://downloads.sourceforge.net/octave/ncarray-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  octave-devel
# For tests
BuildRequires:  octave-netcdf >= 1.0.2
BuildRequires:  octave-statistics >= 1.0.6
Requires:       octave(api) = %{octave_api}
Requires:       octave-netcdf >= 1.0.2
Requires:       octave-statistics >= 1.0.6
Requires(post): octave
Requires(postun): octave

%description
Access a single or a collection of NetCDF files as a multi-dimensional array.


%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/@BaseArray/
%{octpkgdir}/@CatArray/
%{octpkgdir}/@ncArray/
%{octpkgdir}/@ncBaseArray/
%doc %{octpkgdir}/doc-cache
%dir %{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/on_uninstall.m
%{octpkgdir}/private/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 1.0.4-10
- Rebuild with octave 64bit indexes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 1.0.4-8
- Rebuild for octave 5.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 1.0.4-6
- Rebuild for octave 4.4

* Fri Jul 27 2018 Orion Poplawski <orion@cora.nwra.com> - 1.0.4-5
- BR octave-netcdf and octave-statics for tests

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Orion Poplawski <orion@cora.nwra.com> - 1.0.4-1
- Update to 1.0.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.3-6
- Rebuild for octave 4.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.0.3-4
- Rebuild for octave 4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 7 2014 Orion Poplawski <orion@cora.nwra.com> 1.0.3-1
- Update to 1.0.3

* Wed Apr 16 2014 Orion Poplawski <orion@cora.nwra.com> 1.0.2-1
- Initial Fedora package
