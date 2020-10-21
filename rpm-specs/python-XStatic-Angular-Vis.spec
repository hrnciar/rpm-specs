%global pypi_name XStatic-Angular-Vis

Name:           python-%{pypi_name}
Version:        4.16.0.0
Release:        9%{?dist}
Summary:        Angular-Vis (XStatic packaging standard)

License:        MIT
URL:            https://github.com/visjs/angular-visjs
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Angular-Vis JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.


%package -n xstatic-angular-vis-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-angular-vis-common
Angular-Vis JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the JavaScript files.


%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-angular-vis-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Angular-Vis JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_vis'|" xstatic/pkg/angular_vis/__init__.py


%build
%py3_build


%install
%py3_install

mkdir -p %{buildroot}/%{_jsdir}/angular_vis
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_vis/data/angular-vis.js %{buildroot}/%{_jsdir}/angular_vis
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/angular_vis/data/

%files -n xstatic-angular-vis-common
%doc README.txt
%{_jsdir}/angular_vis

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/angular_vis
%{python3_sitelib}/XStatic_Angular_Vis-%{version}-py3.*.egg-info
%{python3_sitelib}/XStatic_Angular_Vis-%{version}-py3.*-nspkg.pth

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.16.0.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.16.0.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.16.0.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.16.0.0-2
- Subpackage python2-XStatic-Angular-Vis has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jul 12 2018 Radomir Dopieralski <rdopiera@redhat.com) - 4.16.0.0-1
- Initial package
