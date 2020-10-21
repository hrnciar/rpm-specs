# Generated by go2rpm
%bcond_without check

# https://github.com/bradfitz/iter
%global goipath         github.com/bradfitz/iter
%global commit          e8f45d346db8021e0dd53899bf55eb6e21218b33

%gometa

%global common_description %{expand:
Package Iter provides a syntactically different way to iterate over integers.}

%global golicenses      LICENSE
%global godocs          README.txt

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Range over integers [0,n)

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 14:34:27 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20200724gite8f45d3
- Bump to commit e8f45d346db8021e0dd53899bf55eb6e21218b33

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 23:29:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190307git33e6a98
- Update to new macros

* Thu Mar 07 2019 Robert-André Mauchin - 0-0.1.20190307git33e6a98
- First package for Fedora
