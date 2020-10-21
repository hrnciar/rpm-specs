%global pypi_name XStatic-Angular-Bootstrap

Name:           python-%{pypi_name}
Version:        2.2.0.0
Release:        13%{?dist}
Summary:        Angular-Bootstrap (XStatic packaging standard)

License:        MIT
URL:            http://angular-ui.github.io/bootstrap/
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.


%package -n xstatic-angular-bootstrap-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-angular-bootstrap-common
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the javascript files.


%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-angular-bootstrap-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.


%prep
%autosetup -n %{pypi_name}-%{version}

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_bootstrap'|" xstatic/pkg/angular_bootstrap/__init__.py


%build
%py3_build


%install
%py3_install

mkdir -p %{buildroot}%{_jsdir}/angular_bootstrap
mv %{buildroot}%{python3_sitelib}/xstatic/pkg/angular_bootstrap/data/angular-bootstrap.js %{buildroot}%{_jsdir}/angular_bootstrap
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/angular_bootstrap/data/
# fix execute flags for js
chmod 644 %{buildroot}%{_jsdir}/angular_bootstrap/angular-bootstrap.js

%files -n xstatic-angular-bootstrap-common
%doc README.txt
%{_jsdir}/angular_bootstrap

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/angular_bootstrap
%{python3_sitelib}/XStatic_Angular_Bootstrap-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_Angular_Bootstrap-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0.0-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.0.0-6
- Subpackage python2-XStatic-Angular-Bootstrap has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb  6 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 2.2.0.0-1
- Upstream 2.2.0.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.11.0.2-6
- Rebuild for Python 3.6

* Sun Sep 11 2016 Jan Beran <jberan@redhat.com> - 0.11.0.2-5
- Provides a Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 10 2015 Matthias Runge <mrunge@redhat.com> - 0.11.0.2-1
- Initial package (rhbz#1180803)


