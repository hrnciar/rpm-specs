# Run tests in check section
# Requires a usb device
%bcond_with check

# https://github.com/google/gousb
%global goipath         github.com/google/gousb
Version:                1.1.0

%global common_description %{expand:
The gousb package is an attempt at wrapping the libusb library into a 
Go-like binding.}

%gometa

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md

%global godevelheader %{expand:
Requires:       pkgconfig(libusb)}

Name:           %{goname}
Release:        2%{?dist}
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 23:37:51 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Jakub Jelen <jjelen@redhat.com> - 0-0.1.20200108git18f4c1d8
- First package for Fedora
