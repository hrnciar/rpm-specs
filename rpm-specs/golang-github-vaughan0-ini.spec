# Generated by go2rpm
%bcond_without check

# https://github.com/vaughan0/go-ini
%global goipath         github.com/vaughan0/go-ini
%global commit          a98ad7ee00ec53921f08832bc06ecf7fd600e6a1

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-vaughan0-go-ini-devel < 0-0.15
Obsoletes:      golang-github-vaughan0-go-ini-unit-test < 0-0.15
}

%global common_description %{expand:
INI parsing library for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.18%{?dist}
Summary:        INI parsing library for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.16.20190523gita98ad7e
- Add Obsoletes for old name

* Thu May 23 20:04:41 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.15.20190523gita98ad7e
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gita98ad7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gita98ad7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gita98ad7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gita98ad7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gita98ad7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gita98ad7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gita98ad7e
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gita98ad7e
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gita98ad7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gita98ad7e
- Update of spec file to spec-2.0
  resolves: #1248163

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gita98ad7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gita98ad7e
- Choose the correct architecture
  related: #1142398

* Fri Sep 19 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.gita98ad7e
- noarch devel package
- don't redefine gopath
- don't own dirs owned by golang
- preserve timestamps of copied files
- devel package buildrequires golang 1.2.1-3 or higher
- correct version and package name

* Mon Sep 15 2014 Eric Paris <eparis@redhat.com - 0.0.0-0.1.gita98ad7e
- Bump to upstream a98ad7ee00ec53921f08832bc06ecf7fd600e6a1
