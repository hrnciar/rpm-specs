%global srcname neomodel
%global sum A Python OGM for Neo4j
%global desc A Python Object Graph Mapper (OGM) for the Neo4j graph database
# Disable Python 2
%bcond_with python2
# Enable Python 3
%bcond_without python3

Name:           python-%{srcname}
Version:        3.3.1
Release:        7%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif
%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif


%description
%{desc}

%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python3-neo4j-driver
Requires:       python3-pytz

%description -n python%{python3_pkgversion}-%{srcname}
%{desc}
%endif


%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
Requires:       python2-neo4j-driver
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       python2-pytz
%else
Requires:       pytz
%endif

%description -n python2-%{srcname}
%{desc}
%endif


%prep
%autosetup -n %{srcname}-%{version}


%build
%if %{with python3}
%py3_build
%endif

%if %{with python2}
%py2_build
%endif


%install
%if %{with python3}
%py3_install

%if !%{with python2}
ln -s %{_bindir}/neomodel_install_labels %{buildroot}/%{_bindir}/neomodel_install_labels-3
ln -s %{_bindir}/neomodel_install_labels %{buildroot}/%{_bindir}/neomodel_install_labels-%{python3_version}
ln -s %{_bindir}/neomodel_remove_labels %{buildroot}/%{_bindir}/neomodel_remove_labels-3
ln -s %{_bindir}/neomodel_remove_labels %{buildroot}/%{_bindir}/neomodel_remove_labels-%{python3_version}
%else
mv %{buildroot}/%{_bindir}/neomodel_install_labels %{buildroot}/%{_bindir}/neomodel_install_labels-3
ln -s %{_bindir}/neomodel_install_labels-3 %{buildroot}/%{_bindir}/neomodel_install_labels-%{python3_version}
mv %{buildroot}/%{_bindir}/neomodel_remove_labels %{buildroot}/%{_bindir}/neomodel_remove_labels-3
ln -s %{_bindir}/neomodel_remove_labels-3 %{buildroot}/%{_bindir}/neomodel_remove_labels-%{python3_version}
%endif

%endif


%if %{with python2}
%py2_install
ln -s %{_bindir}/neomodel_install_labels %{buildroot}/%{_bindir}/neomodel_install_labels-2
ln -s %{_bindir}/neomodel_install_labels %{buildroot}/%{_bindir}/neomodel_install_labels-%{python2_version}
ln -s %{_bindir}/neomodel_remove_labels %{buildroot}/%{_bindir}/neomodel_remove_labels-2
ln -s %{_bindir}/neomodel_remove_labels %{buildroot}/%{_bindir}/neomodel_remove_labels-%{python2_version}
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/neomodel_install_labels-3
%{_bindir}/neomodel_install_labels-%{python3_version}
%{_bindir}/neomodel_remove_labels-3
%{_bindir}/neomodel_remove_labels-%{python3_version}

%if !%{with python2}
%{_bindir}/neomodel_install_labels
%{_bindir}/neomodel_remove_labels
%endif

%endif

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*
%{_bindir}/neomodel_install_labels
%{_bindir}/neomodel_install_labels-2
%{_bindir}/neomodel_install_labels-%{python2_version}
%{_bindir}/neomodel_remove_labels
%{_bindir}/neomodel_remove_labels-2
%{_bindir}/neomodel_remove_labels-%{python2_version}
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 mprahl <mprahl@redhat.com> - 3.3.1-3
- Clean up the specfile to match the Python guidelines

* Mon Jul 22 2019 mprahl <mprahl@redhat.com> - 3.3.1-2
- Stop building Python 2 packages for F31+

* Tue Apr 09 2019 mprahl <mprahl@redhat.com> - 3.3.1-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 mprahl <mprahl@redhat.com> - 3.3.0-1
- new version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.8-6
- Rebuilt for Python 3.7

* Tue Jun 19 2018 mprahl <mprahl@redhat.com> - 3.2.8-5
- unpin the python-neo4j-driver version

* Tue Jun 19 2018 mprahl <mprahl@redhat.com> - 3.2.8-4
- add upstream patch to support python neo4j-driver 1.6.x

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.8-3
- Rebuilt for Python 3.7

* Thu Jun 14 2018 mprahl <mprahl@redhat.com> - 3.2.8-2
- pin the python-neo4j-driver version

* Tue May 01 2018 mprahl <mprahl@redhat.com> - 3.2.8-1
- new version

* Thu Apr 26 2018 mprahl <mprahl@redhat.com> - 3.2.7-1
- new version

* Mon Apr 02 2018 mprahl <mprahl@redhat.com> - 3.2.5.1
- Initial release
