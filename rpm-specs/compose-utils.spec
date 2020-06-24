Name:       compose-utils
Version:    0.1.42
Release:    2%{?dist}
Summary:    Utilities for working with composes

License:    GPLv2
URL:        https://pagure.io/compose-utils
Source0:    https://pagure.io/releases/compose-utils/%{name}-%{version}.tar.bz2
%if 0%{?fedora} < 31
Patch0:     0001-Revert-Update-for-newer-RPM.patch
%endif

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-productmd >= 1.1
BuildRequires:  python%{python3_pkgversion}-freezegun
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-kobo
%if 0%{?fedora} >= 31
BuildRequires:  python%{python3_pkgversion}-kobo-rpmlib >= 0.10.0
%else
BuildRequires:  python%{python3_pkgversion}-kobo-rpmlib
%endif
BuildRequires:  python%{python3_pkgversion}-nose
Requires:       python3-%{name} = %{version}-%{release}

BuildArch:  noarch

%description
A set of tools for working with composes produced by pungi.


%package -n python%{python3_pkgversion}-%{name}
Summary:    Python 3 libraries supporting tools for working with composes
Requires:   python%{python3_pkgversion}-productmd >= 1.1
Requires:   python%{python3_pkgversion}-kobo
%if 0%{?fedora} >= 31
Requires:   python%{python3_pkgversion}-kobo-rpmlib >= 0.10.0
%else
Requires:   python%{python3_pkgversion}-kobo-rpmlib
%endif
Requires:   rsync
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description -n python%{python3_pkgversion}-%{name}
Python 3 libraries supporting tools for working with composes


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files
%license COPYING GPL
%doc AUTHORS README.rst
%{_bindir}/*
%{_mandir}/man1/*

%files -n python%{python3_pkgversion}-%{name}
%license COPYING GPL
%doc AUTHORS README.rst
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.42-2
- Rebuilt for Python 3.9

* Tue May 05 2020 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.42-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.37-1
- New upstream release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.34-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.34-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.34-1
- New upstream release

* Fri Jun 07 2019 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.32-1
- New upstream release

* Tue Jun 04 2019 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.31-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.27-1
- New upstream release

* Mon Oct 15 2018 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.26-1
- New upstream release

* Tue Aug 28 2018 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.25-1
- New upstream release

* Tue Aug 14 2018 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.24-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.23-1
- New upstream release

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.21-2
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.21-1
- New upstream release

* Mon Jun 04 2018 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.20-1
- Fix getting changelogs with malformed versions

* Wed May 16 2018 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.19-1
- Fix changelog generation on Python 3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.18-1
- Update packaging for Python 3
- Ignore module build suffix in changelog

* Mon Oct 02 2017 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.17-1
- Fix copying when compose path ends with slash

* Wed Sep 20 2017 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.16-1
- changelog: Extract changelogs from same days
- Fix flaky test for package moves
- changelog: Use format compatible with Py 2.6
- list: refactor sorting composes to a separate method
- changelog: Format all sizes for readability
- Use datetime for getting current date

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.15-1
- Bump dependency on kobo library
- Handle URLs to composes in latest-symlink script

* Wed May 31 2017 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.14-1
- New upstream release 0.1.14

* Tue Apr 25 2017 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.13-1
- Avoid crash on missing paths in composeinfo

* Tue Mar 07 2017 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.12-1
- Fix partial copy to non-existing directory
- Add compose-create-next-dir utility (qwan)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.11-1
- Fix copying disk images

* Wed Oct 26 2016 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.10-1
- Shorten verbose changelog, --full will display everything

* Thu Sep 15 2016 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.9-1
- Add a script to generate legacy .composeinfo file
- Add COMPOSE_ID file to copied part of compose
- Treat source as a separate arch when copying compose

* Mon Aug 29 2016 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.8-1
- New upstream release

* Tue Aug 09 2016 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.7-1
- Add a script to copy part of compose
- Add a script to check packages moved between variants

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 30 2016 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.6-1
- Fix getting SRPM summary

* Tue Apr 19 2016 Lubomír Sedlář <lsedlar@redhat.com> - 0.1.5-1
- Add utility for listing composes
- Display better error messages when changelog fails to find metadata

* Wed Apr 13 2016 Lubomír Sedlář <lubomir.sedlar@gmail.com> - 0.1.4-1
- Add image diff to changelog (Adam Williamson)

* Wed Mar 30 2016 Lubomír Sedlář <lubomir.sedlar@gmail.com> - 0.1.3-1
- Do not crash changelog when composeinfo.json is missing
- Run tests when building package

* Tue Mar 15 2016 Lubomír Sedlář <lubomir.sedlar@gmail.com> - 0.1.2-1
- Correctly handle epochs

* Thu Feb 25 2016 Lubomír Sedlář <lubomir.sedlar@gmail.com> - 0.1.1-1
- Fix wrong address in license

* Thu Feb 25 2016 Lubomír Sedlář <lubomir.sedlar@gmail.com> - 0.1.0-1
- Initial packaging
