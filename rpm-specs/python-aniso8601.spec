%global srcname aniso8601
%global sum Another ISO 8601 parser for Python

Name:           python-%{srcname}
Version:        8.0.0
Release:        3%{?dist}
Summary:        %{sum}

License:        GPLv3+
URL:            https://bitbucket.org/nielsenb/%{srcname}
Source0:        https://pypi.io/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel python3-dateutil

%description
Python library for parsing date strings
in ISO 8601 format into datetime format.

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       python3-dateutil
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python 3 library for parsing date strings
in ISO 8601 format into datetime format.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m unittest discover aniso8601/tests/

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 František Zatloukal <fzatlouk@redhat.com> - 8.0.0-1
- New upstream release 8.0.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 7.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 František Zatloukal <fzatlouk@redhat.com> - 7.0.0-1
- New upstream release 7.0.0

* Mon Mar 11 2019 František Zatloukal <fzatlouk@redhat.com> - 6.0.0-1
- New upstream release 6.0.0

* Sat Mar 02 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.1.0-1
- Update to upstream 5.1.0 release

* Tue Feb 12 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.1.0-1
- Update to upstream 4.1.0 release
- Drop Python 2 support

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.7

* Fri Jun 01 2018 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.0.0-1
- Update to latest upstream (rhbz#1447152)

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Ralph Bean <rbean@redhat.com> - 1.2.0-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 11 2015 Jan Sedlak <jsedlak@redhat.com> - 1.1.0-1
- update to 1.1.0, rebuild with Python 3

* Wed Jul 08 2015 Jan Sedlak <jsedlak@redhat.com> - 1.0.0-1
- update to newest version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.82-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu May 22 2014 Jan Sedlak <jsedlak@redhat.com> - 0.82-2
- disabled tests for EL6

* Wed Jan 22 2014 Jan Sedlak <jsedlak@redhat.com> - 0.82-1
- initial packaging
