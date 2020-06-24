%bcond_with bootstrap

%global public_key RWQf6LRCGA9i53mlYecO4IzT51TGPpvWucNSCh1CBM0QTaLn73Y7GFO3

Name:           minisign
Version:        0.9
Release:        1%{?dist}
Summary:        A dead simple tool to sign files and verify digital signatures
License:        ISC
URL:            https://github.com/jedisct1/minisign
Source0:        %{url}/releases/download/%{version}/minisign-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/minisign-%{version}.tar.gz.minisig

BuildRequires:  libsodium-devel
BuildRequires:  cmake
BuildRequires:  gcc
%if %{without bootstrap}
BuildRequires:  minisign
%endif

%description
Minisign is a dead simple tool to sign files and verify signatures.

%prep
%if %{without bootstrap}
/usr/bin/minisign -V -m %{SOURCE0} -x %{SOURCE1} -P %{public_key}
%endif

%autosetup

%build
%cmake -DCMAKE_STRIP=0 .
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
* Sun Jun 07 2020 François Kooman <fkooman@tuxed.net> - 0.9-1
- update to 0.9
- verify source tarball (when not bootstrapping)
- do not strip binary during build

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 François Kooman <fkooman@tuxed.net> - 0.8-2
- use macros for Source0

* Wed Jul 17 2019 François Kooman <fkooman@tuxed.net> - 0.8-1
- initial package
