%global octpkg struct

Name:           octave-%{octpkg}
Version:        1.0.16
Release:        5%{?dist}
Summary:        Structure handling for Octave
License:        GPLv3+
URL:            https://octave.sourceforge.io/struct/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel 

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave


%description
Octave includes support for organizing data in structures. This package
contains additional data structure manipulation functions that are not
included in the octave core.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/packinfo
%doc %{octpkgdir}/packinfo/COPYING
%{octpkglibdir}
%{_metainfodir}/octave-struct.metainfo.xml


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 1.0.16-4
- Rebuild with octave 64bit indexes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 1.0.16-2
- Rebuild for octave 5.1

* Sun Apr 14 2019 Orion Poplawski <orion@nwra.com> - 1.0.16-1
- Update to 1.0.16

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 1.0.15-3
- Rebuild for octave 4.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.15-1
- update to 1.0.15

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.14-1
- Update to 1.0.14

* Thu Feb 25 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.12-1
- update to 1.0.12

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.0.11-1
- Update to 1.0.11

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.10-8
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 1.0.10-5
- Rebuild for octave 3.8.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun  5 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.10-1
- update to 1.0.10

* Mon Jan 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.9-7
- rebuild for octave 3.6.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.9-5
- Bump spec since buildroot override was not in place.

* Mon Aug 15 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.9-4
- Comply to Octave Packaging Guidelines by requiring exact version of
  octave(api).

* Mon Jun 13 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> 1.0.9-3
- Add comment regarding patch purpose

* Mon Jun 13 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> 1.0.9-2
- Review input

* Fri Jun 03 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> 1.0.9-1
- initial package for Fedora
