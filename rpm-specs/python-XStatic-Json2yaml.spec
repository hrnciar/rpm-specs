%global pypi_name XStatic-Json2yaml

Name:           python-%{pypi_name}
Version:        0.1.1.0
Release:        9%{?dist}
Summary:        Json2yaml (XStatic packaging standard)

License:        MIT
URL:            https://github.com/jeffsu/json2yaml
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch



%description
Json2yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.


%package -n xstatic-json2yaml-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-json2yaml-common
Json2yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the JavaScript files.


%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-json2yaml-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Json2yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Patch to use webassets directory
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/json2yaml'|" xstatic/pkg/json2yaml/__init__.py


%build
%py3_build


%install
%py3_install

mkdir -p %{buildroot}/%{_jsdir}/json2yaml
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/json2yaml/data/json2yaml.js %{buildroot}/%{_jsdir}/json2yaml
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/json2yaml/data/

%files -n xstatic-json2yaml-common
%doc README.txt
%{_jsdir}/json2yaml

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/json2yaml
%{python3_sitelib}/XStatic_Json2yaml-%{version}-py3.*.egg-info
%{python3_sitelib}/XStatic_Json2yaml-%{version}-py3.*-nspkg.pth


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.1.0-2
- Subpackage python2-XStatic-Json2yaml has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jul 12 2018 Radomir Dopieralski <rdopiera@redhat.com) - 0.1.1.0-1
- Initial package
