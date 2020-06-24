# Generated by go2rpm
%bcond_without check

# https://github.com/VividCortex/godaemon
%global goipath         github.com/VividCortex/godaemon
%global commit          3d9f6e0b234fe7d17448b345b2e14ac05814a758

%gometa

%global common_description %{expand:
Daemonize Go applications with exec() instead of fork().

You can't daemonize the usual way in Go. Daemonizing is a Unix concept that
requires some specific things you can't do easily in Go. But you can still
accomplish the same goals if you don't mind that your program will start
copies of itself several times, as opposed to using fork() the way many
programmers are accustomed to doing.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Daemonize Go applications deviously

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 14:20:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180508git3d9f6e0
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git3d9f6e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git3d9f6e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1.20180508git3d9f6e0
- First package for Fedora