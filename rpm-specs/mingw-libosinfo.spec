%{?mingw_package_header}

Name: mingw-libosinfo
Version: 1.7.1
Release: 3%{?dist}
Summary: MinGW Windows port of a library for managing OS information for virtualization
License: LGPLv2+
Source: https://releases.pagure.io/libosinfo/libosinfo-%{version}.tar.xz
URL: https://libosinfo.org/

### Patches ###

BuildArch: noarch

BuildRequires: git

BuildRequires: intltool
BuildRequires: meson
BuildRequires: gcc
BuildRequires: hwdata

BuildRequires: mingw32-filesystem >= 107
BuildRequires: mingw64-filesystem >= 107
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: mingw32-glib2
BuildRequires: mingw64-glib2
BuildRequires: mingw32-libsoup
BuildRequires: mingw64-libsoup
BuildRequires: mingw32-libxml2
BuildRequires: mingw64-libxml2
BuildRequires: mingw32-libxslt
BuildRequires: mingw64-libxslt

BuildRequires: pkgconfig

BuildRequires: /usr/bin/pod2man

%description
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package -n mingw32-libosinfo
Summary: %{summary}

Requires: pkgconfig

%description -n mingw32-libosinfo
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package -n mingw64-libosinfo
Summary: %{summary}

Requires: pkgconfig

%description -n mingw64-libosinfo
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%{?mingw_debug_package}

%prep
%autosetup -S git -n libosinfo-%{version}

%build
%mingw_meson \
    -Denable-gtk-doc=false \
    -Denable-tests=false \
    -Denable-introspection=disabled \
    -Denable-vala=disabled
%mingw_ninja

%install
%mingw_ninja_install

# Remove static libraries but DON'T remove *.dll.a files.
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libosinfo-1.0.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libosinfo-1.0.a

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

# Manpages don't need to be bundled
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man

rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc

%mingw_find_lang libosinfo

%files -n mingw32-libosinfo -f mingw32-libosinfo.lang
%doc AUTHORS ChangeLog COPYING.LIB NEWS README
%{mingw32_bindir}/osinfo-detect.exe
%{mingw32_bindir}/osinfo-install-script.exe
%{mingw32_bindir}/osinfo-query.exe
%{mingw32_bindir}/libosinfo-1.0-0.dll
%{mingw32_libdir}/libosinfo-1.0.dll.a
%{mingw32_libdir}/pkgconfig/libosinfo-1.0.pc
%dir %{mingw32_includedir}/libosinfo-1.0/
%dir %{mingw32_includedir}/libosinfo-1.0/osinfo
%{mingw32_includedir}/libosinfo-1.0/osinfo/*.h
%dir %{mingw32_datadir}/libosinfo
%{mingw32_datadir}/libosinfo/usb.ids
%{mingw32_datadir}/libosinfo/pci.ids

%files -n mingw64-libosinfo -f mingw64-libosinfo.lang
%doc AUTHORS ChangeLog COPYING.LIB NEWS README
%{mingw64_bindir}/osinfo-detect.exe
%{mingw64_bindir}/osinfo-install-script.exe
%{mingw64_bindir}/osinfo-query.exe
%{mingw64_bindir}/libosinfo-1.0-0.dll
%{mingw64_libdir}/libosinfo-1.0.dll.a
%{mingw64_libdir}/pkgconfig/libosinfo-1.0.pc
%dir %{mingw64_includedir}/libosinfo-1.0/
%dir %{mingw64_includedir}/libosinfo-1.0/osinfo
%{mingw64_includedir}/libosinfo-1.0/osinfo/*.h
%dir %{mingw64_datadir}/libosinfo
%{mingw64_datadir}/libosinfo/usb.ids
%{mingw64_datadir}/libosinfo/pci.ids

%changelog
* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.7.1-3
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.7.1-1
- Update to 1.7.1 release

* Fri Nov 29 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.7.0-1
- Update to 1.7.0 release

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.6.0-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Jul 26 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.6.0-1
- Update to 1.6.0 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.5.0-3
- rhbz#1727768 - CVE-2019-13313 libosinfo: osinfo-install-script
                 option leaks password via command line argument

* Wed Jul 10 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.5.0-2
- Fix coverity issues

* Thu May 09 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.5.0-1
- Update to 1.5.0 release

* Wed Apr 10 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.4.0-2
- Fix usage of application ID
- Fix images' load
- Remove tests depending on osinfo-db

* Mon Mar 04 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.4.0-1
- Update to 1.4.0 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul  1 2016 Daniel P. Berrange <berrange@redhat.com> - 0.3.1-1
- Update to 0.3.1 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec  4 2013 Daniel P. Berrange <berrange@redhat.com> - 0.2.8-1
- Update to 0.2.8 release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Daniel P. Berrange <berrange@redhat.com> - 0.2.3-1
- Update to 0.2.3 release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep  4 2012 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-1
- Update to 0.2.0 release

* Mon Jun 25 2012 Daniel P. Berrange <berrange@redhat.com> - 0.1.2-2
- Remove BuildRoot statement
- Move requires on pkgconfig to sub-RPMs
- Remove quotes around DESTDIR
- Remove defattr from files

* Wed Jun 20 2012 Daniel P. Berrange <berrange@redhat.com> - 0.1.2-1
- Initial package
