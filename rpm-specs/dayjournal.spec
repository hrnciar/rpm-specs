Name:       dayjournal
Version:    23.0.6
Release:    9%{?dist}
Summary:    Digital journal that uses plain text files

License:    GPLv3+
URL:        https://burnsoftware.wordpress.com/dayjournal/
Source0:    https://launchpad.net/~thejambi/+archive/ubuntu/thejambi/+files/%{name}_%{version}.orig.tar.gz
# Desktop file and icon are not released as part of the source tar ball
Source1:    https://raw.githubusercontent.com/thejambi/DayJournal/d9999552462718596a85af313a3156b37ea39c43/deb_help/dayjournal.desktop
Source2:    https://raw.githubusercontent.com/thejambi/DayJournal/d9999552462718596a85af313a3156b37ea39c43/deb_help/dayjournal.png
Source3:    dayjournal.appdata.xml
# Stop the installation of empty documentation
Patch0:     makefile.patch

BuildRequires:    gcc
BuildRequires:    vala
BuildRequires:    pango-devel
BuildRequires:    pkgconfig(gee-0.8)
BuildRequires:    pkgconfig(gtk+-3.0)
BuildRequires:    pkgconfig(libnotify)
BuildRequires:    pkgconfig(gio-2.0)
BuildRequires:    pkgconfig(gdk-3.0)
BuildRequires:    pkgconfig(glib-2.0)
BuildRequires:    pkgconfig(appindicator3-0.1)
BuildRequires:    desktop-file-utils
BuildRequires:    libappstream-glib

%description
DayJournal is a minimalist digital journal that lets the content you
create outlast DayJournal itself.

* Future proofs your journal entries by saving them as plain text and
  organizing them as you go. This means you can read or create entries
  when you don’t have DayJournal.

* Automatically saves as you write.

* Easily sync journals with cloud storage services because you choose
  where your journal folder is.

* Add pictures to your journal entries.

* Manage multiple journals.

* Keyboard shortcuts make it easy to navigate through entries.

* Create a journal archive file, an HTML page that looks great when
  printed so you can keep a physical journal too.

* Add to your journal from anywhere with Blip Journal for
  Android. DayJournal can automatically import entries synced to Dropbox
  from Blip Journal. On iOS? Now DayJournal can automatically import
  entries synced to Dropbox from the Day One app as well.

Simply put, DayJournal is the simple digital journal that finally does
it right.

%prep
%autosetup 

%build
%configure
%make_build

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%install
%make_install install-exec
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -m 644 -D %{SOURCE2} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m 644 -D %{SOURCE3} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%{_bindir}/dayjournal
%{_datadir}/applications/dayjournal.desktop
%{_datadir}/icons/hicolor/48x48/apps/dayjournal.png
%{_datadir}/appdata/%{name}.appdata.xml
%license COPYING

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 23.0.6-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jan 05 2017 Brian Exelbierd <bex@pobox.com> - 23.0.6-1
- Initial Package
