# A lot of inconsistency here :)
%global modname virtualenv-clone
%global undername virtualenv_clone
%global srcname clonevirtualenv

Name:             python-virtualenv-clone
Version:          0.5.4
Release:          2%{?dist}
Summary:          Script to clone virtualenvs

License:          MIT
URL:              http://pypi.python.org/pypi/virtualenv-clone
Source0:          http://pypi.python.org/packages/source/v/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-virtualenv

%description
A script for cloning a non-relocatable virtualenv.

Virtualenv provides a way to make virtualenv's relocatable which could then
be copied as we wanted. However making a virtualenv relocatable this way
breaks the no-site-packages isolation of the virtualenv as well as other
aspects that come with relative paths and '/usr/bin/env' shebangs that may
be undesirable.

Also, the .pth and .egg-link rewriting doesn't seem to work as intended.
This attempts to overcome these issues and provide a way to easily clone an
existing virtualenv.

%package -n python3-virtualenv-clone
Summary:          Script to clone virtualenvs
%{?python_provide:%python_provide python3-%{modname}}

Requires:         python3-virtualenv

%description -n python3-virtualenv-clone
virtualenv cloning script.

A script for cloning a non-relocatable virtualenv.

Virtualenv provides a way to make virtualenv's relocatable which could then
be copied as we wanted. However making a virtualenv relocatable this way
breaks the no-site-packages isolation of the virtualenv as well as other
aspects that come with relative paths and '/usr/bin/env' shebangs that may
be undesirable.

Also, the .pth and .egg-link rewriting doesn't seem to work as intended.
This attempts to overcome these issues and provide a way to easily clone an
existing virtualenv.


%prep
%setup -q -n %{modname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{modname}
%doc README.md
%{python3_sitelib}/%{srcname}.*
%{python3_sitelib}/%{undername}-%{version}-*
%{python3_sitelib}/__pycache__/*%{srcname}*

# goes to py2 if not with_python3
%{_bindir}/virtualenv-clone

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Tadej Janež <tadej.j@nez.si> - 0.5.4-1
- Update to 0.5.4 release
- Add explicit BuildRequires on python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-2
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Tadej Janež <tadej.j@nez.si> - 0.5.3-1
- Update to 0.5.3 release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-13
- Drop the Python 2 package (#1661353)

* Fri Aug 24 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-12
- Only one /usr/bin/virtualenv-clone

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.6-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Ralph Bean <rbean@redhat.com> - 0.2.6-2
- Enable the python3 subpackage.
- Create a separate python2 subpackage and modernize macros.

* Mon Jun 29 2015 Ralph Bean <rbean@redhat.com> - 0.2.6-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.4-1
- initial package for Fedora
