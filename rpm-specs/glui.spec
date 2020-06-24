Name: glui
Version:  2.36
Release:  17%{?dist}
Summary: A GLUT-Based User Interface Library

License: zlib + LGPLv2+
URL: http://glui.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
#Upstream only builds a static library, this makes a solib.
Patch0: glui-2.36-solib.patch
BuildRequires:  gcc-c++
BuildRequires: freeglut-devel libXi-devel libXmu-devel

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description
GLUI is a GLUT-based C++ user interface library which provides controls
such as buttons, checkboxes, radio buttons, and spinners to OpenGL applications. 
It is window-system independent, relying on GLUT to handle all system-dependent 
issues, such as window and mouse management. 


%description devel
GLUI is a GLUT-based C++ user interface library which provides controls
such as buttons, checkboxes, radio buttons, and spinners to OpenGL applications. 
It is window-system independent, relying on GLUT to handle all system-dependent 
issues, such as window and mouse management. 

These are the development files.

%prep
%setup -q
%patch0 -p1 -b .solib
find -type f -name '*.cpp' | xargs chmod -x
find -type f -name '*.h' | xargs chmod -x

%build
pushd src
%{__make} CPPFLAGS="%{optflags} -I./ -I./include -fPIC" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_includedir}/GL
install -p -m 644 src/include/GL/glui.h %{buildroot}%{_includedir}/GL/
mkdir -p %{buildroot}%{_libdir}
install -p -m 755 src/libglui.so.0.0 %{buildroot}%{_libdir}/
ln -s %{_libdir}/libglui.so.0.0 %{buildroot}%{_libdir}/libglui.so.0
ln -s %{_libdir}/libglui.so.0 %{buildroot}%{_libdir}/libglui.so


%ldconfig_scriptlets


%files
%doc src/LICENSE.txt
%{_libdir}/*.so.*

%files devel
%doc src/doc/ src/example/ www/ 
%{_libdir}/*.so
%{_includedir}/GL/
%{_includedir}/GL/glui.h


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.36-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 06 2012 Jon Ciesla <limb@jcomserv.net> - 2.36-2
- Review fixes. from BZ 845308, comment 1.

* Thu Aug 02 2012 Jon Ciesla <limb@jcomserv.net> - 2.36-1
- create.
