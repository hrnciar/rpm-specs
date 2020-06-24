# Generated by go2rpm 1
%bcond_without check

# https://github.com/WireGuard/wgctrl-go
%global goipath         golang.zx2c4.com/wireguard/wgctrl
%global forgeurl        https://github.com/WireGuard/wgctrl-go
%global commit          28f4e240be2d40c8ae16f3bbc8f05c8ee57fc554

%gometa

%global goname          wgctrl

%global common_description %{expand:
Package Wgctrl enables control of WireGuard interfaces on multiple platforms.}

%global golicenses      LICENSE.md
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Control of WireGuard interfaces on multiple platforms

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/mdlayher/genetlink)
BuildRequires:  golang(github.com/mdlayher/netlink)
BuildRequires:  golang(github.com/mdlayher/netlink/nlenc)
BuildRequires:  golang(golang.org/x/crypto/curve25519)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/mdlayher/genetlink/genltest)
BuildRequires:  golang(github.com/mdlayher/netlink/nltest)
BuildRequires:  golang(github.com/mikioh/ipaddr)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
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
%license LICENSE.md
%doc CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 17 22:28:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190729git28f4e24
- Initial package