# Generated by go2rpm
%bcond_without check

# https://github.com/dchest/cssmin
%global goipath         github.com/dchest/cssmin
%global commit          fb8d9b44afdc258bfff6052d3667521babcb2239

%gometa

%global common_description %{expand:
Package Cssmin minifies CSS. It's a port of Ryan Grove's cssmin from Ruby.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.11%{?dist}
Summary:        Go package to minify CSS

# Upstream license specification: BSD-3-Clause
License:        BSD
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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 15:49:55 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.9.20190524gitfb8d9b4
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitfb8d9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitfb8d9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitfb8d9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitfb8d9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitfb8d9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.3.gitfb8d9b4
- Regenerate spec file with gofed 1.0

* Thu Dec 10 2015 Fabio Alessandro Locati <fabio@locati.cc> - 0-0.2.gitfb8d9b4
- Update to version with LICENSE file

* Thu Dec 10 2015 Fabio Alessandro Locati <fabio@locati.cc> - 0-0.1.gita22e1d8
- First package for Fedora
