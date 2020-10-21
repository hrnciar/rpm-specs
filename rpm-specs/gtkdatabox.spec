Name:           gtkdatabox
Version:        0.9.3.1
Release:        5%{?dist}
Summary:        GTK+ widget for fast data display
License:        LGPLv2+
URL:            http://sourceforge.net/projects/gtkdatabox
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gtk2-devel, pkgconfig, autoconf
BuildRequires:  libglade2-devel

%description
GtkDatabox is a widget for the GTK+ library designed to display
large amounts of numerical data fast and easy.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gtk2-devel, pkgconfig

%description    devel
The %{name}-devel package contains libraries, header files, and examples
for developing applications that use %{name}.

%package        libglade2
Summary:        Glade 2 support files for %{name}
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-libglade

%description    libglade2
The %{name}-libglade2 package contains support files for libglade2.

%prep
%autosetup

%build
# need reconfig to support aarch64
autoconf
%configure \
  --disable-static \
  --enable-libglade \
  LIBS="-lm"
# fix rpath libtool issues
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# fix ChangeLog encoding issues
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.tmp && mv -f ChangeLog.tmp ChangeLog
%make_build

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_libdir}/libgtkdatabox-*.so.*

%files devel
%doc examples/*.c
%{_includedir}/gtkdatabox*.h
%{_libdir}/libgtkdatabox.so
%{_libdir}/pkgconfig/gtkdatabox.pc

%files libglade2
%{_libdir}/libglade/2.0/libdatabox.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 06 2020 Eric Work <work.eric@gmail.com> - 0.9.3.1-4
- Remove glade3 subpackage since libgladeui-2.0 is not supported

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.3.1-1
- Update to 0.9.3.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
- Add missing build-dep autoconf

* Sun Mar 24 2013 Eric Work <work.eric@gmail.com> - 0.9.2.0-1
- new upstream version
- drop deprecated GTK feature patches
- enable glade3 subpackage again

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.1.1-7
- Rebuild for new libpng

* Sat Jun 25 2011 Eric Work <work.eric@gmail.com> - 0.9.1.1-6
- Allow deprecated GDK functions
- Disable glade subpackage requires gtk-3.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep  3 2010 Dan Horák <dan[at]danny.cz> 0.9.1.1-4
- fix deprecated GTK 2.22 features

* Thu May 20 2010 Eric Work <work.eric@gmail.com> 0.9.1.1-3
- fix deprecated GTK 2.20 features

* Thu May 20 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.9.1.1-2
- Updated to consume new libgladeui-1.so.9

* Tue Feb 09 2010 Eric Work <work.eric@gmail.com> 0.9.1.1-1
- new upstream version
- enable glade support
- fix new linker problems

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 08 2008 Eric Work <work.eric@gmail.com> 0.9.0.1-1
- new upstream version
- drop patch gcallback

* Mon Sep 01 2008 Eric Work <work.eric@gmail.com> 0.9.0.0-1
- new upstream version
- new gtk-doc documentation
- fix deprecated GTK_SIGNAL_FUNC

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.2.2-2
- Autorebuild for GCC 4.3

* Sat Jan 26 2008 Eric Work <work.eric@gmail.com> 0.8.2.2-1
- new upstream version

* Tue Dec 18 2007 Eric Work <work.eric@gmail.com> 0.8.2.0-1
- new upstream version
- drop patch compilefix
- enable libglade support

* Mon Nov 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.8.0.1-2
- fix license tag
- use rpm optflags

* Mon Nov 26 2007 Eric Work <work.eric@gmail.com> 0.8.0.1-1
- new upstream version

* Tue Mar 20 2007 Eric Work <work.eric@gmail.com> 0.7.0.1-1
- new upstream version

* Sat Nov 11 2006 Eric Work <work.eric@gmail.com> 0.7.0.0-4
- bumped EVR to assure devel replaces FC6

* Fri Sep 15 2006 Eric Work <work.eric@gmail.com> 0.7.0.0-3
- bumped version to prepare for FC6

* Thu Aug 17 2006 Eric Work <work.eric@gmail.com> 0.7.0.0-2
- removed devel post/postun scripts

* Fri Aug 11 2006 Eric Work <work.eric@gmail.com> 0.7.0.0-1
- updated to 0.7.0.0

* Tue Aug 08 2006 Eric Work <work.eric@gmail.com> 0.6.0.0-1
- updated to 0.6.0.0

* Fri Jun 23 2006 Eric Work <work.eric@gmail.com> 0.5.3.0-1
- initial release
