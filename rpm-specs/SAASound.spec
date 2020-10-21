Name:           SAASound
Version:        3.2
Release:        26%{?dist}
Summary:        Phillips SAA 1099 sound chip emulator library
License:        BSD
URL:            http://simonowen.com/sam/saasound
Source0:        http://simonowen.com/sam/saasound/%{name}-%{version}.tar.gz
Patch0:         SAASound-3.2-fixweaksymbol.patch
Provides:       saasound = %{version}-%{release}

BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Phillips SAA 1099 sound chip emulator library


%package devel
Summary:        Development files for SAASound
Requires:       SAASound = %{version}-%{release}
Provides:       saasound-devel = %{version}-%{release}

%description devel
Development files for SAASound


%prep
%setup -q
%patch0 -p1


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la


%ldconfig_scriptlets


%files
%doc LICENCE README
%{_libdir}/*.so.*


%files devel
%{_libdir}/*.so
%{_includedir}/*.h


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 17 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 3.2-5
- Some small cleanups as preperation for Fedora submission
- Change (correct) License tag to: BSD

* Mon Jun 11 2007 Ian Chapman <packages@amiga-hardware.com> 3.2-4%{?dist}
- Dropped old obsoletes/provides, shouldn't be needed anymore
- Added patch to fix undefined-non-weak-symbol warnings

* Mon May 29 2006 Ian Chapman <packages@amiga-hardware.com> 3.2-3%{?dist}
- Added %%{version}-%%{release} to provides
- Added lowercase provides alias in preparation for probable policy change
- Removed superfluous documentation from devel package

* Sun May 07 2006 Ian Chapman <packages@amiga-hardware.com> 3.2-2.iss
- Altered spec file to better follow Fedora Core guidelines
- Package renamed to match upstream
- Static library and libtool libraries removed

* Mon Feb 28 2005 Ian Chapman <packages@amiga-hardware.com> 3.2-1.iss
- Initial Release
