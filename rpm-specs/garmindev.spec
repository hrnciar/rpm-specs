Name:           garmindev
Version:        0.3.4
Release:        21%{?dist}
Summary:        Drivers for communication with Garmin GPS devices

License:        GPLv2+
URL:            http://www.qlandkarte.org
Source0:        http://downloads.sourceforge.net/qlandkartegt/%{name}-%{version}.tar.gz
Provides:       %{name}(interface) = 1.18

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake libusb-devel


%description
Drivers for communication with Garmin GPS devices used by QLandkarteGT.


%prep
%setup -q

mkdir build


%build
cd build
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fsigned-char"
%cmake ..
make VERBOSE=1 %{?_smp_mflags}


%install
cd build
make install DESTDIR=%{buildroot}

# fix perms on plugins
find %{buildroot}%{_libdir}/qlandkartegt -type f -exec chmod 0755 {} \;

# drop the development files
rm -rf %{buildroot}%{_includedir}/garmin
rm -rf %{buildroot}%{_libdir}/qlandkartegt/libgarmin*


%files
%doc
%{_libdir}/qlandkartegt/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 15 2016 Dan Horák <dan[at]danny.cz> - 0.3.4-13
- fix FTBFS (#1307520)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.4-10
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul  4 2010 Dan Horák <dan[at]danny.cz> 0.3.4-1
- update to version 0.3.4

* Sat Feb  6 2010 Dan Horák <dan[at]danny.cz> 0.3.3-1
- update to version 0.3.3

* Tue Jan 26 2010 Dan Horák <dan[at]danny.cz> 0.3.2-1
- update to version 0.3.2

* Wed Dec 23 2009 Dan Horák <dan[at]danny.cz> 0.3.1-1
- update to version 0.3.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Dan Horák <dan[at]danny.cz> 0.3.0-1
- update to version 0.3.0

* Wed Apr 15 2009 Dan Horák <dan[at]danny.cz> 0.1.1-1
- update to version 0.1.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20090208svn1152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Dan Horák <dan[at]danny.cz> 0-0.3.20090208svn1152
- update to revision 1152 - adds support for eTrex LegendHCx, eTrexH, eTrex Legend

* Wed Nov 19 2008 Dan Horák <dan[at]danny.cz> 0-0.2.20081117svn928
- provide garmindev(interface) = 1.15 for correct interraction with QLandkarteGT

* Mon Nov 17 2008 Dan Horák <dan[at]danny.cz> 0-0.1.20081117svn928
- initial Fedora version
