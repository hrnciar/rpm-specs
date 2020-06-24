%{?python_enable_dependency_generator}

%global srcname vconnector
%global sum     vSphere Connector Module for Python

Name:           python-%{srcname}
Version:        0.6.0
Release:        3%{?dist}
Summary:        %{sum}

# setup.py mentions BSD license
License:        BSD
URL:            https://github.com/dnaeon/py-%{srcname}
Source0:        %{pypi_source}#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-docopt
BuildRequires:  python%{python3_pkgversion}-tabulate
BuildRequires:  python%{python3_pkgversion}-pyvmomi
BuildRequires:  help2man

%global _description \
vConnector is a wrapper module around pyVmomi vSphere bindings,\
which provides methods¸ for connecting and retrieving of objects\
from a vSphere server.\
\
The purpose of vConnector is to provide the basic primitives for\
building complex applications. vConnector can also be used for\
managing the user/pass/host credentials for your vSphere\
environment using an SQLite database, which in turn can be shared\
between multiple applications requiring access to your vSphere\
environment through a common interface.

%description
%{_description}

%package     -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
# no magic dependencies in epel
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-pyvmomi
Requires:       python%{python3_pkgversion}-tabulate
Requires:       python%{python3_pkgversion}-docopt
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{_description}


%prep
%autosetup -n%{srcname}-%{version}
# fix shebang, https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
sed -i 1s:python\$:%{__python3}: src/%{srcname}-cli

%build
%py3_build

%install
%py3_install
# W: no-manual-page-for-binary
mkdir -p %{buildroot}%{_mandir}/man1
help2man src/%{srcname}-cli >%{buildroot}%{_mandir}/man1/%{srcname}-cli.1

%check
# run cli to see if any error on stderr
src/%{srcname}-cli -v


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py3.?.egg-info/
%{_bindir}/%{srcname}-cli
%{_mandir}/man1/%{srcname}-cli.1*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Raphael Groner <projects.rg@smart.ms> - 0.6.0-1
- new version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-5
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Raphael Groner <projects.rg@smart.ms> - 0.5.3-4
- drop brand

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Raphael Groner <projects.rg@smart.ms> - 0.5.3-1
- initial
