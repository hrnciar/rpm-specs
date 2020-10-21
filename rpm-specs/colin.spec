%global pypi_name colin

%{?python_enable_dependency_generator}

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

Name:           %{pypi_name}
Version:        0.3.1
Release:        10%{?dist}
Summary:        Tool to check generic rules/best-practices for containers/images/dockerfiles.

License:        GPLv3+
URL:            https://github.com/user-cont/colin
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0001:      0001-Utils-Add-decorator-for-retry.patch

BuildArch:      noarch
Requires:       python3-%{pypi_name}

%description
`colin` is a tool to check generic rules/best-practices
for containers/images/dockerfiles

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Recommends:     moby-engine
Recommends:     atomic

%description -n python3-%{pypi_name}
`colin` as a tool to check generic rules/best-practices
for containers/images/dockerfiles

%package doc
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
Summary:        colin documentation

%description doc
Documentation for colin

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

# generate html docs
PYTHONPATH="${PWD}:${PWD}/docs/" sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files
%license LICENSE
%{_bindir}/%{pypi_name}
%{_datadir}/bash-completion/completions/%{pypi_name}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{_datadir}/%{pypi_name}/
%exclude %{python3_sitelib}/tests

%files doc
%license LICENSE
%doc html

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Lukas Slebodnik <lslebodn@fedoraproject.org> 0.3.1-4
- Change weak dependency in rawhide (docker -> moby-engine)

* Wed May 01 2019 Lukas Slebodnik <lslebodn@fedoraproject.org> 0.3.1-3
- rhbz#1684558 - Remove hard dependency on docker

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Tomas Tomecek <nereone@gmail.com> 0.3.1-1
- 0.3.1 release

* Thu Nov 15 2018 lachmanfrantisek <lachmanfrantisek@gmail.com> 0.3.0-1
- 0.3.0 release

* Mon Oct 22 2018 lachmanfrantisek <lachmanfrantisek@gmail.com> 0.2.1-1
- 0.2.1 release

* Wed Sep 19 2018 Jiri Popelka <jpopelka@redhat.com> 0.2.0-1
- 0.2.0 release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.7

* Wed May 30 2018 Jiri Popelka <jpopelka@redhat.com> 0.1.0-1
- 0.1.0 release

* Wed May 02 2018 Petr Hracek <phracek@redhat.com> - 0.0.4-3
- Polishing texts and remove leftovers (#1572084)

* Wed May 02 2018 Petr Hracek <phracek@redhat.com> - 0.0.4-2
- Fix issues catched by BZ review process (#1572084)

* Wed Apr 25 2018 lachmanfrantisek <flachman@redhat.com> - 0.0.4-1
- bash completion
- better cli
- better ruleset files and loading
- dockerfile support
- python2 compatibility
- better error handling

* Mon Apr 09 2018 Petr Hracek <phracek@redhat.com> - 0.0.3-1
- Initial package.
