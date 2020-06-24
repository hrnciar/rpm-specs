%global srcname colcon-coveragepy-result

Name:           python-%{srcname}
Version:        0.0.5
Release:        2%{?dist}
Summary:        Extension for colcon to collect coverage.py results

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A colcon extension for collecting coverage.py results.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core
Requires:       python%{python3_pkgversion}-coverage
%endif

%description -n python%{python3_pkgversion}-%{srcname}
A colcon extension for collecting coverage.py results.


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
%doc README.md
%{python3_sitelib}/colcon_coveragepy_result/
%{python3_sitelib}/colcon_coveragepy_result-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.5-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Scott K Logan <logans@cottsay.net> - 0.0.5-1
- Update to 0.0.5

* Mon May 11 2020 Scott K Logan <logans@cottsay.net> - 0.0.3-1
- Initial package (rhbz#1834496)
