%global __provides_exclude_from ^%{_libdir}/gsignond/.*\\.so$

%global srcname     gsignond-plugin-sasl

%global commit      671022f3d941509d64249d8f887f4cb60f2a5aab
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20171111

Name:           gsignond-plugin-sasl
Summary:        SASL plugin for gsignond
Version:        0
Release:        0.10.%{commitdate}.git%{shortcommit}%{?dist}
License:        LGPLv2+

URL:            https://gitlab.com/accounts-sso/%{srcname}
Source0:        %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# This patch is needed to fix building with meson 0.47+
Patch0:         00-fix-meson-047-errors.patch

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson

BuildRequires:  pkgconfig(check) >= 0.9.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.30
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsignond)
BuildRequires:  pkgconfig(libgsasl)

Supplements:    gsignond


%description
This plugin for the Accounts-SSO gSignOn daemon handles the SASL
authentication protocol.


%package        docs
Summary:        SASL plugin for gsignond (documentation)
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    docs
This plugin for the Accounts-SSO gSignOn daemon handles the SASL
authentication protocol.

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

%{_libdir}/gsignond/gplugins/libsasl.so

%files docs
%{_datadir}/gtk-doc/html/%{name}/*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20171111.git671022f
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20171111.git671022f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20171111.git671022f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20171111.git671022f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20171111.git671022f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.5.20171111.git671022f
- Add patch to fix building with meson 0.47+.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20171111.git671022f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.3.20171105.git671022f
- Bump to commit 671022f.
- Rebuild for gsignond soname bump.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171105.gitbd61136
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20171105.gitbd61136
- Initial package

