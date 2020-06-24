%bcond_without check
%global pypi_name pre-commit

Name:           %{pypi_name}
Version:        2.5.1
Release:        1%{?dist}
Summary:        Framework for managing and maintaining multi-language pre-commit hooks

License:        MIT
URL:            https://pre-commit.com
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel >= 3.6.1
BuildRequires:  python3dist(setuptools)

%if %{with check}
BuildRequires:  git-core
BuildRequires:  python3dist(aspy.yaml)
BuildRequires:  python3dist(cfgv) >= 2.0.0
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(identify) >= 1.0.0
%if 0%{?fedora} <= 31
BuildRequires:  python3dist(importlib-metadata)
%endif
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(nodeenv) >= 0.11.1
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(virtualenv) >= 20
%endif

%?python_enable_dependency_generator

%description
A framework for managing and maintaining multi-language pre-commit hooks.


%prep
%autosetup -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with check}
%check
git init
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
export PYTHONPATH=%{buildroot}%{python3_sitelib}

# Disable few tests
# * 'make_archives_test' and 'repository_test' need a network connection, hence disabled.
# * 'install_uninstall_test' needs pytest-env (currently not packaged)
%{python3} -m pytest -v                                 \
    --deselect tests/make_archives_test.py              \
    --deselect tests/repository_test.py                 \
    --deselect tests/commands/install_uninstall_test.py
%endif


%files
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/%{pypi_name}
%{_bindir}/%{pypi_name}-validate-config
%{_bindir}/%{pypi_name}-validate-manifest
%{python3_sitelib}/pre_commit/
%{python3_sitelib}/pre_commit-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon Jun 22 2020 Lumír Balhar <lbalhar@redhat.com> - 2.5.1-1
- Update to 2.5.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Thu Apr 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Thu Mar 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Mon Feb 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Mon Feb 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Mon Jan 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.21.0-1
- Update to 1.21.0
- Thanks Aniket Pradhan <major AT fedoraproject DOT org> for help with packaging
- Thanks Miro Hrončok <mhroncok@redhat.com> for help with packaging

* Sun Dec 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.20.0-1
- Update to 1.20.0

* Thu Oct 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.18.3-8
- Update to 1.18.3

* Sat Mar 30 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.14.4-1
- Initial package
