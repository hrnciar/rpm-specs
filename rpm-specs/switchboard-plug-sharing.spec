%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type network
%global plug_name sharing
%global plug_rdnn io.elementary.switchboard.sharing

Name:           switchboard-plug-sharing
Summary:        Switchboard Sharing Plug
Version:        2.1.4
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       rygel
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and rygel)


%description
Configure the sharing of system services.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Thu Apr 02 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.4-1
- Update to version 2.1.4.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 03 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-4
- Add upstream patch to fix FTBFS with vala 0.45+.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-1
- Update to version 2.1.3.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-2
- Adapt to removed AUTHORS file.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-4
- Clean up .spec file.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-3
- Rebuild for the granite 0.5 soname bump.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Clean up .spec file.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-2
- Mass rebuild.

* Tue Aug 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.

