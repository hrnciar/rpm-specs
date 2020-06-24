%global pkg_name flask-security
%global mod_name Flask-Security
%global desc Flask-Security quickly adds security features to your Flask application.

Name:       python-%{pkg_name}
Version:    3.0.0
Release:    10%{?dist}
Summary:    Simple security for Flask apps
License:    MIT
URL:        http://github.com/mattupstate/%{pkg_name}/
Source0:    https://files.pythonhosted.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:  noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-pytest-runner
BuildRequires: python%{python3_pkgversion}-babel
BuildRequires: python%{python3_pkgversion}-flask-sphinx-themes
BuildRequires: python%{python3_pkgversion}-flask-babelex
BuildRequires: python%{python3_pkgversion}-flask-login
BuildRequires: python%{python3_pkgversion}-flask-principal
BuildRequires: python%{python3_pkgversion}-passlib
BuildRequires: python%{python3_pkgversion}-flask-wtf


%description
%{desc}

%package -n python%{python3_pkgversion}-%{pkg_name}
Summary: Simple security for Flask apps
Requires: python%{python3_pkgversion}-flask
Requires: python%{python3_pkgversion}-flask-login
Requires: python%{python3_pkgversion}-flask-mail
Requires: python%{python3_pkgversion}-flask-principal
Requires: python%{python3_pkgversion}-flask-wtf
Requires: python%{python3_pkgversion}-flask-babel
Requires: python%{python3_pkgversion}-itsdangerous
Requires: python%{python3_pkgversion}-passlib

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkg_name}}

%description -n python%{python3_pkgversion}-%{pkg_name}
%{desc}

%package doc
Summary:        Documentation for %{name}, includes full API docs
%{?python_provide:%python_provide python2-%{pkg_name}-doc}
%description doc
This package contains the full API documentation for %{name}.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%py3_build

pushd docs
make html
make man
rm -f docs/_build/html/.buildinfo
popd

%install
%py3_install
install -Dp docs/_build/man/flask-security.1 %{buildroot}%{_mandir}/man1/flask-security.1

%files doc
%doc README.rst AUTHORS CHANGES docs/_build/html
%license LICENSE
%{_mandir}/man1/flask-security.*

%files -n python%{python3_pkgversion}-%{pkg_name}
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/flask_security

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.0-4
- Subpackage python2-flask-security has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.7

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.0.0-1
- new version 3.0.0

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.7.5-2
- improve spec file

* Tue Jan  3 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 1.7.5-1
- Initial package
