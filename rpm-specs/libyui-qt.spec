# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# release commit because SUSE didn't tag it :(
%global relcommit cf7abc3dce267dd8922d7a0b5939c3fec5460985

# CMake-builds go out-of-tree.
%undefine __cmake_in_source_build

Name:		libyui-qt
Version:	2.53.0
Release:	1%{?dist}
Summary:	Qt User Interface for libyui

License:	LGPLv2 or LGPLv3
URL:		https://github.com/libyui/%{name}
# No tag :(
#Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	%{url}/archive/%{relcommit}/%{name}-%{version}.tar.gz

BuildRequires:	boost-devel
BuildRequires:	cmake3
BuildRequires:	fontconfig-devel
BuildRequires:	libyui-devel >= 3.10.0
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)

Supplements:	(libyui%{?_isa} and qt5-qtbase-gui%{?_isa})

%description
This package contains the qt user interface component
for libyui.


%package devel
Summary:	Files needed for developing with %{name}

Requires:	fontconfig-devel%{?_isa}
Requires:	libyui-devel%{?_isa}
Requires:	%{name}%{?_isa}			== %{version}-%{release}
Requires:	qt5-qtbase-devel%{?_isa}
Requires:	qt5-qtsvg-devel%{?_isa}
Requires:	qt5-qtx11extras-devel%{?_isa}

%description devel
libyui can be used independently of YaST for generic (C++)
applications and has very few dependencies.

You do NOT need this package for developing with libyui.
Using libyui-devel is sufficient for such purpose.  This
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
%autosetup -n %{name}-%{relcommit} -p1
./bootstrap.sh


%build
%cmake							\
       	-DENABLE_WERROR=OFF                             \
	-DYPREFIX=%{_prefix}				\
	-DLIB_DIR=%{_libdir}				\
	-DCMAKE_BUILD_TYPE=RELEASE			\
	-DRESPECT_FLAGS=ON				\
	-DSKIP_LATEX=ON

%cmake_build
%cmake_build --target docs


%install
%{__mkdir} -p	%{buildroot}%{_libdir}/yui		\
		%{buildroot}%{_datadir}/%{name}/theme

%cmake_install

pushd %{_vpath_builddir}
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
* Sat Aug 01 2020 Neal Gompa <ngompa13@gmail.com> - 2.53.0-1
- Rebase to 2.53.0 (#1669821)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.47.1-16
- Fix FTBFS - updated path of hardlink

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.47.1-13
- Fix rpc build issue

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Björn Esser <besser82@fedoraproject.org> - 2.47.1-10
- Dependency on cmake-filesystem is autogenerated now
- Skip building of LaTeX-docs

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Björn Esser <besser82@fedoraproject.org> - 2.47.1-8
- Require cmake-filesystem

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.47.1-6
- Rebuilt for Boost 1.64

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 2.47.1-5
- Rebuilt for bootstrapping new arch: s390x

* Fri Apr 14 2017 Björn Esser <besser82@fedoraproject.org> - 2.47.1-4
- Change Supplements: back to qt5-qtbase-gui, since libYUI provides
  selection of UI-plugin based on used desktop environment
- Fix hardlinking of html-docs

* Thu Apr 13 2017 Björn Esser <besser82@fedoraproject.org> - 2.47.1-3
- Rebuilt for libyui.so.8

* Wed Apr 12 2017 Björn Esser <besser82@fedoraproject.org> - 2.47.1-2
- Optimized Supplements: to be not too generic
- Spec-file cosmetics

* Tue Apr 11 2017 Björn Esser <besser82@fedoraproject.org> - 2.47.1-1
- New upstream release

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.46.21-5
- Use rich-dependencies instead of virtual provides
- Get major so-ver from macro

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.46.21-3
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.46.21-2
- Rebuilt for Boost 1.63

* Tue Mar 29 2016 Björn Esser <fedora@besser82.io> - 2.46.21-1
- new upstream release
- handle %%license and %%doc properly

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.46.18-3
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.46.18-2
- Rebuilt for Boost 1.59

* Thu Aug 27 2015 Björn Esser <bjoern.esser@gmail.com> - 2.46.18-1
- new upstream release

* Mon Aug 10 2015 Björn Esser <bjoern.esser@gmail.com> - 2.46.13-8
- disable '-Werror'

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46.13-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.46.13-6
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 2.46.13-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 02 2015 Björn Esser <bjoern.esser@gmail.com> - 2.46.13-3
- rebuilt for libyui-3.1.5, again

* Mon Feb 02 2015 Björn Esser <bjoern.esser@gmail.com> - 2.46.13-2
- Rebuild for boost 1.57.0

* Tue Jan 20 2015 Björn Esser <bjoern.esser@gmail.com> - 2.46.13-1
- new upstream release (#1183542)
- rebuilt for libyui-3.1.5
- keep doc-files in unfied %%{_pkgdocdir}
- small improvements to spec-file

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Björn Esser <bjoern.esser@gmail.com> - 2.46.1-2
- no need to provide `%%{name}-devel-common`

* Fri May 23 2014 Björn Esser <bjoern.esser@gmail.com> - 2.46.1-1
- new upstream release (#1051417)

* Fri May 23 2014 Björn Esser <bjoern.esser@gmail.com> - 2.43.5-3
- Rebuild for boost 1.55.0

* Tue Mar 18 2014 Björn Esser <bjoern.esser@gmail.com> - 2.43.5-2
- rebuilt for libyui-3.0.13
- remove build of pdf-autodocs
- remove the devel-common subpkg
- minor improvents on spec

* Fri Aug 30 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.5-1
- new upstream version
- restructured spec to match with libyui

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.3-2
- changed Provides: `yui_ui =` from `version` to `major_so_ver`
- install lib*.so.`major_so_ver`* in main-pkg not lib*.so.*
- add `-DRESPECT_FLAGS=ON`, will be honored by libyui >= 3.0.5
- removed macros from changelog

* Wed May 15 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.3-1
- new upstream version
- adjusted libyui-devel min-version
- added needed bootstrap to prep

* Mon May 13 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.2-1
- Initial RPM release.
