# what it's called on pypi
%global srcname pyxs
# what it's imported as
%global libname pyxs
# name of egg info directory
%global eggname pyxs
# package name fragment
%global pkgname pyxs

%global common_description %{expand:
It's a pure Python XenStore client implementation, which covers all of the
libxs features and adds some nice Pythonic sugar on top.}

%if (%{defined fedora} && 0%{?fedora} < 30) || (%{defined rhel} && 0%{?rhel} < 8)
%bcond_without  python2
%endif

%bcond_without  python3

%bcond_without  tests


Name:           python-%{pkgname}
Version:        0.4.1
Release:        12%{?dist}
Summary:        Pure Python bindings to XenStore
License:        GPLv3
URL:            https://github.com/selectel/pyxs
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         remove-pytest-runner-requirement.patch
BuildArch:      noarch


%description %{common_description}


%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with tests}
# Test use pytest's yield_fixture decorator, which was first added in 2.4.
# https://github.com/pytest-dev/pytest/blob/2.4.0/CHANGELOG#L26-L33
BuildRequires:  python2-pytest >= 2.4
%endif
%{?python_provide:%python_provide python2-%{pkgname}}


%description -n python2-%{pkgname} %{common_description}
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
# Test use pytest's yield_fixture decorator, which was first added in 2.4.
# https://github.com/pytest-dev/pytest/blob/2.4.0/CHANGELOG#L26-L33
BuildRequires:  python%{python3_pkgversion}-pytest >= 2.4
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}
%endif


%prep
%autosetup -n %{srcname}-%{version} -p 1


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}


%if %{with tests}
%check
%{?with_python2:PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} --verbose}
%{?with_python3:PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose}
%endif


%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE
%doc README
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Oct 01 2019 Carl George <carl@george.computer> - 0.4.1-9
- Run tests on el6
- Disable python2 subpackage on el8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Carl George <carl@george.computer> - 0.4.1-5
- Disable python2 subpackage on F30+ rhbz#1630329

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jul 25 2017 Carl George <carl@george.computer> - 0.4.1-1
- Initial package
