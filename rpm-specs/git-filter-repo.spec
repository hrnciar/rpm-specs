%global gitexecdir %{_libexecdir}/git-core

Name:           git-filter-repo
Version:        2.27.0
Release:        1%{?dist}
Summary:        Quickly rewrite git repository history (git-filter-branch replacement)
License:        MIT
Group:          Development/Tools/Version Control
Url:            https://github.com/newren/git-filter-repo
#
Source0:        https://github.com/newren/git-filter-repo/releases/download/v%{version}/%{name}-%{version}.tar.xz
#
BuildArch:      noarch
#
BuildRequires:  git >= 2.26.0
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
#
Requires:       git >= 2.26.0

%description
git filter-repo is a versatile tool for rewriting history, which includes
capabilities not found anywhere else. It roughly falls into the same space of
tool as git filter-branch but without the capitulation-inducing poor
performance, with far more capabilities, and with a design that scales
usability-wise beyond trivial rewriting cases.

%prep
%autosetup -p1

# Change shebang in all relevant files in this directory and all subdirectories
find -type f -exec sed -i '1s=^#!%{_bindir}/\(python\|env python\)[23]\?=#!%{_bindir}/python3=' {} +

%build

%install
install -d -m 0755 %{buildroot}%{gitexecdir}
install -m 0755 git-filter-repo %{buildroot}%{gitexecdir}/git-filter-repo

install -d -m 0755 %{buildroot}%{python3_sitelib}
ln -sf %{gitexecdir}/git-filter-repo %{buildroot}%{python3_sitelib}/git_filter_repo.py

install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 Documentation/man1/git-filter-repo.1 %{buildroot}%{_mandir}/man1/git-filter-repo.1

%files
%license COPYING
%doc README.md contrib/filter-repo-demos
%{gitexecdir}/git-filter-repo
%{python3_sitelib}/git_filter_repo.py
%{_mandir}/man1/git-filter-repo.1*

%changelog
* Tue Jun 02 2020 Andreas Schneider <asn@redhat.com> - 2.27.0-1
- Update to version 2.27.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.25.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Andreas Schneider <asn@redhat.com> - 2.25.0-4
- Add missing BR for python3-rpm-macros

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Andreas Schneider <asn@redhat.com> - 2.25.0-1
- Update to version 2.25.0
- Fix installation to python3 sitelib

* Fri Dec 20 2019 Andreas Schneider <asn@redhat.com> - 2.24.0-2
- Fixed source tarball permissions
- Fixed souperfluous space in Summary

* Thu Dec 19 2019 Andreas Schneider <asn@redhat.com> - 2.24.0-1
- Initial version 2.24.0
