%define gtk2version %(pkg-config gtk+-2.0 --modversion 2> /dev/null)
%define nogtk2 %(pkg-config gtk+-2.0 --modversion &> /dev/null; echo $?)

#%define git_head 8f8397a
#%define checkout 20100807
#%define alphatag %{checkout}.git%{git_head}

Name:           gtk-nodoka-engine
Version:        0.7.5
Release:        20%{?dist}
Summary:        The Nodoka Gtk2 Theme Engine

License:        GPLv2+
URL:            http://fedorahosted.org/nodoka
Source0:        https://fedorahosted.org/released/nodoka/gtk-nodoka-engine-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gtk2-devel >= 2.18

%if 0%{?nogtk2}
Requires:       gtk2
%else
Requires:       gtk2 >= %{?gtk2version}
%endif
Requires:       nodoka-filesystem
Provides:       gtk2-nodoka-engine = %{version}-%{release}

%description
Nodoka is a Murrine engine based GTK+ theme engine. The package is shipped with 
a default Nodoka theme featuring the Gtk2 engine.

%package extras
Summary:  Extra themes for Nodoka Gtk2 theme engine
Requires: %{name} >= 0.6.90.1
Provides: gtk2-nodoka-engine-extras = %{version}-%{release}

BuildArch:      noarch

%description extras
This package contains extra themes fot the Nodoka Gtk2 theme engine.
%prep
%setup -q


%build
%configure --with-gtk=2.0
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#remove .la files
find $RPM_BUILD_ROOT -name *.la | xargs rm -f || true


%files
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README TODO
%{_libdir}/gtk-2.0/2.10.0/engines/libnodoka.so
%{_datadir}/themes/Nodoka/*

%files extras
%doc COPYING
%{_datadir}/themes/Nodoka-*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.5-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Martin Sourada <mso@fedoraproject.org> - 0.7.5-1
- Add gtk2-* virtual provides to prepare for comming of gtk3 version of the 
  engine
- Make the -extras subpackages noarch
- New upstream release
  - adds support for 'entry-progress' detail
  - all patches upstreamed
  - can be built with gtk3

* Sat Jan 23 2010 Martin Sourada <mso@fedoraproject.org> - 0.7.2-8
- Honor GtkEntry::transparent-bg-hint (rhbz #489111)

* Sun Jan 10 2010 Martin Sourada <mso@fedoraproject.org> - 0.7.2-7
- Fix source URL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Martin Sourada <mso@fedoraproject.org> - 0.7.2-5
- Correctly grey out checkboxes in tree-view (rhbz #513454)

* Sat Mar 07 2009 Maritn Sourada <mso@fedoraproject.org> - 0.7.2-4
- Add missing check for widget when getting RTL info

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 30 2008 Martin Sourada <mso@fedoraproject.org> - 0.7.2-2
- Add support for GtkScale trough-side-details and fill-level (rhbz #477941)
- Support selection and hilight coloring for separator (rhbz #478443)

* Sun Nov 02 2008 Martin Sourada <mso@fedoraproject.org> - 0.7.2-1
- New upstream release, fix misrender in menus on some systems (rhbz #469398)

* Mon Sep 15 2008 Martin Sourada <mso@fedoraproject.org> - 0.7.1-2
- Fix cairo context leak (rhbz #462259)

* Tue Jul 22 2008 Martin Sourada <martin.sourada@gmail.com> - 0.7.1-1
- New bugfix release

* Tue May 20 2008 Martin Sourada <martin.sourada@gmail.com> - 0.7.0-2
- Don't own %%{_datadir}/themes/Nodoka dir, instead require nodoka-filesystem

* Mon Apr 14 2008 Martin Sourada <martin.sourada@gmail.com> - 0.7.0-1
- Update to stable

* Thu Apr 03 2008 Martin Sourada <martin.sourada@gmail.com> - 0.7.0-0.4.gitab3ed15
- Update to latest git

* Wed Apr 02 2008 Martin Sourada <martin.sourada@gmail.com> - 0.7.0-0.3.git98ce81e
- Update to latest git

* Sat Mar 08 2008 Martin Sourada <martin.sourada@gmail.com> - 0.6.99.1-1
- 0.7 RC1

* Fri Feb 08 2008 Martin Sourada <martin.sourada@gmail.com> - 0.6.90.2-2
- Rebuild for gcc 4.3
- Use full source path

* Sat Jan 26 2008 Martin Sourada <martin.sourada@seznam.cz> - 0.6.90.2-1
- Update to 0.7. beta 2 release
 - mostly bug fixes

* Sat Jan 05 2008 Martin Sourada <martin.sourada@seznam.cz> - 0.6.90.1-1
- Update to 0.7 beta 1 release
 - Extra themes add to -extras subpackage

* Mon Oct 29 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.6-5
- fix gimp crashing in some dialogs when using Small theme
 - rhbz #291121 and rhbz #355931

* Mon Sep 24 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.6-4
- update the treeview patch
 - rhbz #297271 and rhbz #302551

* Sun Sep 23 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.6-3
- Require at least the version of gtk it was build against
 - rhbz #301851 (patch from Ignacio Vazquez-Abrams)

* Thu Sep 20 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.6-2
- Add user specified tooltips coloring
- Fix colours in unfocused GTKTreeView (rhbz #297271)

* Sat Aug 25 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.6-1
- new version
  -- first stable
  -- fixes checkbutton firefox positioning issue

* Sun Aug 19 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.5.90-1
- new version

* Thu Aug 09 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.5.3-2
- update License: field to GPLv2

* Sun Aug 05 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.5.3-1
- new version

* Sat Aug 04 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.5.2-1
- new version

* Fri Jul 27 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.5-2
- add Requires: gtk2 for engines directory ownership
- remove --enable-animation
- remove Obsoletes/Provides, not needed now

* Wed Jul 25 2007 Daniel Geiger <dgeiger_343@yahoo.com> - 0.5-1
- Numerous Nodoka specific themeing adjustments (so a large version number jump), including:
 - Adjustment of arrow styling
 - Frames and notebooks now use roundness
 - Adjustment of scrollbar handle styling
 - Scale sliders now use same handle styling as scrollbars
 - Adjustment of resize handle styling
 - Menubaritems are now tab-like, use roundness; menuitems are squared
 - Changing of gtkrc engine configuration options to more fit the Nodoka style (see README), plus general code tweaks

* Mon Jul 16 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.2.1-1
- new upstream version
- fix scrollbar coloring

* Mon Jul 16 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.2-1
- new upstream version
- new, reworked function for setting cairo gradients
- add shadows to buttons and editboxes
- rework radiobutton and checkbutton

* Fri Jul 13 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.1-1
- split metacity and metatheme into separate package in upstream

* Fri Jul 13 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1-1
- merge with Nodoka Theme both in upstream and in rpm
- patches included in upstream

* Thu Jul 12 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.1-2
- Some patches to make it look more like we want

* Thu Jul 12 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.1-1
- Initial release
