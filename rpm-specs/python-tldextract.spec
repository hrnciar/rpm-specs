%global pypi_name tldextract

%global py3_prefix python%{python3_pkgversion}

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{pypi_name}
Version:        2.2.2
Release:        3%{?dist}
Summary:        Accurately separate the TLD from the registered domain and subdomains of a URL

License:        BSD
URL:            https://pypi.python.org/pypi/tldextract
Source0:        %{pypi_source}
# pytest-pylint is not packaged in Fedora
Patch0:         %{pypi_name}-remove-pytest-modules.patch
BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-mock
BuildRequires:  python2-pytest
BuildRequires:  python2-requests >= 2.1.0
BuildRequires:  python2-requests-file >= 1.4
BuildRequires:  python2-responses
BuildRequires:  python2-setuptools
%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has unversioned names for these packages
BuildRequires:  python-idna
%else
BuildRequires:  python2-idna
BuildRequires:  python2-requests
%endif
%endif

BuildRequires:  %{py3_prefix}-devel
BuildRequires:  %{py3_prefix}-idna
BuildRequires:  %{py3_prefix}-pytest
BuildRequires:  %{py3_prefix}-requests >= 2.1.0
BuildRequires:  %{py3_prefix}-requests-file >= 1.4
BuildRequires:  %{py3_prefix}-responses
BuildRequires:  %{py3_prefix}-setuptools

%description
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-requests >= 2.1.0
Requires:       python2-requests-file >= 1.4
Requires:       python2-setuptools
%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has unversioned names for these packages
Requires:       python-idna
%else
Requires:       python2-idna
%endif

%description -n python2-%{pypi_name}
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

This is the Python 2 version of the package.
%endif

%package -n     %{py3_prefix}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       %{py3_prefix}-idna
Requires:       %{py3_prefix}-requests >= 2.1.0
Requires:       %{py3_prefix}-requests-file >= 1.4
Requires:       %{py3_prefix}-setuptools

%description -n %{py3_prefix}-%{pypi_name}
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

This is the Python 3 version of the package.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif
%py3_build

%install
%if %{with python2}
%py2_install
%endif
%py3_install

%check
# test_log_snapshot_diff is an integration test and requires network access
# (additionally that test requires python3-pytest-mock which is not available
# in EPEL 7)
TEST_SELECTOR="not test_log_snapshot_diff"

%if %{with python2}
py.test -x -vk "$TEST_SELECTOR" tests
%endif
py.test-3 -x -vk "$TEST_SELECTOR" tests

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.md
%{python2_sitelib}/tldextract
%{python2_sitelib}/tldextract-%{version}-py?.?.egg-info
%endif

%files -n %{py3_prefix}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/tldextract
%{python3_sitelib}/tldextract-%{version}-py?.?.egg-info
%{_bindir}/tldextract

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-3
- Rebuilt for Python 3.9

* Sun May 17 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.2.2-2
- enable Python 3 tests for EPEL 7

* Tue Apr 28 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.2.2-1
- update to 2.2.2
- run tests in %%check
- add Python 3 subpackage in EPEL 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Eli Young <elyscape@gmail.com> - 2.2.1-5
- Support EPEL8 builds

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 Eli Young <elyscape@gmail.com> - 2.2.1-1
- Update to 2.2.1 (#1685688)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Eli Young <elyscape@gmail.com> - 2.2.0-5
- Remove Python 2 package in Fedora 30+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 2.2.0-2
- Add python2- prefix where possible

* Thu Feb 15 2018 Eli Young <elyscape@gmail.com> - 2.2.0-1
- Initial package (#1545951)
