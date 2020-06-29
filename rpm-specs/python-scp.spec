%global srcname scp
%global pypi_name scp

Name:           python-%{srcname}
Version:        0.13.2
Release:        6%{?dist}
Summary:        Scp module for paramiko

License:        LGPLv2+
URL:            https://github.com/jbardin/scp.py
Source0:        https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch


%description
The scp.py module uses a paramiko transport to send and receive files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.

%if 0%{?fedora} < 30
%package -n     python2-%{pypi_name}
Summary:        scp module for paramiko
BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
# For tests
BuildRequires: python2-paramiko
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-paramiko
%description -n python2-%{pypi_name}
The scp.py module uses a paramiko transport to send and receive files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.
%endif

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        scp module for paramiko
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires: python%{python3_pkgversion}-paramiko
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-paramiko
%description -n python%{python3_pkgversion}-%{pypi_name}
The scp.py module uses a paramiko transport to send and receive files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.

%prep
%setup -q -n %{srcname}-%{version}
rm -r %{srcname}.egg-info

%build
%if 0%{?fedora} < 30
%py2_build
%endif
%py3_build

%install
%py3_install
%if 0%{?fedora} < 30
%py2_install
%endif

%check
# Tests fail without open local ssh server
%if 0%{?fedora} < 30
#{__python2} setup.py test
%endif
#{__python3} setup.py test

%if 0%{?fedora} < 30
%files -n python2-%{pypi_name}
%doc README.rst PKG-INFO
%license LICENSE.txt
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst PKG-INFO
%license LICENSE.txt
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  2 2019 Orion Poplawski <orion@cora.nwra.com> - 0.13.2-1
- Update to 0.13.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Orion Poplawski <orion@cora.nwra.com> - 0.11.0-1
- Update to 0.11.0
- Drop Python 2 package for Fedora 30+ (bugz #1631310)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-9
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.2-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-4
- Rebuild for Python 3.6

* Wed Nov 16 2016 Ben Rosser <rosser.bjr@gmail.com> - 0.10.2-3
- Remove ownership of python3_sitelib/__pycache__ from the python3 subpackage.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 03 2016 Ben Rosser <rosser.bjr@gmail.com> - 0.10.2-1
- Updated package to latest upstream version.
- Modernized spec file.
- Added support for Python 3.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Orion Poplawski <orion@cora.nwra.com> - 0.7.1-3
- Add missing BR python-paramiko for tests

* Wed Feb 19 2014 Orion Poplawski <orion@cora.nwra.com> - 0.7.1-2
- Add missing BR python-setuptools
- Other minor cleanup
- Add %%check

* Fri Feb 14 2014 Orion Poplawski <orion@cora.nwra.com> - 0.7.1-1
- Initial package
