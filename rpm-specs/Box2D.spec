Name: Box2D
Version:  2.3.1
Release:  12%{?dist}
Summary: A 2D Physics Engine for Games

License: zlib
URL: http://box2d.org/
# "Google Code no longer allows for downloads, therefore you will have to use SVN to get v2.3.1"
# <http://box2d.org/2014/04/box2d-v2-3-1-released/>
# svn checkout http://box2d.googlecode.com/svn/tags/v2.3.1/Box2D Box2D-2.3.1
# (^^^ beware only legacy IP works, IPv6 seems broken)
# tar --exclude .svn -czf Box2D-2.3.1.tar.gz Box2D-2.3.1
Source0: %{name}-%{version}.tar.gz
Patch0: Box2D-2.3.1-cmake.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake libXi-devel glew-devel glfw-devel

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description
Box2D is an open source C++ engine for simulating rigid bodies in 2D. 
Box2D is developed by Erin Catto and has the zlib license. 
While the zlib license does not require acknowledgement, 
we encourage you to give credit to Box2D in your product. 

%description devel
Box2D is an open source C++ engine for simulating rigid bodies in 2D. 
Box2D is developed by Erin Catto and has the zlib license. 
While the zlib license does not require acknowledgement, 
we encourage you to give credit to Box2D in your product. 

These are the development files.

%prep
%setup -q
%patch0 -p1
rm -rf glew glfw

%build
sed -i 's/\r//' License.txt
sed -i 's/\r//' Readme.txt
pushd Box2D
%cmake -DBOX2D_INSTALL=ON -DBOX2D_BUILD_SHARED=ON ..
make

%install
pushd Box2D
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.cmake' | xargs rm
find %{buildroot} -name '*.a' | xargs rm


%ldconfig_scriptlets



%files
%doc License.txt
%{_libdir}/*.so.*

%files devel
%doc Readme.txt Documentation/
%{_libdir}/*.so
%{_includedir}/Box2D


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 20 2015 Lubomir Rintel <lkundrak@v3.sk> - 2.3.1-1
- Update

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 06 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.1-3
- Review fixes from BZ 844090 comment 6.

* Thu Aug 02 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.1-2
- Unbundle freeglut and glui.

* Sat Jul 28 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.1-1
- create.
