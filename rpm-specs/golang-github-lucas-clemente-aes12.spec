# Generated by go2rpm
%bcond_without check

# https://github.com/lucas-clemente/aes12
%global goipath         github.com/lucas-clemente/aes12
%global commit          cd47fb39b79f867c6e4e5cd39cf7abd799f71670

%gometa

%global common_description %{expand:
This package modifies the AES-GCM implementation from Go's standard library to
use 12 byte tag sizes. It is not intended for a general audience, and used in
quic-go.}

%global golicenses      LICENSE
%global godocs          Readme.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        AES-GCM with 12 byte tag sizes for Go

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 19:12:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190702gitcd47fb3
- Initial package
