%global srcname colcon-lcov-result

Name:           python-%{srcname}
Version:        0.4.0
Release:        2%{?dist}
Summary:        Extension for colcon to provide test results using LCOV

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to provide aggregate coverage results using LCOV.

LCOV is a graphical front-end for GCC's coverage testing tool gcov, producing
the following coverage metrics:
- Statement coverage
- Function coverage
- Branch coverage


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.5.6
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to provide aggregate coverage results using LCOV.

LCOV is a graphical front-end for GCC's coverage testing tool gcov, producing
the following coverage metrics:
- Statement coverage
- Function coverage
- Branch coverage


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_lcov_result/
%{python3_sitelib}/colcon_lcov_result-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Scott K Logan <logans@cottsay.net> - 0.4.0-1
- Initial package (rhbz#1833741)
