Name:      zhu3d
Version:   4.2.6
Release:   18%{dist}
Summary:   Interactive OpenGL-based mathematical function viewer
License:   GPLv3
URL:       http://www.sourceforge.net/projects/zhu3d
Source0:   http://sourceforge.net/projects/zhu3d/files/zhu3d/%{name}-%{version}.tar.gz
Source1:   zhu3d.desktop 
Patch00:   pri.patch
Patch01:   zhu3d-4.2.6-qt5.patch

BuildRequires: cmake
BuildRequires: dos2unix
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: qt5-qtbase-devel
BuildRequires: mesa-libGLU-devel

# build fails on ppc64le - rhbz#1676264
ExcludeArch: ppc64le

%description
Zhu3D is an interactive OpenGL-based mathematical function viewer.
You can visualize functions, parametric systems and Iso-surfaces. 
The viewer supports special effects like animation, morphing, 
transparency, textures, fog and motion blur

%prep
%setup -q -n %{name}-%{version}
%patch00 -p1 -b .pri
%patch01 -p1

find . -type f -print0|xargs -0 chmod -x  
dos2unix readme.txt license.gpl  

%build
QTDIR="%{_qt4_prefix}" ; export QTDIR ; \
PATH="%{_qt4_bindir}:$PATH" ; export PATH ; \
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ; \
%{qmake_qt5} -r IDE_LIBRARY_BASENAME=%{_lib}
%make_build

%install
# Program binary  
mkdir -p %{buildroot}%{_bindir}  
cp -f %{name} %{buildroot}%{_bindir}  
  
# Other program files  
mkdir -p %{buildroot}%{_datadir}/%{name}  
cp -a -f work system %{buildroot}%{_datadir}/%{name}  
  
# Desktop entry  
mkdir -p %{buildroot}%{_datadir}/applications  
cp -f %SOURCE1 %{buildroot}%{_datadir}/applications  
  
# Desktop icon  
install -m 0755 -d %{buildroot}%{_datadir}/icons/hicolor/64x64/apps  
install -m 0755 -d %{buildroot}%{_datadir}/pixmaps  
install -m 0644 system/icons/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps  
install -m 0644 system/icons/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png  
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%check
desktop-file-validate %{SOURCE1}


%files
%doc readme.txt
%license license.gpl
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/64x64/apps/*
%{_datadir}/pixmaps/zhu3d.png
%{_datadir}/applications/zhu3d.desktop
 
%changelog
* Sat Apr 11 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.2.6-18
- Fix FTBFS#F33

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.2.6-15
- Fix FTBFS on rawhide, spec cleanup and modernization
- Migrate to Qt5, exclude builds on ppc64le for while

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.2.6-7
- use %%qmake_qt4 macro to ensure proper build flags

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.2.6-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 18 2013 Siddharth Sharma <siddharths@fedoraproject.org> - 4.2.6-1
- Upstream update to 4.2.6
- Remove libGLU Patch

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Siddharth Sharma <siddharth.kde@gmail.com> - 4.2.4-2
- rebuilt commit fixes for source

* Fri Mar 2 2012 siddvicious <siddharth.kde@gmail.com> - 4.2.4-1
- Package Update

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 siddharth Sharma <siddharths@fedoraproject.org> - 4.2.2-2
  - Fixes
  - Changelog fix 4.2.4 to 4.2.2
  - URL Source fix
  - Default attributes in files were listed twice.
  - Used macros instead of full paths in some places
  
* Sun Jan 9 2011 siddharth Sharma <siddharths@fedoraproject.org> - 4.2.2-1
  - Initial Release 1
