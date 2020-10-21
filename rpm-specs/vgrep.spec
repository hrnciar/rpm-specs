# https://github.com/vrothberg/vgrep
%global goipath         github.com/vrothberg/vgrep
Version:                2.4.0

%gometa

%global common_description %{expand:
vgrep is a pager for grep, git-grep, ripgrep and similar grep implementations,
and allows for opening the indexed file locations in a user-specified editor
such as vim or emacs. vgrep is inspired by the ancient cgvg scripts but
extended to perform further operations such as listing statistics of files and
directory trees or showing the context lines before and after the matches.}

%global golicenses      LICENSE
%global godocs          README.md

%bcond_without check

Name:           vgrep
Release:        1%{?dist}
Summary:        User-friendly pager for grep
License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/mattn/go-shellwords)
BuildRequires:  golang(github.com/nightlyone/lockfile)
BuildRequires:  golang(github.com/peterh/liner)
BuildRequires:  golang(github.com/sirupsen/logrus)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
export LDFLAGS="-X main.version=%{version} "
%gobuild -o %{gobuilddir}/bin/vgrep %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/vgrep

%gopkgfiles

%changelog
* Tue Aug 18 2020 Carl George <carl@george.computer> - 2.4.0-1
- Latest upstream

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Carl George <carl@george.computer> - 2.3.3-1
- Latest upstream

* Wed Jul 01 2020 Carl George <carl@george.computer> - 2.3.1-2
- Embed version into binary

* Mon Jun 29 2020 Carl George <carl@george.computer> - 2.3.1-1
- Initial package
