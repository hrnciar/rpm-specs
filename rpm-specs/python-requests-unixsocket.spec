%global pypi_name requests-unixsocket

Name:           python-%{pypi_name}
Version:        0.1.5
Release:        7%{?dist}
Summary:        Use requests to talk HTTP via a UNIX domain socket

License:        ASL 2.0
URL:            https://github.com/msabramo/requests-unixsocket
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        Use requests to talk HTTP via a UNIX domain socket
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(requests)

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(urllib3)
BuildRequires:  python3dist(waitress)

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove shebangs
sed -i '1d' requests_unixsocket/tests/test_requests_unixsocket.py
sed -i '1d' setup.py

# Remove pytest-pep8 invocation. Not packaged in Fedora
rm pytest.ini
sed -i '/pytest-pep8/d' test-requirements.txt
# pytest-capturelog isn't actually used, removing it. it's not in Fedora either
sed -i '/pytest-capturelog/d' test-requirements.txt

%build
%py3_build

%install
%py3_install


%check
%{__python3} -m pytest -v

%files -n python3-%{pypi_name} 
%doc README.rst
%license LICENSE
%{python3_sitelib}/requests_unixsocket
%{python3_sitelib}/requests_unixsocket-%{version}-py%{python3_version}.egg-info

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 2 2019 Dan Radez <dradez@redhat.com> - 0.1.5-2
- Updates to initial package to address review comments
* Tue Mar  8 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.5-1
- Initial package.
