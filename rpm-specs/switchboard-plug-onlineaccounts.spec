%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type network
%global plug_name online-accounts

Name:           switchboard-plug-onlineaccounts
Summary:        Switchboard Online Accounts plug
Version:        2.0.1
Release:        6%{?dist}
License:        GPLv2

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# backported patch to fix new compiler errors with vala 0.45+
# https://github.com/elementary/switchboard-plug-onlineaccounts/commit/5fa2882
Patch0:         00-vala-045-fix.patch

# backported patch to fix new compiler errors with vala 0.47+
# https://github.com/elementary/switchboard-plug-onlineaccounts/commit/34164a9
Patch1:         01-vala-047-fix.patch

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libsignon-glib) >= 2.0
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

# libsignon-glib works with both signond and gsignond now,
# but this package recommends gsignond, because it doesn't pull in Qt5
Recommends:     gsignond

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       hicolor-icon-theme

# obsolete old sub-packages (removed in fedora 30)
%global obsoleted_version  0.3.1-4
Obsoletes:      pantheon-online-accounts < %{obsoleted_version}
Obsoletes:      pantheon-online-accounts-libs < %{obsoleted_version}
Obsoletes:      pantheon-online-accounts-devel < %{obsoleted_version}


%description
%{summary}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_libexecdir}/io.elementary.online-accounts.*

%{_datadir}/accounts/providers/*.provider
%{_datadir}/accounts/services/*.service
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOnUI.service
%{_datadir}/icons/hicolor/*/apps/*.svg


%changelog
* Fri Jan 31 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-6
- Add upstream patch to fix FTBFS with vala 0.47+.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-4
- Add upstream patch to fix FTBFS with vala 0.45+.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-2
- Rebuild for granite5 soname bump.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Update to version 0.3.1.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-7.20170417.git5a0270a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1-6.20170417.git5a0270a
- Be lazy about undefined symbols in plugins.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1-5.20170417.git5a0270a
- Remove icon cache scriptlets, replaced by file triggers.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1-4.20170417.git5a0270a
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-3.20170417.git5a0270a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-2.20170417.git5a0270a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1-1.20170417.git5a0270a
- Initial package.

