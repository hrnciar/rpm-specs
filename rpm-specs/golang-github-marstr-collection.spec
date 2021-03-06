# Generated by go2rpm
%bcond_without check

# https://github.com/marstr/collection
%global goipath         github.com/marstr/collection
Version:                1.0.1

%gometa

%global common_description %{expand:
Inspired by .NET's Linq, querying data structures used in this library is a
snap! Build Go pipelines quickly and easily which will apply lambdas as they
query your data structures.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        Golang implementation of a few basic data structures

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 19:26:47 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-2
- Update to new macros

* Mon Mar 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Release 1.0.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.3-1
- First package for Fedora
