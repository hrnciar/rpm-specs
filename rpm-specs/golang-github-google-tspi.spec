# Generated by go2rpm
%bcond_without check

# https://github.com/google/go-tspi
%global goipath         github.com/google/go-tspi
Version:                0.2.0

%gometa

%global goaltipaths     github.com/coreos/go-tspi

%global godevelheader %{expand:
Requires:       trousers-devel}

%global common_description %{expand:
This is a library providing a set of bindings for communication between code
written in Go and libtspi, the library responsible for providing a TPM control
interface.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        TSPI bindings for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/certificate-transparency-go/x509)
BuildRequires:  trousers-devel

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 21:44:05 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package
