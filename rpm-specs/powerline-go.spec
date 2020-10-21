# https://github.com/justjanne/powerline-go
%global goipath         github.com/justjanne/powerline-go
Version:                1.17.0

%gometa

%global common_description %{expand:
A Powerline like prompt for Bash, ZSH and Fish.

 - Shows some important details about the git/hg branch
 - Changes color if the last command exited with a failure code
 - If you're too deep into a directory tree, shortens the displayed
   path with an ellipsis
 - Shows the current Python virtualenv environment
 - It's easy to customize and extend.}

Name:           powerline-go
Release:        2%{?dist}
Summary:        A beautiful and useful low-latency prompt for your shell, written in go

License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(github.com/shirou/gopsutil/load)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/text/width)
BuildRequires:  golang(gopkg.in/yaml.v2)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/powerline-go %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE.md
%doc README.md
%{_bindir}/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 20:13:14 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.17.0-1
- Update to 1.17.0 (#1827401)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 05:21:10 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Release 1.15.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 17:21:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.13.0-1
- Release 1.13.0 (#1727039)

* Sat Mar 02 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.1-1
- Upstream release 1.12.1

* Tue Feb 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-1
- Upstream release 1.12.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.11.0-1
- Upstream release 1.11.0

* Wed Apr 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.9.0-1
- Upstream release 1.9.0
- Update to new Go packaging guidelines

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.2-1
- Upstream release 1.8.2

* Fri Oct 20 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.1-1
- Upstream release 1.8.1

* Sat Sep 02 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.1-1
- Upstream release 1.5.1

* Fri Sep 01 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.0-1
- Initial RPM release

