%global srcname xmlsec

Name:           python-%{srcname}
Version:        1.3.8
Release:        1%{?dist}
Summary:        Python bindings for the XML Security Library

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pyproject-rpm-macros
BuildRequires:  libxml2-devel >= 2.9.1
BuildRequires:  xmlsec1-devel >= 1.2.18
BuildRequires:  libtool-ltdl-devel

%description
%{summary}.


%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires: libxml2 >= 2.9.1
Requires: xmlsec1 >= 1.2.18
Requires: xmlsec1-openssl
Requires: %{py3_dist lxml}


%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel


%install
%pyproject_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/xmlsec*.so
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}.dist-info/


%changelog
* Mon Jun 1 2020 Martin Kutlak <mkfedora@outlook.com> - 1.3.8-1
- Update spec file
- Update to 1.3.8 (#1838368)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-10
- Rebuilt for Python 3.9

* Wed Feb 12 2020 Ken Dreyer <kdreyer@redhat.com> - 1.3.3-9
- pkgconfig is only a build-time dependency (rhbz#1789152)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.3-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.3.3-1
- Initial package.
