%global srcname sexpdata

%global _description %{expand:sexpdata is a simple S-expression parser/serializer. It has simple load and dump
functions like pickle, json or PyYAML module.}


Name:           python-%{srcname}
Version:        0.0.3
Release:        1%{?dist}
Summary:        S-expression parser for Python

License:        BSD
URL:            https://sexpdata.readthedocs.io/
Source0:        https://github.com/jd-boyd/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist setuptools}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install


%check
pytest


%files -n python3-%{srcname}
%doc README.rst
%pycached %{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}-*.egg-info


%changelog
* Mon Aug 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.3-1
- Initial RPM release
