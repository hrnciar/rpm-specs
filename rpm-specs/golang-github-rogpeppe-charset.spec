# Generated by go2rpm
%bcond_without check

# https://github.com/rogpeppe/go-charset
%global goipath         github.com/rogpeppe/go-charset
%global commit          2471d30d28b404738b546df7aaa82c45826bc02e

%gometa

%global common_description %{expand:
Charset conversions in Go.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Charset conversions in Go

# Upstream license specification: BSD-2-Clause
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 14:48:36 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190629git2471d30
- Initial package
