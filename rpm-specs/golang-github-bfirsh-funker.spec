# Generated by go2rpm
%ifnarch s390x
%bcond_without check
%endif

# https://github.com/bfirsh/funker-go
%global goipath         github.com/bfirsh/funker-go
%global commit          eaa0a2e06f30e72c9a0b7f858951e581e26ef773

%gometa

%global common_description %{expand:
A Go implementation of Funker.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Funker for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 21:44:42 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627giteaa0a2e
- Initial package
