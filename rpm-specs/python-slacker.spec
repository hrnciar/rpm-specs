%global srcname  slacker
	
%if 0%{?fedora}
%global with_tests 1
%endif

%if 0%{?rhel}
%global with_tests 0
%endif

Name:           python-%{srcname}
Version:        0.14.0
Release:        2%{?dist}
Summary:        Python Slack API client

License:        ASL 2.0
URL:            https://github.com/os/slacker
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
Slacker is a full-featured Python interface for the Slack API.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
BuildRequires:  python3-responses
%if %{?with_tests}
BuildRequires:  python3-tox
BuildRequires:  python3-mock
%endif
Requires:       python3-requests
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Slacker is a full-featured Python interface for the Slack API.

%package -n python3-%{srcname}-doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description -n python3-%{srcname}-doc
Documentation files for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{?with_tests: %{__python3} setup.py test}

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info/

%files -n python3-%{srcname}-doc
%license LICENSE
%doc examples/
%exclude /tests/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-2
- Rebuilt for Python 3.9

* Sun Feb 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-1
- Update to latest upstream release 0.14.0 (rhbz#1803330)

* Thu Jan 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.0-4
- Update and simplify spec file

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 0.13.0-1
- new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Raphael Groner <projects.rg@smart.ms> - 0.12.0-2
- drop useless shebang
- add explicitly runtime dependency

* Sat Dec 15 2018 Raphael Groner <projects.rg@smart.ms> - 0.12.0-1
- new version
- prepare to support second python version for epel
- fix execution of tests if supported with all needed dependencies
- add documentation

* Fri Nov  2 2018 Raphael Groner <projects.rg@smart.ms> - 0.9.65-1
- initial
