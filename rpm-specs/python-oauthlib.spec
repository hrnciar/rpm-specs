%if (0%{?fedora} > 0 && 0%{?fedora} < 32) || (0%{?rhel} > 0 && 0%{?rhel} <= 7)
  %bcond_without python2
  %bcond_without python3
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
  %bcond_with python2
  %bcond_without python3
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
%{!?__python2:        %global __python2 /usr/bin/python2}
%{!?python2_sitelib:  %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?py2_build:        %global py2_build %{__python2} setup.py build --executable="%{__python2} -s" %{?*}}
%{!?py2_install:      %global py2_install %{__python2} setup.py install --skip-build --root %{buildroot} %{?*}}
%endif

%global modname oauthlib

Name:               python-oauthlib
Version:            3.0.2
Release:            6%{?dist}
Summary:            An implementation of the OAuth request-signing logic

License:            BSD
URL:                https://github.com/oauthlib/oauthlib

# WARNING: The upstream release URL contains a leading 'v' in the
# tarball name, however the URL downloads a tarball name without the
# leading 'v'.  The packaging guidelines
# (https://fedoraproject.org/wiki/Packaging:SourceURL#Troublesome_URLs)
# state in this case one should just use the tarball name and document
# the reason why the full URL was not used.
#Source0: https://github.com/oauthlib/oauthlib/archive/v%{modname}-%{version}.tar.gz
Source0:            %{modname}-%{version}.tar.gz

BuildArch:          noarch

%description
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft
OAuth client support onto your favorite HTTP library, or provider support
onto your favourite web framework. If you're a maintainer of such a
library, write a thin veneer on top of OAuthLib and get OAuth support for
very little effort.

%if %{with python2}
%package -n python2-oauthlib
Summary:            An implementation of the OAuth request-signing logic
%{?python_provide:%python_provide python2-oauthlib}

BuildRequires:      python2-devel
BuildRequires:      python2-setuptools

BuildRequires:      python2-nose
BuildRequires:      python2-mock
BuildRequires:      python2-blinker

BuildRequires:      python2-jwt >= 1.6.0
BuildRequires:      python2-cryptography >= 1.4.0

Requires:           python2-jwt >= 1.6.0
Requires:           python2-cryptography >= 1.4.0

%description -n python2-oauthlib
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft
OAuth client support onto your favorite HTTP library, or provider support
onto your favourite web framework. If you're a maintainer of such a
library, write a thin veneer on top of OAuthLib and get OAuth support for
very little effort.

%endif # with python2

%if %{with python3}
%package -n python3-oauthlib
Summary:            An implementation of the OAuth request-signing logic
%{?python_provide:%python_provide python3-oauthlib}

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

BuildRequires:      python3-nose
BuildRequires:      python3-mock
BuildRequires:      python3-blinker

BuildRequires:      python3-jwt >= 1.6.0
BuildRequires:      python3-cryptography >= 1.4.0

Requires:           python3-jwt >= 1.6.0
Requires:           python3-cryptography >= 1.4.0

%description -n python3-oauthlib
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft
OAuth client support onto your favorite HTTP library, or provider support
onto your favourite web framework. If you're a maintainer of such a
library, write a thin veneer on top of OAuthLib and get OAuth support for
very little effort.

%endif # with python3

%prep
%setup -q -n %{modname}-%{version}

# python-unittest2 is now provided by "python" package and python-unittest is retired
#  adapt setup.py to reflect this fact downstream
sed -i "s/'unittest2', //" setup.py

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%if %{with python2}
%py2_build
%endif # with python2
%if %{with python3}
%py3_build
%endif # with python3

%install
%if %{with python2}
%py2_install
%endif # with python2
%if %{with python3}
%py3_install
%endif # with python3

%check
%if %{with python2}
%{__python2} setup.py test
%endif # with python2
%if %{with python3}
%{__python3} setup.py test
%endif # with python3

%if %{with python2}
%files -n python2-oauthlib
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{modname}-%{version}*
%endif # with python2

%if %{with python3}
%files -n python3-oauthlib
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*
%endif # with python3

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019  <jdennis@redhat.com> - 3.0.2-1
- Update to upstream 3.0.2
- Resolves: rhbz#1730033

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug  3 2018  <jdennis@redhat.com> - 2.1.0-1
- upgrade to latest upstream 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018  <jdennis@redhat.com> - 2.0.1-10
- Restore use of bcond for python conditionals

* Tue Jul 10 2018  <jdennis@redhat.com> - 2.0.1-9
- Unify spec file between Fedora and RHEL

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-8
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.1-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 0.7.19-5
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 John Dennis <jdennis@redhat.com> - 2.0.1-3
- fix dependency on python2-jwt, should be python-jwt

* Thu Apr 13 2017 Dennis Gilmore <dennis@ausil.us> - 2.0.1-2
- add spaces around the >= for Requires

* Thu Mar 16 2017 John Dennis <jdennis@redhat.com> - 2.0.1-1
- Upgrade to upstream 2.0.1
- port from jwt to jwcrypto (conditional build)
- bring into alignment with rhel spec file

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.0.3-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 1.0.3-2
- Modernize python macros.

* Sun Apr 10 2016 Kevin Fenzi <kevin@scrye.com> - 1.0.3-1
- Update to 1.0.3
- Add python2 provides (fixes bug #1313235 and #1314349)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5.20150520git514cad7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4.20150520git514cad7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3.20150520git514cad7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 0.7.2-2.20150520git514cad7
- new version, from a git checkout
- Replace our patch with a sed statement.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Apr 11 2014 Ralph Bean <rbean@redhat.com> - 0.6.0-4
- Use forward-compat python-crypto2.6 package for el6.

* Tue Jan 21 2014 Ralph Bean <rbean@redhat.com> - 0.6.0-3
- Compat macros for el6.

* Fri Nov 01 2013 Ralph Bean <rbean@redhat.com> - 0.6.0-2
- Modernized python2 rpmmacros.

* Thu Oct 31 2013 Ralph Bean <rbean@redhat.com> - 0.6.0-1
- Initial package for Fedora
