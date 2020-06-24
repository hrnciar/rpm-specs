%global srcname nose-testconfig
Name:           python-nose-testconfig
Version:        0.10
Release:        19%{?dist}
Summary:        Test configuration plugin for nosetests

License:        ASL 2.0
URL:            https://bitbucket.org/jnoller/nose-testconfig/
Source0:        https://pypi.python.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

# Upstream does not include the license, which is required for redistribution
# See https://bitbucket.org/jnoller/nose-testconfig/issue/10/
Source1:        LICENSE-2.0

# explicitly accept the API change in pyyaml-5.1 to suppress the warning when
# loading a yaml file. This will load yaml files with yaml.FullLoader, which
# allows for !!python extensions but does not allow arbitrary code execution.
Patch0:         nose-testconfig-pyyaml-warning.patch

BuildArch:      noarch

%description
nose-testconfig is a plugin to the nose test framework which provides a
faculty for passing test-specific (or test-run specific) configuration data
to the tests being executed.

Currently configuration files in the following formats are supported:

- YAML (via PyYAML <http://pypi.python.org/pypi/PyYAML/>)
- INI (via ConfigParser <http://docs.python.org/lib/module-ConfigParser.html>)
- Pure Python (via Exec)
- JSON (via JSON <http://docs.python.org/library/json.html>)

%package -n python3-%{srcname}
Summary:        Test configuration plugin for nosetests for Python3
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-nose
# Require >= 5.1 for yaml.FullLoader, used by Patch0
Requires:       python3-PyYAML >= 5.1

%description -n python3-%{srcname}
nose-testconfig is a plugin to the nose test framework which provides a
faculty for passing test-specific (or test-run specific) configuration data
to the tests being executed.

Currently configuration files in the following formats are supported:

- YAML (via PyYAML <http://pypi.python.org/pypi/PyYAML/>)
- INI (via ConfigParser <http://docs.python.org/lib/module-ConfigParser.html>)
- Pure Python (via Exec)
- JSON (via JSON <http://docs.python.org/library/json.html>)

This is the Python 3 version of the package.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -rf nose_testconfig.egg-info
cp %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE-2.0
%doc ACKS TODO docs/index.txt
%{python3_sitelib}/testconfig.py*
%{python3_sitelib}/__pycache__/testconfig.*
%{python3_sitelib}/nose_testconfig-%{version}-*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 David Shea <dshea@redhat.com> - 0.10-14
- Remove the python2 subpackage (#1701680)

* Mon Mar 25 2019 David Shea <dshea@redhat.com> - 0.10-13
- Handle a warning displayed by pyyaml-5.1 (#1692477)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct  5 2015 David Shea <dshea@redhat.com> - 0.10-1
- Update to upstream version 0.10, which adds support for multiple configs
- Change to the new packaging guildelines which renames python-nose-testconfig to python2-nose-testconfig

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 David Shea <dshea@redhat.com> - 0.9-4
- Use %%license for the license file

* Tue Aug 12 2014 David Shea <dshea@redhat.com> - 0.9-3
- Added a comment about the inclusion of an external copy of the ASL

* Mon Aug 11 2014 David Shea <dshea@redhat.com> - 0.9-2
- Include a copy of the Apache Software License, 2.0.

* Thu Apr 10 2014 David Shea <dshea@redhat.com> - 0.9-1
- Initial package
