%global srcname pymediainfo

Name:           python-%{srcname}
Version:        4.2.1
Release:        2%{?dist}
Summary:        Python wrapper around the MediaInfo library

License:        MIT
URL:            https://github.com/sbraz/%{srcname}
Source0:        https://pypi.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  libmediainfo

%description
%{sum}.

%package     -n python3-%{srcname}
Summary:        Python3 wrapper around the MediaInfo library
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-setuptools_scm
Requires:       libmediainfo
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This small package is a Python3 wrapper around the MediaInfo library.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
export LC_ALL=C.UTF-8
PYTEST_ADDOPTS='-k "not test_parse_url"' %{__python3} setup.py test


%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS README.rst
%{python3_sitelib}/%{srcname}*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 4.2.1-1
- Update to 4.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 4.1-1
- Update to 4.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 05 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 4.0-1
- Update to 4.0

* Thu Apr 04 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.2.1-1
- Update to 3.2.1

* Tue Mar 05 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1-1
- Update to 3.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0-1
- Update to 3.0

* Fri Sep 07 2018 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.0-4
- rebuild for mediainfo 18.08
- drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.7

* Tue May 15 2018 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.0-1
- Update to 2.3.0

* Tue Feb 27 2018 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.1-1
- Update to 2.2.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.0-1
- Initial package
