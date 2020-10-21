# Generated by go2rpm 1
%bcond_without check

# https://github.com/putdotio/go-putio
%global goipath         github.com/putdotio/go-putio
Version:                1.3.2

%gometa

%global common_description %{expand:
Putio is a Go client library for accessing the Put.io API v2.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Put.io Go API client

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(golang.org/x/oauth2)
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
* Sat Aug 01 00:53:02 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 19:18:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190927git19b9c63
- Initial package
