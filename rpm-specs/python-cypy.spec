# No tests in the package at all
%bcond_with tests

%global pypi_name cypy

%global _description %{expand:
Useful utilities for Python.}

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        4%{?dist}
Summary:        Useful utilities for Python

License:        MIT
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        %pypi_source
# Not included in pypi tar
Source1:        https://raw.githubusercontent.com/cyrus-/%{pypi_name}/master/LICENSE

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
# Not mentioned in setup.py
Requires:       %{py3_dist matplotlib}
Requires:       %{py3_dist numpy}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

cp %{SOURCE1} . -v

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.0-1
- Initial build
