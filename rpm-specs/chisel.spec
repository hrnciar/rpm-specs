%bcond_without check

# https://github.com/jpillora/chisel
%global goipath         github.com/jpillora/chisel
Version:                1.7.2
%global tag             v1.7.2

%gometa

%global common_description %{expand:
A fast TCP tunnel over HTTP.}

%global godocs          example README.md

Name:           chisel
Release:        1%{?dist}
Summary:        TCP tunnel over HTTP

License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/armon/go-socks5)
BuildRequires:  golang(github.com/fsnotify/fsnotify)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/jpillora/backoff)
BuildRequires:  golang(github.com/jpillora/requestlog)
BuildRequires:  golang(github.com/jpillora/sizestr)
BuildRequires:  golang(golang.org/x/crypto/ssh)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/chisel %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%doc example README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Oct 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.2-1
- Update ot latest upstream release 1.7.2 (#1889172)

* Mon Sep 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.1-1
- Update ot latest upstream release 1.7.1 (#1880651)

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-1
- Update ot latest upstream release 1.7.0 (#1880651)

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Update ot latest upstream release 1.6.0

* Fri Jul 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update ot latest upstream release 1.5.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2-1
- Initial package for Fedora