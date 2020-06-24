Name:           libspnav
Version:        0.2.3
Release:        11%{?dist}
Summary:        Open source alternative to 3DConnextion drivers

License:        BSD
URL:            http://spacenav.sourceforge.net/
Source:         http://downloads.sourceforge.net/spacenav/%{name}-%{version}.tar.gz

Patch0:         libspnav-0.2.3-lib_links.patch

BuildRequires:  gcc libX11-devel


%description
The spacenav project provides a free, compatible alternative to the proprietary
3Dconnexion device driver and SDK, for their 3D input devices (called "space
navigator", "space pilot", "space traveller", etc).

This package provides the library needed for applications to connect to the 
user land daemon.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%autosetup -p1


%build
# Set libdir properly
sed -i "s/libdir=lib/libdir=%{_lib}/g" configure
%configure 
sed -i "s/CFLAGS =/CFLAGS +=/g" Makefile
%make_build


%install
%make_install

# Remove static library
rm -f %{buildroot}%{_libdir}/%{name}.a


%ldconfig_scriptlets


%files
%doc README
%{_libdir}/*.so.0*

%files devel
%doc examples
%{_libdir}/*.so
%{_includedir}/*.h


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Richard Shaw <hobbes1069@gmail.com> - 0.2.3-1
- Update to latest upstream release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Richard Shaw <hobbes1069@gmail.com> - 0.2.2-3
- Rebuild for GCC 4.7.0.

* Wed Aug 17 2011 Richard Shaw <hobbes1069@gmail.com> - 0.2.2-2
- Patched make file to honor Fedora CFLAGS defaults.
- Removed static library package.
- Other minor updates to the spec file.

* Mon Aug 15 2011 Richard Shaw <hobbes1069@gmail.com> - 0.2.2-1
- Initial release.
