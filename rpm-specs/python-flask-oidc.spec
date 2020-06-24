%global srcname flask_oidc
%global tar_name flask-oidc
%global sum An openID Connect support for Flask

Name:           python-%{tar_name}
Version:        1.4.0
Release:        8%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://github.com/puiterwijk/flask-oidc
Source0:        https://pypi.io/packages/source/f/flask-oidc/%{tar_name}-%{version}.tar.gz

BuildArch:      noarch

%description
OpenID Connect support for Flask.
This library should work with any standards compliant
OpenID Connect provider. It has been tested with:
Google+ Login, Ipsilon

%package -n         python3-%{tar_name}
Summary:            %{sum}

Requires:           python3-setuptools
Requires:           python3-flask
Requires:           python3-itsdangerous
Requires:           python3-oauth2client
Requires:           python3-six
BuildRequires:      python3-flask
BuildRequires:      python3-itsdangerous
BuildRequires:      python3-oauth2client
BuildRequires:      python3-six
BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-nose
BuildRequires:      python3-mock


%{?python_provide:%python_provide python3-%{tar_name}}

%description -n python3-%{tar_name}
Currently designed around Google’s oauth2client library and OpenID Connect
implementation. May or may not interoperate with other OpenID Connect
identity providers, for example, Microsoft’s Azure Active Directory

%prep
%autosetup -n %{tar_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{tar_name}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/*.egg-info/
%{_bindir}/oidc-register

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-3
- Drop python2 support.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 08 2018 Ralph Bean <rbean@redhat.com> - 1.4.0-1
- new version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Ralph Bean <rbean@redhat.com> - 1.1.1-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Simon M <skrzepto@gmail.com> - 1.0.1
- Working on initial spec file
- Typo in version in this change log
- Updating email address of author

* Wed Jul 13 2016 Simon M <skrzepto@gmail.com> - 1.0.3
- Updating package version 
