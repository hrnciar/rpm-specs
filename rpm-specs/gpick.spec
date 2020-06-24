%global commit 3b17cf9e8b8514bdf16c49ca970e6f47da34e6ae
%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
%global date 20181011

Name:		gpick
Version:	0.2.6
Release:	0.rc1%{?date:.%{date}git}.2%{?dist}.2
Summary:	Advanced color picker

License:	BSD
URL:		http://gpick.org

%{?shortcommit:
Source:		https://github.com/thezbyg/%{name}/archive/%{commit}/%{name}-%{version}rc1-%{shortcommit}.tar.gz}
%{!?shortcommit:
Source:		https://github.com/thezbyg/%{name}/archive/%{name}-%{version}rc1.tar.gz#/%{name}-%{version}rc1.tar.gz}

# This patch addresses the changes from GCC 10+ 
# eliminating header indirection
Patch:		include.patch

BuildRequires:	gcc-c++
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils 
BuildRequires:	gcc-c++
BuildRequires:	gettext-devel
BuildRequires:	libappstream-glib
BuildRequires:	libcurl-devel
BuildRequires:	OpenThreads-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	ragel

%description
Advanced color picker

%package	libs
Summary:	Libraries for %{name}

%description	libs
The %{name}-libs package contains shared library for %{name}.
	

%prep
%{?shortcommit:
%autosetup -p1 -n %{name}-%{commit}}
%{!?shortcommit:
%autosetup -p1 -n %{name}-%{version}rc1}
mkdir .git

# Delete external libraries and only use system dependencies to build GPick
rm -rf extern
echo "INTERNAL_EXPAT=False" >> user-config.py
echo "INTERNAL_LUA=False" >> user-config.py
echo "LOCALEDIR=\"%{_datadir}/locale\"" >> user-config.py

%build
#scons %%{?_smp_mflags} CFLAGS="%%{optflags}" CXXFLAGS="%%{optflags}" LDFLAGS="%%{optflags}"
%cmake \
	-DCFLAGS="%{optflags} -Wl,--as-needed" \
	-DCXXFLAGS="%%{optflags} -Wl,--as-needed" \
	-DLDFLAGS="%%{optflags} -Wl,--as-needed"
%make_build

%install
%make_install

# copy libraries
mkdir -p %{buildroot}%{_libdir}
cp -p %{_builddir}/%{name}-%{commit}/*.so %{buildroot}%{_libdir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%find_lang %{name}

%files -f %{name}.lang
%doc %{_docdir}/%{name}/copyright
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1.*

%files libs
%{_libdir}/*.so

%changelog
* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.2.6-0.rc1.20181011git.2.2
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-0.rc1.20181011git.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.2.6-0.rc1.20181011git.2
- Clean up files
- Patch to include string C header due to gcc 10+
- Drop ExcludeArch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-0.rc1.20181011git.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.2.6-0.rc1.20181011git.1
- Add missing libraries

* Sun Feb 17 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.2.6-0.rc1.20181011git
- 20181011 snapshot
- Switch to cmake for build
- Add OpenThread dependency for build requirement
- Use pkgconfig for expat dependency
- Use new macro for metainfo directort
- Drop patch
- Drop no longer needed posttrans

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-0.rc1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 0.2.6-0.rc1.3
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-0.rc1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-0.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 0.2.6-0.rc1
- Update to 2.6rc1
- Enable GTK3 support

* Fri Aug 18 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 0.2.5-21.20170217git
- Rebuilt for boost
- Exclude s390x arch

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-20.20170217git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-19.20170217git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 0.2.5-18.20170217git
- Latest git snapshot
- Clean up spec
- Set ExcludeArch for ppc64 ppc64le aarch64 armv7hl

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-17.20160613git569ee0f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 13 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0.2.5-16.20160613git569ee0f
- Latest upstream git snapshot
- Dropped downstream appdata
- Added ragel,libcurl and libappstream-lib as dependency

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.2.5-14
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.2.5-13
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.2.5-11
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.5-9
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.2.5-8
- Add an AppData file for the software center

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.2.5-7
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.2.5-4
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.2.5-2
- Rebuild for boost 1.54.0

* Wed May 15 2013 Tom Callaway <spot@fedoraproject.org> - 0.2.5-1
- update to 0.2.5, lua 5.2

* Sat Apr 13 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 0.2.4-4
- Updated spec based Packaging review (rhbz #913367)

* Wed Feb 20 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 0.2.4-2
- Adherance to Fedora Packaging guideline

* Sat Sep 01 2012 Alexis Lameire <alexisis-pristontale@hotmail.com> - 0.2.4-1
- initial release

