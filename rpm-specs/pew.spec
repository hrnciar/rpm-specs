%bcond_without check

Name: pew
Version: 1.2.0
Release: 9%{?dist}
Summary: Tool to manage multiple virtualenvs written in pure Python

License: MIT
URL: https://github.com/berdario/pew
Source0: https://github.com/berdario/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: README.md

# This patch removes Python version management on Fedora.
#
# NOTE: This removes the pythonz-bd dependency which is not available in Fedora
# anymore.
# Furthermore, there is strong support upstream to either remove Pew's
# Python version management or replace it with pyenv:
# https://github.com/berdario/pew/issues/195.
Patch0: 0001-Remove-Python-version-management-on-Fedora.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(virtualenv) >= 1.11
BuildRequires: python3dist(virtualenv-clone) >= 0.2.5
# Required for %%autosetup.
BuildRequires:  git-core

%if %{with check}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pip)
%endif

%{?python_provide:%python_provide python3-%{name}}

%description
Python Env Wrapper is a set of commands to manage multiple virtual
environments. Pew can create, delete and copy your environments, using a
single command to switch to them wherever you are, while keeping them in a
single (configurable) location.


%prep
%autosetup -n %{name}-%{version} -N -S git
%if %{without py_ver_management}
%autopatch
%endif

# Rename the Fedora-specific README.md to avoid conflict with the upstream
# README.md.
# NOTE: The source file should stay named README.md so that Pagure renders it
# when one visits https://src.fedoraproject.org/rpms/pew.
mv %{SOURCE1} README.Fedora.md

# This script for shell completion can't be used for Fedora package
rm -rf %{name}/shell_config/complete_deploy


%build
%py3_build


%install
%py3_install


%if %{with check}
%check
PATH=%{buildroot}%{_bindir}:$PATH \
PYTHONPATH=%{buildroot}%{python3_sitelib} \
py.test-3 -v tests
%endif


%files
%license LICENSE
%doc README.md README.Fedora.md
%{_bindir}/pew
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Tadej Janež <tadej.j@nez.si> - 1.2.0-7
- Replace Python version glob with macro to support Python 3.10
- Drop conditionals for EOL Fedora releases

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Tadej Janež <tadej.j@nez.si> 1.2.0-1
- Update to 1.2.0 release
- Drop the tests-connection-marker-fix patch since it has been upstreamed
- Remove Python version management functionality in Fedora 30+
- Use automatic Python dependency generator
- Improve pytest call to not include the current working directory as suggested
  by Zbigniew Jędrzejewski-Szmek:
  https://bugzilla.redhat.com/show_bug.cgi?id=1720757#c1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Michal Cyprian <mcyprian@redhat.com> - 1.1.2-1
- Initial package.
