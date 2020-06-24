# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# CMake-builds go out-of-tree.
%global _cmake_build_subdir build-%{_target_platform}


Name:		libyui-gtk
Version:	2.44.9
Release:	15%{?dist}
Summary:	Gtk3 User Interface for libyui

License:	LGPLv2 or LGPLv3
URL:		https://github.com/libyui/%{name}
Source0:	%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?fedora} >= 25 || 0%{?rhel} >= 8
# Patches submitted upstream.
# See:  https://github.com/libyui/libyui-gtk/pull/58
Patch10:	https://github.com/besser82/libyui-gtk/commit/cc3ac74b1186b33bd9e6dcd532e189b5b4cb29bb.patch#/libyui-gtk-2.44.9-fix_misleading_indentation.patch
Patch11:	https://github.com/besser82/libyui-gtk/commit/5077aae7d96d607d96600a38484384ca8e5a0dee.patch#/libyui-gtk-2.44.9-fix_gtk_style_context_get_background_color.patch
Patch12:	https://github.com/besser82/libyui-gtk/commit/e48985c2384ee09fe60fd06003b013e90c94205a.patch#/libyui-gtk-2.44.9-fix_gtk_container_set_resize_mode.patch
Patch13:	https://github.com/besser82/libyui-gtk/commit/21ecc082bdf5628b91bb844e6993de4789e5d15d.patch#/libyui-gtk-2.44.9-fix_gtk_window_set_has_resize_grip.patch
Patch14:	https://github.com/besser82/libyui-gtk/commit/2c5c33d978b95bc9dd7613ddfc61810fa42c2ec8.patch#/libyui-gtk-2.44.9-fix_gtk_misc_set_alignment.patch
Patch15:	https://github.com/besser82/libyui-gtk/commit/a7b7b50c21f6e59b1325143dcbdf8555d4027804.patch#/libyui-gtk-2.44.9-fix_gtk_misc_set_padding.patch
Patch16:	https://github.com/besser82/libyui-gtk/commit/8ab57a0d462e3d65859cd56bcd1b73eacba9740d.patch#/libyui-gtk-2.44.9-fix_gtk_alignment_set_padding.patch
Patch17:	https://github.com/besser82/libyui-gtk/commit/d963977c528dc694f06ecd52a47c7f2129e1aca0.patch#/libyui-gtk-2.44.9-fix_gtk_alignment_new.patch
Patch18:	https://github.com/besser82/libyui-gtk/commit/7f6cc848f21e9f76c7247e46e934c80c339a0371.patch#/libyui-gtk-2.44.9-fix_gdk_cursor_new.patch
Patch19:	https://github.com/besser82/libyui-gtk/commit/11884a67cf26ed46e967dca9dee5e6fa32eb92b6.patch#/libyui-gtk-2.44.9-fix_gtk_widget_get_root_window.patch
Patch20:	https://github.com/besser82/libyui-gtk/commit/1191d564180b0a2ca489fdc762c302cc65a8c876.patch#/libyui-gtk-2.44.9-fix_gtk_menu_popup.patch
Patch21:	https://github.com/besser82/libyui-gtk/commit/355cbac51273f87b68e19430f591cee2c16766ed.patch#/libyui-gtk-2.44.9-fix_gtk_tree_view_set_rules_hint.patch
Patch22:	https://github.com/besser82/libyui-gtk/commit/509292d88c1cf4bf198aab2d7e5e5d075f301722.patch#/libyui-gtk-2.44.9-fix_gtk_arrow_new.patch
Patch23:	https://github.com/besser82/libyui-gtk/commit/a7eb80016ca13d33872b558cdb00eac353b3cde1.patch#/libyui-gtk-2.44.9-fix_display_get_device_manager_gdk_device_manager_get_client_pointer.patch
%endif # 0%%{?fedora} >= 25 || 0%%{?rhel} >= 8

BuildRequires:  gcc-c++
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	gtk3-devel
BuildRequires:	libyui-devel

Supplements:	(libyui%{?_isa} and gtk3%{?_isa})

%description
This package contains the Gtk3 user interface component
for libyui.


%package devel
Summary:	Files needed for developing with %{name}

Requires:	gtk3-devel%{?_isa}
Requires:	libyui-devel%{?_isa}
Requires:	%{name}%{?_isa}		== %{version}-%{release}

%description devel
libyui can be used independently of YaST for generic (C++)
applications and has very few dependencies.

You do NOT need this package for developing with libyui.
Usinglibyui-devel is sufficient for such purpose. This
package is only needed when you want to develop an extension
for %{name} which is not covered within the UI-plugin.


%package doc
Summary:	Documentation files for %{name}
BuildArch:	noarch

BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	hardlink

%description doc
This package includes the developer's documentation as HTML
for %{name}.


%prep
%autosetup -p 1
./bootstrap.sh


%build
%{__mkdir} -p %{_cmake_build_subdir}
pushd %{_cmake_build_subdir}
%cmake							\
	-DENABLE_WERROR=OFF				\
	-DYPREFIX=%{_prefix}				\
	-DLIB_DIR=%{_libdir}				\
	-DCMAKE_BUILD_TYPE=RELEASE			\
	-DRESPECT_FLAGS=ON				\
	-DSKIP_LATEX=ON					\
	..

%make_build
%make_build docs
popd


%install
pushd %{_cmake_build_subdir}
%{__mkdir} -p	%{buildroot}%{_libdir}/yui		\
		%{buildroot}%{_datadir}/%{name}/theme

%make_install

# Delete obsolete files.
%{__rm} -rf	%{buildroot}%{_defaultdocdir}		\
		doc/html/*.m*

# Install documentation.
%{__mkdir} -p	%{buildroot}%{?_pkgdocdir}
%{__cp} -a	../package/%{name}.changes doc/html/	\
		%{buildroot}%{?_pkgdocdir}

# Hard-link documentation.
%{_bindir}/hardlink -cv %{buildroot}%{?_pkgdocdir}/html
popd


%files
%doc %dir %{?_pkgdocdir}
%license COPYING*
%{_libdir}/yui/%{name}.so.%{_libyui_major_so_ver}*

%files devel
%doc %{?_pkgdocdir}/%{name}.changes
%{_includedir}/yui/*
%{_libdir}/yui/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

%files doc
# Pickup license-files from main-pkg's license-dir
# If there's no license-dir they are picked up by %%doc previously
%{?_licensedir:%license %{_datadir}/licenses/%{name}*}
%doc %{?_pkgdocdir}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.44.9-14
- Fix FTBFS - updated path of hardlink

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-9
- Dependency on cmake-filesystem is autogenerated now
- Skip building of LaTeX-docs

* Mon Jul 31 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-8
- Apply patches only on fc25+ or el8+

* Sun Jul 30 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-7
- Require cmake-filesystem

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.44.9-5
- Rebuilt for Boost 1.64

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-4
- Rebuilt for bootstrapping new arch: s390x

* Wed Apr 19 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-3
- Add patches submitted upstream

* Fri Apr 14 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-2
- Change Supplements: back to gtk3, since libYUI provides selection
  of UI-plugin based on used desktop environment

* Fri Apr 14 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-1
- New upstream release

* Thu Apr 13 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.8-4
- Rebuilt for libyui.so.8

* Wed Apr 12 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.8-3
- Optimized Supplements: to be not too generic
- Spec-file cosmetics

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.8-2
- Use rich-dependencies instead of virtual provides
- Get major so-ver from macro

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.8-1
- New upstream release fixing GTK-warnings

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.44.7-2
- Rebuilt for Boost 1.63

* Tue Mar 29 2016 Björn Esser <fedora@besser82.io> - 2.44.7-1
- new upstream release
- handle %%license and %%doc properly

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.44.5-14
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.44.5-13
- Rebuilt for Boost 1.59

* Thu Aug 27 2015 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-12
- rebuilt for so-name-bump in libyui-3.2.1

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.44.5-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.44.5-10
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.44.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 2.44.5-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 02 2015 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-7
- rebuilt for libyui-3.1.5, again

* Mon Feb 02 2015 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-6
- Rebuild for boost 1.57.0

* Tue Jan 20 2015 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-5
- rebuilt for libyui-3.1.5
- keep doc-files in unfied %%{_pkgdocdir}
- small improvements to spec-file

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.44.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.44.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-2
- no need to provide `%%{name}-devel-common`

* Fri May 23 2014 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-1
- new upstream release

* Fri May 23 2014 Björn Esser <bjoern.esser@gmail.com> - 2.43.7-3
- Rebuild for boost 1.55.0

* Tue Mar 18 2014 Björn Esser <bjoern.esser@gmail.com> - 2.43.7-2
- rebuilt for libyui-3.0.13
- remove build of pdf-autodocs
- remove the devel-common subpkg
- minor improvents on spec

* Fri Aug 30 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.7-1
- new upstream version
- restructured spec to match with libyui

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.3-3
- build fails on rawhide with -Werror enabled, because of
  'gtk_widget_modify_fg' is deprecated in gtk3-devel >= 3.9.0,
  use 'gtk_widget_override_color' instead [-Werror=deprecated-declarations]
- informed upstream and provided build-logs
- added cmake -DENABLE_WERROR=OFF

* Thu May 16 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.3-2
- changed Provides: `yui_ui =` from `version` to `major_so_ver`
- install lib*.so.`major_so_ver`* in main-pkg not lib*.so.*
- add `-DRESPECT_FLAGS=ON`, will be honored by libyui <= 3.0.5
- removed macros from changelog

* Wed May 15 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.3-1
- new upstream version
- adjusted libyui-devel min-version
- added needed bootstrap to prep

* Mon May 13 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.2-1
- Initial RPM release.
