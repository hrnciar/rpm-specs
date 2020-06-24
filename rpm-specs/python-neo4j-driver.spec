%global srcname neo4j-driver
%global sum The official Neo4j Python driver
# Disable Python 2
%bcond_with python2
# Enable Python 3
%bcond_without python3

Name:           python-%{srcname}
Version:        1.6.2
Release:        8%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif
%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%description
The official Python Neo4j driver that supports Neo4j 3.0 and above

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{sum}
Requires:       python2-neotime
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
The official Python Neo4j driver that supports Neo4j 3.0 and above
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
Requires:       python3-neotime
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
The official Python Neo4j driver that supports Neo4j 3.0 and above
%endif


%prep
%autosetup -n %{srcname}-%{version}
find ./ -name '*.py' -exec sed -i '/^#!\/usr\/bin\/env python$/d' '{}' ';'

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


%if %{with python2}
%files -n python2-%{srcname}
%doc README.rst
%{python2_sitearch}/*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%{python3_sitearch}/*
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 mprahl <mprahl@redhat.com> - 1.6.2-4
- Clean up the specfile to match the Python guidelines

* Tue Jul 23 2019 mprahl <mprahl@redhat.com> - 1.6.2-3
- Stop building Python 2 packages for F31+

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 mprahl <mprahl@redhat.com> - 1.6.2-1
- new version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.7

* Sat Jun 09 2018 mprahl <mprahl@redhat.com> - 1.6.0-2
- Add the dependency on python-neotime
- Drop Python 3 on EPEL7 due to python-neotime dependencies that aren't packaged for Python 3

* Tue May 29 2018 mprahl <mprahl@redhat.com> - 1.6.0-1
- new version

* Mon Apr 02 2018 mprahl <mprahl@redhat.com> - 1.5.3-2
- Fix EPEL build failures

* Thu Mar 29 2018 mprahl <mprahl@redhat.com> - 1.5.3-1
- Initial release
