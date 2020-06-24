%global pypi_name feedgen

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        2%{?dist}
Summary:        Feed Generator (ATOM, RSS, Podcasts)

License:        BSD or LGPLv3
URL:            https://lkiesow.github.io/python-feedgen
Source0:        https://github.com/lkiesow/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-dateutil
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-setuptools

%description
Feedgenerator This module can be used to generate web feeds in both ATOM and
RSS format. It has support for extensions. Included is for example an extension
to produce Podcasts.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-dateutil
Requires:       python3-lxml
%description -n python3-%{pypi_name}
Feedgenerator This module can be used to generate web feeds in both ATOM and
RSS format. It has support for extensions. Included is for example an extension
to produce Podcasts.


%prep
%autosetup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license license.lgpl license.bsd
%doc readme.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Lars Kiesow <lkiesow@uos.de> - 0.9.0-1
- New upstream version 0.9.0 (fixes CVE-2020-5227)

* Mon Sep 09 2019 Lumír Balhar <lbalhar@redhat.com> - 0.8.0-1
- New upstream version 0.8.0

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Lumír Balhar <lbalhar@redhat.com> - 0.7.0-4
- Get rid of Python 2 subpackage in Fedora 30+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.7

* Tue May 22 2018 Lumir Balhar <lbalhar@redhat.com> - 0.7.0-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Lumir Balhar <lbalhar@redhat.com> - 0.6.1-1
- Initial package.
