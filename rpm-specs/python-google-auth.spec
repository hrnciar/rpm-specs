%{?python_enable_dependency_generator}

%if 0%{?rhel} == 7
%bcond_with    python3
%bcond_without python2
%else
%bcond_with    python2
%bcond_without python3
%endif

%global library google-auth

%if 0%{?rhel} == 7
%global py3 python%{python3_pkgversion}
%else
%global py3 python3
%endif

Name:       python-%{library}
Version:    1.18.0
Release:    1%{?dist}
Epoch:      1
Summary:    Google Auth Python Library
License:    ASL 2.0
URL:        https://github.com/googleapis/google-auth-library-python

Source0:    https://github.com/googleapis/google-auth-library-python/archive/v%{version}.tar.gz

BuildArch:  noarch

%description
Google Auth Python Library

%if 0%{?with_python2}
%package -n python2-%{library}
Summary:    Google Auth Python Library
%{?python_provide:%python_provide python2-%{library}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  git

Requires:  python2-pyasn1
Requires:  python2-pyasn1-modules
Requires:  python2-rsa
Requires:  python2-six
Requires:  python-cachetools

%description -n python2-%{library}
Google Auth Python Library
%endif

%if 0%{?with_python3}
%package -n %{py3}-%{library}
Summary:    Google Auth Python Library
%{?python_provide:%python_provide %{py3}-%{library}}

BuildRequires:  %{py3}-devel
BuildRequires:  %{py3}-setuptools
BuildRequires:  git
%if %{undefined __pythondist_requires}
Requires:  %{py3}-pyasn1
Requires:  %{py3}-pyasn1-modules
Requires:  %{py3}-rsa
Requires:  %{py3}-six
Requires:  %{py3}-cachetools
%endif

%description -n %{py3}-%{library}
Python client for the kubernetes API.

%endif

%prep
%autosetup -n google-auth-library-python-%{version}

#Allow newer cachetools
sed -i 's/<3\.2/<5.0/g' setup.py

%build
%if %{with python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif

%check

%if %{with python2}
%files -n python2-%{library}
%license LICENSE
%{python2_sitelib}/google/auth
%{python2_sitelib}/google/oauth2
%{python2_sitelib}/google_auth-%{version}*.egg-info
%{python2_sitelib}/google_auth-%{version}*.pth
%endif

%if 0%{?with_python3}
%files -n %{py3}-%{library}
%license LICENSE
%{python3_sitelib}/google/auth
%{python3_sitelib}/google/oauth2
%{python3_sitelib}/google_auth-%{version}*.egg-info
%{python3_sitelib}/google_auth-%{version}*.pth
%endif

%changelog
* Fri Jun 19 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1:1.18.0-1
- Update to 1.18.0 (#1846258)

* Thu Jun 04 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1:1.16.1-1
- Update to 1.16.1 (#1841468)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:1.14.3-2
- Rebuilt for Python 3.9

* Tue May 12 2020 Jason Montleon <jmontleo@redhat.com> - 1:1.14.3-1
- Update to 1.14.3

* Thu May 07 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1:1.14.2-1
- Update to 1.14.2 (#1832794)

* Wed Apr 22 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1:1.14.1-1
- Update to 1.14.1 (#1824032)

* Thu Apr 02 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1:1.13.1-1
- Update to 1.13.1 (#1817303)

* Mon Mar 16 2020 Jason Montleon <jmontleo@redhat.com> - 1:1.11.3-1
- Update to 1.11.3

* Wed Feb 19 2020 Jason Montleon <jmontleo@redhat.com> - 1:1.11.2-1
- Update to 1.11.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1:1.11.0-1
- Update to 1.11.0 (#1794771)

* Thu Jan 23 2020 Jason Montleon <jmontleo@redhat.com> - 1:1.10.2-2
- Update to 1.10.2 (#1793920)

* Wed Jan 15 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1:1.10.1-1
- Update to 1.10.1 (#1779733)

* Fri Dec 20 2019 Jason Montleon <jmontleo@redhat.com> - 1:1.10.0-1
- Update to 1.10.0

* Wed Dec 11 2019 Jason Montleon <jmontleo@redhat.com> - 1:1.9.0-2
- Allow newer cachetools

* Wed Dec 11 2019 Jason Montleon <jmontleo@redhat.com> - 1:1.9.0-1
- Update to 1.9.0

* Wed Dec 11 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1:1.8.2-1
- Update to 1.8.2 (#1779733)

* Thu Nov 19 2019 Jason Montleon <jmontleo@redhat.com> - 1:1.7.1-1
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.1.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.1.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.1.1-6
- Enable python dependency generator

* Mon Jan 14 2019 Jason Montleon <jmontleo@redhat.com> - 1:1.1.1-5
- Fix cachetools dependency for python2

* Thu Dec 13 2018 Jason Montleon <jmontleo@redhat.com> - 1:1.1.1-4
- Use python3_pkgversion for EPEL

* Mon Dec 3 2018 Jason Montleon <jmontleo@redhat.com> - 1:1.1.1-3
- Use GitHub instead of PyPI source tarball to build

* Tue Oct 23 2018 Alfredo Moralejo <amoralej@redhat.com> - 1:1.1.1-2
- Removed python2 subpackages in Fedora (rhbz#1636936).

* Mon Aug 13 2018 Alfredo Moralejo <amoralej@redhat.com> - 1:1.1.1-1
- Revert to version 1.1.1. Version 1.3.0 requires pyasn1-modules newer that in Fedora (rhbz#1577286).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Alfredo Moralejo <amoralej@redhat.com> 1.3.0-1
- Update to 1.3.0

* Fri Oct 13 2017 Jason Montleon <jmontleo@redhat.com> 1.1.1-1
- Initial Build
