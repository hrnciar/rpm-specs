%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type hardware
%global plug_name about
%global plug_rdnn io.elementary.switchboard.about

Name:           switchboard-plug-about
Summary:        Switchboard System Information plug
Version:        2.6.3
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       system-logos


%description
This switchboard plug shows system information.


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
* Fri May 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.6.3-1
- Update to version 2.6.3.

* Wed Apr 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.6.2-1
- Update to version 2.6.2.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.1-1
- Update to version 2.6.1.

* Wed Sep 25 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0-1
- Update to version 2.6.0.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.2-1
- Update to version 2.5.2.
- Switch to using LOGO from os-release, dropping the downstream patch.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1-1
- Update to version 2.5.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-2
- Rebuild for granite5 soname bump.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-1
- Update to version 0.2.5.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4-3
- Clean up .spec file.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4-2
- Rebuild for granite soname bump.

* Fri Sep 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4-1
- Update to version 0.2.4.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3.1-1
- Update to version 0.2.3.1.

* Wed Jun 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-1
- Update to version 0.2.3.

* Thu Apr 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-1
- Initial package.

