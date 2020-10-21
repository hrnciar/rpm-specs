# Created by pyp2rpm-3.2.3
%global pypi_name sqlalchemy-collectd

%if 0%{?fedora} > 0
%global with_python3 1
%endif

%if (0%{?fedora} > 0) && (0%{?fedora} < 30)
%global with_python2 1
%endif

%global with_checks 1

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        7%{?dist}
Summary:        Send database connection pool stats to collectd

License:        MIT
URL:            https://github.com/sqlalchemy/%{pypi_name}
Source0:        https://github.com/sqlalchemy/%{pypi_name}/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
 sqlalchemy-collectd Send statistics on SQLAlchemy <>_ connection and
transaction metrics used by Python applications to the collectd <
service.sqlalchemy-collectd works as a SQLAlchemy plugin invoked via the
database URL, so can be used in any SQLAlchemy application (1.1 or greater)
that accepts arbitrary connection URLs. The plugin is loaded using setuptools
entrypoints and no code changes...

%if 0%{?with_python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-setuptools
Requires:       python2-sqlalchemy >= 1.1
Requires:       collectd-python

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

BuildRequires:  python2-mock
BuildRequires:  python2-pytest
BuildRequires:  python2-pytest-runner
BuildRequires:  python2-sqlalchemy >= 1.1

%description -n python2-%{pypi_name}
 sqlalchemy-collectd Send statistics on SQLAlchemy <>_ connection and
transaction metrics used by Python applications to the collectd <
service.sqlalchemy-collectd works as a SQLAlchemy plugin invoked via the
database URL, so can be used in any SQLAlchemy application (1.1 or greater)
that accepts arbitrary connection URLs. The plugin is loaded using setuptools
entrypoints and no code changes...
%endif

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-setuptools
Requires:       python3-sqlalchemy >= 1.1
Requires:       collectd-python

BuildRequires:  python3-setuptools
BuildRequires:  python3-sqlalchemy >= 1.1
BuildRequires:  python3-devel
%if 0%{?with_checks} > 0
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
%endif

%description -n python3-%{pypi_name}
 sqlalchemy-collectd Send statistics on SQLAlchemy <>_ connection and
transaction metrics used by Python applications to the collectd <
service.sqlalchemy-collectd works as a SQLAlchemy plugin invoked via the
database URL, so can be used in any SQLAlchemy application (1.1 or greater)
that accepts arbitrary connection URLs. The plugin is loaded using setuptools
entrypoints and no code changes...
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif


%check
%if 0%{?with_checks} > 0
%if 0%{?with_python2}
%{__python2} setup.py test
%endif

%if 0%{?with_python3}
%{__python3} setup.py test
%endif
%endif

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%doc README.rst LICENSE examples/
%{python2_sitelib}/sqlalchemy_collectd
%{python2_sitelib}/sqlalchemy_collectd-%{version}-py?.?.egg-info
%{_bindir}/connmon
%endif

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst LICENSE examples/
%{python3_sitelib}/sqlalchemy_collectd
%{python3_sitelib}/sqlalchemy_collectd-%{version}-py%{python3_version}.egg-info
%{_bindir}/connmon
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Mike Bayer <mbayer@redhat.com> - 0.0.4-1
- upgrade to 0.0.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Matthias Runge <mrunge@redhat.com> - 0.0.3-4
- drop python2 for Fedora > 29
- add collectd-python as dependency

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-2
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Matthias Runge <mrunge@redhat.com> - 0.0.3-1
- Initial package (rhbz#1564206)
