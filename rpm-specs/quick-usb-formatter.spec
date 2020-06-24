Name: quick-usb-formatter  
%define binname quickusbformatter     
Version: 0.4.1        
Release: 20%{?dist}
Summary: A small application to format usb sticks and devices   
    
License: LGPLv2+       

URL: http://kde-apps.org/content/show.php?content=137493
Source0: http://sourceforge.net/projects/chakra/files/Tools/Quick-Usb-Formatter/quick-usb-formatter-%{version}.tar.gz
Patch00: desktop.patch

BuildRequires: cmake kdelibs4-devel gettext
Requires: qt qt-x11      

%description
Quick Usb Formatter it is a tiny app designed for enhance the usability of the
device notifier, an additional option for quick format usb sticks

%prep
%setup -q -n chakra-quick-usb-formatter
%patch00 -p1 -b .desktop

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. 
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast -C %{_target_platform} DESTDIR=%{buildroot}
%find_lang %{binname}


%check
desktop-file-validate %{binname}.desktop


%files -f %{binname}.lang
%doc README.txt
%{_bindir}/%{binname}
%dir %{_datadir}/apps/
%dir %{_datadir}/apps/solid/
%dir %{_datadir}/apps/solid/actions/
%{_datadir}/apps/solid/actions/%{binname}.desktop

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.1-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 siddvicious <siddharth.kde@gmail.com> - 0.4.1-4
- Fixed permission on spec and source files
- rebuilt src.rpm

* Fri Mar 2 2012 siddharth Sharma <siddharths@fedoraproject.org> - 0.4.1-3
  - Fixes with BuildRequires and Bug Fixing

* Mon Oct 31 2011 siddharth Sharma <siddharths@fedoraproject.org> - 0.4.1-2
  - Fixes with BuildRequires and Bug Fixing

* Thu Jul 28 2011 siddharth Sharma <siddharths@fedoraproject.org> - 0.4-1
  - Initial Release 1
