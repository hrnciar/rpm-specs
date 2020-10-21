%global pypi_name entry_point_inspector
%global sname epi

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-%{sname}
Version:        0.1.1
Release:        7%{?dist}
Summary:        Tool for looking at the entry point plugins on a system

License:        ASL 2.0
URL:            https://github.com/dhellmann/entry_point_inspector
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Entry Point Inspector is a tool for looking at the entry point plugins
installed on a system.

%if %{with python2}
%package -n     python2-%{sname}
Summary:        Tool for looking at the entry point plugins on a system
%{?python_provide:%python_provide python2-%{sname}}

Requires:       python2-cliff
Requires:       python2-setuptools

BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
# test requirements
BuildRequires:  python2-mock
BuildRequires:  python2-nose
BuildRequires:  python2-coverage
BuildRequires:  python2-cliff

%description -n python2-%{sname}
Entry Point Inspector is a tool for looking at the entry point plugins
installed on a system.
%endif

%if %{with python3}
%package -n     python3-%{sname}
Summary:        Tool for looking at the entry point plugins on a system
%{?python_provide:%python_provide python3-%{sname}}

Requires:       python3-cliff
Requires:       python3-setuptools

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
# test requirements
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-coverage
BuildRequires:  python3-cliff

%description -n python3-%{sname}
Entry Point Inspector is a tool for looking at the entry point plugins
installed on a system.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif

%check
%if %{with python2}
%{__python2} setup.py nosetests
%endif

%if %{with python3}
%{__python3} setup.py nosetests
%endif

%if %{with python2}
%files -n python2-%{sname}
%license LICENSE
%doc README.rst announce.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{_bindir}/%{sname}
%endif


%if %{with python3}
%files -n python3-%{sname}
%license LICENSE
%doc README.rst announce.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_bindir}/%{sname}
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Alan Pevec <alan.pevec@redhat.com> 0.1.1-1
- Update to 0.1.1
- Drop python2 in Fedora

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-10
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-5
- Rebuild for Python 3.6

* Thu Oct 20 2016 Chandan Kumar <chkumar246@gmail.com> - 0.1-4
- Fixed package name

* Wed Sep 28 2016 Chandan Kumar <chkumar246@gmail.com> - 0.1-3
- Fixed source macro in prep section

* Wed Sep 28 2016 Chandan Kumar <chkumar246@gmail.com> - 0.1-2
- Added sources for LICENSE, README.rst and announce.rst
- Included check macro to run unit tests

* Tue Sep 27 2016 Chandan Kumar <chkumar246@gmail.com> - 0.1-1
- Initial package.
