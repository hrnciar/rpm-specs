%global pypi_name genty
Name:           python-%{pypi_name}
Version:        1.3.2
Release:        7%{?dist}
Summary:        Allows you to run a test with multiple data sets
License:        ASL 2.0
URL:            https://github.com/box/genty
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)

%description
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of input
Genty makes this a breeze.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(six)

%description -n python3-%{pypi_name}
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of input
Genty makes this a breeze.


%prep
%autosetup -n %{pypi_name}-%{version}

# Use mock from standard library:
sed -i 's/from mock/from unittest.mock/' test/test_genty.py


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-1
- Initial package
