Name:		ggobi      
Version:	2.1.7
Release:	24%{?dist}
Summary:	Open source visualization for exploring high-dimensional data 
License:	GPLv2
URL:		http://www.ggobi.org/ 
Source0:	http://www.ggobi.org/downloads/ggobi-%{version}.tar.bz2 
Source1:	ggobi.desktop
Patch0:		ggobi-2.1.7-format-security.patch
Patch1:		ggobi-2.1.7-configure.patch
BuildRequires:  gcc
BuildRequires:	libxml2-devel gtk2-devel, desktop-file-utils, autoconf, automake, libtool-ltdl-devel
Requires:	gtk2, libxml2 >= 2.6

%description
GGobi is an open source visualization program for
exploring high-dimensional data. It provides highly dynamic
and interactive graphics such as tours, as well as familiar
graphics such as the scatterplot, barchart and parallel coordinates plots.
Plots are interactive and linked with brushing and identification.

%package devel
Summary:	Open source visualization for exploring high-dimensional data
Requires:	%{name} = %{version}-%{release}

%description devel
GGobi devel files

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --with-all-plugins --datadir=%{_libdir} --disable-rpath
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
make ggobirc
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
rm $RPM_BUILD_ROOT%{_libdir}/applications/ggobi.desktop
mv $RPM_BUILD_ROOT%{_libdir}/pixmaps/ggobi.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/ggobi.png

desktop-file-install					\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications		\
  %{SOURCE1}


%ldconfig_scriptlets

%files
%doc ABOUT-NLS AUTHORS ChangeLog COPYING CPLicense.txt INSTALL README
%{_bindir}/ggobi
%{_libdir}/*.so.*
%{_libdir}/ggobi
%{_datadir}/pixmaps/ggobi.png
%{_datadir}/applications/*.desktop
%exclude %{_libdir}/*.la

%files devel
%{_includedir}/ggobi
%{_libdir}/*.so
%{_libdir}/pkgconfig/ggobi.pc

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Jeff Law <law@redhat.com> - 2.1.7-22
- Fix configure tests compromised by LTO

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.1.7-12
- Fix FTBFS with -Werror=format-security (#1037083, #1106529)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> - 2.1.7-9
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.1.7-5
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 31 2007 Marek Mahut <mmahut@fedoraproject.org> - 2.1.7-1
- Update to 2.1.7
- Light review of the spec file

* Sat Feb 17 2007 Zachary Whitley <mail@zacharywhitley.com> - 2.1.4-1
- Initial RPM release.
