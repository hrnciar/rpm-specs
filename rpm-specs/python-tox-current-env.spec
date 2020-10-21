%global pypi_name tox-current-env
%global pypi_under tox_current_env

Name:           python-%{pypi_name}
Version:        0.0.3
Release:        1%{?dist}
Summary:        Tox plugin to run tests in current Python environment

License:        MIT
URL:            https://github.com/fedora-python/tox-current-env
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%description
The tox-current-env plugin allows to run tests in current Python environment.


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
The tox-current-env plugin allows to run tests in current Python environment.


%prep
%autosetup -n %{pypi_name}-%{version}


%generate_buildrequires
# Don't use %%pyproject_buildrequires -t/-e to avoid a build dependency loop
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


#check
# the tests currently only work within actual tox and with various Python
# versions installed, so we skip them.


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_under}/
%{python3_sitelib}/%{pypi_under}-%{version}.dist-info/


%changelog
* Wed Sep 30 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-1
- Update to 0.0.3

* Wed Aug 12 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-7
- Fix FTBFS with pyproject-rpm-macros >= 0-23

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-2
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-1
- Update to 0.0.2

* Wed Jul 24 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-1
- Initial package
