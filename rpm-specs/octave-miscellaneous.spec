%global octpkg miscellaneous

Name:           octave-%{octpkg}
Version:        1.3.0
Release:        4%{?dist}
Summary:        Miscellaneous functions for Octave
License:        GPLv3+
URL:            https://octave.sourceforge.io/miscellaneous/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel
BuildRequires:  dos2unix
BuildRequires:  units
%if 0%{?fedora} >= 30
BuildRequires:  /usr/bin/2to3
BuildRequires:  python3-rpm-macros
%else
BuildRequires:  python2-rpm-macros
%endif
BuildRequires:  /usr/bin/pathfix.py

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave


%description
Miscellaneous tools that don't fit somewhere else. It includes
additional functions for manipulating cell arrays, computation of
Chebyshev, Hermite, Legendre and Laguerre polynomials, working with
CSV data and for Latex export.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install
chmod a-x %{buildroot}/%{octpkgdir}/*.m
dos2unix %{buildroot}/%{octpkgdir}/*.m
chmod a-x %{buildroot}/%{octpkgdir}/private/*.m
dos2unix %{buildroot}/%{octpkgdir}/private/*.m
%if 0%{?fedora} >= 30
/usr/bin/2to3 --write --nobackups %{buildroot}%{octpkgdir}
/usr/bin/pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{octpkgdir}
%else
/usr/bin/pathfix.py -pni "%{__python2} %{py2_shbang_opts}" %{buildroot}%{octpkgdir}
%endif
rm -rf %{buildroot}/%{octpkgdir}/test

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/private/*.m
%{octpkgdir}/*.py*
%{octpkgdir}/packinfo
%doc %{octpkgdir}/packinfo/COPYING

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 1.3.0-2
- Rebuild with octave 64bit indexes

* Sun Oct 27 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.3.0-1
- drop BR on octave-general
- Update to 1.3.0 (#1765941)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 1.2.1-15
- Rebuild for octave 5.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-13
- Rebuild for octave 4.4
- Use Python 3 on Fedora 30+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-7
- Rebuild for octave 4.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-5
- Rebuild for octave 4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.1-1
- update to 1.2.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.0-4
- Rebuild for octave 3.8.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.0-1
- update to 1.2.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.0-1
- update to 1.1.0

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-6
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.11-5
- rebuild for octave 3.6.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 06 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.11-3
- Bump spec due to change of octave api version.

* Tue Jun 14 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.11-2
- Review input

* Fri Jun 03 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> 1.0.11-1
- initial package for Fedora
