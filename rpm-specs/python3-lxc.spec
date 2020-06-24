Name:           python3-lxc
Version:        3.0.4
Release:        6%{?dist}
Summary:        Python binding for LXC
License:        LGPLv2+
URL:            https://linuxcontainers.org/lxc
Source0:        https://linuxcontainers.org/downloads/lxc/%{name}-%{version}.tar.gz
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  lxc-devel >= 3.0.0
BuildRequires:  pkgconfig
BuildRequires:  gcc

%global desc Linux Resource Containers provide process and resource isolation\
without the overhead of full virtualization.\
\
The python%{python3_pkgversion}-lxc package contains the Python3\
binding for LXC.

%description
%{desc}


%if 0%{?python3_pkgversion} != 3
%global subpkg -n python%{python3_pkgversion}-lxc
%package %{?subpkg}
Summary: Python binding for LXC

%description %{?subpkg}
%{desc}
%endif


%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}_lxc\\..*\\.so


%prep
%autosetup


%build
%py3_build


%install
%py3_install

# fix examples
chmod -x examples/*.py
sed -i -e '1 s@^#!.*@#!%{__python3}@' examples/*.py


%check
%{__python3} setup.py test


%files %{?subpkg}
%license COPYING
%doc README.md examples
%{python3_sitearch}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul  7 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.4-1
- Update to 3.0.4.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.3-1
- Update to 3.0.3.

* Sun Aug 19 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.2-1
- Update to 3.0.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-3
- Rebuilt for Python 3.7

* Fri Apr  6 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.1-2
- Update BRs.

* Fri Apr  6 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.1-1
- New package.
