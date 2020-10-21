%global octpkg parallel

Name:           octave-%{octpkg}
Version:        3.1.3
Release:        6%{?dist}
Summary:        Parallel execution package for cluster computers for Octave
License:        GPLv3+
URL:            https://octave.sourceforge.io/parallel/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Patch0:         parallel-20190802.diff

BuildRequires:  octave-devel
BuildRequires:  gnutls-devel
BuildRequires:  tex(latex)
BuildRequires:  ghostscript
BuildRequires:  octave-struct
BuildRequires:  autoconf
BuildRequires:  automake

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave


%description
Parallel execution package for cluster computers.

%prep
#setup -qcT
%setup -q -n %{octpkg}-%{version}
%patch0 -p1
pushd src
aclocal
autoconf
autoheader
popd

%build
export CXXFLAGS="%{optflags}"
#octave_pkg_build -T
%octave_pkg_build

%install
%octave_pkg_install
chmod a-x %{buildroot}/%{octpkgdir}/*.m
rm -rf  %{buildroot}/%{octpkgdir}/doc

%check
%octave_pkg_check
rm -rf  %{buildroot}/%{octpkgdir}/doc

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
%{octpkgdir}/private/*.m
%dir %{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/on_uninstall.m
%{octpkglibdir}
%{_metainfodir}/octave-%{octpkg}.metainfo.xml
%{octpkgdir}/bin/octave-pserver

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.3-4
- update to hg 20190802 to resolve build errors

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 3.1.3-2
- Rebuild for octave 4.4

* Mon Aug 13 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.3-1
- Update to 3.1.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.2-1
- Update to 3.1.2

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Orion Poplawski <orion@cora.nwra.com> - 3.1.1-6
- Rebuild to ship metainfo.xml so this package will appear in Software

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Orion Poplawski <orion@cora.nwra.com> - 3.1.1-2
- Rebuild for octave 4.2.0

* Mon Oct 03 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.1.1-1
- Update to 3.1.1

* Thu Feb 25 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.0.4-1
- Update to 3.0.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 1 2015 Orion Poplawski <orion@cora.nwra.com> - 3.0.3-1
- Update to 3.0.3

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-2
- Rebuild for octave 4.0.0

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-1
- Update to 2.2.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> 2.2.0-1
- update to 2.2.0

* Thu Jan 09 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> 2.1.1-3
- remove GFDL license as no files are licensed that way

* Thu Jan 09 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> 2.1.1-2
- update according to reviewer comments

* Thu Jan 09 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> 2.1.1-1
- initial package for Fedora
