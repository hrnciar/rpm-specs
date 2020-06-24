%global pypi_name pipsi

# test suite is disabled by default for koji builds,
# because tests require internet connection

# Conditial build macro
# http://www.rpm.org/wiki/PackagerDocs/ConditionalBuilds
%bcond_with tests

Name:           %{pypi_name}
Version:        0.9
Release:        16%{?dist}
Summary:        Wraps pip and virtualenv to install scripts

License:        BSD
URL:            http://github.com/mitsuhiko/pipsi/
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:	python3-click
BuildRequires:	python3-virtualenv

%if %{with tests}
# Required for tests
BuildRequires:	python3-pytest
BuildRequires:	openssl-devel
BuildRequires:	libacl-devel
%endif

Requires:       python3-click
Requires:       python3-setuptools
Requires:       python3-virtualenv	

%description
Pipsi is a wrapper around virtualenv and pip which installs scripts provided
by python packages into separate virtualenvs to shield them from your system
and each other.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Point to namespaced Python 3 version of virtualenv executable if available
for cand in virtualenv-3 py3-virtualenv; do
    if [ -e "%{_bindir}/$cand" ]; then
        sed -i "233 s/virtualenv/$cand/" %{pypi_name}.py
        sed -i "70 s/virtualenv/$cand/" get-%{pypi_name}.py
        break
    fi
done


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
# Tests need UTF-8 encoding
export LC_CTYPE="C.UTF-8"
# Invoke tests and disable the test that checks if pipsi is already installed
%{__python3} -m pytest -k "not test_find_scripts" -vv
%endif


%files
%doc README.rst
%license LICENSE
%{_bindir}/pipsi
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Nils Philippsen <nils@redhat.com> - 0.9-10
- only point to namespaced Python 3 version of virtualenv if it's available
  (#1638088)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.9-2
- Disable test suite for koji builds.

* Thu Apr 07 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.9-1
- Initial package.
