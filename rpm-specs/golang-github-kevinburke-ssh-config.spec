# Generated by go2rpm
%bcond_without check

# https://github.com/kevinburke/ssh_config
%global goipath         github.com/kevinburke/ssh_config
Version:                1.0
%global tag             %{version}

%gometa

%global common_description %{expand:
Package ssh_config provides tools for manipulating SSH config files.

Importantly, this parser attempts to preserve comments in a given file, so you
can manipulate a `ssh_config` file from a program, if your heart desires.

The Get() and GetStrict() functions will attempt to read values from
$HOME/.ssh/config, falling back to /etc/ssh/ssh_config. The first argument is
the host name to match on ("example.com"), and the second argument is the key
you want to retrieve ("Port"). The keywords are case insensitive.}

%global golicenses      LICENSE
%global godocs          AUTHORS.txt README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go parser for ssh_config files

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pelletier/go-buffruneio)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Dominik Mierzejewski <dominik@greysector.net> - 1.0-1
- update to 1.0 (#1742298)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 22:54:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5-2
- Update to new macros

* Sat Apr 06 01:14:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5-1
- Release 0.5 (#1695256)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.4-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Dominik Mierzejewski <dominik@greysector.net> - 0.4-1
- First package for Fedora
