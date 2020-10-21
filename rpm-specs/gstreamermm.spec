%global api_ver 1.0
%global branch 1.10

Name:           gstreamermm
Version:        1.10.0
Release:        8%{?dist}

Summary:        C++ wrapper for GStreamer library

License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gstreamermm/%{branch}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires: glibmm24-devel >= 2.21.1
# Enable GUI examples build as a test
BuildRequires: gtkmm30-devel >= 3.0
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: libxml++-devel >= 2.14.0
BuildRequires: doxygen graphviz m4


%description
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.


%package        devel
Summary:        Headers for developing programs that will use %{package_name}
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the static libraries and header files needed for
developing gstreamermm applications.


%package          doc
Summary:          Developer's documentation for the gstreamermm library
BuildArch:        noarch
BuildRequires:    doxygen graphviz
Requires:         glibmm24-doc

%description      doc
This package contains developer's documentation for the GStreamermm
library. Gstreamermm is the C++ API for the GStreamer library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.


%prep
%setup -q -n %{name}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}-%{api_ver}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}-%{api_ver}

%files doc
%license COPYING
%doc %{_docdir}/%{name}-%{api_ver}/
%doc %{_datadir}/devhelp/books/%{name}-%{api_ver}/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 06 2020 Kalev Lember <klember@redhat.com> - 1.10.0-7
- Fix incorrect gstreamer-devel (0.10) dep in the -devel subpackage

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 hguemar <hguemar@nozarashi.seireitei> - 1.10.0-1
- Upstream 1.10.0
- Fix dir ownership  in doc subpackage
- Some cleanup in spec

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun  7 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.4.3-1
- Upstream 1.4.3
- Based on Ankur Sinha work (RHBZ#1315852)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.10.11-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 0.10.11-6
- Rebuilt for GCC 5 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.11-1
- upstream 0.10.11 (bugfixes: memleaks and library startup speed-up)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 17 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.10.10-3
- Add gstreamermm-0.10.10-glib2-2.31.patch to work around glib2 API changes.
  (Fix mass rebuild FTBFS). 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 07 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.10-1
- upstream 0.10.10
- remove DSO linking patch

* Tue Apr 19 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.9-1
- upstream 0.10.9
- temporary patch to fix DSO linking issue with code generator

* Tue Feb 22 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.8-3
- split doc into subpackage

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 24 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.8-1
- Update to upstream 0.10.8

* Fri Apr 30 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.7-1
- Update to upstream 0.10.7

* Mon Jan  4 2010 Denis Leroy <denis@poolshark.org> - 0.10.6-1
- Update to upstream 0.10.6

* Sat Nov  7 2009 Denis Leroy <denis@poolshark.org> - 0.10.5.2-1
- Update to 0.10.5.2
- Fix devhelp doc setup

* Mon Sep 14 2009 Denis Leroy <denis@poolshark.org> - 0.10.5-1
- Update to upstream 0.10.5
- doc patch upstreamed

* Wed Sep  2 2009 Denis Leroy <denis@poolshark.org> - 0.10.4-2
- Rebuild for new glibmm24
- Added patch to remove beautify_docs

* Thu Aug 20 2009 Denis Leroy <denis@poolshark.org> - 0.10.4-1
- Update to upstream 0.10.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Denis Leroy <denis@poolshark.org> - 0.10.2-1
- Update to upstream 0.10.2

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Denis Leroy <denis@poolshark.org> - 0.10.1-1
- Update to upstream 0.10.1
- No longer uses gstreamerbase include dir

* Sun Dec 28 2008 Denis Leroy <denis@poolshark.org> - 0.9.8-2
- Rebuild for pkgconfig

* Fri Dec 26 2008 Denis Leroy <denis@poolshark.org> - 0.9.8-1
- Update to upstream 0.9.8
- Disabled parallel make

* Fri Oct 10 2008 Denis Leroy <denis@poolshark.org> - 0.9.7-1
- Update to upstream 0.9.7

* Wed Sep  3 2008 Denis Leroy <denis@poolshark.org> - 0.9.6-1
- Update to upstream 0.9.6

* Sat May 31 2008 Denis Leroy <denis@poolshark.org> - 0.9.5-1
- Update to upstream 0.9.5
- Fixed gstreamer plugin BuildRequires

* Fri Feb 22 2008 Denis Leroy <denis@poolshark.org> - 0.9.4-1
- Updated to upstream 0.9.4

* Sun Feb 17 2008 Denis Leroy <denis@poolshark.org> - 0.9.2-1
- First draft
