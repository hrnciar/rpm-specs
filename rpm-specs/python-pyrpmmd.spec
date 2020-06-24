%global srcname pyrpmmd

%global sum Python module for reading rpm-md repo data

%global desc \
pyrpmmd is an independent Python module for reading \
rpm-md repository metadata. The code is derived from \
the repomd parsing code from Yum.


Name:           python-%{srcname}
Version:        0.1.1
Release:        12%{?dist}
Summary:        %{sum}

License:        GPLv2+
URL:            https://pagure.io/%{srcname}
Source0:        https://releases.pagure.org/%{srcname}/%{srcname}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description %{desc}


%package     -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-six

%description -n python3-%{srcname} %{desc}

This package provides the Python 3 version.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license COPYING
%doc README.md ChangeLog
%{python3_sitelib}/rpmmd/
%{python3_sitelib}/%{srcname}-%{version}*/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-6
- Remove remaining bits of Python 2 legacy

* Wed Oct 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-5
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 12 2017 Neal Gompa <ngompa13@gmail.com> - 0.1.1
- Update to 0.1.1

* Sun May 14 2017 Neal Gompa <ngompa13@gmail.com> - 0.1.0
- Initial packaging
