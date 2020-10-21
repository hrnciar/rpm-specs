%global pypi_name sphinx-autodoc-typehints

Name:           python-%{pypi_name}
Version:        1.11.1
Release:        1%{?dist}
Summary:        Type hints support for the Sphinx autodoc extension

License:        MIT
URL:            https://github.com/agronholm/sphinx-autodoc-typehints
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This extension allows you to use Python 3 annotations for documenting
acceptable argument types and return value types of functions.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
#BuildRequires:  python3-pytest

Requires:       python3-sphinx
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This extension allows you to use Python 3 annotations for documenting
acceptable argument types and return value types of functions.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -Rf requirements.txt test-requirements.txt *.egg-info

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

#%check
#export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
#PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/sphinx_autodoc_typehints-%{version}*.egg-info/
%{python3_sitelib}/sphinx_autodoc_typehints.py

%changelog
* Tue Oct 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.11.1-1
- Update to latest upstream release 1.11.1 (#1849421)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.11.0-1
- Update to latest upstream release 1.11.0 (#1849421)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.3-2
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.3-1
- Add tests
- Update to latest upstream release 1.10.3 (#1697057)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-5
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 1.2.3-1
- Initial packaging
