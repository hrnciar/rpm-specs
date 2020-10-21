%define _legacy_common_support 1

# gerbv Package description for Fedora/Free Electronic Lab
#
Name:             gerbv
Version:          2.7.0
Release:          7%{?dist}
Summary:          Gerber file viewer from the gEDA toolkit
License:          GPLv2
URL:              http://gerbv.gpleda.org/
Source:           http://downloads.sourceforge.net/gerbv/%{name}-%{version}.tar.gz

# patch src to handle -Werror=format-security
Patch0:           01-Fix-Werror-format-security-problem.patch

BuildRequires:    gcc-c++
BuildRequires:    automake
BuildRequires:    desktop-file-utils
BuildRequires:    ImageMagick-devel
BuildRequires:    libpng-devel
#BuildRequires:    gtk2-devel
BuildRequires:    pkgconfig(gtk+-2.0)

Requires:         electronics-menu

%description
Gerber Viewer (gerbv) is a viewer for Gerber files. Gerber files
are generated from PCB CAD system and sent to PCB manufacturers
as basis for the manufacturing process. The standard supported
by gerbv is RS-274X.

gerbv also supports drill files. The format supported are known
under names as NC-drill or Excellon. The format is a bit undefined
and different EDA-vendors implement it different.

gerbv is listed among Fedora Electronic Lab (FEL) packages.


%package devel
Summary:          Header files, libraries and development documentation for %{name}
Requires:         %{name} = %{version}-%{release}
Requires:         gtk2-devel, libpng-devel

%description devel
This package contains the header files, libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%prep
%autosetup -p1

%build
# default measurement units set to millimeters
%configure                              \
  --enable-unit-mm                      \
  --disable-update-desktop-database     \
  --disable-static   --disable-rpath    
#  CFLAGS="${RPM_OPT_FLAGS}"             \
#  LIBS="-ldl -lpthread"

# Don't use rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# Clean unused-direct-shlib-dependencies. This should have been already removed in 2.5.0-2 ?
#sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build


%install
%make_install

desktop-file-install --vendor ""               \
    --remove-category Education                \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original                          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%{__rm} -f %{buildroot}%{_libdir}/libgerbv.la
%{__rm} -f  {doc,example}/Makefile*

pushd example/
for dir in * ; do
  [ -d $dir ] && %{__rm} -f $dir/Makefile*
done
popd

pushd doc/
for dir in * ; do
  [ -d $dir ] && %{__rm} -f $dir/Makefile*
done
popd

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO CONTRIBUTORS HACKING
%doc example/
%doc doc/example-code
%doc doc/eagle
%doc doc/sources.txt
%doc doc/aperturemacro.txt
%doc doc/PNG-print
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/gerbv.*
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.geda-user.gerbv.gschema.xml
%{_libdir}/lib%{name}.so.1*


%files devel
%dir %{_includedir}/%{name}-%{version}
%{_includedir}/%{name}-%{version}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libgerbv.pc


%Changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 2.7.0-6
- Enable legacy common support

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Alain <alain DOT vigne DOT 14 AT gmail DOT com> - 2.7.0-2
- Explicitely BR a C++ compiler, to solve FTBFS: libtool did not build the shared lib. libgerbv.so.1*
- Simplify .spec file

* Sun Feb 03 2019 Alain <alain DOT vigne DOT 14 AT gmail DOT com> - 2.7.0-1
- new upstream release
- add patch to cope with gcc compiler options. Upstream has updated this, for next release => Remove the patch for > 2.7.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.6.2-1
- new upstream release 2.6.2 fixes rhbz #1100403

* Tue Apr 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.6.0-14
- spec cleanup / modernization

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.0-12
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 03 2012 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.6.0-1
- new upstream release

* Tue Jul 05 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-2
- Hack libtool to not add rpath.
- Propagate RPM_OPT_FLAGS to CFLAGS.
- Pass -ldl through LIBS.
- Fix date of previous changelog entry.
- Remove "unused-direct-shlib-dependencies" libtool hacking.

* Sun Jul 03 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.5.0-1
- new upstream release

* Thu Jul 01 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.4.0-1
- new upstream release

* Sun Sep 13 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.3.0-3
- Fixed gerbv-2.3.0-1 png failed to open - FEL ticket #47
- Fixed bug 2841371 (segfault on edit->orientation with no layer loaded)

* Sat Jul 11 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.3.0-1
- new upstream release

* Sat Mar 07 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.2.0-3
- added requires electronics-menu #485585

* Thu Jan 22 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.2.0-1
- new upstream release

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.0-3
- Include unowned headers directory.

* Thu Nov 13 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.1.0-2
- BR ImageMagick-devel added

* Thu Nov 13 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.1.0-1
- New upstream release and split into -devel package

* Fri Feb 01 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.0.0-1
- New upstream release

* Tue Dec 04 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0.3-1
- new upstream release

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0.2-3
- mass rebuild for fedora 8 - ppc

* Thu Jun 28 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0.2-2
- remove gdk-pixbuf-devel as BR

* Thu Sep 14 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0.2-1
- Initial package for Fedora Core
