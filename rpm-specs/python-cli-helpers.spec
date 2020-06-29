%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

# python2-backports-csv not in Fedora yet, disable Python 2 version 
%global with_python2 0

%global pypi_name cli_helpers

Summary:        Python helpers for common CLI tasks
Name:           python-cli-helpers
Version:        1.2.1
Release:        5%{?dist}
License:        BSD
URL:            https://github.com/dbcli/cli_helpers
Source0:        https://files.pythonhosted.org/packages/source/c/cli_helpers/cli_helpers-%{version}.tar.gz
BuildArch:      noarch
%if 0%{?with_python2}
BuildRequires:  python2-backports-csv
BuildRequires:  python2-configobj
BuildRequires:  python2-devel
BuildRequires:  python2-pytest
BuildRequires:  python-setuptools
BuildRequires:  python2-tabulate
BuildRequires:  python2-terminaltables
BuildRequires:  python2-wcwidth
%endif
%if %{with python3}
BuildRequires:  python3-configobj
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-tabulate
BuildRequires:  python3-terminaltables
BuildRequires:  python3-wcwidth
%endif 
%global _description\
CLI Helpers is a Python package that makes it easy to perform common\
tasks when building command-line apps. Its a helper library for\
command-line interfaces.
%description %_description

%if 0%{?with_python2}
%package -n     python2-cli-helpers
Summary:        %{summary}
%{?python_provide:%python_provide python2-cli-helpers}
%{?el6:Provides: python-cli-helpers}
Requires:       python2-configobj >= 5.0.5
Requires:       python2-pygments >= 1.6
Requires:       python2-tabulate >= 0.8.2
Requires:       python2-terminaltables >= 3.0.0
Requires:       python2-wcwidth
%description -n python2-cli-helpers %_description
%endif

%if %{with python3}
%package -n     python3-cli-helpers
Summary:        %{summary}
%{?python_provide:%python_provide python3-cli-helpers}
Requires:       python3-configobj >= 5.0.5
Requires:       python3-pygments >= 1.6
Requires:       python3-tabulate >= 0.8.2
Requires:       python3-terminaltables >= 3.0.0
Requires:       python3-wcwidth
%description -n python3-cli-helpers %_description
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?with_python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python3}
%py3_install
%endif
%if 0%{?with_python2}
%py2_install
%endif

%check
%if 0%{?with_python2}
PYTHONPATH=build/lib/ py.test-2 || :
%endif
%if %{with python3}
PYTHONPATH=build/lib/ py.test-3 || :
%endif

%if 0%{?with_python2}
%files -n python2-cli-helpers
%license LICENSE
%doc AUTHORS CHANGELOG README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-cli-helpers
%license LICENSE
%doc AUTHORS CHANGELOG README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.2.1-1
- 1.2.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.2.0-1
- 1.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-3
- Rebuilt for Python 3.7

* Mon May 21 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.0.2-2
- Fix description, (rhzb#1580109), thanks to Dick Marinus!

* Sun Apr 08 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.0.2-1
- 1.0.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-2
- Fix reqs.

* Thu Jan 04 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-1
- 1.0.1

* Tue Oct 24 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.0.0-1
- 1.0.0

* Wed Aug 16 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.2.3-1
- 0.2.3
- Rename
- Use summary and desc macros
- Drop Python 2 sub package for now, backports.csv not available
- Add patch to remove Python 2 specific reqs into Python 3 package

* Mon Jun 26 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.2.0-1
- 0.2.0
- Rename

* Mon May 15 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.1.0-2
- Minor tweaks

* Sat May 13 2017 Dick Marinus <dick@mrns.nl> - 0.1.0-1
- Initial package
