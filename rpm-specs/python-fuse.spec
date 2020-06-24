%global srcname fusepy

Name:    python-fuse
# TODO rename to python-fusepy
Version: 2.0.4
Release: 16%{?dist}
Summary: Python module that provides a simple interface to FUSE and MacFUSE

License: ISC
URL:     https://github.com/terencehonles/fusepy
Source0: https://github.com/terencehonles/fusepy/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel

%description
fusepy is a Python module that provides a simple interface to FUSE and MacFUSE.
It's just one file and is implemented using ctypes.

%package -n python3-fusepy
Summary: %{summary}
%{?python_provide:%python_provide python3-fuse}
%{?python_provide:%python_provide python3-fusepy}
Provides: python3-fuse = %{version}-%{release}
Obsoletes: python3-fuse < 2.0.4-10
Requires: fuse-libs

%description -n python3-fusepy
fusepy is a Python module that provides a simple interface to FUSE and MacFUSE.
It's just one file and is implemented using ctypes.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-fusepy
%doc README.rst
%{python3_sitelib}/fuse.py
%{python3_sitelib}/fusepy-*egg-info/
%{python3_sitelib}/__pycache__

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-10
- Rename python3-fuse to python3-fusepy
- Drop python2-fuse, that is done by fuse-python SRPM

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-4
- Rebuild for Python 3.6

* Tue Nov 22 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.4-3
- Add fuse-libs dependency

* Mon Oct 17 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.4-2
- Remove unused commit and shortcommit variables
- Change Source0 to download %%{srcname}-%%{version}.tar.gz
- Reuse %%{summary} macro

* Sun Sep 4 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.4-1
- Initial RPM
