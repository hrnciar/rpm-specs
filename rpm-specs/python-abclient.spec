%global pypi_name abclient

%global common_desc \
Abclient is a python library for EISOO AnyBackup APIs. It is a client \
library for EISOO AnyBackup APIs. It allows openstack karbor to \
create backups for databases and file systems.


Name:		python-%{pypi_name}
Version:	0.2.3
Release:	14%{?dist}
Summary:	Python client library for EISOO AnyBackup API

License:	ASL 2.0
URL:		https://pypi.python.org/pypi/abclient
Source0:	https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch

%description
%{common_desc}

%package -n	python3-%{pypi_name}
Summary:	Python client library for EISOO AnyBackup API
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

Requires:	python3-requests
Requires:	python3-oslo-utils
Requires:	python3-oslo-log 

%description -n python3-%{pypi_name}
%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove requirements.txt
rm -f requirements.txt

%build

%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.3-8
- Subpackage python2-abclient has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-6
- Rebuilt for Python 3.7

* Thu Mar 08 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.3-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Chandan Kumar <chkumar246@gmail.com> - 0.2.3-2
- Fixed Python3 subpackage requires.
- Fixed Package URL

* Fri Jul 14 2017 Chandan Kumar <chkumar246@gmail.com> - 0.2.3-1
- Initial package.
