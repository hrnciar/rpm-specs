# Generated by go2rpm 1
%bcond_without check

# https://github.com/aaronjanse/3mux
%global goipath         github.com/aaronjanse/3mux
Version:                1.0.1

%gometa

%global common_description %{expand:
Terminal multiplexer inspired by i3.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           3mux
Release:        1%{?dist}
Summary:        Terminal multiplexer inspired by i3

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/aaronjanse/pty)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/BurntSushi/xdg)
BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(github.com/npat-efault/poller)
BuildRequires:  golang(github.com/sevlyar/go-daemon)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/text/language)
BuildRequires:  golang(golang.org/x/text/message)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/3mux %{goipath}
for cmd in fuzz; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Update to latest upstream release 1.0.1 (rhbz#1829334)

* Wed Apr 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package for Fedora