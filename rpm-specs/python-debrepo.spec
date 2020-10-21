%global srcname debrepo

Name:           python-%{srcname}
Version:        0.0.3
Release:        18%{?dist}
Summary:        Inspect and compare Debian repositories
License:        GPLv3+
URL:            https://pagure.io/debrepo
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel

BuildArch:      noarch


%description
debrepo is a library for inspecting composes of Debian repositories and
their elements, including package archives. It includes classes capable
of reading compose, repository, and package data from the filesystem,
and methods to compare the data between different versions. To this end,
the debrepodiff tool provides a command line interface for comparing
composes.

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-debian
# https://bugs.debian.org/858906
Requires:       python3-chardet
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
debrepo is a library for inspecting composes of Debian repositories and
their elements, including package archives. It includes classes capable
of reading compose, repository, and package data from the filesystem,
and methods to compare the data between different versions. To this end,
the debrepodiff tool provides a command line interface for comparing
composes.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%{py3_build}

%install
%py3_install
sed -i -e 's|#!/usr/bin/env python|#!%{__python3}|' \
   %{buildroot}%{_bindir}/debrepodiff

%files -n python3-%{srcname}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/debrepodiff


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-11
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-9
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.0.3-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.3-6
- Fix py2 chardet requirement

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.3-4
- BR python-setuptools on el7

* Mon Jul 10 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.3-3
- BR python2-setuptools

* Thu Jul 06 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.3-2
- Drop duplicate BuildRequires: python2-devel
- Use %%global macro instead of %%define

* Mon Jul 03 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.3-1
- Update to latest upstream release
- Drop Requires: python3
- Require chardet
- Include LICENSE.rst
- More precise sitelib contents

* Mon Mar 13 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.1-1
- initial package
