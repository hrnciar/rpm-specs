
%global service set_version

Name:           obs-service-%{service}
Version:        0.5.12
Release:        3%{?dist}
Summary:        An OBS source service: Update spec file version
License:        GPLv2+
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3dist(ddt)
BuildRequires:  python3dist(packaging)
Recommends:     python3dist(packaging)
Requires:       python3
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

Very simply script to update the version in .spec or .dsc files according to
a given version or to the existing files.

%prep
%autosetup

%build
sed -i -e "1 s,#!/usr/bin/python$,#!%{__python3}," set_version

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 set_version %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 set_version.service %{buildroot}%{_prefix}/lib/obs/service

%check
%{__python3} -m unittest discover tests/

%files
# In lieu of a proper license file: https://github.com/openSUSE/obs-service-set_version/issues/57
%license debian/copyright
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Neal Gompa <ngompa13@gmail.com> - 0.5.12-1
- Update to 0.5.12

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.10-1
- Update to 0.5.10
- Run unit tests
- Set sed properly as a build dependency

* Sat Mar 24 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.8-1
- Initial packaging

