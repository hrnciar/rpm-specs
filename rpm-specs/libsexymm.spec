Name:           libsexymm
Version:        0.1.9
Release:        29%{?dist}

Summary:        C++ wrapper for libsexy

License:        LGPLv2+
URL:            http://www.chipx86.com/wiki/Libsexy
Source0:        http://releases.chipx86.com/libsexy/libsexymm/libsexymm-%{version}.tar.gz


BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  gtkmm24-devel >= 2.4.0
BuildRequires:  libsexy-devel >= 0.1.10
BuildRequires: libxml2-devel

%description
libsexymm is a set of C++ bindings around libsexy, 
compatible with programs using gtkmm.

%package devel
Summary:        Headers for developing programs that will use libsexymm
Requires:       %{name} = %{version}-%{release}
Requires:       gtkmm24-devel >= 2.4.0
Requires:       libsexy-devel >= 0.1.10


%description devel
This package contains the headers that programmers will need to
develop applications which will use libsexymm.


%prep
%setup -q -n libsexymm-%{version}


%build
%configure --disable-static --enable-docs

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc COPYING ChangeLog INSTALL NEWS
%{_libdir}/*.so.*


%files devel
%{_includedir}/libsexymm/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libsexymm/*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.9-19
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.9-12
- Rebuild for new libpng

* Mon Feb 21 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.9-11
- rpm spec cleaning

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 31 2010 Haikel Guémar <karlthered@gmail.com> - 0.1.9-9
- Rebuilt for F-13

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1.9-6
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.9-5
- Autorebuild for GCC 4.3

* Thu Aug 29 2007 Haïkel Guémar <karlthered@gmail.com> - 0.1.9-4
- fixed devel dependencies issues 

* Wed Mar 28 2007 Haïkel Guémar <karlthered@gmail.com> - 0.1.9-3
- unowned directory

* Sun Jan 21 2007 Haïkel Guémar <karlthered@gmail.com> - 0.1.9-2
- rebuild against new cairomm package

* Tue Nov 17 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.9-1
- updated to 0.1.9, license file issue has been fixed upstream

* Tue Sep 12 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.7-4
- rebuild for FC6

* Sun Aug 13 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.7-3
- fixed some rpmlint issues, add a patch to correct the license file

* Tue Jun 13 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.7-2
- some syntax fixes to post and postun section

* Mon May 22 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.7-1
- First Packaging
