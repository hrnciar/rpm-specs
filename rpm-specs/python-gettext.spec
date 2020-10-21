%global module	gettext

Name:		python-%{module}
Version:	4.0
Release:	1%{?dist}
Summary:	Python Gettext po to mo file compiler
License:	BSD

URL:		https://pypi.org/project/python-gettext/
Source0:	%{pypi_source %{name}}
BuildArch:	noarch

%description
This implementation of Gettext for Python includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.

%package -n	python3-%{module}
Summary:	Python 3 Gettext po to mo file compiler
BuildRequires:	python3-devel
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
This implementation of Gettext for Python 3 includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.

%prep
%autosetup -p1

# Remove bundled egg-info
rm -rf python_gettext.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python3_sitelib}/pythongettext/
%{python3_sitelib}/python_gettext-%{version}-py%{python3_version}.egg-info/

%changelog
* Sun Oct 04 2020 Neal Gompa <ngompa13@gmail.com> - 4.0-1
- Initial package


