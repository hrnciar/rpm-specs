%global pypi_name WSGIProxy2
%global package_name wsgiproxy

Name:           python-%{pypi_name}
Version:        0.4.6
Release:        5%{?dist}
Summary:        WSGI Proxy that supports several HTTP backends

License:        MIT
URL:            https://github.com/gawel/WSGIProxy2/
Source0:        https://pypi.python.org/packages/source/W/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%global _description\
WSGI Proxy that supports several HTTP backends.

%description %_description

%package -n     python3-%{pypi_name}
Summary:        WSGI Proxy that supports several HTTP backends
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-webob
Requires:       python3-six
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

Python 3 version.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README_fixt.py README.rst
%{python3_sitelib}/%{package_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.4.6-2
- Removed python2 support (BZ#1747976)

* Mon Aug 26 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.4.6-1
- Update to upstream

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.4.1-10
- Modernize spec
- Get back old name

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.1-9
- Python 2 binary package renamed to python2-wsgiproxy2
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 05 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.1-1
- Initial package.
