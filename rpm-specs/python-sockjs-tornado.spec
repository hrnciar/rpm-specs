# Created by pyp2rpm-3.0.2
%global pypi_name sockjs-tornado

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        16%{?dist}
Summary:        SockJS python server implementation on top of Tornado framework

License:        MIT

URL:            http://github.com/mrjoes/sockjs-tornado/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
SockJS-tornado is a Python server side counterpart of SockJS-client
browser library running on top of Tornado framework.

%package -n     python3-%{pypi_name}
Summary:        SockJS python server implementation on top of Tornado framework
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-tornado >= 2.1.1
%description -n python3-%{pypi_name}
SockJS-tornado is a Python server side counterpart of SockJS-client
browser library running on top of Tornado framework.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sockjs
%{python3_sitelib}/sockjs_tornado-%{version}-py?.?.egg-info
%{python3_sitelib}/sockjs_tornado-%{version}-py?.?-nspkg.pth

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-11
- Subpackage python2-sockjs-tornado has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.3-6
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Rebuild for Python 3.6

* Sun Jun 5 2016 Ben Rosser <rosser.bjr@gmail.com> - 1.0.3-2
- Use new PyPI URL format
- Use license macro for LICENSE file rather than putting it under doc.

* Tue May 10 2016 "Ben Rosser <rosser.bjr@gmail.com>" - 1.0.3-1
- Initial package.
