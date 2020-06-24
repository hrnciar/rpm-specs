Name:           hawknl
Version:        1.68
Release:        24%{?dist}
Summary:        Game oriented network library
License:        LGPLv2+ 
URL:            http://www.hawksoft.com/hawknl/
Source0:        http://www.sonic.net/~philf/download/HawkNL168src.tar.gz
Patch0:         hawknl-64bit.patch
Patch1:         hawknl-nlinternal.h.patch

BuildRequires:  gcc
%description
HawkNL is a free, open source, game oriented network API released under the 
GNU LGPL. HawkNL (NL) is a fairly low level API, a wrapper over Berkeley/Unix
Sockets and Winsock. But NL also provides other features.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}%{version}
# some fixups
sed -i 's|ln -s $(LIBDIR)/$(OUTPUT)|ln -s $(OUTPUT)|g' src/makefile.linux
sed -i 's|-soname,NL.so|-soname,libNL.so|' src/makefile.linux
sed -i 's|\r||g' src/readme.txt src/nlchanges.txt


%build
make %{?_smp_mflags} -f makefile.linux \
  OPTFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
make -f makefile.linux install LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
  INCDIR=$RPM_BUILD_ROOT%{_includedir}/%{name}
# some apps want this semi-private header
install -p -m 0644 src/nlinternal.h $RPM_BUILD_ROOT%{_includedir}/%{name}
# some cleanup
rm $RPM_BUILD_ROOT%{_libdir}/libNL.a $RPM_BUILD_ROOT%{_libdir}/NL.so \
  $RPM_BUILD_ROOT%{_libdir}/libNL.so.1



%ldconfig_scriptlets


%files
%doc src/readme.txt src/nlchanges.txt
%{_libdir}/libNL.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libNL.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Hans de Goede <hdegoede@redhat.com> - 1.68-22
- Some apps want the semi-private nlinternal.h header, add it to hawknl-devel

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.68-4
- fix license tag

* Wed Feb 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.68-3
- Fix building with latest glibc (define _GNU_SOURCE)
- Rebuild for gcc-4.3

* Tue Aug  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.68-2
- Update License tag for new Licensing Guidelines compliance

* Mon Mar 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.68-1
- Initial FE package
