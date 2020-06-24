# Generated by go2rpm
%bcond_without check

# https://github.com/exoscale/egoscale
%global goipath         github.com/exoscale/egoscale
Version:                0.23.0

%gometa

%global common_description %{expand:
Package Egoscale is a mapping for the Exoscale API.}

%global golicenses      LICENSE
%global godocs          AUTHORS CHANGELOG.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Wrapper for the Exoscale public cloud API

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gofrs/uuid)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
# https://github.com/exoscale/egoscale/issues/421
%gocheck -d .
%endif

%gopkgfiles

%changelog
* Fri Feb 07 03:01:22 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.23.0-1
- Update to 0.23.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 19:35:38 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.18.1-1
- Release 0.18.1

* Fri Apr 12 22:36:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.16.0-1
- Release 0.16.0 (#1699359)

* Tue Apr 02 19:39:59 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.15.0-1
- Release 0.15.0 (#1694789)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Carl George <carl@george.computer> - 0.13.2-1
- Latest upstream

* Sun Jan 06 2019 Carl George <carl@george.computer> - 0.13.1-1
- Initial package
