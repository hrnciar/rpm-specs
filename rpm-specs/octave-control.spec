%global octpkg control

Name:           octave-%{octpkg}
Version:        3.2.0
Release:        5%{?dist}
Summary:        Computer-Aided Control System Design (CACSD) Tools for Octave
License:        GPLv3+
URL:            http://octave.sourceforge.net/control/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://netix.dl.sourceforge.net/project/octave/Octave%20Forge%20Packages/Individual%20Package%20Releases/%{octpkg}-%{version}.tar.gz
BuildRequires:  octave-devel >= 3.8.0
# for arm
BuildRequires:  blas-devel
BuildRequires:  lapack-devel

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave


%description
The Octave control systems package contains functions for analyzing
and designing automatic control systems and algorithms.

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install
for i in %{octpkgdir}/doc/references.txt; do
  iconv -f iso8859-1 -t utf-8 %{buildroot}/$i > %{buildroot}/$i.conv && mv -f %{buildroot}/$i.conv %{buildroot}/$i
done;

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
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/packinfo
%doc %{octpkgdir}/packinfo/COPYING
%{octpkgdir}/@lti
%{octpkgdir}/@ss
%{octpkgdir}/@tf
%{octpkgdir}/@tfpoly
%{octpkgdir}/@frd
%{octpkgdir}/@iddata
%doc %{octpkgdir}/doc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 3.2.0-4
- Rebuild with octave 64bit indexes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 3.2.0-2
- Rebuild for octave 5.1

* Fri Apr 05 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.2.0-1
- update to 3.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 3.1.0-3
- Rebuild for octave 4.4
- Add upstream patches to fix crash

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.0-1
- update to 3.1.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-3
- Rebuild for gcc 7

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-2
- Rebuild for octave 4.2

* Thu Feb 04 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.0.0-1
- update to 3.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Orion Poplawski <orion@cora.nwra.com> - 2.8.3-2
- Add %%check

* Mon Jul 6 2015 Orion Poplawski <orion@cora.nwra.com> - 2.8.3-1
- Update to 2.8.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.6.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Oct 13 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.6-1
- update to 2.6.6

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.5-1
- update to 2.6.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.4-1
- update to 2.6.4

* Tue Feb  4 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.2-1
- update to 2.6.2

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-3
- Rebuild for octave 3.8.0

* Sat Dec 28 2013 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-2
- Rebuild for octave 3.8.0

* Sat Dec 14 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.1-1
- update to 2.6.1

* Sun Nov 24 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.0-1
- update to 2.6.0

* Thu Sep 26 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.4.3-3
- rebuild for blas and atlas

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.4.3-1
- update to 2.4.3

* Tue Feb 19 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.4.2-1
- update to 2.4.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov  2 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.4.1-1
- update to 2.4.1

* Thu Sep 27 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.4.0-1
- update to 2.4.0

* Sun Sep 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.3.54-1
- update to 2.3.54

* Tue Aug 28 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.3.53-1
- update to 2.3.53

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.3.52-1
- update to 2.3.52

* Tue Jun  5 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.3.51-1
- update to 2.3.51

* Mon Feb 13 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.5-1
- update to 2.2.5

* Mon Jan 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.4-2
- rebuild for octave 3.6.0

* Fri Jan 13 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.4-1
- update to 2.2.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec  8 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.3-1
- update to 2.2.3

* Mon Dec  5 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.2-1
- update to 2.2.2

* Tue Oct 25 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.1-1
- update to 2.2.1

* Tue Sep 27 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.2.0-1
- update to 2.2.0

* Thu Sep  8 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.1.55-1
- update to 2.1.55

* Fri Aug 26 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.1.54-1
- update to 2.1.54

* Wed Aug 24 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.1.53-1
- update to 2.1.53

* Sat Aug 06 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0.2-3
- Bump spec due to change of octave api version.

* Wed Jun 15 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.0.2-2
- Review input

* Fri Jun 03 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> 2.0.2-1
- initial package for Fedora
