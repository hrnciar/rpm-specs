%global forgeurl https://github.com/fboender/multi-git-status
Version:         2.0

%forgemeta

Name:            multi-git-status
Release:         1%{?dist}
Summary:         Show uncommitted, untracked and unpushed changes for multiple Git repos
URL:             %{forgeurl}
# Ideally this would be %{forgesource} but the upstream is doing something different
Source:          https://github.com/fboender/multi-git-status/archive/%{version}.tar.gz
License:         MIT
BuildArch:       noarch

BuildRequires:   ShellCheck
Requires:        coreutils
Requires:        findutils
Requires:        gawk
Requires:        git
Requires:        sed

%description
Show uncommitted, untracked and unpushed changes for multiple Git repos.

multi-git-status shows:
* Uncommitted changes if there are unstaged or uncommitted changes on the
  checked out branch.
* Untracked files if there are untracked files which are not ignored.
* Needs push (BRANCH) if the branch is tracking a (remote) branch which is
  behind.
* Needs upstream (BRANCH) if a branch does not have a local or remote
  upstream branch configured. Changes in the branch may otherwise
  never be pushed or merged.
* Needs pull (BRANCH) if the branch is tracking a (remote) branch which is
  ahead. This requires that the local git repo already knows about the remote
  changes (i.e. you've done a fetch), or that you specify the -f option.
  Multi-git-status does NOT contact the remote by default.
* X stashes if there are stashes.

%prep
%forgesetup

%build

%install
install -p -D -m755 mgitstatus %{buildroot}%{_bindir}/mgitstatus
install -p -D -m755 mgitstatus.1 %{buildroot}%{_mandir}/man1/mgitstatus.1

%check
bash -c ". build.sla && test"

%files
%{_bindir}/mgitstatus
%license LICENSE.txt
%doc README.md
%doc screenshot.png
%doc %{_mandir}/man1/mgitstatus.1*

%changelog
* Thu May 21 2020 Brian (bex) Exelbierd <bex@pobox.com> - 2.0-1
* New Version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Brian (bex) Exelbierd <bex@pobox.com> - 1.0-1
* New Version

* Sat Jul 27 2019 Brian (bex) Exelbierd <bex@pobox.com> - 1.0-1.20190728git2e6049d
- Initial package
