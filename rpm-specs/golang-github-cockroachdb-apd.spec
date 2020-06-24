# Generated by go2rpm
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/cockroachdb/apd
%global goipath         github.com/cockroachdb/apd
Version:                2.0.1

%gometa

%global common_description %{expand:
Apd is an arbitrary-precision decimal package for Go.

Apd implements much of the decimal specification from the General Decimal
Arithmetic description. This is the same specification implemented by python’s
decimal module and GCC’s decimal extension.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Arbitrary-precision decimals for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pkg/errors)

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 23:15:43 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-1
- Initial package