Name:		quodlibet
Version:	4.3.0
Release:	3%{?dist}
Summary:	A music management program

License:	GPLv2+
URL:		https://quodlibet.readthedocs.org/en/latest/
Source0:	https://github.com/quodlibet/quodlibet/releases/download/release-%{version}/quodlibet-%{version}.tar.gz
Source1:	README.fedora

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 3.5
# needed for gtk-update-icon-cache
BuildRequires:	gtk2 >= 2.6.0
# needed for py_byte_compile
BuildRequires:	python3-devel

Requires:	exfalso = %{version}-%{release}
Requires:	gstreamer1
Requires:	gstreamer1-plugins-base
Requires:	gstreamer1-plugins-good
Requires:	python3-dbus

%description
Quod Libet is a music management program. It provides several different ways
to view your audio library, as well as support for Internet radio and
audio feeds. It has extremely flexible metadata tag editing and searching
capabilities.
Supported file formats include Ogg Vorbis, MP3, FLAC, MOD/XM/IT, Musepack,
Wavpack, and MPEG-4 AAC.


%package -n exfalso
Summary: Tag editor for various music files

Requires:	adwaita-icon-theme
Requires:	gtk3 >= 3.18
Requires:	hicolor-icon-theme
Requires:	libsoup >= 2.44
Requires:	pkgconfig
Requires:	python3-gobject >= 3.18
Requires:	python3 >= 3.5
Requires:	python3-mutagen >= 1.14
Requires:	python3-feedparser
Requires:	webkitgtk4

# for musicbrainz plugin
Requires:	python3-musicbrainzngs


%description -n exfalso
Ex Falso is a tag editor with the same tag editing interface as Quod Libet,
but it does not play files.
Supported file formats include Ogg Vorbis, MP3, FLAC, MOD/XM/IT, Musepack,
Wavpack, and MPEG-4 AAC.


%package zsh-completion
Summary: zsh completion files for %{name}
Requires: quodlibet = %{version}-%{release}
Requires: zsh

%description zsh-completion
This package installs %{summary}.


%prep
%autosetup -p 1

install -pm 0644 %{S:1} .


%build
%py3_build


%install
%py3_install

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications		\
	--delete-original					\
	%{buildroot}%{_datadir}/applications/io.github.quodlibet.QuodLibet.desktop
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications		\
	--delete-original					\
	%{buildroot}%{_datadir}/applications/io.github.quodlibet.ExFalso.desktop

%find_lang quodlibet


%files
%doc README.fedora
%{_bindir}/quodlibet
%{_datadir}/applications/io.github.quodlibet.QuodLibet.desktop
%{_datadir}/bash-completion/completions/quodlibet
%{_datadir}/gnome-shell/search-providers/io.github.quodlibet.QuodLibet-search-provider.ini
%{_datadir}/icons/hicolor/*x*/apps/io.github.quodlibet.QuodLibet.png
%{_datadir}/appdata/io.github.quodlibet.QuodLibet.appdata.xml
%{_datadir}/dbus-1/services/net.sacredchao.QuodLibet.service
%{_mandir}/man1/quodlibet.1*


%files -n exfalso -f %{name}.lang
%license COPYING
%doc NEWS README
%{_bindir}/exfalso
%{_bindir}/operon
%{_datadir}/applications/io.github.quodlibet.ExFalso.desktop
%{_datadir}/bash-completion/completions/operon
%{_mandir}/man1/exfalso.1*
%{_mandir}/man1/operon.1*
%{_datadir}/icons/hicolor/*x*/apps/io.github.quodlibet.ExFalso.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/appdata/io.github.quodlibet.ExFalso.appdata.xml

%{python3_sitelib}/quodlibet-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/quodlibet


%files zsh-completion
%{_datadir}/zsh/site-functions/_quodlibet


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-3
- Rebuilt for Python 3.9

* Mon Apr 13 2020 Johannes Lips <hannes@fedoraproject.org> - 4.3.0-2
- fixed icon theme dependency - bug #1814119

* Mon Feb 24 2020 Johannes Lips <hannes@fedoraproject.org> - 4.3.0-1
- update to recent upstream release 4.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Björn Esser <besser82@fedoraproject.org> - 4.2.1-3
- Fix FTBFS

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Johannes Lips <hannes@fedoraproject.org> - 4.2.0-1
- update to recent upstream release 4.2.1

* Mon Dec 10 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-2
- Require python3-gobject instead of python2-gobject

* Fri Nov 23 2018 Johannes Lips <hannes@fedoraproject.org> - 4.2.0-1
- update to recent upstream release 4.2.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Johannes Lips <hannes@fedoraproject.org> - 4.1.0-3
- Rebuilt for Python 3.7 site-tag

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.7

* Mon Jun 04 2018 Johannes Lips <hannes@fedoraproject.org> - 4.1.0-1
- update to recent upstream release 4.1.0
- name changes to multiple files

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.2-2
- Remove obsolete scriptlets

* Thu Jan 18 2018 Johannes Lips <hannes@fedoraproject.org> - 4.0.2-1
- update to recent upstream release 4.0.2

* Sat Jan 13 2018 Johannes Lips <hannes@fedoraproject.org> - 4.0.1-1
- update to recent upstream release 4.0.1

* Wed Jan 03 2018 Johannes Lips <hannes@fedoraproject.org> - 4.0.0-2
- updated missing deps for bug #1461590

* Wed Jan 03 2018 Johannes Lips <hannes@fedoraproject.org> - 4.0.0-1
- transition to python3
- license changed to GPLv2+

* Thu Nov 02 2017 Johannes Lips <hannes@fedoraproject.org> - 3.9.1-3
- fixed bug #1461484 requires of python-feedparser

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Johannes Lips <hannes@fedoraproject.org> - 3.9.1-1
- update to recent upstream release 3.9.1

* Thu May 25 2017 Johannes Lips <hannes@fedoraproject.org> - 3.9.0-2
- added python2-faulthandler as dependency

* Thu May 25 2017 Johannes Lips <hannes@fedoraproject.org> - 3.9.0-1
- update to recent upstream release 3.9.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Johannes Lips <hannes@fedoraproject.org> - 3.8.1-1
- update to recent upstream release 3.8.1

* Fri Dec 30 2016 Johannes Lips <hannes@fedoraproject.org> - 3.8.0-1
- update to recent upstream release 3.8.0

* Thu Oct 13 2016 Johannes Lips <hannes@fedoraproject.org> - 3.7.1-1
- update to recent upstream release 3.7.1

* Sun Aug 28 2016 Johannes Lips <hannes@fedoraproject.org> - 3.7.0-1
- update to recent upstream release 3.7.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 25 2016 Johannes Lips <hannes@fedoraproject.org> - 3.6.2-1
- update to recent upstream release 3.6.2

* Thu Apr 07 2016 Johannes Lips <hannes@fedoraproject.org> - 3.6.1-1
- update to recent upstream release 3.6.1

* Fri Mar 25 2016 Johannes Lips <hannes@fedoraproject.org> - 3.6.0-1
- update to recent upstream release 3.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Johannes Lips <hannes@fedoraproject.org> - 3.5.3-1
- update to recent upstream release 3.5.3

* Thu Jan 14 2016 Johannes Lips <hannes@fedoraproject.org> - 3.5.2-1
- update to recent upstream release 3.5.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Oct 18 2015 Johannes Lips <hannes@fedoraproject.org> - 3.5.1-1
- update to recent upstream release 3.5.1

* Thu Oct 08 2015 Johannes Lips <hannes@fedoraproject.org> - 3.5.0-1
- update to recent upstream release 3.5.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 24 2015 Johannes Lips <hannes@fedoraproject.org> - 3.4.1-1
- update to recent upstream release 3.4.1

* Sun Apr 19 2015 Johannes Lips <hannes@fedoraproject.org> - 3.4.0-2
- added call to update-desktop-database

* Sun Apr 12 2015 Johannes Lips <hannes@fedoraproject.org> - 3.4.0-1
- update to recent upstream release 3.4.0
- changed upstream url

* Sun Jan 11 2015 Johannes Lips <hannes@fedoraproject.org> - 3.3.1-1
- update to recent upstream release 3.3.1

* Sat Jan 03 2015 Johannes Lips <hannes@fedoraproject.org> - 3.3.0-1
- update to recent upstream release 3.3.0

* Fri Aug 11 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.23-1
- First version for Fedora Extras
