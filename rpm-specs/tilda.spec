Name:           tilda
Version:        1.5.1
Release:        2%{?dist}
Summary:        A Gtk based drop down terminal for Linux and Unix

License:        GPLv2 and MIT
URL:            http://github.com/lanoxx/tilda 
Source0:        https://github.com/lanoxx/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  glib-devel
BuildRequires:  gtk3-devel
BuildRequires:  libconfuse-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXt-devel
BuildRequires:  vte291-devel

# License GPLv2
Provides:  bundled(eggaccelerators)
Provides:  bundled(xerror)
# License MIT
Provides:  bundled(tomboykeybinder)

%description
Tilda is a Linux terminal taking after the likeness of many classic terminals
from first person shooter games, Quake, Doom and Half-Life (to name a few),
where the terminal has no border and is hidden from the desktop until a key is
pressed.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}

make install DESTDIR=%{buildroot}
desktop-file-install --vendor=""                               \
        --dir=%{buildroot}%{_datadir}/applications             \
        --mode 0644                                            \
        --remove-category="Application"                        \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

install -D -p -m 644 %{name}.png \
        %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.md ChangeLog TODO.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/tilda.appdata.xml

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Johannes Lips <hannes@fedoraproject.org> - 1.5.1-1
- update to upstream version 1.5.1
- added the provides for bundled libraries
- additional license MIT for bundled library

* Fri May 01 2020 Johannes Lips <hannes@fedoraproject.org> - 1.5.0-1
- update to upstream version 1.5.0
- added fix to also run on Wayland

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Johannes Lips <hannes@fedoraproject.org> - 1.4.1-1
- update to upstream version 1.4.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.3-8
- Remove obsolete scriptlets

* Tue Aug 22 2017 Johannes Lips <hannes@fedoraproject.org> - 1.3.3-7
- libconfuse rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.3.3-4
- libconfuse rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Jon Ciesla <limburgher@gmail.com> - 1.3.3-2
- libconfuse rebuild.

* Sat Apr 30 2016 Johannes Lips <hannes@fedoraproject.org> - 1.3.3-1
- update to upstream version 1.3.3

* Mon Mar 14 2016 Johannes Lips <hannes@fedoraproject.org> - 1.3.2-1
- update to upstream version 1.3.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Johannes Lips <hannes@fedoraproject.org> - 1.2.4-1
- update to upstream version 1.2.4

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 17 2014 Johannes Lips <hannes@fedoraproject.org> - 1.2.2-1
- update to upstream version 1.2.2
- fixed bug #1164476

* Thu Oct 16 2014 Johannes Lips <hannes@fedoraproject.org> - 1.2.1-1
- update to upstream version 1.2.1

* Thu Oct 16 2014 Johannes Lips <hannes@fedoraproject.org> - 1.2-1
- update to upstream version 1.2

* Sun Sep 14 2014 Johannes Lips <hannes@fedoraproject.org> - 1.1.13-1
- Initial Release
