Name:       bemenu
Version:    0.5.0
Release:    2%{?dist}
Summary:    Dynamic menu library and client program inspired by dmenu

# In case upstream do not bump program version when tagging; this should usually just resolve to %%{version}
%global     soversion   0.4.1

# Library and bindings are LGPLv3+, other files are GPLv3+
License:    GPLv3+ and LGPLv3+
URL:        https://github.com/Cloudef/bemenu
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
# Created with: gpg --export-options export-minimal --armor --export 0CBD2CD395613887
Source2:    pgpkey-0CBD2CD395613887.asc

Patch0:     respect-env-build-flags.patch

BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for extending %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%make_build   PREFIX='%{_prefix}' libdir='/%{_lib}'

%install
%make_install PREFIX='%{_prefix}' libdir='/%{_lib}'

%files
%doc README.md
%license LICENSE-CLIENT LICENSE-LIB
%{_bindir}/%{name}
%{_bindir}/%{name}-run
%{_mandir}/man1/%{name}*.1*
# Long live escaping! %%%% resolves to %%; ${v%%.*} strips everything after first dot
%{_libdir}/lib%{name}.so.%(v=%{soversion}; echo ${v%%%%.*})
%{_libdir}/lib%{name}.so.%{soversion}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}-renderer-curses.so
%{_libdir}/%{name}/%{name}-renderer-wayland.so
%{_libdir}/%{name}/%{name}-renderer-x11.so

%files devel
%doc README.md
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Jan Staněk <jstanek@redhat.com> - 0.5.0-1
- Upgrade to version 0.5.0

* Mon Apr 20 2020 Jan Staněk <jstanek@redhat.com> - 0.4.1-2
- Fix build-time path definitions (PREFIX, libdir, …)

* Tue Apr 14 2020 Jan Staněk <jstanek@redhat.com> - 0.4.1-1
- Upgrade to release 0.4.1

* Fri Feb 07 2020 Jan Staněk <jstanek@redhat.com> - 0.3.0-3
- Fix declarations of wayland globals (https://github.com/Cloudef/bemenu/pull/86)
- Enable GPG verification of source signatures

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Jan Staněk <jstanek@redhat.com> - 0.3.0-1
- Upgrade to release 0.3.0

* Fri Oct 25 2019 Jan Staněk <jstanek@redhat.com> - 0.2.0-1
- Upgrade to release 0.2.0

* Mon Aug 19 2019 Jan Staněk <jstanek@redhat.com> - 0.1.0-3.20190819git442d283
- Upgrade to snapshot 442d2833f48590122e5ce54a2bca3a327ffa0311

* Mon Jun 10 2019 Jan Staněk <jstanek@redhat.com> - 0.1.0-2.f464f0e
- Upgrade to snapshot f464f0e30a34c27babc9d533a52fbe260f134034

* Mon May 13 2019 Jan Staněk <jstanek@redhat.com> - 0.1.0.121367b
- Initial package import
