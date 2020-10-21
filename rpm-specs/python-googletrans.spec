%global         pypi_name googletrans

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        2%{?dist}
Summary:        Google Translate API for Python

License:        MIT
URL:            https://py-googletrans.readthedocs.io/en/latest/
Source0:        %{pypi_source}
Patch0:			googletrans-relax-dependency-requirements.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(httpx)

%global _description %{expand:
Googletrans is a free and unlimited python library that implemented Google
Translate API. This uses the Google Translate Ajax API to make calls to such
methods as detect and translate.}

%description %{_description}

%package -n python3-%{pypi_name}
Summary:        Google Translate API for Python

Requires:       python3dist(httpx)

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# This is to avoid a conflict with libtranslate
# See https://github.com/ssut/py-googletrans/issues/231
mv %{buildroot}%{_bindir}/translate %{buildroot}%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info
%{python3_sitelib}/%{pypi_name}/
%{_bindir}/%{pypi_name}

%changelog
* Sun Oct 18 2020 Lyes Saadi <fedora@lyes.eu> - 3.0.0-2
- RHBZ#1889104

* Thu Oct 15 2020 Lyes Saadi <fedora@lyes.eu> - 3.0.0-1
- Unretiring python-googletrans
- Updating to 3.0.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.0-6
- Subpackage python2-googletrans has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 williamjmorenor@gmail.com - 2.2.0-2
- Initial import of BZ#1529026

* Tue Dec 26 2017 williamjmorenor@gmail.com - 2.2.0-1
- Initial packaging
