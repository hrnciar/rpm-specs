Name:           gimp-normalmap
Version:        1.2.3
Release:        22%{?dist}
Summary:        Plugin that enabled the creation of normal maps

License:        GPLv2+
URL:            http://code.google.com/p/gimp-normalmap/
Source0:        http://%{name}.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0:         %{name}-fixmake.patch

BuildRequires:  gcc
BuildRequires:  gimp-devel
BuildRequires:  gtkglext-devel
BuildRequires:  glew-devel
Requires:       gimp

%description
A plugin for Gimp that enables the creation of normal maps
that you can use to achieve a number of lighting effects in pixel-based artwork.

%prep
%setup -q
%patch0

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
mkdir -p %{buildroot}%{_libdir}/gimp/2.0/plug-ins/
install -m 755 normalmap %{buildroot}%{_libdir}/gimp/2.0/plug-ins/

%files
%doc COPYING README
%{_libdir}/gimp/2.0/plug-ins/normalmap


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.2.3-19
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-13
- Rebuild for glew 2.0.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1.2.3-11
- Rebuild for glew 1.13

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 1.2.3-7
- rebuilt for GLEW 1.10

* Mon Sep 02 2013 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.2.3-6
- No longer claim the plug-ins directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.2.3-4
- Removed the -O3 flag

* Thu Feb 07 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.2.3-3
- Patched Makefile and spec to use optflags

* Fri Feb 01 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.2.3-2
- Requires Gimp added

* Thu Jan 31 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.2.3-1
- First packaging effort

