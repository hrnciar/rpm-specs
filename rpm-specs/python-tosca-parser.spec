%global pypi_name tosca-parser

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        7%{?dist}
Summary:        Parser for TOSCA Simple Profile in YAML

License:        ASL 2.0
URL:            https://github.com/openstack/tosca-parser
Source0:        https://pypi.io/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The TOSCA Parser is an OpenStack project and licensed under Apache 2. 
It is developed to parse TOSCA Simple Profile in YAML. It reads the TOSCA
templates and creates an in-memory graph of TOSCA nodes and their relationship.

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        Parser for TOSCA Simple Profile in YAML
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-pbr >= 1.3
BuildRequires:  python2-babel
BuildRequires:  PyYAML
BuildRequires:  python2-setuptools
# Required for testing
BuildRequires:  python2-six
BuildRequires:  python2-dateutil
BuildRequires:  python-cliff
BuildRequires:  python2-fixtures
BuildRequires:  python2-testrepository
BuildRequires:  python2-testtools
BuildRequires:  python2-testscenarios
BuildRequires:  python-oslotest
BuildRequires:  python2-subunit
BuildRequires:  python2-stestr
# Required for doc
BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme

Requires:       python2-pyyaml
Requires:       python2-cliff
Requires:       python2-dateutil
Requires:       python2-requests 
Requires:       python2-stevedore
Requires:       python2-six

%description -n python2-%{pypi_name}
The TOSCA Parser is an OpenStack project and licensed under Apache 2. 
It is developed to parse TOSCA Simple Profile in YAML. It reads the TOSCA
templates and creates an in-memory graph of TOSCA nodes and their relationship.
%endif

%package -n python-%{pypi_name}-doc
Summary:        Parser for TOSCA Simple Profile in YAML - documentation
Provides:  python2-%{pypi_name}-doc = %{version}-%{release}
Obsoletes: python2-%{pypi_name}-doc < %{version}-%{release}
Provides:  python3-%{pypi_name}-doc = %{version}-%{release}
Obsoletes: python3-%{pypi_name}-doc < %{version}-%{release}


%description -n python-%{pypi_name}-doc
The TOSCA Parser is an OpenStack project and licensed under Apache 2. 
This package contains its documentation

%if %{with python3}
%package -n python3-%{pypi_name}
Summary:        Parser for TOSCA Simple Profile in YAML
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 1.3
BuildRequires:  python3-babel
BuildRequires:  python3-PyYAML
BuildRequires:  python3-setuptools
# Required for testing
BuildRequires:  python3-six
BuildRequires:  python3-dateutil
BuildRequires:  python3-cliff
BuildRequires:  python3-fixtures
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools
BuildRequires:  python3-testscenarios
BuildRequires:  python3-oslotest
BuildRequires:  python3-subunit
BuildRequires:  python3-stestr
# Required for doc
BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

Requires:       python3-PyYAML
Requires:       python3-cliff
Requires:       python3-dateutil
Requires:       python3-requests
Requires:       python3-stevedore
Requires:       python3-six

%description -n python3-%{pypi_name}
The TOSCA Parser is an OpenStack project and licensed under Apache 2. 
It is developed to parse TOSCA Simple Profile in YAML. It reads the TOSCA
templates and creates an in-memory graph of TOSCA nodes and their relationship.
%endif


%prep
%setup -q -n %{pypi_name}-%{version}

# Let's manage requirements using rpm.
rm -f *requirements.txt

%build

%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%check
%if %{with python3}
# Cleanup test repository
PYTHON=python3 %{__python3} setup.py test || :
rm -rf .testrepository
%endif

%if %{with python2}
# Ignore test results for now, they are trying to access external URLs
# which are not accessible in Koji
PYTHON=python2 %{__python2} setup.py test || :
%endif

%install
%if %{with python3}
%{py3_install}
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# Set executable permission on test scripts
find %{buildroot}/%{python3_sitelib}/toscaparser/tests -name '*.sh' -execdir chmod +x '{}' \;
# Fix shebang on some test scripts
find %{buildroot}/%{python3_sitelib}/toscaparser/tests -name '*.py' -exec sed -i 's/^#!\/usr\/bin\/python/#!\/usr\/bin\/python3/' {} \;
mv %{buildroot}%{_bindir}/tosca-parser %{buildroot}%{_bindir}/tosca-parser-%{python3_version}
ln -s ./tosca-parser-%{python3_version} %{buildroot}%{_bindir}/tosca-parser-3
ln -s ./tosca-parser-3 %{buildroot}%{_bindir}/tosca-parser
%endif

%if %{with python2}
%{py2_install}
# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# Set executable permission on test scripts
find %{buildroot}/%{python2_sitelib}/toscaparser/tests -name '*.sh' -execdir chmod +x '{}' \;
# Fix shebang on some test scripts
find %{buildroot}/%{python2_sitelib}/toscaparser/tests -name '*.py' -exec sed -i 's/^#!\/usr\/bin\/python/#!\/usr\/bin\/python2/' {} \;
mv %{buildroot}%{_bindir}/tosca-parser %{buildroot}%{_bindir}/tosca-parser-%{python2_version}
ln -s ./tosca-parser-%{python2_version} %{buildroot}%{_bindir}/tosca-parser-2
ln -s ./tosca-parser-2 %{buildroot}%{_bindir}/tosca-parser
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/tosca-parser
%{_bindir}/tosca-parser-2
%{_bindir}/tosca-parser-%{python2_version}
%{python2_sitelib}/toscaparser
%{python2_sitelib}/tosca_parser-%{version}-py?.?.egg-info
%endif

%files -n python-%{pypi_name}-doc
%doc html README.rst
%license LICENSE

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/tosca-parser
%{_bindir}/tosca-parser-3
%{_bindir}/tosca-parser-%{python3_version}
%{python3_sitelib}/toscaparser
%{python3_sitelib}/tosca_parser-%{version}-py%{python3_version}.egg-info
%endif

%changelog
* Mon Jun 01 2020 Javier Peña <jpena@redhat.com> - 1.4.0-7
- Remove python-hacking requirement, it is not actually needed for the build

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Alfredo Moralejo <amoralej@redhat.xom> - 1.4.0-1
- Update to 1.4.0.
- Remove python2 subpackages in Fedora.
- Make documentation subpackage unversioned

* Tue Sep 11 2018 Javier Peña <jpena@redhat.com> - 1.1.0-1
- Updated to upsteam 1.1.0 (bz#1541379)
- Fix unversioned python shebangs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Javier Peña <jpena@redhat.com> - 0.8.1-1
- Updated to upstream release 0.8.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Javier Peña <jpena@redhat.com> - 0.7.0-1
- Updated to upstream release 0.7.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuild for Python 3.6

* Wed Nov 02 2016 Javier Peña <jpena@redhat.com> - 0.6.0-3
- Fix shebang for certain test scripts in python3 subpackage, so python2 is not included (bz#1390505)
- Invert test execution, so python3 tests are executed
- Use pypi.io for Source0 URL

* Tue Aug 16 2016 Javier Peña <jpena@redhat.com> - 0.6.0-2
- Ignore test results, they're trying to access the Internet

* Tue Aug 16 2016 Javier Peña <jpena@redhat.com> - 0.6.0-1
- Updated to upstream version 0.6.0

* Wed Sep 09 2015 jpena <jpena@redhat.com> - 0.1.0-3
- Fix file permissions for test scripts

* Wed Sep 09 2015 jpena <jpena@redhat.com> - 0.1.0-2
- Created docs subpackages
- Added tests
- Fixes for python3 subpkg

* Tue Sep 08 2015 jpena <jpena@redhat.com> - 0.1.0-1
- Initial package.
