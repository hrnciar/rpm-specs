%global commit cce2e5ec01df09ca4b05f055f21942e0de7eb7dd

Name:    cutecom
Version: 0.51.0
Summary: A graphical serial terminal, like minicom or Hyperterminal on Windows
Release: 4%{?dist}
License: GPLv3
URL:     http://gitlab.com/cutecom/cutecom

Source0: https://gitlab.com/%{name}/%{name}/-/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:  3944c431-add-appdata.patch


BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: qt5-devel
BuildRequires: qt5-qtserialport-devel

%description
CuteCom is a graphical serial terminal, like minicom or Hyperterminal on 
Windows. It is aimed mainly at hardware developers or other people who need 
a terminal to talk to their devices. 

%prep
%autosetup -n %{name}-v%{version}-%{commit}
# Change icon to "utilities-terminal":
sed 's/=openterm/=utilities-terminal/' cutecom.desktop > cutecom.desktop.new
mv -f cutecom.desktop.new cutecom.desktop

%build
%cmake .
make VERBOSE=1 %{?_smp_mflags}

%install
%make_install
install -p -D -m 644 $(pwd)/cutecom.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/cutecom.1
install -p -D -m 644 com.gitlab.cutecom.cutecom.appdata.xml %{buildroot}%{_metainfodir}/com.gitlab.cutecom.cutecom.appdata.xml

# Upstream script does not install the .desktop file if KDE is not installed, 
# so we install it manually:
desktop-file-install \
   --remove-key=Path --remove-key=Encoding \
   --remove-key=BinaryPattern --remove-key=TerminalOptions \
   --add-category=System \
   --dir ${RPM_BUILD_ROOT}%{_datadir}/applications/ \
   $(pwd)/cutecom.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%doc LICENSE README.md Changelog TODO
%{_bindir}/cutecom
%{_mandir}/man1/cutecom.1*
%{_datadir}/applications/cutecom.desktop 
%{_metainfodir}/*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 24 2018 Rich Mattes <richmattes@gmail.com> - 0.51.0-1
- Update to releas 0.51.0 (rhbz#1583195)
- Add upstream appstream data (rhbz#1476499)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.22.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 15 2012 Rich Mattes <richmattes@gmail.com> - 0.22.0-4
- Add support for xmodem via lrzsz package (rhbz#848449)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-2
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Rich Mattes <richmattes@gmail.com> - 0.22.0-1
- Update to release 0.22.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.20.0-3
- Fixed .desktop file and .spec file comments.

* Tue Feb 17 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.20.0-2
- Added documentation files.
- Fixed License field.
- .desktop file installed with desktop-file-install

* Sun Feb 15 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.20.0-1
- Initial packaging for Fedora.

