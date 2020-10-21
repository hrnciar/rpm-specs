Summary: Git commit message linting tool
Name: gitlint
Version: 0.13.1
Release: 1%{?dist}
License: MIT
Source: %pypi_source
Patch0: strict-dependencies.patch
URL: https://jorisroovers.github.io/gitlint
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: %{py3_dist Click} >= 7.0.0
BuildRequires: %{py3_dist arrow} >= 0.15.5
BuildRequires: %{py3_dist sh} >= 1.12.14
BuildRequires: git-core
Requires: git-core

%description
gitlint checks git commit messages for style, using validations based on
well-known community standards or on checks which have proved useful:
maximum title length, trailing white-space checks, punctuation, tabs,
minimum body length, valid email addresses...

%prep
%autosetup -p1

%build
%py3_build

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/
%{_bindir}/gitlint

%changelog
* Mon Sep 14 2020 Stephen Kitt <skitt@fedoraproject.org> - 0.13.1-1
- initial package
