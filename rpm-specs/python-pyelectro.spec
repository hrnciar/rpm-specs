%bcond_without tests

%global pypi_name pyelectro

%global _description %{expand:
Tool for analysis of electrophysiology in Python.

This package was originally developed by Mike Vella. This has been updated by
Padraig Gleeson and others (and moved to NeuralEnsemble) to continue
development of pyelectro and Neurotune for use in OpenWorm, Open Source Brain
and other projects.}

Name:           python-%{pypi_name}
Version:        0.1.10
Release:        6%{?dist}
Summary:        A library for analysis of electrophysiological data

License:        BSD
URL:            https://github.com/NeuralEnsemble/%{pypi_name}
Source0:        https://github.com/NeuralEnsemble/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel

# For documentation
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist setuptools}

Requires:       %{py3_dist scipy}
Requires:       %{py3_dist numpy}
Requires:       %{py3_dist matplotlib}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

make -C doc SPHINXBUILD=sphinx-build-3 html
rm -rf doc/_build/html/{.doctrees,.buildinfo} -vf

%install
%py3_install

%check
%if %{with tests}
nosetests-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%files doc
%doc doc/_build/html

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.10-5
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.10-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.1.10-1
- Added mock back to the BuildRequires

* Wed Dec 25 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.1.10-1
- Updated to v0.1.10
- Using a pre-defined release instead of a git commit
- Removed matplotlib and mock from BuildRequires

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-20190723git7a64bc7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-20190722git7a64bc7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-20190721git7a64bc7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.9-20190720git7a64bc7
- Initial build
