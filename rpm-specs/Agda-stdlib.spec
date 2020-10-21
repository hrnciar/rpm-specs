# https://fedoraproject.org/wiki/Packaging:Haskell

Name:           Agda-stdlib
Version:        1.3
Release:        4%{?dist}
Summary:        Agda standard libraries

License:        MIT
URL:            http://wiki.portal.chalmers.se/agda/agda.php?n=Libraries.StandardLibrary
Source0:        https://github.com/agda/agda-stdlib/archive/v%{version}.tar.gz#/agda-stdlib-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-filemanip-devel
BuildRequires:  Agda
# .agdai files are arch independent
BuildArch:      noarch
Obsoletes:      ghc-agda-lib-ffi < 0.0.2-6, ghc-agda-lib-ffi-devel < 0.0.2-6
Requires:       Agda = 2.6.1

%description
Agda standard libraries


%package docs
Summary:        Agda standard libraries documentation
BuildArch:      noarch

%description docs
This package provides the html documentation for the stdlibs
generated by the Agda compiler program.


%prep
%setup -q -n agda-stdlib-%{version}


%build
%ghc_bin_build
dist/build/GenerateEverything/GenerateEverything

%global agda agda --no-libraries -i. -isrc
%{agda} Everything.agda

%{agda} --html README.agda


%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr src _build %{buildroot}%{_datadir}/%{name}

install -p -m 0644 standard-library.agda-lib %{buildroot}%{_datadir}/%{name}/


%check
%{agda} README.agda


%files
%license LICENCE
%doc CHANGELOG.md README.md
%{_datadir}/%{name}


%files docs
%license LICENCE
%doc CHANGELOG Everything* HACKING.md README*
%doc html

%changelog
* Mon Aug 24 2020 Jens Petersen <petersen@redhat.com> - 1.3-4
- Agda-2.6.1 puts .agdai files under _build/
- move Everything and README modules to docs

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Jens Petersen <petersen@redhat.com> - 1.3-2
- make package noarch

* Sat Jun 27 2020 Jens Petersen <petersen@redhat.com> - 1.3-1
- https://github.com/agda/agda-stdlib/blob/v1.3/CHANGELOG.md

* Tue May 26 2020 Jens Petersen <petersen@redhat.com> - 1.2-1
- update to 1.2
- https://github.com/agda/agda-stdlib/blob/v1.2/CHANGELOG.md
- requires Agda instead of ghc-Agda now

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Jens Petersen <petersen@redhat.com> - 1.1-1
- update to 1.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Jens Petersen <petersen@redhat.com> - 0.17-1
- update to 0.17

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Jens Petersen <petersen@redhat.com> - 0.15-4
- keep README*.agdai
- require ghc-Agda

* Wed Aug 22 2018 Jens Petersen <petersen@redhat.com> - 0.15-3
- install library files correctly under src/

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul  1 2018 Jens Petersen <petersen@redhat.com> - 0.15-1
- update to 0.15 for Agda-2.5.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 12 2017 Jens Petersen <petersen@redhat.com> - 0.13-1
- update to 0.13
- install standard-library.agda-lib package file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Jens Petersen <petersen@redhat.com> - 0.11-3
- update to 0.11

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 Jens Petersen <petersen@redhat.com> - 0.9-1
- update to 0.9
- include ffi lib in main package

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb  5 2014 Jens Petersen <petersen@redhat.com> - 0.7-3
- no ghc-rpm-macros-extra on F19

* Mon Feb  3 2014 Jens Petersen <petersen@redhat.com> - 0.7-2
- only build on arch's where Agda builds

* Tue Jun 25 2013 Jens Petersen <petersen@redhat.com> - 0.7-1
- update to 0.7 with agda-lib-ffi-0.0.2
- use ghc-rpm-macros-extra
- add ffi_ver macro for agda-lib-ffi version

* Thu Jul 12 2012 Jens Petersen <petersen@redhat.com> - 0.6-4
- move stdlib files to datadir
- subpackage html docs

* Wed Jul 11 2012 Jens Petersen <petersen@redhat.com> - 0.6-3
- subpackage agda-lib-ffi for MAlonzo backend

* Wed Jul 11 2012 Jens Petersen <petersen@redhat.com> - 0.6-2
- fix the manifest to include the libraries
- add html
- turn off debuginfo
- remove README interface files

* Wed Jul 11 2012 Jens Petersen <petersen@redhat.com> - 0.6-1
- update to 0.6

* Sat Jun  4 2011 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- initial packaging for Fedora automatically generated by cabal2spec-0.23
