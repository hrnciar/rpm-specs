%global pypi_name influxdb

Name:           python-%{pypi_name}
Version:        5.2.0
Release:        8%{?dist}
Summary:        InfluxDB client

License:        MIT
URL:            https://github.com/influxdb/influxdb-python
Source0:        https://pypi.python.org/packages/e1/af/94faea244de2a73b7a0087637660db2d638edaae58f22d3f0d0d219ad8b7/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
InfluxDB Python is a client for interacting with InfluxDB. 

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-requests
Requires:       python3-dateutil
Requires:       python3-pytz
Requires:       python3-six

%description -n python3-%{pypi_name}
InfluxDB Python is a client for interacting with InfluxDB.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-2
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 04 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-1
- Update from upstream - Bug 1595473. 

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.0.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Nov 21 2017 David Hannequin <david.hannequin@gmail.com> - 5.0.0-2
- Update from uptsream.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 David Hannequin <david.hannequin@gmail.com> - 4.1.1-2
- Update from uptsream,
- Change source url.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 David Hannequin <david.hannequin@gmail.com> - 4.0.0-1
- Update from uptsream,
- Improvements in timezone handling,
- Properly quote all identifiers and literals,
- Removed get_list_servers,
- Fixes in tutorial_server_data.py,
- Added more data type examples to tutorial.py.


* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuild for Python 3.6

* Wed Oct 05 2016 David Hannequin <david.hannequin@gmail.com> - 3.0.0-1
- Initial package.
