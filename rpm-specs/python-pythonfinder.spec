%global pypi_name pythonfinder
%global _descripion %{expand:
Library that returns all Python interpreter files paths,
capable of following links.}
Name:           python-%{pypi_name}
Version:        1.2.1
Release:        5%{?dist}
Summary:        Python library for finding Python interpreter files
License:        MIT
URL:            https://github.com/sarugaku/pythonfinder
Source0:        https://github.com/sarugaku/pythonfinder/archive/%{version}/pythonfinder-%{version}.tar.gz

# tests tries to make hardlinks from /usr/bin/python, patching this to instead copy
Patch0:         test_python_versions_fix.patch
BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %{_descripion}

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(cached-property)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(crayons)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(vistir)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(twine)
BuildRequires:  python3dist(yaspin)
BuildRequires:  python3dist(virtualenv)
BuildRequires:  tox

BuildRequires:  python3dist(invoke)
BuildRequires:  python3dist(parver)
BuildRequires:  python3dist(towncrier)


Requires:       python3-vistir

%description -n python3-%{pypi_name} %{_descripion}

%prep
%autosetup -n %{pypi_name}-%{version} -p1

#Delete vendor dependency. It is usefull only for Windows.
rm -rf src/pythonfinder/_vendor/pep514tools

# deleting shebang
sed -i '/.!env python/d' ./src/pythonfinder/__main__.py

%build
%py3_build

%install
%py3_install

%check
mkdir .tmp
export TMPDIR=$(pwd)/.tmp

# skiping failing tests
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest -v -k 'not test_shims_are_kept and not test_shims_are_removed'

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}/
%{_bindir}/pyfinder

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.8

* Tue Mar 12 2019 Patrik Kopkan <pkopkan@redhat> - 1.2.1-1
- initial package
