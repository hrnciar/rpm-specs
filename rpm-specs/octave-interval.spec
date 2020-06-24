%global octpkg interval

Name:           octave-%{octpkg}
Version:        3.2.0
Release:        9%{?dist}
Summary:        Interval arithmetic for Octave
# The source code is GPLv3+ except src/crlibm/ which is LGPLv2+
License:        GPLv3+ and LGPLv2+
URL:            https://octave.sourceforge.io/%{octpkg}/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.8.0
BuildRequires:  mpfr-devel

Requires:       octave(api) = %{octave_api}
Requires:       mpfr >= 3.1.0
Requires(post): octave
Requires(postun): octave


%description
The Octave-forge Interval package for real-valued interval arithmetic
allows one to evaluate functions over subsets of their domain.  All
results are verified, because interval computations automatically keep
track of any errors.  These concepts can be used to handle
uncertainties, estimate arithmetic errors and produce reliable
results.  Also it can be applied to computer-assisted proofs,
constraint programming, and verified computing.  The implementation is
based on interval boundaries represented by binary64 numbers and is
conforming to IEEE Std 1788-2015, IEEE standard for interval
arithmetic.


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
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/@infsup
%{octpkgdir}/@infsupdec
%{octpkgdir}/test
%doc %{octpkgdir}/doc
%dir %{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/CITATION
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/*.m
%{_metainfodir}/octave-%{octpkg}.metainfo.xml


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 3.2.0-8
- Rebuild with octave 64bit indexes

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 3.2.0-7
- Rebuild for mpfr 4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 3.2.0-5
- Rebuild for octave 5.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 3.2.0-3
- Rebuild for octave 4.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Colin B. Macdonald <cbm@m.fsf.org> - 3.2.0-1
- Version bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 25 2017 Colin B. Macdonald <cbm@m.fsf.org> - 3.1.0-1
- Version bump

* Sun Nov 05 2017 Colin B. Macdonald <cbm@m.fsf.org> - 3.0.0-2
- Minor bump

* Mon Aug 28 2017 Colin B. Macdonald <cbm@m.fsf.org> - 3.0.0-1
- Version bump, drop patch

* Mon Aug 21 2017 Colin B. Macdonald <cbm@m.fsf.org> - 2.1.0-4
- Add sources

* Thu Aug 17 2017 Colin B. Macdonald <cbm@m.fsf.org> - 2.1.0-3
- included library has different license
- remove Group tag
- thanks to Robert-André Mauchin for the review

* Tue Aug 15 2017 Colin B. Macdonald <cbm@m.fsf.org> - 2.1.0-2
- patch for SSE detection

* Mon Aug 14 2017 Colin B. Macdonald <cbm@m.fsf.org> - 2.1.0-1
- initial package for Fedora

* Thu Dec 03 2015 Colin B. Macdonald <cbm@m.fsf.org> - 1.3.0-1
- initial package
