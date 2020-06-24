%global majorver 3 

Name: libapogee
Version: 3.2
Release: 4%{?dist}
Summary: Library for Apogee CCD Cameras

License: GPLv2+ and MPLv2.0
URL: http://indilib.org

# Tar is generated from the huge all-in-one tar from INDI
# by using ./libapogee-generate-tarball.sh 1.3.1
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-generate-tarball.sh

BuildRequires:  gcc-c++
BuildRequires: boost-devel cmake libusb-devel libcurl-devel systemd

%description
Apogee library is used by applications to control Apogee CCDs.

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
These are the header files needed to develop a %{name} application

%prep
%setup -q -n %{name}-%{version}
sed -i 's|/etc/udev/rules.d|%{_udevrulesdir}|g' CMakeLists.txt
sed -i 's|DESTINATION lib|DESTINATION lib${LIB_SUFFIX}|g' CMakeLists.txt

%build
%cmake
make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%ldconfig_scriptlets

%files
%license LICENSE
%doc README
%{_libdir}/*.so.*
%{_sysconfdir}/Apogee/*
%{_udevrulesdir}/99-apogee.rules

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Christian Dersch <lupinix@fedoraproject.org> - 3.2-3
- rebuilt

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 3.2-1
- new version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 3.1-3
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 3.1-1
- new version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3234-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 3.0.3234-7
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3234-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3234-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 3.0.3234-4
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 3.0.3234-3
- Rebuilt for Boost 1.64

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 3.0.3234-2
- Rebuilt for Boost 1.63

* Thu Dec 15 2016 Christian Dersch <lupinix@mailbox.org> - 3.0.3234-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 25 2015 Christian Dersch <lupinix@fedoraproject.org>- 2.2-17
- Spec adjustments (use license tag, global instead of define)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2-15
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Sergio Pascual <sergiopr at fedoraproject.org> - 2.2-12
- Adding the patch

* Tue Dec 03 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 2.2-11
- Fix bz #1037156 (format-security)
- Spec cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 2.2-6
- curl/types.h removed in latest curl
- Bug filled upstream
- Cleanup the specfile

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Sergio Pascual <sergiopr at fedoraproject.org> -  2.2-2
- Fixing license tag
- Patch to remove sys/io.h
- Bug filled upstream about calling exit()

* Sat Feb 07 2009 Sergio Pascual <sergiopr at fedoraproject.org> -  2.2-1
- Initial spec file

