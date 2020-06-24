%define gtkglext_major 1.0
%define gtkglextmm_major 1.2
%define gtkmm_major 2.4

Summary: C++ wrapper for GtkGlExt
Name: gtkglextmm
Version: 1.2.0
Release: 32%{?dist}
License: LGPLv2+
URL: http://projects.gnome.org/gtkglext/

Source0: http://downloads.sourceforge.net/gtkglext/%{name}-%{version}.tar.gz
Patch0: gtkglextmm-1.2.0-aclocal.diff
Patch1: fix_ftbfs_gtk_2_20.patch
Patch2: fix_ftbfs_gtk_2_36.patch
Patch3: fix_ftbfs_gtk_2_37.patch

BuildRequires: gcc-c++
BuildRequires: gtkglext-devel >= %{gtkglext_major}
BuildRequires: gtkmm24-devel >= %{gtkmm_major}

%description
gtkglextmm is a C++ wrapper for GtkGlExt, an OpenGL extension to GTK+.

%package devel
Summary: Development tools for gtkglextmm

Requires: %{name} = %{version}
Requires: gtkmm24-devel
Requires: gtkglext-devel

%description devel
The gtkglextmm-devel package contains the header files, static libraries,
and developer docs for gtkglextmm.

%prep
%setup -q -n gtkglextmm-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# file-not-utf8
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 -t utf-8 README > README.conv && mv -f README.conv README

# zero-length
echo '# Nothing' >> tools/m4/convert_gtkglext.m4

%build
%configure --disable-static --disable-dependency-tracking

# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
DESTDIR=$RPM_BUILD_ROOT make install

%files
%doc ChangeLog README AUTHORS COPYING.LIB COPYING NEWS
%{_libdir}/libgtkglextmm-x11-*so.*
%{_libdir}/libgdkglextmm-x11-*so.*

%files devel
%{_includedir}/*
%{_libdir}/%{name}-%{gtkglextmm_major}
%{_libdir}/lib*la
%{_libdir}/lib*so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%dir %{_datadir}/doc/%{name}-%{gtkglextmm_major}
%doc %{_datadir}/doc/%{name}-%{gtkglextmm_major}/html/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.0-22
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-18
- Corrected bogus date in %%changelog
- Added another patch to solve FTBFS on F20+

* Sun May 19 2013 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-17
- Added Patch from Debian so this can be built in F19+
- Remove rpath from libtool
- Convert docs to UTF8
- Remove zero-length TODO from doc
- Add comment to zero-length convert_gtkglext.m4
- Updated URL and Source0 URL

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.0-14
- Add debian patch to fix FTBFS

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-13
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2.0-8
- Include unowned doc directories in -devel pkg.
- post/postun: execute ldconfig directly

* Fri Jul 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.0-7
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.0-6
- Autorebuild for GCC 4.3

* Mon Sep 11 2006 Gilles Gagniard <gilles.gagniard@gmail.com> 1.2.0-5
- Rebuild for FC6

* Tue Jun 06 2006 Ralf Corsépius <rc040203@freenet.de> 1.2.0-4
- Add --disable-dependency-tracking.
- Fix broken gtkglmmext.m4 (PR 194201).

* Wed May 24 2006 Ralf Corsépius <rc040203@freenet.de> 1.2.0-3
- Increment Release, add %%{?dist}.

* Wed May 17 2006 Gilles Gagniard <gilles.gagniard@gmail.com> 1.2.0-2
- Removed unnecessary dependencies

* Fri May 12 2006 Gilles Gagniard <gilles.gagniard@gmail.com> 1.2.0-1
- First version of the package
