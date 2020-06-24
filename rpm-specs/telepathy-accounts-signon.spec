Name:           telepathy-accounts-signon
Summary:        Telepathy integration for the Accounts SSO framework
Version:        2.1
Release:        1%{?dist}
License:        LGPLv2

URL:            https://gitlab.com/accounts-sso/telepathy-accounts-signon
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libsignon-glib) >= 2.0
BuildRequires:  pkgconfig(mission-control-plugins)

%description
%{summary}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING.LGPL
%doc README.md
%{_libdir}/mission-control-plugins.0/mcp-account-manager-accounts-sso.so


%changelog
* Mon Feb 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.1-1
- 2.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0-1
- Update to version 2.0 to support libsignon-glib 2.0+.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Daniel Vrátil <dvratil@redhat.com> - 1.0-1
- Initial version

