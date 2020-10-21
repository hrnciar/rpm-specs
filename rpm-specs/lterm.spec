%define _legacy_common_support 1

Name:           lterm
Version:        1.5.1
Release:        6%{?dist}
Summary:        Terminal and multi protocol client
License:        GPLv2
URL:            http://%{name}.sourceforge.net/
Source0:        https://sourceforge.net/projects/%{name}/files/1.5/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  vte-devel
BuildRequires:  openssl-devel
BuildRequires:  libssh-devel
BuildRequires:	desktop-file-utils

%description
It is mainly used as SSH/Telnet client

%prep
%autosetup

%build
%configure --with-gtk2

%install
%make_install

desktop-file-install                                    \
--add-category="TerminalEmulator"                       \
--delete-original                                       \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%license COPYING
%doc README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/mime/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.5.1-5
- Fix FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Luis Segundo <blackfile@fedoraproject.org> - 1.5.1-1
- Initial Spec
