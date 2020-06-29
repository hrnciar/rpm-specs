%global pypi_name ryu

# Use Python 2 on EL7, Python 3 otherwise
%if 0%{?rhel} == 7
BuildRequires:   python2-devel
%global python   python2
%{?__python2:%global __python %__python2}
%else
BuildRequires:   python3-devel
%global python   python3
%global __python %__python3
%endif

# Enable tests by default
%bcond_without check

Name:           python-%{pypi_name}
Version:        4.29
Release:        10%{?dist}
Summary:        Component-based Software-defined Networking Framework

License:        Apache-2.0
Url:            https://osrg.github.io/ryu
Source:         https://pypi.io/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Ryu provides software components with well defined API that make it easy for developers to create new
network management and control applications.

%package -n     %{python}-%{pypi_name}
Summary:        Component-based Software-defined Networking Framework
%{?python_provide:%python_provide %{python}-%{pypi_name}}

# Remove in Fedora 33:
Provides:  python-%{pypi_name}-common = %{version}-%{release}
Obsoletes: python-%{pypi_name}-common < 4.29-2

Requires:  %{python}-eventlet
Requires:  %{python}-debtcollector
Requires:  %{python}-lxml
Requires:  %{python}-msgpack
Requires:  %{python}-netaddr
Requires:  %{python}-openvswitch
Requires:  %{python}-oslo-config
Requires:  %{python}-paramiko
Requires:  %{python}-routes
Requires:  %{python}-six
Requires:  %{python}-tinyrpc
Requires:  %{python}-webob

BuildRequires:  %{python}-devel
BuildRequires:  %{python}-debtcollector
BuildRequires:  %{python}-eventlet
BuildRequires:  %{python}-greenlet
BuildRequires:  %{python}-lxml
BuildRequires:  %{python}-msgpack
BuildRequires:  %{python}-openvswitch
BuildRequires:  %{python}-oslo-config
BuildRequires:  %{python}-paramiko
BuildRequires:  %{python}-repoze-lru
BuildRequires:  %{python}-routes
BuildRequires:  %{python}-sphinx
BuildRequires:  %{python}-tinyrpc
BuildRequires:  %{python}-setuptools
BuildRequires:  %{python}-webob

%if %{with check}
BuildRequires:  %{python}-dns
BuildRequires:  %{python}-pylint
BuildRequires:  %{python}-coverage
BuildRequires:  %{python}-formencode
BuildRequires:  %{python}-nose
BuildRequires:  %{python}-mock
BuildRequires:  %{python}-monotonic
BuildRequires:  %{python}-tinyrpc
%endif

%description -n %{python}-%{pypi_name}
Ryu provides software components with well defined API that make it easy for developers to create new
network management and control applications.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# drop deps in egginfo, let rpm handle them
rm tools/*-requires
rm tools/install_venv.py
# Remove non-working tests (internet connection needed)
rm -vf %{pypi_name}/tests/unit/test_requirements.py
# Remove pip usage (used only in test_requirements.py)
sed -i '/^from pip/d' ryu/utils.py


%build
%py_build

%if "%{python}" == "python3"
cd doc && make SPHINXBUILD=sphinx-build-3 man
%else
cd doc && make man
%endif


%install
%py_install

install -d -m 755 %{buildroot}%{_sysconfdir}/%{pypi_name}
mv %{buildroot}%{_prefix}%{_sysconfdir}/%{pypi_name}/%{pypi_name}.conf %{buildroot}%{_sysconfdir}/%{pypi_name}/%{pypi_name}.conf

%if %{with check}
%check
# Tests without virtualenv (N) and without PEP8 tests (P)
PYTHON=%{__python} ./run_tests.sh -N -P
%endif

%files -n     %{python}-%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python_sitelib}/%{pypi_name}
%{_bindir}/%{pypi_name}
%{_bindir}/%{pypi_name}-manager
%{_sysconfdir}/%{pypi_name}/%{pypi_name}.conf


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.29-10
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 4.29-9
- Fix string quoting for rpm >= 4.16

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Alfredo Moralejo <amoralej@redhat.com> - 4.29-7
- Removed pep8 as BR

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.29-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.29-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Miro Hrončok <mhroncok@redhat.com> - 4.29-2
- Remove python2 subpackage on Fedora (#1638709)

* Sun Sep 30 2018 Slawek Kaplonski <skaplons@redhat.com> 4.29-1
- Update to 4.29

* Thu Aug 16 2018 Slawek Kaplonski <skaplons@redhat.com> 4.27-2
- Stop removing integration tests code before build, it requires docker to
  run properly but it shouldn't be run if docker is not available on build
  machine

* Tue Aug 07 2018 Slawek Kaplonski <skaplons@redhat.com> 4.27-1
- Update to 4.27

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Alan Pevec <alan.pevec@redhat.com> 4.25-1
- Update to 4.25

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.15-4
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.15-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Alan Pevec <alan.pevec@redhat.com> 4.15-1
- Update to 4.15

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Lumír Balhar <lbalhar@redhat.com> - 4.13-2
- Tests enabled

* Mon May 29 2017 Alan Pevec <alan.pevec@redhat.com> 4.13-1
- Update to 4.13
- Add missing dependencies

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.3-5
- Rebuild for Python 3.6

* Wed Sep 07 2016 Arie Bregman <abregman@redhat.com> - 4.3-4
- Moved tests related lines to depend on with_check

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 01 2016 Matthias Runge <mrunge@redhat.com> - 4.3-2
- add python_provides for python2 package

* Thu Jun 23 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 4.3-1
- Upstream 4.3
- Enable python3 subpackage

* Thu Apr  7 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 3.30-1
- Upstream 3.30

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 22 2015 Arie Bregman <abregman@redhat.com> - 3.26-1
- Initial package.
