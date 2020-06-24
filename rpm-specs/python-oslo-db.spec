
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1
%global pypi_name oslo.db
%global pkg_name oslo-db

# guard for rhosp obsoletes
%global rhosp 0

%global common_desc \
The OpenStack Oslo database handling library. Provides database connectivity \
to the different backends and helper utils.

Name:           python-%{pkg_name}
Version:        8.1.0
Release:        1%{?dist}
Summary:        OpenStack oslo.db library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git

%description
%{common_desc}

%package -n python3-%{pkg_name}
Summary:        OpenStack oslo.db library

%{?python_provide:%python_provide python3-%{pkg_name}}

%if 0%{rhosp} == 1
Obsoletes: python-%{pkg_name}-tests < %{version}-%{release}
Obsoletes: python2-%{pkg_name}-tests < %{version}-%{release}
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# test requirements
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslo-config
BuildRequires:  python3-six
BuildRequires:  python3-fixtures
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-context
# Required to compile translation files
BuildRequires:  python3-babel
BuildRequires:  python3-migrate
BuildRequires:  python3-alembic
BuildRequires:  python3-psycopg2
BuildRequires:  python3-testresources
BuildRequires:  python3-testscenarios

Requires:       python3-PyMySQL
Requires:       python3-oslo-config >= 2:5.2.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-sqlalchemy >= 1.2.0
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-pbr
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-alembic >= 0.9.6
Requires:       python3-migrate >= 0.11.0
Requires:       python-%{pkg_name}-lang = %{version}-%{release}

%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo database handling library

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-apidoc
BuildRequires:  python3-openstackdocstheme

%description -n python-%{pkg_name}-doc
%{common_desc}

Documentation for the Oslo database handling library.
%endif

%package -n python3-%{pkg_name}-tests
Summary:    test subpackage for the Oslo database handling library

Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  python3-oslo-utils
Requires:  python3-oslo-config
Requires:  python3-fixtures
Requires:  python3-oslotest
Requires:  python3-alembic
Requires:  python3-migrate
Requires:  python3-psycopg2
Requires:  python3-testresources
Requires:  python3-testscenarios

%description -n python3-%{pkg_name}-tests
%{common_desc}

Test subpackage for the Oslo database handling library.

%package  -n python-%{pkg_name}-lang
Summary:   Translation files for Oslo db library

%description -n python-%{pkg_name}-lang
%{common_desc}

Translation files for Oslo db library

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# Let RPM handle the dependencies
rm -rf *requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

# Generate i18n files
python3 setup.py compile_catalog -d build/lib/oslo_db/locale

%install
%{py3_install}

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_db/locale/*/LC_*/oslo_db*po
rm -f %{buildroot}%{python3_sitelib}/oslo_db/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_db/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang oslo_db --all-name

%check
python3 setup.py test

%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_db
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_db/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_db/tests

%files -n python-%{pkg_name}-lang -f oslo_db.lang
%license LICENSE

%changelog
* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 8.1.0-1
- Update to upstream version 8.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.2-5
- Rebuilt for Python 3.9

* Mon May 04 2020 Javier Peña <jpena@redhat.com> - 5.0.2-4
- Drop unittest2 usage (bz#1830970)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 5.0.2-2
- Update to upstream version 5.0.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.45.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.45.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 RDO <dev@lists.rdoproject.org> 4.45.0-1
- Update to 4.45.0

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 4.44.0-1
- Update to 4.44.0

