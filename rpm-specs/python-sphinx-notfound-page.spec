%global pypi_name sphinx-notfound-page
%global srcname sphinx_notfound_page
%global importname notfound
%global project_owner readthedocs
%global github_name sphinx-notfound-page
%global desc Create a custom 404 page with absolute URLs hardcoded

%if 0%{?fedora} > 30 || 0%{?rhel} > 7
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{pypi_name}
Version:        0.4
Release:        8%{?dist}
Summary:        Create a custom 404 page with absolute URLs hardcoded

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{version}.tar.gz

# Fix test failures with Sphinx 3
# Resolved upstream: https://github.com/readthedocs/sphinx-notfound-page/pull/88
Patch0: fix-sphinx3-tests.patch

BuildArch:      noarch

%description
%desc

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
BuildRequires:  python2-pytest
Requires:       python2-setuptools
Requires:       python2-sphinx
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%desc
%endif

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python3-pytest
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-sphinx
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%desc


%prep
%autosetup -n %{pypi_name}-%{version} -p1

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
%if %{with python2}
PYTHONPATH="$(pwd)" py.test-%{python2_version} -v .
%endif
PYTHONPATH="$(pwd)" py.test-%{python3_version} -v .

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst CHANGELOG.rst docs
%{python2_sitelib}/%{srcname}-%{version}*-py%{python2_version}.egg-info/
%{python2_sitelib}/%{importname}/
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst CHANGELOG.rst docs
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitelib}/%{importname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-8
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.4-7
- Fix test failures with Sphinx 3 (rhbz#1823521)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Kevin Fenzi <kevin@scrye.com> - 0.4-2
- Use bcond for python2 support.

* Wed Jul 03 2019 Kevin Fenzi <kevin@scrye.com> - 0.4-1
- Initial version for Fedora.
