Name:		libdxfrw
Version:	0.6.3
Release:	14%{?dist}
Summary:	Library to read/write DXF files
License:	GPLv2+
URL:		http://sourceforge.net/p/libdxfrw/home/Home/
Source0:	http://downloads.sourceforge.net/project/libdxfrw/%{name}-%{version}.tar.bz2
Patch0:		libdxfrw-LibreCad-2.1.0-changes.patch
Patch1:		libdxfrw-0.6.3-CVE-2018-19105.patch

BuildRequires:  gcc-c++

%description
libdxfrw is a free C++ library to read and write DXF files in both formats, 
ASCII and binary form.

%package devel
Summary:	Development files for libdxfrw
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libdxfrw.

%prep
%setup -q
%patch0 -p1 -b .lc210
%patch1 -p1 -b .CVE-2018-19105

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="/usr/bin/install -c -p"
rm -rf %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/dwg2dxf
%{_libdir}/*.so.*

%files devel
%{_includedir}/libdxfrw0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdxfrw0.pc

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Tom Callaway <spot@fedoraproject.org> - 0.6.3-10
- add fix from librecad for CVE-2018-19105

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun  6 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.3-3
- apply changes from LibreCad 2.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.3-1
- update to 0.6.3

* Fri Sep 11 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.1-1
- update to 0.6.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.11-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.11-4
- Rebuilt for GCC 5 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Tom Callaway <spot@fedoraproject.org> - 0.5.11-1
- update to 0.5.11
- resync with librecad changes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-3
- apply fixes from librecad 2.0.0beta5

* Wed Apr 24 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-2
- drop empty NEWS and TODO files
- force INSTALL to use -p to preseve timestamps

* Sun Feb 24 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-1
- initial package
