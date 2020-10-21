%global srcname sphinxtesters

Name:           python-%{srcname}
Version:        0.2.3
Release:        7%{?dist}
Summary:        Utilities for testing Sphinx extensions

License:        BSD
URL:            https://github.com/matthew-brett/%{srcname}
Source0:        https://github.com/matthew-brett/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(setuptools)

%description
This package contains utilities for testing Sphinx extensions.

%package -n     python3-%{srcname}
Summary:        Utilities for testing Sphinx extensions
Requires:       python3dist(sphinx)

%description -n python3-%{srcname}
This package contains utilities for testing Sphinx extensions.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build
rst2html --no-datestamp README.rst README.html
python3 setup.py build_sphinx
rm -f build/sphinx/html/.{buildinfo,nojekyll}

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest
#PYTHONPATH=$PWD nosetests-%%{python3_version} -v

%files -n python3-%{srcname}
%doc README.html build/sphinx/html
%license LICENSE
%{python3_sitelib}/%{srcname}*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Jerry James <loganjerry@gmail.com> - 0.2.3-4
- Build and ship the documentation
- Ship the README as an html file

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Jerry James <loganjerry@gmail.com> - 0.2.3-1
- New upstream version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Jerry James <loganjerry@gmail.com> - 0.2.1-2
- Drop the python2 subpackage (bz 1653087)

* Wed Aug 29 2018 Jerry James <loganjerry@gmail.com> - 0.2.1-1
- Initial RPM
