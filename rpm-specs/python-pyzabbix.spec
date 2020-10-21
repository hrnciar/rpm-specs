%global srcname pyzabbix
%global commit aed72dfe30cd5f8262013af73356a76924cbeb83

Name:           python-pyzabbix
Version:        0.7.4
Release:        11%{?dist}
Summary:        PyZabbix is a Python module for working with the Zabbix API

# license is in README.markdown
License:        LGPLv2+
URL:            https://github.com/lukecyca/pyzabbix
Source0:        https://github.com/lukecyca/pyzabbix/archive/%{commit}/%{srcname}-%{commit}.tar.gz#/%{srcname}-%{commit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-httpretty
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose


%description
%{summary}.


%package -n python3-%{srcname}
Summary:        PyZabbix is a Python module for working with the Zabbix API
License:        LGPLv2
Requires:       python3-requests
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -n %{srcname}-%{commit}
sed -i 's/"httpretty<0.8.7",/"httpretty",/' setup.py


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py nosetests


%files -n python3-%{srcname}
%doc README.markdown examples/
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Piotr Popieluch <piotr1212@gmail.com> - 0.7.4-4
- Remove Python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-2
- Rebuilt for Python 3.7

* Tue Feb 13 2018 Piotr Popieluch <piotr1212@gmail.com> - 0.7.4-1
- Update to 0.7.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Piotr Popieluch <piotr1212@gmail.com> - 0.7.3-9
- Update to new package guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.7.3-3
- Rebuilt for Python 3.5

* Tue Aug 25 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.7.3-2
- Enable tests for epel

* Fri Jul 03 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 19 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.7.2-2
- Explicitly name BuildRequires: python-setuptools
- Disabled tests for EPEL

* Thu Feb 12 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.7.2-1
- Initial package
