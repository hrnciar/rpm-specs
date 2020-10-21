%global rpmname debianbts
%global pypi_name python-debianbts

Name:           %{pypi_name}
Version:        2.8.2
Release:        4%{?dist}
Summary:        Python interface to Debian's Bug Tracking System

License:        MIT
URL:            https://github.com/venthur/python-debianbts
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/venthur/python-debianbts/master/LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)

%description
Python-debianbts is a Python library that allows for querying
Debian's Bug Tracking System.

%package -n     python3-%{rpmname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{rpmname}}

Requires:       python3dist(mock)
Requires:       python3dist(pysimplesoap)
Requires:       python3dist(setuptools)

%description -n python3-%{rpmname}
python-debianbts is a Python library that allows for querying
Debian's Bug Tracking System.

%prep
%autosetup -n %{pypi_name}-%{version}
for lib in debianbts/*.py; do
 sed -e '1{\@^#! /usr/bin/env python@d}' -e '1{\@^#!/usr/bin/env python@d}' \
     -e '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
cp -p %{SOURCE1} .

# Remove bundled egg-info
#rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{rpmname}
%doc README.md
%license LICENSE
%{_bindir}/debianbts
%{python3_sitelib}/debianbts
%{python3_sitelib}/python_debianbts-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 2.8.2-1
- Initial package.
