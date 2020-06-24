# Created by pyp2rpm-3.2.1
%global pypi_name pykafka
%global alphatag .dev2

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

# Note: there's already a python-kafka package which is a separate
# project (kafka-python on pypi)
# FIXME: requested upstream to include license in source tarball
# https://github.com/Parsely/pykafka/pull/654

Name:           python-%{pypi_name}
Version:        2.6.0
Release:        0.12%{?alphatag}%{?dist}
Summary:        Full-Featured Pure-Python Kafka Client

License:        ASL 2.0
URL:            https://github.com/Parsely/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}%{?alphatag}.tar.gz

BuildRequires:  gcc
BuildRequires:  librdkafka-devel

%description
PyKafka is a cluster-aware Kafka client for Python.
PyKafka’s primary goal is to provide a similar level of abstraction to the
JVM Kafka client using idioms familiar to Python programmers and exposing the
most Pythonic API possible.

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Full-Featured Pure-Python Kafka Client
%{?python_provide:%python_provide python2-%{pypi_name}}
BuildRequires:  python2-devel
BuildRequires:  python2-pytest
BuildRequires:  python2-pytest-cov
BuildRequires:  python2-snappy
BuildRequires:  python2-mock
BuildRequires:  python2-unittest2
BuildRequires:  python2-setuptools
BuildRequires:  python2-kazoo
BuildRequires:  python2-gevent >= 1.1.0
  
Requires:       python2-six >= 1.5
Requires:       python2-kazoo
Requires:       python2-tabulate
Requires:       python2-gevent >= 1.1.0
Requires:       python2-setuptools

%description -n python2-%{pypi_name}
%{description}
%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        Full-Featured Pure-Python Kafka Client
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-snappy
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-kazoo
BuildRequires:  python3-gevent >= 1.1.0

Requires:       python3-six >= 1.5
Requires:       python3-kazoo
Requires:       python3-tabulate
Requires:       python3-gevent >= 1.1.0
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
%{description}
%endif


%prep
%autosetup -n %{pypi_name}-%{version}%{?alphatag}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif


%install
%if 0%{with python3}
%py3_install
cp -p %{buildroot}/%{_bindir}/kafka-tools %{buildroot}/%{_bindir}/kafka-tools-3
ln -sf %{_bindir}/kafka-tools-3 %{buildroot}/%{_bindir}/kafka-tools-%{python3_version}
# Remove tests as they're not installed in package specific path
rm -rf %{buildroot}%{python3_sitearch}/tests
# Remove python module C source code
rm %{buildroot}%{python3_sitearch}/%{pypi_name}/rdkafka/_rd_kafkamodule.c
%endif

%if %{with python2}
%py2_install
cp -p %{buildroot}/%{_bindir}/kafka-tools %{buildroot}/%{_bindir}/kafka-tools-2
ln -sf %{_bindir}/kafka-tools-2 %{buildroot}/%{_bindir}/kafka-tools-%{python2_version}
# Remove tests as they're not installed in package specific path
rm -rf %{buildroot}%{python2_sitearch}/tests
# Remove python module C source code
rm %{buildroot}%{python2_sitearch}/%{pypi_name}/rdkafka/_rd_kafkamodule.c
%endif

%check
# FIXME: missing deps on python-testinstances
# make tests non-failing until it is available
%if %{with python2}
%{__python2} setup.py test ||:
%endif
%if 0%{with python3}
%{__python3} setup.py test ||:
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%{_bindir}/kafka-tools
%{_bindir}/kafka-tools-2
%{_bindir}/kafka-tools-%{python2_version}
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/kafka-tools
%{_bindir}/kafka-tools-3
%{_bindir}/kafka-tools-%{python3_version}
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-*.egg-info
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-0.12.dev2
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-0.11.dev2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-0.10.dev2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Oct 03 2019 Javier Peña <jpena@redhat.com> - 2.6.0-0.9.dev2
- Removed unittest2 dependency from python3 subpackage, not needed

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-0.8.dev2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-0.7.dev2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Javier Peña <jpena@redhat.com> - 2.6.0-0.6.dev2
- Disable the python2 subpackage on Fedora (bz#1701959)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-0.5.dev2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-0.4.dev2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-0.3.dev2
- Rebuilt for Python 3.7

* Tue May 29 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-0.2.dev2
- Fix python ambiguous requires

* Tue Feb 14 2017 hguemar <karlthered@gmail.com> - 2.6.0.dev2-1
- Initial package.
