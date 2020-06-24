Name:           mercator
Version:        0.3.3
Release:        16%{?dist}
Summary:        Terrain library for WorldForge client/server

License:        GPL+
URL:            http://worldforge.org/dev/eng/libraries/mercator
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  wfmath-devel >= 0.3.2
BuildRequires:  doxygen

%description
Mercator is primarily aimed at terrain for multiplayer online games and forms
one of the WorldForge core libraries. It is intended to be used as a terrain
library on the client, while a subset of features are useful on the server.


%package devel
Summary: Development files for mercator library
Requires: %{name} = %{version}-%{release} wfmath-devel pkgconfig


%description devel
Development libraries and headers for linking against the mercator library.


%prep
%autosetup


%build
%configure
%make_build
make docs

# Remove timestamps from the generated documentation to avoid
# multiarch conflicts

for file in doc/html/*.html ; do
    sed -i -e 's/Generated on .* for Mercator by/Generated for Mercator by/' $file
done

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{name}-*.la

%check
# Run tests in debug mode so asserts won't be skipped
sed -i -e 's/-DNDEBUG/-DDEBUG/' tests/Makefile
make %{?_smp_mflags} check

%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_libdir}/lib%{name}-*.so.*


%files devel
%doc doc/html/*
%{_includedir}/Mercator-*
%{_libdir}/lib%{name}-*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.3.3-14
- Fix FTBFS + spec cleanup/modernization fixes rhbz#1604816 and rhbz#1675364

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.3-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.3.3-2
- Rebuilt for new usptream version, spec cleanup, fixes rhbz #1003329 and #926137

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 14 2012 Tom Callaway <spot@fedoraproject.org> - 0.3.2-1
- update to 0.3.2

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for c++ ABI breakage

* Sun Jan 22 2012 Bruno Wolff III <bruno@wolff.to> - 0.3.0-4
- Rebuild for wfmath soname bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun May 15 2011 Bruno Wolff III <bruno@wolff.to> - 0.3.0-2
- Adjust the files spec to be less version dependent

* Sun May 15 2011 Bruno Wolff III <bruno@wolff.to> - 0.3.0-1
- Upstream update to 0.3.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.2.7-2
- Actually perform the tests

* Fri Feb 27 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.2.7-1
- Update to 0.2.7

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 17 2008 Wart <wart at kobold.org> 0.2.6-1
- Update to 0.2.6

* Sat Feb 9 2008 Wart <wart at kobold.org> 0.2.5-4
- Rebuild for gcc 4.3

* Sun Dec 16 2007 Wart <wart at kobold.org> 0.2.5-3
- Modify docs for multiarch support (BZ #342591)

* Mon Aug 20 2007 Wart <wart at kobold.org> 0.2.5-2
- License tag clarification
- Better download URL

* Fri Aug 25 2006 Wart <wart at kobold.org> 0.2.5-1
- Update to 0.2.5

* Fri Jul 14 2006 Wart <wart at kobold.org> 0.2.4-2
- Added Requires: pkgconfig to -devel subpackage
- Remove BR: pkgconfig as it will be provided by wfmath-devel
- added smp_mflags to 'make check'

* Wed Jun 14 2006 Wart <wart at kobold.org> 0.2.4-1
- Initial spec file for Fedora Extras
