%global __provides_exclude_from ^%{_libdir}/gsignond/.*\\.so$

Name:           gsignond-plugin-mail
Summary:        E-Mail plugin for gsignond
Version:        0.3.0
Release:        5%{?dist}
License:        LGPLv2+

URL:            https://gitlab.com/accounts-sso/%{name}
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsignond) >= 1.2.0

Requires:       gsignond%{?_isa} >= 1.2.0
Supplements:    gsignond

%description
This plugin for the Accounts-SSO gSignOn daemon handles the E-Mail
credentials.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING.LIB
%doc README.md

%{_libdir}/gsignond/gplugins/libmail.so


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-1
- Initial packaging for fedora.

