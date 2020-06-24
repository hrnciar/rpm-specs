Name:		gnome-mud
Version:	0.11.2
Release:	26%{?dist}
Summary:	A MUD client for GNOME

License:	GPLv2+
URL:		http://live.gnome.org/GnomeMud
Source:		http://ftp.gnome.org/pub/gnome/sources/%{name}/0.11/%{name}-%{version}.tar.gz

# https://bugzilla.gnome.org/show_bug.cgi?id=625739
Patch0:		gnome-mud-desktop.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=629472
Patch1:		gnome-mud-vte.patch

BuildRequires:  gcc
BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: pcre-devel
BuildRequires: gstreamer-devel
BuildRequires: gnet2-devel
BuildRequires: vte-devel
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: libglade2-devel
BuildRequires: GConf2-devel

Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2

%description
GNOME-MUD is a simple MUD client for GNOME. It supports scripting in
Python and C, and tabbed mudding.

%prep
%setup -q
%patch0 -p 1
%patch1 -p 1
iconv -f iso-8859-1 -t utf8 ./AUTHORS > ./AUTHORS.utf8
mv ./AUTHORS.utf8 ./AUTHORS

%build
%configure --enable-mccp --enable-gstreamer
make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%pre
if [ "$1" -gt 1 ] ; then
	export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
	gconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
fi

%post 
export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null

%preun
if [ "$1" -eq 0 ] ; then
	export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
	gconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%config(noreplace) %{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6.gz

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.2-21
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.11.2-10
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.11.2-8
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.11.2-6
- Rebuilt for gcc bug 634757

* Sun Sep 12 2010 Sean Middleditch <sean@middleditch.us> - 0.11.2-5
- Patch for compilation with sealed VTE properties.

* Sat Jul 21 2010 Sean Middleditch <sean@middleditch.us> - 0.11.2-4
- Fix .desktop file categories.

* Wed Jun 18 2009 Sean Middleditch <sean@middleditch.us> - 0.11.2-3
- Rebuild against upstream's 0.11.2 tarball.
- Apply UTF8 conversion to AUTHORS file.
- Mark gconf schema file as config(noreplace).

* Wed Jun 05 2009 Sean Middleditch <sean@middleditch.us> - 0.11.2-2
- Cleaned up spec file compliance.
- Removed use of scrollkeeper until upstream fixes documentation.

* Wed Apr 13 2009 Sean Middleditch <sean@middleditch.us> - 0.11.2-1
- Initial Fedora package.
