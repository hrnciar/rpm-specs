Summary:	Resolution Switching Applet
Name:		resapplet
Version:	0.1.4
Release:	24%{?dist}
License:	GPLv2+ and GPLv2
# This is the best we have to silence rpmlint:
URL:		http://svn.gnome.org/viewcvs/resapplet/
# Source obtained from OpenSuSE
Source:		resapplet-%{version}.tar.bz2
Source1:	resapplet.desktop.in
Patch1:		resapplet-transparent-trayicon.patch
Patch2:		resapplet-susebug25115.patch
Patch3:		resapplet-rotate-wacom.patch
Patch4:		resapplet-0.1.1-link_X11.patch
Patch5:		resapplet-0.1.4-properties.patch
BuildRequires:  gcc
BuildRequires:	gnome-icon-theme gnome-themes libgnomeui-devel 
BuildRequires:	intltool, automake, gettext, desktop-file-utils
Requires:	libgnomeui >= 2.2 gtk2 >= 2.4 
#Requires: gconf-editor >= 2.6 
Requires:	gnome-icon-theme

%description
Resapplet is a simple utility that sits in the system notification area
and allows switching the resolution and refresh rate.  It uses the
xrandr extensions to switch the resolution on-the-fly and user
resolution preferences to save the resolution.

It works in both GNOME and KDE, because it uses the system notification
area.

%prep
%setup -q 
cp -a %{S:1} . 
%patch1 -p0
%patch2 -p0
%patch3 -p1 -b .wacom
%patch4 -p1 -b .lX11
%patch5 -p1

%build
#glib-gettextize
aclocal
intltoolize --force
autoheader
automake --add-missing
autoconf
export CFLAGS="$RPM_OPT_FLAGS"

%configure	--datadir=%{_datadir} \
		--libdir=%{_libdir} \
		--localstatedir=%{_libdir} \
		--prefix=%{_prefix}
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original		\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications		\
	--add-category Utility					\
	--add-category X-Red-Hat-Base				\
	$RPM_BUILD_ROOT%{_datadir}/applications/resapplet.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome/autostart/
# install autostart file
cp $RPM_BUILD_ROOT%{_datadir}/applications/resapplet.desktop $RPM_BUILD_ROOT%{_datadir}/gnome/autostart/
%find_lang %name

%files -f %name.lang
%doc COPYING README
%{_bindir}/resapplet
%{_datadir}/applications/*resapplet.desktop
%{_datadir}/gnome/autostart/*resapplet.desktop
%{_datadir}/icons/hicolor/16x16/apps/resapplet.png
%{_datadir}/icons/hicolor/22x22/apps/resapplet.png
%{_datadir}/icons/hicolor/24x24/apps/resapplet.png
%{_datadir}/icons/hicolor/32x32/apps/resapplet.png
%{_datadir}/icons/hicolor/scalable/apps/resapplet.svg

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-17
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 0.1.4-8
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.4-4
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep  3 2010 Radek Vokal <rvokal@redhat.com> - 0.1.4-2
- recreated wacom patch

* Fri Sep  3 2010 Radek Vokal <rvokal@redhat.com> - 0.1.4-1
- update to 0.1.4 from Suse trunk
- drop dependency on s-c-display

* Tue Mar 23 2010 Radek Vokal <rvokal@redhat.com>
- patch from bruno@wolff.to fixes DSO Linking (#564599)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.1-7
- Autorebuild for GCC 4.3

* Thu Sep  6 2007 Stepan Kasal <skasal@redhat.com> 0.1.1-6
- resapplet.desktop.in; s/SystemTools/System/, to conform with
  http://standards.freedesktop.org/menu-spec/latest/apa.html
- Fix License: tag, add Url:

* Fri Dec 22 2006 Radek Vokál <rvokal@redhat.com> 0.1.1-5
- Call automake with "--add-missing".
- Call aclocal before intltoolize.

* Tue Dec 12 2006 Radek Vokál <rvokal@redhat.com> 0.1.1-4
- remove suse icons
- add scriplets 

* Thu Dec  7 2006 Radek Vokál <rvokal@redhat.com> 0.1.1-3
- fix desktop file

* Wed Dec  6 2006 Radek Vokál <rvokal@redhat.com> 0.1.1-2
- spec file changes

* Wed Dec  6 2006 Radek Vokál <rvokal@redhat.com> 0.1.1-1
- initial Fedora build
