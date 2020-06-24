%global srcname libsignon-glib

%global common_description %{expand:
This project is a library for managing single signon credentials which can be
used from GLib applications. It is effectively a GLib binding for the D-Bus API
provided by signond. It is part of the accounts-sso project.
}

Name:           signon-glib
Summary:        Single signon authentication library for GLib applications
Version:        2.1
Release:        9%{?dist}
License:        LGPLv2+

URL:            https://gitlab.com/accounts-sso/%{srcname}
Source0:        %{url}/-/archive/%{version}/%{srcname}-%{version}.tar.gz

# the shared dbus interfaces are maintained in a separate git submodule
%global ifaces  signon-dbus-specification
%global iurl    https://gitlab.com/accounts-sso/%{ifaces}
%global icommit 67487954653006ebd0743188342df65342dc8f9b
Source1:        %{iurl}/-/archive/%{icommit}/%{ifaces}-%{icommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  vala

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gio-2.0) >= 2.36
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0) >= 2.35.1
BuildRequires:  pkgconfig(gobject-introspection-1.0)

# both signond and gsignond services are supported with version 2.0+
Requires:       (signond >= 8.60 or gsignond >= 1.2.0)

# prefer gsignond over signond to not pull in Qt5 dependencies unnecessarily
Suggests:       gsignond

%description %{common_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{common_description}
This package contains the development headers.


%package     -n python3-signon
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-gobject

%description -n python3-signon %{common_description}
This package contains the GObject introspection overrides for python3.


%package        doc
Summary:        Documentation for %{name}

BuildArch:      noarch

%description    doc %{common_description}
This package contains the developer documentation.


%prep
%autosetup -n %{srcname}-%{version} -p1

# initialise git submodule manually
pushd libsignon-glib/interfaces
tar -xzf %{SOURCE1}
mv %{ifaces}-%{icommit}/* ./
rmdir %{ifaces}-%{icommit}
popd


%build
%meson
%meson_build


%install
%meson_install


%files
%doc README.md NEWS
%license COPYING

%{_libdir}/libsignon-glib.so.2*

%{_libdir}/girepository-1.0/Signon-2.0.typelib


%files devel
%{_includedir}/libsignon-glib/

%{_libdir}/libsignon-glib.so
%{_libdir}/pkgconfig/libsignon-glib.pc

%{_datadir}/gir-1.0/Signon-2.0.gir
%{_datadir}/vala/vapi/libsignon-glib.deps
%{_datadir}/vala/vapi/libsignon-glib.vapi


%files doc
%{_datadir}/gtk-doc/html/%{srcname}/


%files -n python3-signon
%{python3_sitearch}/gi/overrides/Signon.py
%{python3_sitearch}/gi/overrides/__pycache__/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.1-4
- Rebuild with Meson fix for #1699099

* Mon Apr 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1-3
- Prefer gsignond over signond.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1-1
- Update to version 2.1.
- Support both signond and gsignond services.
- Enable building documentation.
- Enable building GObject overrides for python3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.9-4
- NOCONFIGURE=1 autogen.sh, track lib soname
- pkgconfig_private.patch: avoid overlinking

* Wed Oct 14 2015 Daniel Vrátil <dvratil@redhat.com> - 1.9-3
- fix license
- fix versions in changelog

* Tue Oct 13 2015 Daniel Vrátil <dvratil@redhat.com> - 1.9-2
- Fix dependencies

* Thu Aug 27 2015 Daniel Vrátil <dvratil@redhat.com> - 1.9-1
- Initial version

