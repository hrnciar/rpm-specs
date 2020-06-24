%global __provides_exclude_from ^%{_libdir}/gsignond/.*\\.so$

%global dbus_type       session
%global extension_type  desktop

Name:           gsignond
Summary:        GSignOn daemon
Version:        1.2.0
Release:        7%{?dist}
License:        GPLv3

URL:            https://gitlab.com/accounts-sso/%{name}
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(sqlite3)

Requires:       %{name}-config

Requires:       dbus%{?_isa}

# gsignond and signon provide the same DBus interfaces
Conflicts:      signon

Provides:       gsignond-extension-pantheon = %{version}-%{release}
Obsoletes:      gsignond-extension-pantheon < 0.3.0-5


%description
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.


%package        libs
Summary:        GSignOn daemon libraries

%description    libs
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.

This package contains the shared libraries.


%package        devel
Summary:        GSignOn daemon development files
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.

This package contains the development headers.


%package        doc
Summary:        GSignOn daemon documentation
BuildArch:      noarch

%description    doc
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.

This package contains the documentation.


%package        default-config
Summary:        GSignOn daemon default configuration
BuildArch:      noarch

Provides:       %{name}-config
Obsoletes:      gsignond-pantheon-config

%description    default-config
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.

This package contains the default configuration.


%prep
%autosetup -p1


%build
%meson -Dbus_type=%{dbus_type} -Dextension=%{extension_type}
%meson_build


%install
%meson_install


%files
%{_bindir}/gsignond

%if "x%{?dbus_type}" != "xp2p"
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOn.service
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.SingleSignOn.service
%endif


%files libs
%license COPYING.LIB

%{_libdir}/libgsignond-common.so.1*

%{_libdir}/girepository-1.0/GSignond-1.0.typelib

%dir %{_libdir}/gsignond

%{_libdir}/gsignond/pluginloaders/

%dir %{_libdir}/gsignond/gplugins
%{_libdir}/gsignond/gplugins/libdigest.so
%{_libdir}/gsignond/gplugins/libpassword.so

%dir %{_libdir}/gsignond/extensions
%{_libdir}/gsignond/extensions/libextension-desktop.so


%files devel
%{_includedir}/gsignond/

%{_libdir}/gsignond/gplugins/libssotest.so
%{_libdir}/libgsignond-common.so
%{_libdir}/pkgconfig/gsignond.pc

%{_datadir}/gir-1.0/GSignond-1.0.gir
%{_datadir}/vala/vapi/gsignond.deps
%{_datadir}/vala/vapi/gsignond.vapi


%files doc
%{_datadir}/gtk-doc/html/gsignond/


%files default-config
%config(noreplace) %{_sysconfdir}/gsignond.conf


%changelog
* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 1.2.0-7
- Fix string quoting for rpm >= 4.16

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.2.0-5
- Remove unnecessary BR on libecryptfs-devel, fixing builds on i686.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.2.0-3
- Conflict with signon to make sure only one of them is installed.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.0-1
- Update to version 1.2.0.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-4
- Add patch to fix building with meson 0.48+.

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.1.0-3
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-2
- Rebuild for new binutils

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.7-1
- Update to version 1.0.7.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-6.20180412.gitadc8904
- Bump to commit adc8904 (fixing FTBFS on f28+).
- Obsolete pantheon extension, replaced by the builtin desktop extension.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-2
- Fix subpackage descriptions.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-1
- Initial package.

