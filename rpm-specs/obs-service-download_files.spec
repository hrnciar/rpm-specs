%global service download_files

Name:           obs-service-%{service}
Version:        0.6.2
Release:        3%{?dist}
Summary:        An OBS source service: download files

License:        GPLv2+
URL:            https://github.com/openSUSE/obs-service-%{service}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
Requires:       diffutils
Requires:       wget
# for appimage parser:
Requires:       perl(YAML::XS)


%description
This is a source service for openSUSE Build Service.

This service is parsing all spec files and downloads all
Source files which are specified via http, https, or ftp URLs.


%prep
%autosetup


%build
perl -p -i -e "s{#!/usr/bin/env bash}{#!/bin/bash}" download_files


%install
%make_install


%files
%license COPYING
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service
%dir %{_sysconfdir}/obs
%dir %{_sysconfdir}/obs/services
%config(noreplace) %{_sysconfdir}/obs/services/*



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Neal Gompa <ngompa13@gmail.com> - 0.6.2-1
- Initial packaging
