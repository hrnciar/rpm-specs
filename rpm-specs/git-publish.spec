Name:           git-publish
Version:        1.6.1
Release:        1%{?dist}
Summary:        Prepare and store patch revisions as git tags
License:        MIT
URL:            https://github.com/stefanha/git-publish
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%if (0%{?rhel} && 0%{?rhel} <= 7)
BuildRequires:  python2-devel
%else
BuildRequires:  python3-devel
%endif
BuildRequires:  perl-podlators
Requires:       git-core git-email

%description
git-publish handles repetitive and time-consuming details of managing patch
email submission.  It works with individual patches as well as patch series and
has support for pull request emails.

Each revision is stored as a git tag including the cover letter (if any).  This
makes it easy to refer back to previous revisions of a patch.  Numbering is
handled automatically and the To:/Cc: email addresses are remembered across
revisions to save you retyping them.

Many projects have conventions for submitting patches.  It is possible to
encode them as a .gitpublish file and hooks/ scripts.  This automatically uses
the right settings and can run a coding style checker or linting tools before
emails are sent.

%prep
%autosetup

# Force Python 3 in recent distros
# https://fedoraproject.org/wiki/Packaging:Python#Multiple_Python_Runtimes
%if ! (0%{?rhel} && 0%{?rhel} <= 7)
sed -i '1c #!%{__python3}' git-publish
%endif

%build
pod2man --center "git-publish Documentation" --release "%{version}" git-publish.pod git-publish.1

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/git-publish/hooks
install -p -m 755 git-publish %{buildroot}%{_bindir}/
install -p -m 644 git-publish.1 %{buildroot}%{_mandir}/man1/
install -p -m 644 hooks/pre-publish-send-email.example %{buildroot}%{_datadir}/git-publish/hooks/

%files
%license LICENSE
%_bindir/git-publish
%_mandir/man1/git-publish.1*
%_datadir/git-publish/hooks/pre-publish-send-email.example

%changelog
* Mon Mar 30 2020 Stefan Hajnoczi <stefanha@gmail.com> - 1.6.1-1
- Fix Subject: line wrap
- Use --batch-size when using --relogin-delay

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 3 2020 Stefan Hajnoczi <stefanha@gmail.com> - 1.6.0-1
- Add --add-header option for adding git-format-patch(1) email headers
- Allow git-publish --edit during rebase
- Fix --keyid for specifying a GPG key
- Fix --edit in worktree
- Fix configuration file precedence (.gitpublish, .git/config, ~/.gitconfig)
- Fix --no-cover-letter with empty tag messages
- Python 3 fixes

* Thu Oct 3 2019 Stefan Hajnoczi <stefanha@gmail.com> - 1.5.1-1
- Fix always-on --no-binary parameter
- Include git command-line in error messages
- Print git-format-patch(1) errors
- Print an error when publishing a base branch (like 'master')

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Stefan Hajnoczi <stefanha@gmail.com> - 1.5.0-1
- Add --keyid parameter
- Add --no-binary parameter
- Fix character set issues by honoring the local encoding

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Stefan Hajnoczi <stefanha@gmail.com> - 1.4.4-4
- Add missing git-email package dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.4-2
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Stefan Hajnoczi <stefanha@gmail.com> - 1.4.4-1
- Merge To: list but offer --override-to to stop this behavior
- Add --blurb-template for cover-letter templates
- Pass through extra arguments to git-format-patch(1)
- Add missing UTF-8 encoding for 's'elect menu item
- Don't treat config strings as lists in Python 3

* Wed Apr 18 2018 Stefan Hajnoczi <stefanha@gmail.com> - 1.4.3-1
- Add 's' menu command to select a subset of patches to send
- Use UTF-8 encoding for annotated tags
- Use a cover letter by default for pull requests
- Convert README.rst to git-publish.pod man page
- Add --no-sign-pull option to skip pull request signing
- Run cccmd in the top-level directory
- Show meaningful error message when run outside top-level directory

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 8 2017 Stefan Hajnoczi <stefanha@gmail.com> - 1.4.2-2
- Add missing BuildRequires: pythonX-devel

* Mon Nov 6 2017 Stefan Hajnoczi <stefanha@gmail.com> - 1.4.2-1
- Further Python 2 & 3 character encoding fixes

* Sat Nov 4 2017 Stefan Hajnoczi <stefanha@gmail.com> - 1.4.1-1
- Fix UTF-8 output from git(1) commands

* Thu Nov 2 2017 Stefan Hajnoczi <stefanha@gmail.com> - 1.4-1
- Python 3 support
- Report unexpected changes to temporary directory
- Fix broken hooks path function

* Mon Aug 21 2017 Stefan Hajnoczi <stefanha@gmail.com> - 1.3-1
- Add 'e' menu command to edit patches
- Add --notes options for git-notes(1) users
- Replace DEBUG with -v/--verbose option
- Fix git_config_with_profile() profile variable lookup
- Fix --pull-request error when remote cannot be determined
- Support worktrees when invoking hooks
- Improve git error handling

* Wed Mar 1 2017 Stefan Hajnoczi <stefanha@gmail.com> - 1.2-1
- Honor git-config(1) pushDefault/pushRemote options
- Display git-send-email(1) CC list before sending
- Fix git-publish --setup when run outside of a git repo

* Fri Dec 9 2016 Stefan Hajnoczi <stefanha@gmail.com> - 1.1-1
- git-publish 1.1
