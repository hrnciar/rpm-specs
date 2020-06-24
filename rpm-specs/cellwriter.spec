Summary: Grid-entry natural handwriting input panel
Name: cellwriter
Version: 1.3.5
Release: 18%{?dist}
License: GPLv2+
URL: http://code.google.com/p/cellwriter/
Source0: http://cellwriter.googlecode.com/files/cellwriter_%{version}-1.tar.gz
BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: libXtst-devel
BuildRequires: gtk2-devel
BuildRequires: libgnome-devel

%description
CellWriter is a grid-entry natural handwriting input panel. As 
you write characters into the cells, your writing is instantly 
recognized at the character level. When you press 'Enter' on the 
panel, the input you entered is sent to the currently focused 
application as if typed on the keyboard.

Works well on a Wacom tablet, TabletPC, or any device with a stylus.

%prep
%setup -qn cellwriter

%build
%configure
make %{?_smp_mflags} CFLAGS="$CFLAGS -fcommon" LIBS="$LIBS -lX11 -lm -lXtst"

%install
make install DESTDIR="$RPM_BUILD_ROOT" INSTALL="install -p"

desktop-file-install --delete-original \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
  ${RPM_BUILD_ROOT}/%{_datadir}/applications/cellwriter.desktop


%files
%doc README COPYING TODO AUTHORS
%{_bindir}/cellwriter
%dir %{_datadir}/cellwriter
%{_datadir}/cellwriter/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/cellwriter.svg
%{_datadir}/pixmaps/cellwriter.xpm
%{_mandir}/*/*


%changelog
* Fri Jan 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.3.5-18
- Fix FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.5-12
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.3.5-3
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- cleanup spec file

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Jon Ciesla <limburgher@gmail.com> - 1.3.5-1
- Latest upstream, BZ 833060.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 1.3.4-7.
- Rebuild for libpng 1.5.

* Fri Mar 04 2011 Jon Ciesla <limb@jcomserv.net> - 1.3.4-6.
- Updated description to match relevant keywords, BZ 682014.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 1.3.4-4.
- FTBFS fix, 599941.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 26 2008 Jeremy Katz <katzj@redhat.com> - 1.3.4-1
- Update to 1.3.4

* Thu Apr 24 2008 Jeremy Katz <katzj@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.1-3
- Autorebuild for GCC 4.3

* Tue Dec 11 2007 Jeremy Katz <katzj@redhat.com> - 1.3.1-2
- Add patch to make desktop file validate with stricter desktop-file-utils
- Update the icon cache
- Cleaner URL

* Mon Dec 10 2007 Jeremy Katz <katzj@redhat.com> - 1.3.1-1
- Initial build.

