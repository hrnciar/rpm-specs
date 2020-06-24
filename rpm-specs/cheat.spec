%global sheets_commit 18c937413ef9108342c5ca671c3e68118d20ae51
%global sheets_commit_short 18c9374

# https://github.com/cheat/cheat
%global goipath         github.com/cheat/cheat
Version:                3.6.0
%global tag             3.6.0

%gometa

%global common_description %{expand:
Cheat allows you to create and view interactive cheatsheets on the command-
line. It was designed to help remind *nix system administrators of options for
commands that they use frequently, but not frequently enough to remember.}

%global golicenses      LICENSE.txt
%global godocs          README.md CONTRIBUTING.md cmd/cheat/docopt.txt

Name:           cheat
Release:        1%{?dist}
Summary:        Help for various commands and their use cases

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        https://github.com/cheat/cheatsheets/archive/%{sheets_commit_short}.tar.gz#/cheatsheets.tar.gz
Patch1:         cheat-3.6.0-config.patch

BuildRequires:  golang(github.com/alecthomas/chroma/quick)
BuildRequires:  golang(github.com/docopt/docopt-go)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/mgutz/ansi)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(gopkg.in/yaml.v1)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)

Recommends:     cheat-community-cheatsheets

%description
%{common_description}

# We wont use full versioned dependency because rpmdiff then complains about
# difference between noarch subpackages on different architectures
%package bash-completion
Summary: Bash completion support for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: bash bash-completion

%description bash-completion
Files needed to support bash completion.

%package fish-completion
Summary: Fish completion support for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: fish

%description fish-completion
Files needed to support fish completion.

%package community-cheatsheets
Summary:   Cheatsheets created by comunity for %{name}
URL:       https://github.com/cheat/cheatsheets
License:   CC0
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}
Supplements:  cheat

%description community-cheatsheets
Cheatsheets for various programs created and maintained by the
community.

%gopkg

%prep
%goprep
%patch1 -p1 -b .cheat-conf
tar -xf %{SOURCE1}

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
mkdir -m 0755 -p                            %{buildroot}%{_datadir}/bash-completion/completions
mkdir -m 0755 -p                            %{buildroot}%{_datadir}/fish/vendor_completions.d

install -m 0644 -p scripts/cheat.bash %{buildroot}%{_datadir}/bash-completion/completions/cheat
install -m 0644 -p scripts/cheat.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/cheat.fish

install -m 0755 -vd                         %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/cheat %{buildroot}%{_bindir}/

# Install cheatsheets
mkdir -m 0755 -p %{buildroot}/%{_datadir}/cheat

for sheet in cheatsheets-%{sheets_commit}/* ; do
  install -m 0644 -p $sheet %{buildroot}/%{_datadir}/cheat/
done

mkdir -m 0755 -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -m 0755 -p %{buildroot}%{_sysconfdir}/cheat

%check
%gocheck

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md cmd/cheat/docopt.txt
%{_bindir}/cheat

%files community-cheatsheets
%license cheatsheets-%{sheets_commit}/.github/LICENSE.txt
%dir %{_datadir}/cheat
%{_datadir}/cheat/*

%files bash-completion
%{_datadir}/bash-completion/completions/cheat

%files fish-completion
%{_datadir}/fish/vendor_completions.d/cheat.fish

%gopkgfiles

%changelog
* Thu Jan 30 2020 Tomas Korbar <tkorbar@redhat.com> - 3.6.0-1
- Rebase cheat to version 3.6.0 (#1793381)
- Rebase cheatsheets to commit 18c9374

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Tomas Korbar <tkorbar@redhat.com> - 3.2.2-1
- Rebase cheat to version 3.2.2 (#1786883)

* Mon Dec 16 2019 Tomas Korbar tkorbar@redhat.com - 3.2.1-1
- Rebase cheat to version 3.2.1 (#1771683)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Tomas Korbar <tkorbar@redhat.com> - 2.5.1-3
- Fix typo in fish completions folder
- Related: 1716145

* Wed Jun 12 2019 Tomas Korbar <tkorbar@redhat.com> - 2.5.1-2
- 1716145 - Package autocompletion files for cheat

* Wed Feb 20 2019 Tomas Korbar <tkorbar@redhat.com> - 2.5.1-1
- Specfile changed accordingly to review

* Mon Jan 28 2019 Tomas Korbar tkorbar@redhat.com - 2.5.1-1
- Initial commit of package
