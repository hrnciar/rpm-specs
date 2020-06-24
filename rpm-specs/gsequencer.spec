Name:     gsequencer
Version:  3.4.5
Release:  0%{?dist}
Summary:  Audio processing engine
License:  GPLv3+ and AGPLv3+ and GFDL-1.3+
URL:      http://nongnu.org/gsequencer
Source:   http://download.savannah.gnu.org/releases/gsequencer/3.4.x/%{name}-%{version}.tar.gz
BuildRequires:      libtool
BuildRequires:      chrpath
BuildRequires:      docbook-style-xsl
BuildRequires:      gettext-devel
BuildRequires:      gtk-doc
BuildRequires:      pkgconfig(uuid)
BuildRequires:      pkgconfig(libxml-2.0)
BuildRequires:      pkgconfig(libsoup-2.4)
BuildRequires:      pkgconfig(alsa)
BuildRequires:      pkgconfig(fftw3)
BuildRequires:      ladspa-devel
BuildRequires:      dssi-devel
BuildRequires:      lv2-devel
BuildRequires:      pkgconfig(jack)
BuildRequires:      pkgconfig(samplerate)
BuildRequires:      pkgconfig(sndfile)
BuildRequires:      pkgconfig(libinstpatch-1.0)
BuildRequires:      pkgconfig(gtk+-3.0)
BuildRequires:      pkgconfig(webkit2gtk-4.0)
BuildRequires:      pkgconfig(gobject-introspection-1.0)
BuildRequires:      pkgconfig(libpulse)
BuildRequires:      CUnit-devel
BuildRequires:      desktop-file-utils
BuildRequires:      xorg-x11-server-Xvfb
Requires:           xml-common

%description
Advanced Gtk+ Sequencer audio processing engine is an audio
sequencer application supporting LADPSA, DSSI and Lv2 plugin
format. It can output to Pulseaudio server, JACK audio connection
kit, ALSA and OSS4.

You may add multiple sinks, mix different sources by producing
sound with different sequencers. Further it features a pattern
and piano roll. Additional there is a automation editor to
automate ports.

%prep
%autosetup -N

%build
%undefine _strict_symbol_defs_build
autoreconf -fi
export CPPFLAGS='-DAGS_CSS_FILENAME=\"/usr/share/gsequencer/styles/ags.css\" -DAGS_ANIMATION_FILENAME=\"/usr/share/gsequencer/images/gsequencer-800x450.png\" -DAGS_LOGO_FILENAME=\"/usr/share/gsequencer/images/ags.png\" -DAGS_LICENSE_FILENAME=\"/usr/share/licenses/gsequencer/COPYING\" -DAGS_ONLINE_HELP_START_FILENAME=\"file:///usr/share/doc/gsequencer/html/index.html\"'
%configure HTMLHELP_XSL="/usr/share/sgml/docbook/xsl-stylesheets/htmlhelp/htmlhelp.xsl" --disable-upstream-gtk-doc --enable-introspection --disable-oss --enable-gtk-doc --enable-gtk-doc-html
%make_build
%make_build html
%make_build fix-local-html

%install
%make_install
%make_install install-compress-changelog
%make_install install-html-mkdir
%make_install install-html-mkdir-links
%make_install install-html
chrpath --delete %{buildroot}%{_bindir}/gsequencer
chrpath --delete %{buildroot}%{_bindir}/midi2xml
chrpath --delete %{buildroot}%{_libdir}/libags.so*
chrpath --delete %{buildroot}%{_libdir}/libags_server.so*
chrpath --delete %{buildroot}%{_libdir}/libags_thread.so*
chrpath --delete %{buildroot}%{_libdir}/libags_gui.so*
chrpath --delete %{buildroot}%{_libdir}/libags_audio.so*
chrpath --delete %{buildroot}%{_libdir}/libgsequencer.so*
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/doc-base/

%check
xvfb-run --server-args="-screen 0 1920x1080x24" -a make check
desktop-file-validate %{buildroot}/%{_datadir}/applications/gsequencer.desktop

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libags.so.*
%{_libdir}/libags_thread.so.*
%{_libdir}/libags_server.so.*
%{_libdir}/libags_gui.so.*
%{_libdir}/libags_audio.so.*
%{_libdir}/libgsequencer.so.*
%{_libdir}/girepository-1.0
%{_bindir}/gsequencer
%{_bindir}/midi2xml
%{_mandir}/man1/gsequencer.1*
%{_mandir}/man1/midi2xml.1*
%{_datadir}/gsequencer/
%{_datadir}/xml/gsequencer/
%{_datadir}/icons/hicolor/*/apps/gsequencer.png
%{_datadir}/metainfo/
%{_datadir}/mime/packages/
%{_docdir}/gsequencer/
%{_datadir}/applications/gsequencer.desktop

%package devel
Summary:  Advanced Gtk+ Sequencer library development files
Requires: %{name}%{_isa} = %{version}-%{release}
%description devel
Advanced Gtk+ Sequencer library development files.

%files devel
%{_includedir}/ags/
%{_libdir}/libags.so
%{_libdir}/libags_thread.so
%{_libdir}/libags_server.so
%{_libdir}/libags_gui.so
%{_libdir}/libags_audio.so
%{_libdir}/libgsequencer.so
%{_datadir}/gir-1.0
%{_libdir}/pkgconfig/libags.pc
%{_libdir}/pkgconfig/libags_audio.pc
%{_libdir}/pkgconfig/libags_gui.pc
%{_libdir}/pkgconfig/libgsequencer.pc

%package -n gsequencer-devel-doc
Summary:  Advanced Gtk+ Sequencer library development documentation
BuildArch: noarch
%description -n gsequencer-devel-doc
Advanced Gtk+ Sequencer library development documentation.

%files -n gsequencer-devel-doc
%{_datadir}/gtk-doc/
%{_datadir}/doc/libags-audio-doc/

%changelog
* Sun Jun 21 2020 Joël Krähemann <jkraehemann@gmail.com> 3.4.3-0
- updated Source to point to new minor version directory

* Mon May 18 2020 Joël Krähemann <jkraehemann@gmail.com> 3.3.1-0
- updated Source to point to new minor version directory

* Fri Mar 13 2020 Joël Krähemann <jkraehemann@gmail.com> 3.2.0-0
- updated Source to point to new minor version directory

* Wed Feb 05 2020 Joël Krähemann <jkraehemann@gmail.com> 3.1.1-0
- updated Source to point to new minor version directory
- using configure flag --disable-upstream-gtk-doc

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Joël Krähemann <jkraehemann@gmail.com> 3.0.4-0
- dropped gsequencer.0-makefile-am.patch
- updated build requires gtk2 to gtk3
- additional build requires webkit2gtk3, libsoup and
  gobject-introspection-devel
- edited configure variables
- edited make install target

* Thu Nov 28 2019 Joël Krähemann <jkraehemann@gmail.com> 2.4.1-0
- updated Source to point to new minor version directory
- added configure flags to deal with gnulib

* Tue Sep 10 2019 Joël Krähemann <jkraehemann@gmail.com> 2.3.1-0
- updated Source to point to new minor version directory

* Wed Jun 26 2019 Joël Krähemann <jkraehemann@gmail.com> 2.2.5-0
- updated Source to point to new minor version directory

* Mon Jan 07 2019 Joël Krähemann <jkraehemann@gmail.com> 2.1.32-0
- updated install to package hicolor icon theme images
- updated install to provide mime type information
- updated install to provide gsequencer.appdata.xml

* Sat Dec 01 2018 Joël Krähemann <jkraehemann@gmail.com> 2.1.3-0
- updated Source to point to new minor version directory
- removed build dependency ladspa-cmt-plugins and lv2-swh-plugins

* Sun Nov 04 2018 Joël Krähemann <jkraehemann@gmail.com> 2.37.1-0
- removed patch because functional tests are disabled by default

* Sun Sep 09 2018 Joël Krähemann <jkraehemann@gmail.com> 2.0.1-1
- provide patch to disable functional tests

* Sun Sep 09 2018 Joël Krähemann <jkraehemann@gmail.com> 2.0.1-0
- updated Source to point to new major version directory

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Joël Krähemann <jkraehemann@gmail.com> 1.4.14-1
- updated Source to point to new minor version directory
- disabled strict symbol defs of linker

* Fri Jan 05 2018 Joël Krähemann <jkraehemann@gmail.com> 1.3.1-1
- updated Source to point to new minor version directory

* Fri Dec 22 2017 Joël Krähemann <jkraehemann@gmail.com> 1.2.4-1
- updated Source to point to new minor version directory
- removed libgmp-devel requires since not used anymore

* Sun Oct 15 2017 Joël Krähemann <jkraehemann@gmail.com> 1.1.4-1
- updated Source to point to new minor version directory

* Sun Oct 08 2017 Joël Krähemann <jkraehemann@gmail.com> 1.0.4-1
- updated gsequencer.0-makefile-am.patch to fix globbing issue

* Sun Oct 08 2017 Joël Krähemann <jkraehemann@gmail.com> 1.0.3-1
- did some formating to the spec file, removed empty newline
- merged all Makefile.am related patches to one single patch

* Mon Oct 02 2017 Joël Krähemann <jkraehemann@gmail.com> 1.0.0-1
- provide patch to fix libgsequencer API reference manual

* Sat Sep 16 2017 Joël Krähemann <jkraehemann@gmail.com> 0.9.25-1
- remove patch to fix logo and license since it can be passed as macro
- provide patch to apply different gtk-doc paths
- modified documentation paths

* Tue Aug 22 2017 Joël Krähemann <jkraehemann@gmail.com> 0.9.14-1
- added libpulse dependency
- modified description to tell about pulseaudio support

* Sun Aug 06 2017 Joël Krähemann <jkraehemann@gmail.com> 0.9.5-1
- new upstream

* Fri Aug 04 2017 Joël Krähemann <jkraehemann@gmail.com> 0.9.4-1
- new upstream

* Wed Aug 02 2017 Joël Krähemann <jkraehemann@gmail.com> 0.9.3-1
- modified version because bug fixes available
- modified SOURCE0 because new minor version available

* Mon Jun 26 2017 Joël Krähemann <jkraehemann@gmail.com> 0.8.7-1
- modified version because new features available

* Wed Jun 14 2017 Joël Krähemann <jkraehemann@gmail.com> 0.8.4-1
- removed some patches since applied upstream
- added gettext-devel dependency
- removed make target merged by upstream

* Mon May 22 2017 Joël Krähemann <jkraehemann@gmail.com> 0.8.0-2
- provide 2 more patches to fix unitialized pointer and unit test

* Fri Apr 28 2017 Joël Krähemann <jkraehemann@gmail.com> 0.8.0-1
- removed patch to fix missing type because upstream includes changes

* Wed Apr 19 2017 Joël Krähemann <jkraehemann@gmail.com> 0.7.135-1
- provide patch to fix missing license and logo within about dialog
- provide patch to fix missing type for ags-play-dssi

* Wed Apr 12 2017 Joël Krähemann <jkraehemann@gmail.com> 0.7.122.21-0
- removed patch to fix reference manual because upstream includes changes

* Mon Apr 10 2017 Joël Krähemann <jkraehemann@gmail.com> 0.7.122.20-0
- removed 3 patches since new upstream package contains the changes
- modified screen size for functional tests of xvfb-run to be 1920x1080x24
- added ladspa cmt and lv2 swh plugins as build requires for functional tests
- added patch 2 to fix upstream bug of reference manual

* Mon Mar 20 2017 Joël Krähemann <jkraehemann@gmail.com> 0.7.122.7-1
- provide patch to fix possible SIGSEGV as no soundcard configured

* Wed Mar 15 2017 Joël Krähemann <jkraehemann@gmail.com> 0.7.122.7-0
- removed 3 patches that was applied upstream
- modified libgsequencer blue-print patch because upstream changed
- do make check with xvfb-run

* Wed Mar 08 2017 Joël Krähemann <jkraehemann@gmail.com> 0.7.122.6-3
- make docs noarch

* Tue Mar 07 2017 Joël Krähemann <jkraehemann@gmail.com> 0.7.122.6-2
- provide libgsequencer blue-print patch to install to default linker path
- provide libgsequencer gtk-doc patch to generate application API reference
- provide libgsequencer.xml patch to fix non-existing XML files
- provide libgsequencer.pc patch to make it available

* Thu Mar 02 2017 Joël Krähemann <jkraehemann@gmail.com> 0.7.122.6-1
- modified manpage expression
- modified binary expression
- removed CFLAGS and BINDIR flags of make_build

* Sat Dec 31 2016 Joël Krähemann <jkraehemann@gmail.com> 0.7.122-0
- RPM release

* Tue Dec 27 2016 Joël Krähemann <jkraehemann@gmail.com> 0.7.121-0
- fixed license field

* Mon Dec 26 2016 Joël Krähemann <jkraehemann@gmail.com> 0.7.120-0
- added xml-common requires
- gsequencer-devel-doc owns /usr/share/gtk-doc/
- pass compiler optimization flags
- added missing make install-html
- added build requires of docbook-xsl
- added patch to fix docbook path

* Thu Dec 22 2016 Joël Krähemann <jkraehemann@gmail.com> 0.7.119-0
- removed debian specific directory /usr/share/doc-base

* Tue Dec 13 2016 Joël Krähemann <jkraehemann@gmail.com> 0.7.115-0
- Initial RPM release
- unified usage of buildroot within gsequencer.spec
- run make check during check
