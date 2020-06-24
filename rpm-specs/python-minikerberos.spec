%global pypi_name minikerberos

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Kerberos manipulation library in Python

License:        MIT
URL:            https://github.com/skelsec/minikerberos
Source0:        %pypi_source
BuildArch:      noarch

%description
Kerberos manipulation library in pure Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Kerberos manipulation library in pure Python

%package -n %{pypi_name}
Summary:        %{summary}
Requires:       python3-%{pypi_name}

%description -n %{pypi_name}
Command line tools for Kerberos manipulations.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebangs. https://github.com/skelsec/minikerberos/issues/7
sed -i -e '/^#!\//, 1d' %{pypi_name}/{*.py,*/*.py,*/*/*.py}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info

%files -n %{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Mon Jun 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Update to new upstream version 0.2.2 (rhbz#1846178)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Update to new upstream version 0.2.1 (rhbz#1808881)

* Mon Mar 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Update to new upstream version 0.2.0 (rhbz#1808881)

* Sun Feb 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Update to new upstream version 0.1.0

* Sat Feb 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.12-1
- Update to new upstream version 0.0.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.11-1
- Update to new upstream version 0.0.11

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.10-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.10-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-2
- Remove binary (rhbz#1722597)

* Thu Jun 20 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-1
- Update to latest upstream release 0.0.10

* Sat Jun 15 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.7-1
- Initial package for Fedora
