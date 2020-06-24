%global sname   pymod2pkg

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:             python-pymod2pkg
Version:          0.17.1
Release:          6%{?dist}
Summary:          python module name to package name map
License:          ASL 2.0
URL:              https://github.com/openstack/pymod2pkg.git
Source0:          https://pypi.io/packages/source/p/pymod2pkg/pymod2pkg-%{version}.tar.gz
BuildArch:        noarch


%description
pymod2pkg provides simple python function to translate python module names to
their corresponding distro package names.

%if %{with python2}
%package -n python2-%{sname}
Summary:          python module name to package name map
Requires:         python2-pbr
BuildRequires:    python2-setuptools
BuildRequires:    python2-devel
BuildRequires:    python2-pbr
BuildRequires:    python2-stestr
BuildRequires:    python2-testresources
BuildRequires:    python2-testtools
%{?python_provide:%python_provide python2-%{sname}}

%description -n python2-%{sname}
pymod2pkg provides simple python function to translate python module names to
their corresponding distro package names.
%endif

%if %{with python3}
%package -n python3-%{sname}
Summary:          python module name to package name map
Requires:         python3-pbr
BuildRequires:    python3-setuptools
BuildRequires:    python3-devel
BuildRequires:    python3-pbr
BuildRequires:    python3-stestr
BuildRequires:    python3-testresources
BuildRequires:    python3-testtools
%{?python_provide:%python_provide python3-%{sname}}

%description -n python3-%{sname}
pymod2pkg provides simple python function to translate python module names to
their corresponding distro package names.

This is a Python3 version.
%endif

%prep
%setup -q -n pymod2pkg-%{version}


%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%check
%if %{with python3}
PYTHON=python3 stestr-3 run
rm -rf .testrepository
%endif
%if %{with python2}
PYTHON=python2 stestr run
%endif

%install
%if %{with python2}
%py2_install
mv %{buildroot}%{_bindir}/%{sname} %{buildroot}%{_bindir}/%{sname}-%{python2_version}
ln -s ./%{sname}-%{python2_version} %{buildroot}%{_bindir}/%{sname}-2
ln -s ./%{sname}-%{python2_version} %{buildroot}%{_bindir}/%{sname}
%endif

%if %{with python3}
%py3_install
mv %{buildroot}%{_bindir}/%{sname} %{buildroot}%{_bindir}/%{sname}-%{python3_version}
ln -s ./%{sname}-%{python3_version} %{buildroot}%{_bindir}/%{sname}-3
ln -s ./%{sname}-%{python3_version} %{buildroot}%{_bindir}/%{sname}
%endif

%if %{with python2}
%files -n python2-%{sname}
%doc README.rst AUTHORS
%license LICENSE
%{_bindir}/%{sname}
%{_bindir}/%{sname}-2*
%{python2_sitelib}/%{sname}
%{python2_sitelib}/pymod2pkg-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-%{sname}
%doc README.rst AUTHORS
%license LICENSE
%{_bindir}/%{sname}
%{_bindir}/%{sname}-3*
%{python3_sitelib}/%{sname}
%{python3_sitelib}/pymod2pkg-%{version}-py?.?.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Javier Peña <jpena@redhat.com> - 0.17.1-1
- Update to upstream 0.17.1
- Removed python2 subpackage from Fedora

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Javier Peña <jpena@redhat.com> - 0.14.0-1
- Updated to upstream 0.14.0
- Fixed Rawhide build (bz#1605857)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.11.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Jakub Ružička <jruzicka@redhat.com> 0.11.0-1
- Updated to upstream release 0.11.0

* Tue Sep 19 2017 Javier Peña <jpena@redhat.com> 0.10.1-1
- Updated to upstream release 0.10.1
- Enable unit tests

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Jakub Ruzicka <jruzicka@redhat.com> 0.6.1-4
- Add runtime dependency on pbr

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-2
- Rebuild for Python 3.6

* Fri Dec  2 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.6.1-1
- Upstream 0.6.1

* Fri Jul 29 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.5.2-1
- Upstream 0.5.2
- Add pymod2pkg utility
- Add python3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.2.1-1
- Update to 0.2.1

* Wed Aug 05 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.2-2
- Use python versioned macros
- List files instead of using wildcard

* Thu Jul 23 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.2-1
- Update to 0.2

* Fri Jul 17 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.1-1
- Initial version
