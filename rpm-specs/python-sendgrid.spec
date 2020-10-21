%global srcname sendgrid

Name:           python-%{srcname}
Version:        3.6.5
Release:        14%{?dist}
Summary:        SendGrid library for Python

License:        MIT
URL:            https://github.com/%{srcname}/%{srcname}-python/
Source0:        https://github.com/%{srcname}/%{srcname}-python/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  python3-http-client
BuildRequires:  python3-PyYAML
BuildRequires:  python3-werkzeug
BuildRequires:  python3-flask
BuildRequires:  python3-six

%description
This library allows to quickly and easily send emails through
SendGrid using Python.


%package -n python3-%{srcname}
Summary:    %{summary}
Requires:   python3-http-client
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This library allows to quickly and easily send emails through
SendGrid using Python3.


%package examples
Summary:        SendGrid library examples

%description examples
This package contains SendGrid library usage examples.


%prep
%setup -qn %{srcname}-python-%{version}
rm -fr %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
# Exclude test_sendgrid.py, as it downloads extertal lib `prism` from Github.
rm test/test_sendgrid.py
%{__python3} -m unittest discover -v


%files -n python3-%{srcname}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%files examples
%doc examples/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.5-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.5-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.5-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.6.5-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.5-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.6.5-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Iryna Shcherbina <ishcherb@redhat.com> - 3.6.5-1
- Update to 3.6.3 and add examples subpackage
- Run tests

* Mon Mar 20 2017 Dominika Krejci <dkrejci@redhat.com> - 3.1.10-1
- Update to 3.1.10
- Add Python3 subpackage
- Add tests

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 23 2013 Daniel Bruno <dbruno@fedoraproject.org> - 0.1.4-1
- Initial package for Fedora

