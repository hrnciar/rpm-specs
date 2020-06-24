# Generated by go2rpm
%bcond_without check

# https://github.com/jmhodges/clock
%global goipath         github.com/jmhodges/clock
Version:                1.1

%gometa

%global common_description %{expand:
Package Clock provides an abstraction for system time that enables testing of
time-sensitive code.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Abstraction for system time that enables testing of time-sensitive code

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 22:01:22 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1-1
- Initial package
