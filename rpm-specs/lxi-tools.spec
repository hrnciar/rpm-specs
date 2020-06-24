Summary:        Tools collection to control LXI enabled instruments
Name:           lxi-tools
Version:        1.21
Release:        3%{?dist}
License:        BSD
URL:            https://lxi-tools.github.io/
Source0:        https://github.com/lxi/lxi-tools/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxi/lxi-tools/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1.gpg
BuildRequires:  gcc
BuildRequires:  readline-devel
BuildRequires:  liblxi-devel >= 1.13
BuildRequires:  lua-devel >= 5.1
BuildRequires:  gnupg2

%description
LXI tools are a collection of open source software tools for GNU/Linux
systems that enable control of LXI enabled instruments such as modern
oscilloscopes, power supplies, spectrum analyzers etc.

%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/lxi
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/lxi*
%{_mandir}/man1/lxi.1*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Robert Scheck <robert@fedoraproject.org> 1.21-1
- Upgrade to 1.21

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.20-4
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Robert Scheck <robert@fedoraproject.org> 1.20-1
- Upgrade to 1.20

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Robert Scheck <robert@fedoraproject.org> 1.12-1
- Upgrade to 1.12

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.5-1
- Upgrade to 1.5

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.4-1
- Upgrade to 1.4

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.3-1
- Upgrade to 1.3

* Sun Oct 08 2017 Robert Scheck <robert@fedoraproject.org> 1.1-1
- Upgrade to 1.1
- Initial spec file for Fedora and Red Hat Enterprise Linux
