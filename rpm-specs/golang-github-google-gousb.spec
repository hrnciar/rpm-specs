# Run tests in check section
# Requires a usb device
%bcond_with check

# https://github.com/google/gousb
%global goipath         github.com/google/gousb
%global commit          18f4c1d8a750878c4f86ac3d7319b8aa462a79f9

%global common_description %{expand:
The gousb package is an attempt at wrapping the libusb library into a 
Go-like binding.}

%gometa

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md

%global godevelheader %{expand:
Requires:       pkgconfig(libusb)}

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Idiomatic Go bindings for libusb-1.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  pkgconfig(libusb)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gochecks
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Jakub Jelen <jjelen@redhat.com> - 0-0.1.20200108git18f4c1d8
- First package for Fedora

