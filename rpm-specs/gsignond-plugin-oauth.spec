%global __provides_exclude_from ^%{_libdir}/gsignond/.*\\.so$

%global srcname     gsignond-plugin-oa

%global commit      43fee492ef84533ea2282a161b2695e0a95eb186
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20180513

Name:           gsignond-plugin-oauth
Summary:        OAuth plugin for gsignond
Version:        0
Release:        0.8.%{commitdate}.git%{shortcommit}%{?dist}
License:        LGPLv2+

URL:            https://gitlab.com/accounts-sso/%{srcname}
Source0:        %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# This patch is needed to fix building with meson 0.47+
Patch0:         00-fix-meson-047-errors.patch

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsignond)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)

Supplements:    gsignond


%description
This plugin for the Accounts-SSO gSignOn daemon handles the OAuth 1.0
and 2.0 authentication protocols.


%package        docs
Summary:        OAuth plugin for gsignond (documentation)
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    docs
This plugin for the Accounts-SSO gSignOn daemon handles the OAuth 1.0
and 2.0 authentication protocols.

This package contains the documentation.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license COPYING.LIB
%doc README.md

%{_libdir}/gsignond/gplugins/liboauth.so

%files docs
%{_datadir}/gtk-doc/html/%{name}/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20180513.git43fee49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20180513.git43fee49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20180513.git43fee49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.5.20180513.git43fee49
- Bump to commit 43fee49.
- Add patch to fix building with meson 0.47+.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20171111.gitb36060b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.3.20171111.gitb36060b
- Bump to commit b36060b.
- Rebuild for gsignond soname bump.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171105.git787e8bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20171105.git787e8bc
- Initial package

