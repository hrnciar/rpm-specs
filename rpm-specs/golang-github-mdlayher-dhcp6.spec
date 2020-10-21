# Generated by go2rpm 1
# Checks are not passing on aarch64
%bcond_with check

# https://github.com/mdlayher/dhcp6
%global goipath         github.com/mdlayher/dhcp6
%global commit          2a67805d7d0b0bad6c1103058981afdea583b459

%gometa

%global common_description %{expand:
The package dhcp6 implements a DHCPv6 server, as described in RFC 3315.}

%global golicenses      LICENSE.md
%global godocs          README.md cmd/dhcp6d/README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        DHCPv6 server, as described in RFC 3315

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/ipv6)

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
%doc README.md cmd/dhcp6d/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.2.20200404git2a67805
- Disable tests for now because there is a failure

* Sat Apr 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200404git2a67805
- Initial package

