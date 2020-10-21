# Created by pyp2rpm-3.2.2
%global pypi_name network-runner
%global ansible_role network-runner

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        2%{?dist}
Summary:        Abstraction and Python API for Ansible Networking

License:        ASL 2.0
URL:            https://github.com/ansible-network/%{pypi_name}
Source0:        https://github.com/ansible-network/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: ansible >= 2.6
BuildRequires:  python3-devel
BuildRequires:  python3dist(ansible-runner)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)

%description
Network Runner is a set of ansible roles and python library that
abstracts Ansible Networking operations. It interfaces
programatically through ansible-runner.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(ansible-runner)
# Python code cannot work without the ansible roles
Requires:  ansible-role-%{ansible_role} = %{version}-%{release}

%description -n python3-%{pypi_name}
Network Runner is a set of ansible roles and python library that
abstracts Ansible Networking operations. It interfaces
programatically through ansible-runner.

%package -n ansible-role-%{ansible_role}
Summary:   Role for Python Network Runner Library

Requires: ansible >= 2.6
# No cross sub-package dependency.
# Can be installed and used without python package.

%description -n ansible-role-%{ansible_role}
Role for Python Network Runner Library

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
LANG=C.utf-8 %{__python3} -m pytest --ignore=build

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/network_runner
%{python3_sitelib}/network_runner-%{version}-py%{python3_version}.egg-info

%files -n ansible-role-%{ansible_role}
%license LICENSE
%doc %{_sysconfdir}/ansible/roles/%{ansible_role}/README.md
%{_sysconfdir}/ansible/roles/%{ansible_role}/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Dan Radez <dradez@redhat.com> - 0.2.2-1
- update to 0.2.2

* Tue May 26 2020 Yatin Karel <ykarel@redhat.com> - 0.2.1-3
- Fix 0.2.1 sources and cleanup old sources

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.9

* Tue Mar 24 2020 Dan Radez <dradez@redhat.com> - 0.2.1-1
- Updated to 0.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Dan Radez <dradez@redhat.com> - 0.1.7-1
- Updated to 0.1.7

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Dan Radez <dradez@redhat.com> - 0.1.6-1
- Updated to 0.1.6

* Tue Apr 02 2019 Dan Radez <dradez@redhat.com> - 0.1.5-1
- Updated to 0.1.5
- added %check

* Wed Mar 20 2019 Dan Radez <dradez@redhat.com> - 0.1.1-1
- Initial package.
