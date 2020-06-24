# Define libsuffix, minimum libyui-devel version
# and so-version of libyui.
%global libsuffix yui
%global libname lib%{libsuffix}
%global devel_min_ver 3.0.4

# No proper release-tags, yet.  :(
%global commit b508e88ff9ee76ce7419af649f7a9c877946d702
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20140119
%global git_ver -git%{shortcommit}.%{gitdate}
%global git_rel .git%{shortcommit}.%{gitdate}

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# CMake-builds go out-of-tree.
%global _cmake_build_subdir build-%{?_arch}%{?dist}


Name:			%{libname}-mga-qt
Version:		1.0.3
Release:		0.20%{?git_rel}%{?dist}
Summary:		Libyui-Qt extensions for Mageia tools

License:		LGPLv2 or LGPLv3
URL:			https://github.com/xquiet/%{name}
Source0:		%{url}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?git_ver}.tar.gz

BuildRequires:		boost-devel
BuildRequires:		cmake				>= 2.8
BuildRequires:		%{libname}-devel		>= %{devel_min_ver}
BuildRequires:		%{libname}-mga-devel
BuildRequires:		%{libname}-qt-devel

Supplements:		(libyui-mga%{?_isa} and libyui-qt%{?_isa})

%description
This package contains the Libyui-Qt extensions for Mageia tools.


%package devel
Summary:		Files needed for developing with %{name}

Requires:		%{libname}-devel%{?_isa}	>= %{devel_min_ver}
Requires:		%{libname}-mga-devel%{?_isa}
Requires:		%{libname}-qt-devel%{?_isa}
Requires:		%{name}%{?_isa}			== %{version}-%{release}

%description devel
%{libname} can be used independently of YaST for generic (C++)
applications and has very few dependencies.

You do NOT need this package for developing with %{libname}.
Using %{libname}-devel is sufficient for such purpose. This
package is only needed when you want to develop an extension
for %{name}.


%package doc
Summary:		Documentation files for %{name}
BuildArch:		noarch

BuildRequires:		doxygen
BuildRequires:		graphviz
BuildRequires:		hardlink

%description doc
This package includes the developer's documentation as HTML
for %{name}.


%prep
%setup -qn %{name}-%{commit}
./bootstrap.sh


%build
%{__mkdir} -p %{_cmake_build_subdir}
pushd %{_cmake_build_subdir}
%cmake							\
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
%{__mkdir} -p	%{buildroot}%{_libdir}/%{libsuffix}	\
		%{buildroot}%{_datadir}/%{name}/theme

%make_install

# Delete obsolete files.
%{__rm} -rf	%{buildroot}%{_defaultdocdir}		\
		doc/html/*.m*

# Hard-link documentation.
%{_bindir}/hardlink -cv doc/html

# Install documentation.
%{__mkdir} -p	%{buildroot}%{?_pkgdocdir}
%{__cp} -a	../ChangeLog doc/html/			\
		%{buildroot}%{?_pkgdocdir}
popd


%files
%doc %dir %{?_pkgdocdir}
%license COPYING*
%{_libdir}/%{libsuffix}/%{name}.so.%{_libyui_major_so_ver}*

%files devel
%doc %{?_pkgdocdir}/ChangeLog
%{_includedir}/%{libsuffix}/*
%{_libdir}/%{libsuffix}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

%files doc
# Pickup license-files from main-pkg's license-dir
# If there's no license-dir they are picked up by %%doc previously
%{?_licensedir:%license %{_datadir}/licenses/%{name}*}
%doc %{?_pkgdocdir}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.20.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.3-0.19.gitb508e88.20140119
- Fix FTBFS - updated path of hardlink

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.18.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.17.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.16.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.15.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.14.gitb508e88.20140119
- Dependency on cmake-filesystem is autogenerated now
- Skip building of LaTeX-docs

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.13.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.12.gitb508e88.20140119
- Require cmake-filesystem

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.11.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.10.gitb508e88.20140119
- Rebuilt for Boost 1.64

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.9.gitb508e88.20140119
- Rebuilt for bootstrapping new arch: s390x

* Thu Apr 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.8.gitb508e88.20140119
- Rebuilt for libyui.so.8

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.7.gitb508e88.20140119
- Use rich-dependencies instead of virtual provides
- Get major so-ver from macro

* Thu Mar 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.6.gitb508e88.20140119
- Add Provides: %%{libsuffix}-mga-gui without isa-bits, too

* Thu Mar 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.5.gitb508e88.20140119
- Add Provides: %%{libsuffix}-mga-gui

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.4.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.3.gitb508e88.20140119
- Rebuilt for Boost 1.63

* Fri Feb 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.2.gitb508e88.20140119
- Initial import (#1418882)

* Fri Feb 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.1.gitb508e88.20140119
- Initial rpm-release (#1418882)