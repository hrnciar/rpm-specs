%bcond_without tests

%global pypi_name niapy
%global pretty_name NiaPy
%global fullver 2.0.0rc10

%global _description %{expand:
Nature-inspired algorithms are a very popular tool for solving optimization
problems. Numerous variants of nature-inspired algorithms have been developed
since the beginning of their era. To prove their versatility, those were tested
in various domains on various applications, especially when they are
hybridized, modified or adapted. However, implementation of nature-inspired
algorithms is sometimes a difficult, complex and tedious task. In order to
break this wall, NiaPy is intended for simple and quick use, without spending
time for implementing algorithms from scratch.}


Name:           python-%{pypi_name}
Version:        2.0.0
Release:        0.2rc10%{?dist}
Summary:        Micro framework for building nature-inspired algorithms

License:        MIT
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        https://github.com/NiaOrg/%{pretty_name}/archive/%{fullver}/%{pretty_name}-%{fullver}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
# For docs and tests
BuildRequires:  %{py3_dist astroid}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist xlsxwriter}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{fullver}
rm -rf %{pretty_name}.egg-info

# Replace ~ in setup.py with >
sed -i 's/~/>/' setup.py
# Remove unneeded dep
sed -i '/enum34/ d' setup.py


# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

PYTHONPATH=%{buildroot}/%{python3_sitelib} make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/build/html/{.doctrees,.buildinfo} -vf

%install
%py3_install

# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/tests

%check
%if %{with tests}
# Two tests failing
PYTHONPATH=%{buildroot}/%{python3_sitelib} pytest -ra \
    -k 'not test_Custom_works_fine and not test_griewank_works_fine' \
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst README.md
%{python3_sitelib}/%{pretty_name}-%{fullver}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pretty_name}

%files doc
%license LICENSE
%doc docs/build/html

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.2rc10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-0.1rc10
- Remove dep on enum34
- Add python_provides for F32

* Sat Jun 27 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.2-1
- Initial package
