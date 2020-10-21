%global pname GridDataFormats
%bcond_without check

%global desc \
GridDataFormats provides the Python package 'gridData'. It contains a class \
('Grid') to handle data on a regular grid --- basically NumPy n-dimensional \
arrays. It supports reading from and writing to some common formats (such as \
OpenDX).

Name: python-%{pname}
Version: 0.5.0
Release: 4%{?dist}
Summary: Read and write data on regular grids in Python
License: LGPLv3+
URL: https://github.com/orbeckst/GridDataFormats
Source0: https://files.pythonhosted.org/packages/source/G/%{pname}/%{pname}-%{version}.tar.gz
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
Requires: python3-numpy
Recommends: python3-scipy
BuildRequires: python3-devel
BuildRequires: python3-numpy
%if %{with check}
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-scipy
BuildRequires: python3-six
BuildRequires: python3-tempdir
%endif
%{?python_provide:%python_provide python3-%{pname}}

%description -n python3-%{pname}
%{desc}

%prep
%setup -q -n %{pname}-%{version}
# force rebuild of Egg Metadata
rm -r %{pname}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
pytest-3 -v --numprocesses=auto ./gridData/tests
%endif

%files -n python3-%{pname}
%license COPYING.LESSER
%doc AUTHORS README.rst
%{python3_sitelib}/%{pname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/gridData

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Dominik Mierzejewski <dominik@greysector.net> 0.5.0-1
- update to 0.5.0 (#1696989)
- use pythonX_version macros
- upstream switched to pytest for testing
- run tests in parallel

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.0-4
- Subpackage python2-GridDataFormats has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Dominik Mierzejewski <dominik@greysector.net> 0.4.0-1
- update to 0.4.0 (#1535726)
- fix build on 32-bit arches
- drop RHEL5 stuff
- use standard bcond for enabling/disabling tests

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Dominik Mierzejewski <dominik@greysector.net> 0.3.3-1
- update to 0.3.3 (#1336061)
- use current python2 module requirements specification
- drop no longer relevant Obsoletes:

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Dominik Mierzejewski <dominik@greysector.net> 0.3.2-2
- enable tests (python2/3-tempdir is in Fedora now)

* Sat Dec 12 2015 Dominik Mierzejewski <dominik@greysector.net> 0.3.2-1
- update to 0.3.2 (#1289547)
- works without scipy now, so make it a soft dependency
- prepare to enable tests (depends on python2/3-tempdir)

* Wed Dec 09 2015 Dominik Mierzejewski <dominik@greysector.net> 0.3.1-1
- update to 0.3.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 24 2015 Dominik Mierzejewski <dominik@greysector.net> 0.3.0-1
- update to 0.3.0
- add python3 subpackage and update to current Python packaging guidelines

* Fri Jul 10 2015 Dominik Mierzejewski <dominik@greysector.net> 0.2.5-1
- update to 0.2.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 03 2015 Dominik Mierzejewski <dominik@greysector.net> 0.2.4-1
- initial build
