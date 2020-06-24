# Enabled by default
# If the package needs to download data for the test which cannot be done in
# koji, these can be disabled in koji by using `bcond_with` instead, but the
# tests must be validated in mock with network enabled like so:
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enable-network --rpmbuild-opts="--with tests"
%bcond_with tests

%global desc %{expand: \
wxnatpy is a wxPython widget which allows users to browse the contents of a XNAT repository.
It is built on top of wxPython and xnatpy.}

%global pypi_name wxnatpy

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        3%{?dist}
Summary:        wxnatpy is a wxPython widget which allows users to browse the contents of a XNAT repository.
License:        ASL 2.0
URL:            https://github.com/pauldmccarthy/wxnatpy
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wxpython4
BuildRequires:  python3-xnat
BuildRequires:  python3-fsleyes-widgets

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

#%check
#%{__python3} setup.py test
 
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/wxnat/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.3.2-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.3.11-2
- enable xnat

* Mon Nov 19 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.3.11-1
- New upstream
