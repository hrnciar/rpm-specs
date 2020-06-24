%global srcname colcon-cd

Name:           python-%{srcname}
Version:        0.1.1
Release:        5%{?dist}
Summary:        Extension for colcon to change the current working directory

License:        ASL 2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

# Not submitted upstream
Patch0:         %{name}-0.1.1-install-data-files-manually.patch

%description
A shell function for colcon-core to change the current working directory.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.4.1
Requires:       python%{python3_pkgversion}-colcon-package-information
%endif # __pythondist_requires

%description -n python%{python3_pkgversion}-%{srcname}
A shell function for colcon-core to change the current working directory.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install

install -p -D function/colcon_cd.sh %{buildroot}%{_datadir}/colcon_cd/function/colcon_cd.sh


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_cd/
%{python3_sitelib}/colcon_cd-%{version}-py%{python3_version}.egg-info/
%{_datadir}/colcon_cd/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Scott K Logan <logans@cottsay.net> - 0.1.1-3
- Install files to %%{_datadir} manually for older setuptools compat

* Wed Oct 30 2019 Scott K Logan <logans@cottsay.net> - 0.1.1-2
- Fix ownership of %%{_datadir}/colcon_cd

* Wed Oct 30 2019 Scott K Logan <logans@cottsay.net> - 0.1.1-1
- Initial package
