%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

%global pypi_name textfsm

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        11%{?dist}
Summary:        Python module for parsing semi-structured text into python tables

License:        ASL 2.0
URL:            https://github.com/google/textfsm
Source0:        https://github.com/google/textfsm/archive/%{version}/textfsm-%{version}.tar.gz
# https://github.com/google/textfsm/issues/26
Source1:        COPYING
BuildArch:      noarch

%description
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
Requires:       python2-six

%description -n python2-%{pypi_name}
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.
%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
Requires:       python3-six

%description -n python3-%{pypi_name}
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# License is missing from the tarball, see https://github.com/google/textfsm/issues/26
cp %{SOURCE1} .

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python3}
%py3_install
%endif
%if %{with python2}
%py2_install
%endif

%check
# Unit tests are currently missing from the tarball,
# see https://github.com/google/textfsm/issues/50
# %if %{with python2}
# %{__python2} setup.py test
# %endif
# %if %{with python3}
# %{__python3} setup.py test
# %endif

%if %{with python2}
%files -n python2-%{pypi_name}
%license COPYING
%{python2_sitelib}/copyable_regex_object.py*
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/terminal.py*
%{python2_sitelib}/clitable.py*
%{python2_sitelib}/texttable.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%license COPYING
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/copyable_regex_object.py
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/terminal.py
%{python3_sitelib}/clitable.py
%{python3_sitelib}/texttable.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Javier Peña <jpena@redhat.com> - 0.3.2-6
- Switch sources to use GitHub release
- Disable unit tests until they are present in the tarball

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Javier Peña <jpena@redhat.com> - 0.3.2-4
- Removed Python 2 package from Fedora 30+ (bz#1634614)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-2
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Javier Peña <jpena@redhat.com> - 0.3.2-1
- Initial package.
