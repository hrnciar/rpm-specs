%global octpkg netcdf

Name:           octave-%{octpkg}
Version:        1.0.14
Release:        1%{?dist}
Summary:        A MATLAB compatible NetCDF interface for Octave
License:        GPLv2+
URL:            https://octave.sourceforge.io/%{octpkg}/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel
BuildRequires:  netcdf-devel

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
A MATLAB compatible NetCDF interface for Octave.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_pkg_build

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
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo
%{octpkgdir}/private/
%{_metainfodir}/octave-%{octpkg}.metainfo.xml

%changelog
* Fri Oct 16 2020 Orion Poplawski <orion@nwra.com> - 1.0.14-1
- Update to 1.0.14

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Orion Poplawski <orion@nwra.com> - 1.0.13-1
- Update to 1.0.13

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 1.0.12-8
- Rebuild with octave 64bit indexes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 1.0.12-6
- Rebuild for octave 5.1

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 1.0.12-5
- Rebuild for netcdf 4.6.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 1.0.12-3
- Rebuild for octave 4.4

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.0.12-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Orion Poplawski <orion@cora.nwra.com> - 1.0.12-1
- Update to 1.0.12
- Add %%check

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.11-2
- Rebuild for octave 4.2.0

* Mon May 23 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.11-1
- Update to 1.0.11

* Sat May 7 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.10-1
- Update to 1.0.10

* Fri Mar 18 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.9-1
- Update to 1.0.9

* Thu Feb 4 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.8-1
- Update to 1.0.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.7-2
- Rebuild for netcdf 4.4.0

* Mon Jul 6 2015 Orion Poplawski <orion@cora.nwra.com> - 1.0.7-1
- Update to 1.0.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 26 2015 Orion Poplawski <orion@cora.nwra.com> 1.0.6-1
- Update to 1.0.6

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 8 2014 Orion Poplawski <orion@cora.nwra.com> 1.0.5-1
- Update to 1.0.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> 1.0.4-1
- Update to 1.0.4

* Thu May 8 2014 Orion Poplawski <orion@cora.nwra.com> 1.0.3-1
- Update to 1.0.3

* Tue Feb 18 2014 Orion Poplawski <orion@cora.nwra.com> 1.0.2-1
- Initial Fedora package
