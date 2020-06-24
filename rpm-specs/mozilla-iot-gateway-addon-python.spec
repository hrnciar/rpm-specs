%global pypi_name gateway_addon
%global addon_name gateway-addon-python

%{?python_enable_dependency_generator}

Name:           mozilla-iot-gateway-addon-python
Summary:        Python bindings for Mozilla IoT Gateway
Version:        0.9.0
Release:        3%{?dist}
License:        MPLv2.0
URL:            https://github.com/mozilla-iot/gateway-addon-python
Source0:        https://github.com/mozilla-iot/%{addon_name}/archive/v%{version}.tar.gz
Requires:       python3-pip
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-jsonschema
BuildRequires:  python3-nnpy
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{pypi_name}}

%description
Python bindings for Python add-ons for Mozilla IoT Gateway.


%prep
%autosetup -n %{addon_name}-%{version}


%build
%py3_build


%install
%py3_install


%files
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Troy Dawson <tdawson@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Troy Dawson <tdawson@redhat.com> - 0.8.0-2
- Requires python3-pip for python addons to work

* Thu Apr 25 2019 Troy Dawson <tdawson@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Wed Feb 20 2019 Troy Dawson <tdawson@redhat.com> - 0.4.0-1
- Initial package
