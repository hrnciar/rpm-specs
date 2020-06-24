# what it's called on pypi
%global srcname PyJWT
# what it's imported as
%global libname jwt
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{libname}

%global common_description %{expand:
A Python implementation of JSON Web Token draft 01. This library provides a
means of representing signed content using JSON data structures, including
claims to be transferred between two parties encoded as digitally signed and
encrypted JSON objects.}

%if %{defined fedora} && 0%{?fedora} < 32
%bcond_without  python2
%endif
%bcond_without  python3


Name:           python-%{pkgname}
Version:        1.7.1
Release:        8%{?dist}
Summary:        JSON Web Token implementation in Python
License:        MIT
URL:            https://github.com/jpadilla/pyjwt
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-cryptography >= 1.4.0
BuildRequires:  python2-pytest
Requires:       python2-cryptography >= 1.4.0
%{?python_provide:%python_provide python2-%{pkgname}}


%description -n python2-%{pkgname} %{common_description}
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-cryptography >= 1.4.0
BuildRequires:  python%{python3_pkgversion}-pytest
Requires:       python%{python3_pkgversion}-cryptography >= 1.4.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}
%endif


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info
# prevent pullng in `addopts` for pytest run later
rm setup.cfg


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}


%check
%{?with_python2:PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} --verbose tests}
%{?with_python3:PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose tests}


%if %{with python2}
%files -n python2-%{pkgname}
%doc README.rst AUTHORS
%license LICENSE
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%doc README.rst AUTHORS
%license LICENSE
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info
%{_bindir}/pyjwt
%endif


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 29 2019 Carl George <carl@george.computer> - 1.7.1-5
- Disable python2 subpackage on F32+ rhbz#1744643

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Carl George <carl@george.computer> - 1.7.1-2
- Re-enable python2 subpackage since python-oauthlib still needs it

* Mon Mar 04 2019 Yatin Karel <ykarel@redhat.com> - 1.7.1-1
- Update to 1.7.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Carl George <carl@george.computer> - 1.6.4-2
- Disable python2 subpackage on F30+
- Don't share doc and license dir between subpackages, can cause upgrade issues
- Add patch1 to skip failing tests

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.6.4-1
- Update to 1.6.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-2
- Rebuilt for Python 3.7

* Thu Apr 05 2018 Carl George <carl@george.computer> - 1.6.1-1
- Latest upstream
- Add patch0 to remove pytest-{cov,runner} deps
- Share doc and license dir between subpackages
- Enable EPEL PY3 build

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Kevin Fenzi <kevin@scrye.com> - 1.5.3-1
- Update to 1.5.3. Fixes bug #1488693
- 1.5.1 fixed CVE-2017-11424 Fixes bug #1482529

* Mon Aug 14 2017 Troy Dawson <tdawson@redhat.com> - 1.5.2-3
- Fixup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 24 2017 Kevin Fenzi <kevin@scrye.com> - 1.5.2-1
- Update to 1.5.2. Fixes bug #1464286

* Sat May 27 2017 Kevin Fenzi <kevin@scrye.com> - 1.5.0-1
- Update to 1.5.0. Fixes bug #1443792

* Mon Apr 17 2017 Kevin Fenzi <kevin@scrye.com> - 1.4.2-4
- Modernize spec and make sure to provide python2-jwt

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.4.2-2
- Rebuild for Python 3.6

* Mon Aug 15 2016 Kevin Fenzi <kevin@scrye.com> - 1.4.2-1
- Update to 1.4.2. Fixes bug #1356333

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 1.4.0-1
- new version

* Wed Jun 17 2015 Ralph Bean <rbean@redhat.com> - 1.3.0-1
- new version
- start running the test suite.

* Fri Mar 27 2015 Ralph Bean <rbean@redhat.com> - 1.0.1-1
- new version

* Thu Mar 19 2015 Ralph Bean <rbean@redhat.com> - 1.0.0-1
- new version

* Fri Feb 20 2015 Ralph Bean <rbean@redhat.com> - 0.4.3-1
- Latest upstream.
- Expand the description as per review feedback.
- Add a comment about the test suite.
- Declare noarch.
- Declare _docdir_fmt

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 0.4.2-1
- initial package for Fedora.
