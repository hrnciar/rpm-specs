%global srcname Deprecated
%global pkgname deprecated

Name:           python-%{pkgname}
Version:        1.2.10
Release:        1%{?dist}
Summary:        Python decorator to deprecate old python classes, functions or methods
License:        MIT
URL:            https://github.com/tantale/%{pkgname}
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python @deprecated decorator to deprecate old python classes,
functions or methods.

%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
Python @deprecated decorator to deprecate old python classes,
functions or methods.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{pkgname}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkgname}
%license LICENSE.rst
%doc README.md
%{python3_sitelib}/%{pkgname}/
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info/


%changelog
* Fri Aug 07 2020 Hunor Csomortáni <csomh@redhat.com> - 1.2.10-1
- new upstream release: 1.2.10

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-4
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Petr Hracek <phracek@redhat.com> - 1.2.6-3
- Enable python dependency generator

* Fri Jul 26 2019 Petr Hracek <phracek@redhat.com> - 1.2.6-2
- Fix python3_sitelib issue

* Fri Jul 26 2019 Petr Hracek <phracek@redhat.com> - 1.2.6-1
- Initial package
