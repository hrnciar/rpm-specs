%global __provides_exclude_from ^%{_libdir}/gsignond/.*\\.so$

%global commit      0a7a5f8511282e45cfe35987b81f27f158f0648c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20180507

Name:           gsignond-plugin-lastfm
Summary:        Last.FM plugin for gsignond
Version:        0
Release:        0.4.%{commitdate}.git%{shortcommit}%{?dist}
License:        LGPLv2+

URL:            https://gitlab.com/accounts-sso/%{name}
Source0:        %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsignond) >= 1.2.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)

Requires:       gsignond%{?_isa}
Supplements:    gsignond%{?_isa}

%description
This plugin for the Accounts-SSO gSignOn daemon handles the Last.FM
credentials.


%prep
%autosetup -n %{name}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING.LIB
%doc README.md

%{_libdir}/gsignond/gplugins/liblastfm.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20180507.git0a7a5f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20180507.git0a7a5f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20180507.git0a7a5f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20180507.git0a7a5f8
- Initial packaging for fedora.

