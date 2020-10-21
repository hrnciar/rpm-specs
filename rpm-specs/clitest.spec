%global forgeurl https://github.com/aureliojargas/clitest
%global tag %{version}

Name:    clitest
Version: 0.4.0
Release: 2%{?dist}
Summary: Command Line Tester

License: MIT
URL:     %{forgeurl}

%forgemeta
Source:  %{forgesource}

BuildArch:     noarch
BuildRequires: /usr/bin/perl
BuildRequires: bash dash mksh zsh

Requires: diffutils
Requires: sed
Requires: grep
Suggests: perl

%description
clitest is a portable POSIX shell script that performs automatic testing in \
Unix command lines.

It's the same concept as in Python's doctest module: you document both the \
commands and their expected output, using the familiar interactive prompt \
format, and a specialized tool tests them.

%prep
%forgesetup

%build
#no build, only shell script

%check
make test docker_run=

%install
install -D -m755 -p clitest %{buildroot}%{_bindir}/clitest

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/clitest


%changelog
* Sun Oct 04 2020 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-2
- Added runtime dependencies

* Fri Oct 02 2020 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-1
- Initial package
