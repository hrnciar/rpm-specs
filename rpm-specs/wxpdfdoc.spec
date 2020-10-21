Name:           wxpdfdoc
Version:        0.9.7
Release:        5%{?dist}
Summary:        A library for creating PDF documents in C++ with wxWidgets
License:        wxWidgets
URL:            https://utelle.github.io/wxpdfdoc/
Source:         https://github.com/utelle/wxpdfdoc/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  wxGTK3-devel

%global _wxdir /wx-3.0/wx
%global build_dir bld


%description
wxPdfDocument allows wxWidgets applications to generate PDF documents. 
The code is a port of FPDF - a free PHP class for generating PDF files - 
to C++ using the wxWidgets library. Several add-on PHP scripts found on 
the FPDF web site are incorporated into wxPdfDocument. Embedding of PNG, 
JPEG, GIF and WMF images is supported. In addition to the 14 standard 
Adobe fonts it is possible to use other Type1 or TrueType fonts - with 
or without embedding them into the generated document. In Unicode build 
CJK fonts are supported, too. Graphics primitives allow the creation of 
simple drawings.


%package devel
Summary:        Development files needed for the wxPdfDocument library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       wxGTK3-devel
Requires:       pkgconfig


%description devel
wxPdfDocument allows wxWidgets applications to generate PDF documents. 
This package contains the development files needed to use the 
wxPdfDocument library.


%prep
%autosetup
autoreconf


%build
mkdir %{build_dir}
pushd %{build_dir}
ln -s ../configure
%configure --disable-static
%make_build
popd
pushd docs
doxygen Doxyfile
rm Doxyfile
popd


%install
pushd %{build_dir}
%make_install includewxdir=%{_includedir}%{_wxdir}
popd
rm -f %{buildroot}/%{_libdir}/*.la


%files 
%{_libdir}/libwxcode_gtk3u_pdfdoc-3.0.so.*
%license LICENCE.txt


%files devel
%{_includedir}%{_wxdir}/pdf*
%{_libdir}/libwxcode_gtk3u_pdfdoc-3.0.so
%{_libdir}/pkgconfig/wxpdfdoc.pc
%doc readme.md docs/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Scott Talbert <swt@techie.net> - 0.9.7-1
- New upstream release 0.9.7

* Wed Oct 31 2018 Scott Talbert <swt@techie.net> - 0.9.6-1
- New upstream release 0.9.6
- Rebuild with wxWidgets 3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 21 2015 Ralf Corsepius <corsepiu@fedoraproject.org> - 0.9.3-7
- Pass CXXFLAGS to make (Fix F23TBFS, RHBZ#1240063).
- Add %%license.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 24 2012 Domingo Becker <domingobecker@gmail.com> - 0.9.3-1
- Updated to latest upstream version.
- Moved Readme.txt and docs/html to -devel package (Bug #889889).
- Removed Doxyfile from installed package (Bug #889889).
- Updated patch for build/GNUmakefile for the new version and to fix a missing library problem with samples/pdfdc/printing.

* Sun Oct 28 2012 Domingo Becker <domingobecker@gmail.com> - 0.9.2.1-4
- Removed BuildRoot definition.
- Removed initial cleaning of buildroot in install section.
- Removed clean section.
- Removed defattr lines in files section.

* Sun Oct 21 2012 Domingo Becker <domingobecker@gmail.com> - 0.9.2.1-3
- Fixed macro in comment warning by removing all unnecessary comments.
- Removed spurious executable permission on source files.

* Wed May 16 2012 Domingo Becker <domingobecker@gmail.com> - 0.9.2.1-2
- Apply patch to build/GNUmakefile to install headers in the correct directory. 

* Mon May 07 2012 Domingo Becker <domingobecker@gmail.com> - 0.9.2.1-1
- Updated to new upstream version.
- Fixed required base package.
- Group set to System Environment/Libraries.
- Removed gcc-c++ as requires.
- Added wxGTK-devel dependency in -devel package.

* Tue Aug 16 2011 Domingo Becker <domingobecker@gmail.com> - 0.9.1-3
- Fixed for a proper multilib support.
- devel package requires core package.

* Tue Aug 16 2011 Domingo Becker <domingobecker@gmail.com> - 0.9.1-2
- Fixed lib64 dir name issue in x86_64 with a patch.

* Mon Aug 15 2011 Domingo Becker <domingobecker@gmail.com> - 0.9.1-1
- Initial version.


