# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# CMake-builds go out-of-tree.
%global _cmake_build_subdir build-%{_target_platform}


Name:		libyui-qt-graph
Version:	2.44.6
Release:	7%{?dist}
Summary:	Qt Graph Widget for libyui

License:	LGPLv2 or LGPLv3
URL:		https://github.com/libyui/%{name}
Source0:	%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	graphviz-devel
BuildRequires:	libyui-devel
BuildRequires:	libyui-qt-devel

Supplements:	(libyui-qt%{?_isa} and graphviz%{?_isa})

%description
This package contains the qt graph widget component
for libyui.


%package devel
Summary:	Files needed for developing with %{name}

Requires:	graphviz-devel%{?_isa}
Requires:	libyui-devel%{?_isa}
Requires:	libyui-qt-devel%{?_isa}
Requires:	%{name}%{?_isa}			== %{version}-%{release}

%description devel
libyui can be used independently of YaST for generic (C++)
applications and has very few dependencies.

You do NOT need this package for developing with libyui.
Using libyui-devel is sufficient for such purpose.  This
package is only needed when you want to develop an extension
for %{name} which is not covered within this plugin.


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
		../examples/{CMake*,.gitignore}		\
		doc/html/*.m*

# Install documentation.
%{__mkdir} -p	%{buildroot}%{?_pkgdocdir}
%{__cp} -a	../package/%{name}.changes doc/html/	\
		../examples/				\
		%{buildroot}%{?_pkgdocdir}

# Hard-link documentation.
%{_bindir}/hardlink -cv %{buildroot}%{?_pkgdocdir}/html
popd


%files
%doc %dir %{?_pkgdocdir}
%license COPYING*
%{_libyui_plugindir}/%{name}.so.%{_libyui_major_so_ver}*


%files devel
%doc %{?_pkgdocdir}/%{name}.changes
%{_includedir}/yui/*
%{_libyui_plugindir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/*


%files doc
# Pickup license-files from main-pkg's license-dir.
# If there's no license-dir they are picked up by %%doc previously.
%{?_licensedir:%license %{_datadir}/licenses/%{name}*}
%doc %{?_pkgdocdir}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.44.6-6
- Fix FTBFS - updated path of hardlink

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.6-1
- Initial import (rhbz#960201)

* Sun Aug 13 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.6-0.1
- New upstream release, fixes FTBFS for Qt5Svg and Qt5X11Extras

* Sun Apr 23 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.5-0.3
- Remove .gitignore-file from packaged examples

* Sun Apr 16 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.5-0.2
- Add examples to %%doc

* Sat Apr 15 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.5-0.1
- Initial rpm-release (rhbz#960201)
