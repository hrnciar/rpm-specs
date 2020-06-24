Name:           varconf
Version:        1.0.1
Release:        17%{?dist}
Summary:        Configuration library used by WorldForge clients

License:        LGPLv2+
URL:            http://worldforge.org/dev/eng/libraries/varconf
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  libsigc++20-devel

%description
Varconf is a configuration library intended for all applications. It manages
configuration data in files, command line arguments, and is used by most
WorldForge components.


%package devel
Summary: Development files for varconf library
Requires: pkgconfig %{name} = %{version}-%{release}


%description devel
Development libraries and headers for linking against the varconf library.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

## cleaning up redundant docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%check
make %{?_smp_mflags} check
cd tests ; ./conftest < conf.cfg

%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog README THANKS TODO
%license COPYING
%{_libdir}/lib%{name}-1.0.so.*


%files devel
%{_includedir}/%{name}-1.0
%{_libdir}/lib%{name}-1.0.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.1-15
- Rebuilt to fix FTBFS plus spec cleanup and modernization

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jonathan Wakely <jwakely@redhat.com> - 1.0.1-8
- Rebuilt for Boost 1.63

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.1-2
- New upstream release, spec fixes/cleanup, fix rhbz #874011 and #926692

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Bruno Wolff III <bruno@wolff.to> - 1.0.0-1
- New upstream release

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 19 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.7-1
- New upstream release
- Looks like minor fixes and added test cases

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 06 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.6.6-1
- Update to 0.6.6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 9 2008 Wart <wart at kobold.org> 0.6.5-3
- Rebuild for gcc 4.3

* Tue Aug 21 2007 Wart <wart at kobold.org> 0.6.5-2
- License tag clarification

* Tue Jan 16 2007 Wart <wart at kobold.org> 0.6.5-1
- Update to 0.6.5

* Mon Aug 28 2006 Wart <wart at kobold.org> 0.6.4-4
- Rebuild for Fedora Extras

* Wed Jul 19 2006 Wart <wart at kobold.org> 0.6.4-3
- Add command to %%check to execute tests

* Fri Jul 14 2006 Wart <wart at kobold.org> 0.6.4-2
- Added Requires: pkgconfig to -devel subpackage
- Change license from GPL -> LGPL
- Added missing header to test file
- Use smp_mflags with test suie

* Wed Jun 14 2006 Wart <wart at kobold.org> 0.6.4-1
- Initial spec file for Fedora Extras
