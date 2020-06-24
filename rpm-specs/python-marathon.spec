
%global pypi_name marathon

Name:           python-%{pypi_name}
Version:        0.8.8
Release:        14%{?dist}
Summary:        Python client library/interface to the Mesos Marathon REST API

License:        MIT
URL:            https://github.com/thefactory/marathon-python
Source0:        https://pypi.io/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/thefactory/marathon-python/%{version}/README.md
BuildArch:      noarch

%description
Marathon Client Library

Python interface to the Mesos Marathon REST API

%package -n python3-%{pypi_name}
Summary: Python interface to the Mesos Marathon REST API
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-requests

%description -n python3-%{pypi_name}
Python client library/interface to the Mesos Marathon REST API

%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} README

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.8-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.8-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.8-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.8-8
- Subpackage python2-marathon has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.8-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.8-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 4 2017 David Moreau Simard <dmsimard@redhat.com> - 0.8.8-1
- Update to upstream 0.8.8
- Include license in package (fixed by upstream issue #156)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.7-2
- Rebuild for Python 3.6

* Fri Oct 14 2016 David Moreau Simard <dmsimard@redhat.com> - 0.8.6-1
- First version

