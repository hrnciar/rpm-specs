%global         usegit      0
%global         mainrel     2

%global         githash     8c8534159d4898935b47f9103cf32cd9b21b3df5
%global         shorthash   %(TMP=%githash ; echo ${TMP:0:10})
%global         gitdate     Thu, 14 Sep 2017 00:32:14 +0300
%global         gitdate_num 20170914

%if 0%{?usegit} >= 1
%global         fedorarel   %{mainrel}.D%{gitdate_num}git%{shorthash}
%else
%global         fedorarel   %{?prever:0.}%{mainrel}%{?prever:.%{prerpmver}}
%endif

Name:           menu-cache
Version:        1.1.0
Release:        %{fedorarel}%{?dist}.2
Summary:        Caching mechanism for freedesktop.org compliant menus

License:        LGPLv2+ and GPLv2+
URL:            http://lxde.org
#VCS: git:git://lxde.git.sourceforge.net/gitroot/lxde/menu-cache
%if 0%{?usegit} >= 1
Source0:        https://github.com/lxde/menu-cache/archive/%{githash}/%{name}-%{version}-D%{gitdate_num}git%{githash}.tar.gz
%else
Source0:        http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
%endif
%if 0%{?el7}
# bz#1451069 - CVE-2017-8933 menu-cache: Insecure temporary file creation in get_socket_name function 
Patch0:         menu-cache-CVE-2017-8933.patch
%endif
# https://github.com/lxde/menu-cache/pull/19
Patch1:         menu-cache-1.1.0-0001-Support-gcc10-compilation.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libfm-extra)
%if 0%{?usegit} >= 1
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libtool
%endif

%description
Menu-cache is a caching mechanism for freedesktop.org compliant menus to 
speed up parsing of the menu entries. It is currently used by some of 
components of the LXDE desktop environment such as LXPanel or LXLauncher.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%if 0%{?usegit} >= 1
%setup -q -n %{name}-%{githash}
%else
%setup -q
%endif

%if 0%{?usegit} >= 1
sh autogen.sh
%endif
%patch1 -p1 -b .gcc10

%build
%global optflags %optflags -fno-common
%configure --disable-static --disable-silent-rules
# remove rpath in menu-cache-gen
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets


%files
#FIXME: add ChangeLog and NEWS if there is content
%doc AUTHORS
%license COPYING
%if 0%{?usegit} < 1
%doc NEWS
%endif
%doc README
%{_libexecdir}/%{name}/menu-cache-gen
%{_libexecdir}/%{name}/menu-cached
%{_libdir}/libmenu-cache.so.3*
#%{_mandir}/man*/*.gz


%files devel
%dir %{_includedir}/menu-cache/
%{_includedir}/menu-cache/*.h
%{_libdir}/libmenu-cache.so
%{_libdir}/pkgconfig/libmenu-cache.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 23 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-2
- Fix compilation with gcc10 -fno-common

* Fri Sep 20 2019 Zamir SUN <sztsian@gmail.com> - 1.1.0-1.5
- Improve compatibility for epel7
- Remove changelog that is out-of-order

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-1
- 1.1.0

* Fri Sep 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-7.D20170914git8c8534159d
- Update to the latest git

* Wed Sep 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-6.D20170913gitfd52af607c
- Update to the latest git
  - Yet another possible fix for #7

* Thu Sep  7 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-5.D20170905git2ef9df036c
- Update to the latest git
  - github #13 #16

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4.D20170514git56f6668459.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4.D20170514git56f6668459.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-4.D20170514git56f6668459
- Update to the latest git
  - use runtime home directory for socket path
    instead of tmpdir

* Sun Apr 23 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-3.D20170419gitdffb1314ec
- Update to the latest git
  - New API needed for new lxqt-runner (github #15)

* Tue Apr 18 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-2.D20170417git54ab9e4576
- Update to the latest git
  - Tentative fix for menu-cache-gen segv (sourceforge bug 863)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov  8 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-1
- 1.0.2

* Sun Oct 23 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.1-3.D20161021git441f0ca9a1
- Update to the latest git

* Sat Aug 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.1-2.D20160506git2932d67f30
- Update to the latest git
- Backport 2 patches from my branch
  - removal of monitored *.menu file triggers core dump (github#8)
  - menu-cached utilize 100% CPU (github#7)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  8 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.1-1
- 1.0.1

* Sat Nov 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-4.D20151128git0b1e85c263
- Again try the latest git, this should fix bug 1264489

* Sat Nov 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-3.D20151126git7e63ae3f66
- Again try the latest git

* Tue Nov 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-2.D20151117git2d65876eb6
- Try latest git

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-1
- 1.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 11 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 25 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.3-2
- No longer require redhat-menus

* Sun Jun 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3 (#827783)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Sun Feb 21 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Tue Nov 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.6-1
- Update to 0.2.6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Mon Apr 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Tue Mar 31 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Wed Dec 10 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Tue Dec 09 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0
- Split into base and devel package

* Sun Dec 07 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.3-1
- Initial Fedora package
