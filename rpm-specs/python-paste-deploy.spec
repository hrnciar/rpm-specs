%global desc This tool provides code to load WSGI applications and servers from\
URIs; these URIs can refer to Python Eggs for INI-style configuration\
files.  PasteScript provides commands to serve applications based on\
this configuration file.
%global sum Load, configure, and compose WSGI applications and servers
%global srcname PasteDeploy

Name:           python-paste-deploy
Version:        2.1.0
Release:        3%{?dist}
Summary:        %{sum}
License:        MIT
URL:            https://github.com/Pylons/pastedeploy
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools


%description
%{desc}


%package -n python3-paste-deploy
Summary:        %{sum}

Requires:       python3-paste
Requires:       python3-setuptools

%{?python_provide:%python_provide python3-paste-deploy}


%description -n python3-paste-deploy
%desc



%prep
%setup -q -n %{srcname}-%{version}

# Remove bundled egg-info if it exists
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/test


%check
PYTHONPATH=. py.test-3


%files -n python3-paste-deploy
%license license.txt
%{python3_sitelib}/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 (#1797302).
- https://docs.pylonsproject.org/projects/pastedeploy/en/latest/news.html

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-4
- Subpackage python2-paste-deploy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Dan Callaghan <dcallagh@redhat.com> - 1.5.2-17
- invoke Python 2 explicitly, use modern Python RPM macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-15
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.2-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
