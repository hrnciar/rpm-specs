# Generated by go2rpm
# Needs network
%bcond_with check

# https://github.com/RackSec/srslog
%global goipath         github.com/RackSec/srslog
%global commit          a4725f04ec91af1a91b380da679d6e0c2f061e59

%gometa

%global common_description %{expand:
Golang package that is a drop-in replacement for the standard library
log/syslog, but with extra features.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Drop-in replacement for the standard library log/syslog, but with extra features

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 18:47:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627gita4725f0
- Initial package