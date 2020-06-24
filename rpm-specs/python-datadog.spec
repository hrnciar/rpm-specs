# Enable Python dependency generation
%{?python_enable_dependency_generator}

%if 0%{?fedora} >= 28
%global python2_pkgversion 2
%else
%global python2_pkgversion %{nil}
%endif

%{!?python3_pkgversion: %global python3_pkgversion 3}

%if 0%{?rhel} && 0%{?rhel} < 8
%bcond_without python2
%else
%bcond_with python2
%endif

Name:           python-datadog
Version:        0.23.0
Release:        8%{?dist}
Summary:        Python wrapper for the Datadog API
License:        BSD

URL:            https://github.com/DataDog/datadogpy
Source0:        %{url}/archive/v%{version}/datadogpy-%{version}.tar.gz
# https://github.com/DataDog/datadogpy/pull/305
Patch0001:      0001-setup.py-Rename-script-names-from-dog-to-dogshell.patch

%if %{with python2}
BuildRequires:  python%{python2_pkgversion}-setuptools
BuildRequires:  python%{python2_pkgversion}-devel
%endif

BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel

BuildArch:      noarch

%description
Datadogpy is a collection of tools suitable for inclusion in existing Python
projects or for development of standalone scripts. It provides an abstraction on
top of Datadog's raw HTTP interface and the Agent's StatsD metrics aggregation
server, to interact with Datadog and efficiently report events and metrics.



%if %{with python2}
%package -n python2-datadog
Summary:        Python wrapper for the Datadog API
%if %{undefined python_enable_dependency_generator}
Requires:       python%{python2_pkgversion}-decorator >= 3.3.2
Requires:       python%{python2_pkgversion}-requests >= 2.6.0
Requires:       python%{python2_pkgversion}-simplejson >= 2.0.9
%endif

%{?python_provide:%python_provide python2-datadog}

%description -n python2-datadog
Datadogpy is a collection of tools suitable for inclusion in existing Python
projects or for development of standalone scripts. It provides an abstraction on
top of Datadog's raw HTTP interface and the Agent's StatsD metrics aggregation
server, to interact with Datadog and efficiently report events and metrics.
%endif



%package -n python%{python3_pkgversion}-datadog
Summary:        Python wrapper for the Datadog API
%if %{undefined python_enable_dependency_generator}
Requires:       python%{python3_pkgversion}-decorator >= 3.3.2
Requires:       python%{python3_pkgversion}-requests >= 2.6.0
Requires:       python%{python3_pkgversion}-simplejson >= 3.0.0
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-datadog}

%description -n python%{python3_pkgversion}-datadog
Datadogpy is a collection of tools suitable for inclusion in existing Python
projects or for development of standalone scripts. It provides an abstraction on
top of Datadog's raw HTTP interface and the Agent's StatsD metrics aggregation
server, to interact with Datadog and efficiently report events and metrics.

%prep
%autosetup -n datadogpy-%{version} -p1

%build
%if %{with python2}
%py2_build
%endif

%py3_build

%install
%if %{with python2}
%py2_install
# Not used/incompatible with python2, will automatically use alternative method
rm %{buildroot}/%{python2_sitelib}/datadog/dogstatsd/context_async.py*
%endif

%py3_install
%if 0%{?rhel} == 7 && 0%{?python3_pkgversion} < 35
# EPEL provides Python 3.4 which doesn't have async support
rm %{buildroot}/%{python3_sitelib}/datadog/dogstatsd/context_async.py*
%endif

%if %{with python2}
%files -n python2-datadog
%license LICENSE
%{python2_sitelib}/datadog*
%endif

%files -n python%{python3_pkgversion}-datadog
%license LICENSE
%{python3_sitelib}/datadog*
%{_bindir}/dogshell
%{_bindir}/dogshellwrap

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Dalton Miner <daltonminer@gmail.com> - 0.23.0-2
- Added a patch to rename binaries that conflicted with sheepdog
* Thu Oct 25 2018 Dalton Miner <daltonminer@gmail.com> - 0.23.0-1
- Initial packaging
