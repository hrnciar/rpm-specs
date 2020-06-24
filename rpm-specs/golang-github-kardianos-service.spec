# Generated by go2rpm
%bcond_without check

# https://github.com/kardianos/service
%global goipath         github.com/kardianos/service
Version:                1.0.0

%gometa

%global common_description %{expand:
service will install / un-install, start / stop, and run a program as a
service (daemon). Currently supports Windows XP+, Linux/(systemd | Upstart |
SysV), and OSX/Launchd.}

%global golicenses      LICENSE
%global godocs          example README.md linux_test/README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Run go programs as a service on major platforms

# Upstream license specification: Zlib
License:        zlib
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
%gocheck -d .
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 20:57:59 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-2
- Update to new macros

* Mon Mar 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Release 1.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git615a14e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git615a14e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1.20180509git615a14e
- First package for Fedora