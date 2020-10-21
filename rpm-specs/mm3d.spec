%global         plugin_3ds_ver          0.8.1
%global         plugin_imtex_ver        1.4.0
%global         mm3d_plugins            ad3dsfilter imtex
%global         major_version           1.3

Name:           mm3d
Version:        1.3.12
Release:        3%{?dist}
Summary:        3D model editor

License:        GPLv2+
URL:            https://clover.moe/mm3d
Source0:        https://github.com/zturtleman/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       http://www.misfitcode.com/misfitmodel3d/download/plugins/ad3dsfilter-%{plugin_3ds_ver}.tar.gz
Source11:       http://www.misfitcode.com/misfitmodel3d/download/plugins/imtex-%{plugin_imtex_ver}.tar.gz
Patch0:         mm3d-1.3.11-sighandler.patch
Patch10:        mm3d-ad3dsfilter-make.patch
Patch11:        mm3d-imtex-make.patch
Patch12:        mm3d-imtex-gcc43.patch

BuildRequires:  dos2unix
BuildRequires:  libtool
# for Qt5Core Qt5Gui Qt5Widgets Qt5OpenGL
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  libXmu-devel
BuildRequires:  libGLU-devel
BuildRequires:  lua-devel
BuildRequires:  perl(HTML::Template)
BuildRequires:  desktop-file-utils
# for plugins
BuildRequires:  lib3ds-devel
BuildRequires:  imlib2-devel


%description
Maverick Model 3D is an OpenGL-based 3D model editor that works with
triangle-based models. It supports multi-level undo, skeletal animations,
simple texturing, scripting, command-line batch processing, and a plugin
system for adding new model and image filters. Complete online help
is included. It is designed to be easy to use and easy to extend
with plugins and scripts.


%prep
%setup -q -a 10 -a 11

%patch0 -p1 -b .sigh

%patch10 -b .ad3ds
%patch11 -b .imtex
%patch12 -b .gcc43

autoreconf -vif

for i in AUTHORS COPYING ChangeLog INSTALL README TODO doc/html/TODO
do
    dos2unix -q --keepdate $i
done

# remove bundled lib3ds
rm -rf plugins/ad3ds/lib3ds


%build
export CPPFLAGS="-DSHARED_PLUGINS=\\\"%{_libdir}/%{name}\\\""
%configure --with-Qt-include-dir=%{_qt5_includedir} --with-Qt-bin-dir=%{_qt5_bindir} --with-lua-dir=%{_usr} --with-lualib-dir=%{_usr} --with-lualib-lib=lua
make %{?_smp_mflags} "CFLAGS=$RPM_OPT_FLAGS -fPIC" "CXXFLAGS=$RPM_OPT_FLAGS -fPIC"

cd plugins
for d in %{mm3d_plugins}
do
    pushd $d
    make "CFLAGS=$RPM_OPT_FLAGS" "CXXFLAGS=$RPM_OPT_FLAGS"
    popd
done


%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/%{major_version}
for d in %{mm3d_plugins}
do
    install -p -m 0755 plugins/$d/$d.so $RPM_BUILD_ROOT%{_libdir}/%{name}/%{major_version}
done
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# docs
cp -p AUTHORS COPYING ChangeLog README TODO $RPM_BUILD_ROOT%{_datadir}/doc/%{name}


%files
%doc %{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*
%{_datadir}/%{name}/
%{_mandir}/man1/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Dan Horák <dan[at]danny.cz> 1.3.12-1
- update to 1.3.12

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Dan Horák <dan[at]danny.cz> 1.3.11-2
- modernize desktop support

* Thu Jan 03 2019 Dan Horák <dan[at]danny.cz> 1.3.11-1
- update to 1.3.11 with new upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8a-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8a-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8a-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8a-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8a-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8a-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.8a-11
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8a-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8a-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Dan Horák <dan[at]danny.cz> - 1.3.8a-8
- update for Lua 5.2 (#992270)
- update for unversioned docdir (#993907)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8a-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 15 2012 Dan Horák <dan[at]danny.cz> 1.3.8a-4
- fix build

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  6 2010 Dan Horák <dan[at]danny.cz> 1.3.8a-1
- rebuilt with updated source archive (no change)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Dan Horák <dan[at]danny.cz> 1.3.8-1
- update to 1.3.8

* Tue Feb 24 2009 Dan Horák <dan[at]danny.cz> 1.3.7a-1
- update to 1.3.7a
- better fix for the conflict between list type and parameter

* Thu Feb 19 2009 Dan Horák <dan[at]danny.cz> 1.3.7-3
- fixes for gcc 4.4

* Fri Jul  4 2008 Dan Horák <dan[at]danny.cz> 1.3.7-2
- fix plugin installation directory
- change how the docs are installed
- fix DocPath in the desktop file
- add scriptlets for updating the desktop database

* Tue Jul  1 2008 Dan Horák <dan[at]danny.cz> 1.3.7-1
- initial Fedora version
