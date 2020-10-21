%global srcname stylesheet
%global appname io.elementary.stylesheet

Name:           elementary-theme
Summary:        Stylesheet from elementary
Version:        5.4.2
Release:        2%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildArch:      noarch


%description
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment.


%package        gtk2
Summary:        Stylesheet from elementary (GTK+2 version)

Requires:       %{name} = %{version}-%{release}
Requires:       gtk-murrine-engine

Supplements:    (%{name} and gtk2)

%description    gtk2
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment.

This package contains the GTK+2 theme.


%package        gtk3
Summary:        Stylesheet from elementary (GTK+3 version)

Requires:       %{name} = %{version}-%{release}

Supplements:    (%{name} and gtk3)

%description    gtk3
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment.

This package contains the GTK+3 theme.


%package        plank
Summary:        Stylesheet from elementary (plank theme)

Requires:       %{name} = %{version}-%{release}
Requires:       plank

Supplements:    (%{name} and plank)

%description    plank
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment.

This package contains the plank theme.


%prep
%autosetup -n %{srcname}-%{version}


%build
%meson
%meson_build


%install
%meson_install


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files
%doc README.md
%license COPYING

%{_datadir}/metainfo/%{appname}.appdata.xml

%dir %{_datadir}/themes/elementary
%{_datadir}/themes/elementary/index.theme

%files          gtk2
%{_datadir}/themes/elementary/gtk-2.0/

%files          gtk3
%{_datadir}/themes/elementary/gtk-3.0/

%files          plank
%{_datadir}/themes/elementary/plank/
%{_datadir}/plank/themes/elementary-dark/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 29 2020 Fabio Valentini <decathorpe@gmail.com> - 5.4.2-1
- Update to version 5.4.2.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Fabio Valentini <decathorpe@gmail.com> - 5.4.1-1
- Update to version 5.4.1.

* Mon Dec 30 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0-1
- Update to version 5.4.0.

* Sat Nov 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.0-1
- Update to version 5.3.0.

* Sun Aug 04 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5-1
- Update to version 5.2.5.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.4-1
- Update to version 5.2.4.

* Thu Apr 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3-1
- Update to version 5.2.3.

* Fri Mar 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.2-1
- Update to version 5.2.2.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.1-1
- Update to version 5.2.1.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.0-1
- Update to version 5.2.0.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1-1
- Update to version 5.1.1.

* Sat Aug 12 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0-1
- Update to version 5.1.0.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4-1
- Update to version 5.0.4.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3-3
- Remove unused Source file.

* Fri Jan 20 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3-2
- Clean up spec file.

* Fri Jan 20 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3-1
- Initial package.

