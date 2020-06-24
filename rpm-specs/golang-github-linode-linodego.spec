# Generated by go2rpm
# Needs network
%bcond_with check

# https://github.com/linode/linodego
%global goipath         github.com/linode/linodego
Version:                0.10.0

%gometa

%global common_description %{expand:
Go client for Linode REST v4 API.}

%global golicenses      LICENSE
%global godocs          API_SUPPORT.md CHANGELOG.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go client for Linode REST v4 API

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gopkg.in/resty.v1)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 23:31:29 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.10.0-1
- Release 0.10.0

* Thu Jun 27 15:23:53 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.0-1
- Release 0.9.0

* Sun May 12 2019 Carl George <carl@george.computer> - 0.8.0-1
- Latest upstream

* Fri Mar 15 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.1-1
- Release 0.7.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Carl George <carl@george.computer> - 0.7.0-1
- Latest upstream
- Skip tests on 32bit architectures

* Tue Nov 27 2018 Carl George <carl@george.computer> - 0.6.2-1
- Initial package