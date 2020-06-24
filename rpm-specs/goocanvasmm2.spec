%global tarname goocanvasmm
%global api_ver 2.0

%global glibmm_version 2.46.1
%global gtkmm_version 3.18.0
%global goocanvas_version 2.0.1

Name:           goocanvasmm2
Version:        1.90.11
Release:        10%{?dist}
Summary:        C++ interface for goocanvas2

License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{tarname}/1.90/%{tarname}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel >= %{glibmm_version}
BuildRequires:  gtkmm30-devel >= %{gtkmm_version}
BuildRequires:  goocanvas2-devel >= %{goocanvas_version}

Requires:       glibmm24%{?_isa} >= %{glibmm_version}
Requires:       gtkmm30%{?_isa} >= %{gtkmm_version}
Requires:       goocanvas2%{?_isa} >= %{goocanvas_version}

%description
This package provides a C++ interface for goocanvas. It is a
sub-package of the gtkmm project. The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch
BuildRequires:  doxygen graphviz
Requires:       gtkmm30-doc

%description      doc
This package contains developer's documentation for the goocanvasmm2
library. Goocanvasmm2 is the C++ API for the goocanvas graphics library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

If using a web browser the documentation is at
/usr/share/doc/%{tarname}-%{api_ver}

%prep
%setup -q -n %{tarname}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/%{tarname}-%{api_ver}/
%{_libdir}/pkgconfig/%{tarname}-%{api_ver}.pc

%files doc
%license COPYING
%doc %{_datadir}/devhelp/books/%{tarname}-%{api_ver}
%doc %{_docdir}/%{tarname}-%{api_ver}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 1.90.11-1
- Update to 1.90.11
- Use license macro for COPYING
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.90.8-8
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1.90.8-1
- upstream 1.90.8

* Tue Oct 11 2011 Haïkel Guémar <haikel.guemar@sysfera.com> - 1.90.6-1
- upstream 1.90.6

* Sun Apr 10 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1.90.3-2
- add doctooldir patch

* Fri Feb 11 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1.90.3-1
- initial package

