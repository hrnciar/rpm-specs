%global srcname pyinsane2

Name:           python-%{srcname}
Version:        2.0.13
Release:        9%{?dist}
Summary:        Python library to access and use image scanners (Linux/Windows/etc)

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/OpenPaperwork/pyinsane
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  sane-backends
BuildRequires:  sane-backends-drivers-scanners

%global _description \
Python library to access and use image scanners (devices). Works on GNU/Linux \
(Sane), *BSD (Sane), Windows > Vista (WIA 2), MacOSX (Sane), etc.

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose >= 1.0
BuildRequires:  python3-pillow

Requires:       sane-backends
Requires:       python3-pillow

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
nosetests-3


%files -n python3-%{srcname}
%doc README.md ChangeLog
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.13-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.13-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.13-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.13-2
- Drop Python 2 subpackage

* Sun Aug 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.13-1
- Update to latest version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.12-3
- Rebuilt for Python 3.7

* Mon Mar 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.12-2
- Fix permissions and shebang on daemon file.

* Mon Mar 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.12-1
- Update to latest version.

* Sat Feb 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.11-1
- Update to latest version.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 26 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.10-1
- Initial package.
