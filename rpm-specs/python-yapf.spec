%global pypi_name yapf

%global desc %{expand: \
YAPF Introduction Most of the current formatters for Python e.g., autopep8, and
pep8ify are made to remove lint errors from code. This has some obvious
limitations. For instance, code that conforms to the PEP 8 guidelines may not
be}

Name:		python-%{pypi_name}
Version:	0.30.0
Release:	3%{?dist}
Summary:	A formatter for Python code
License:	ASL 2.0
URL:		https://github.com/google/yapf
Source0:	%{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch
 
BuildRequires:	python3-devel
BuildRequires:	python3dist(setuptools)

%description
%{desc}

%package -n	python3-%{pypi_name}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:	python3dist(setuptools)
%description -n	python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

for lib in $(find . -type f -name "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

cp plugins/README.rst README-plugins.rst

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README-plugins.rst README.rst
%{_bindir}/yapf
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/yapftests
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.30.0-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.30.0-1
- New upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.29.0-2
- Rebuild f32

* Mon Dec 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.29.0-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.28.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.28.0-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.28.0-1
- New upstream version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.27.0-1
- New upstream version

* Mon Apr 01 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.26.0-2
- Fix comment #7 BZ #1691609

* Fri Mar 22 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.26.0-1
- Initial package.
