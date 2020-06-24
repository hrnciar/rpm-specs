
%if 0%{?fedora} > 21 || "%{?copr_projectname}" == "plasma-5"
%global plasma5 1
%else
%if 0%{?fedora} || 0%{?epel}
%global xscreensaver 1
%endif
%endif

Name:    kdeartwork
Version: 15.08.3
Release: 10%{?dist}
Summary: Additional artwork for KDE

License: GPLv2
URL:     http://www.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

# Upstream me! :) -- Rex
Patch0: kdeartwork-4.3.75-template.patch

BuildRequires: kdelibs4-devel >= 4.14
%if ! 0%{?plasma5}
BuildRequires: kde-workspace-devel
%endif

%description
%{summary}, including additional styles, themes.

%package common
Summary: Common files for %{name}
# when split occurred
Conflicts: kdeartwork < 4.11.90
Obsoletes: kdeartwork-sounds < 4.11.90
%if 0%{?plasma5}
Obsoletes: kdeartwork < %{version}-%{release}
Obsoletes: kdeartwork-kxs < %{version}-%{release}
Obsoletes: kdeartwork-screensavers < %{version}-%{release}
%endif
BuildArch: noarch
%description common
%{summary}.

%package -n nuvola-icon-theme
Summary: Nuvola icon theme
Requires: %{name}-common = %{version}-%{release}
BuildArch: noarch
%description -n nuvola-icon-theme
%{summary}.

%package -n kdeclassic-icon-theme
Summary: KDE classic icon theme
Requires: %{name}-common = %{version}-%{release}
BuildArch: noarch
%description -n kdeclassic-icon-theme
%{summary}.

%package -n kde-style-phase
Summary: Classic GUI style for KDE
Requires: %{name}-common = %{version}-%{release}
%description -n kde-style-phase
%{summary}.

%if ! 0%{?plasma5}
%package screensavers
Summary: screensavers for KDE
Requires: %{name}-common = %{version}-%{release}
BuildRequires: pkgconfig(libkexiv2)
%if 0%{?fedora} || 0%{?epel}
BuildRequires: pkgconfig(eigen3)
%endif
%if 0%{?xscreensaver}
BuildRequires: xscreensaver-extras xscreensaver-gl-extras
Requires: xscreensaver-extras xscreensaver-gl-extras
Requires: %{name}-kxs = %{version}-%{release}
%endif
%description screensavers
%{summary}.

%package kxs
Summary: Support for xscreensaver-based screensavers
Requires: %{name}-common = %{version}-%{release}
Requires: kde-workspace >= 4.11 
Requires: xscreensaver-base
%description kxs
%{summary}.
%endif

%package wallpapers
Summary: Additional wallpapers
Requires: %{name}-common = %{version}-%{release}
Requires: kde-filesystem
BuildArch: noarch
%description wallpapers
%{summary}.

%package -n mono-icon-theme
Summary: Mono icon theme
Requires: %{name}-common = %{version}-%{release}
# moved (in 4.6.80) from kdeaccessibility which had Epoch: 1
# this pkg listed last so Epoch doesn't pollute other subpkgs
Epoch: 1
BuildArch: noarch
%description -n mono-icon-theme
%{summary}.


%prep
%setup -q -n kdeartwork-%{version}%{?alphatag}

%if 0%{?xscreensaver}
%patch0 -p1 -b .template

# create missing xscreensavers desktop files
if [ -f kscreensaver/kxsconfig/screensaver.sh ] ; then
 sh kscreensaver/kxsconfig/screensaver.sh
fi
%endif

# omit trademarked icons
rm -fv IconThemes/*/*/apps/{acroread,mozilla*,opera,mac}.{png,svgz}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. \
%if 0%{?plasma5}
  -DBUILD_ColorSchemes:BOOL=OFF \
  -DBUILD_emoticons:BOOL=OFF \
  -DBUILD_kscreensaver:BOOL=OFF \
  -DBUILD_kwin-styles:BOOL=OFF \
  -DBUILD_WeatherWallpaper:BOOL=OFF \
  -DBUILD_desktopthemes:BOOL=OFF
%endif

popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%if 0%{?kdeclassic_icons}
%post -n kdeclassic-icon-theme
touch --no-create %{_kde4_iconsdir}/kdeclassic &> /dev/null || :

%posttrans -n kdeclassic-icon-theme
gtk-update-icon-cache %{_kde4_iconsdir}/kdeclassic &> /dev/null || :

%postun -n kdeclassic-icon-theme
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/kdeclassic &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/kdeclassic &> /dev/null || :
fi
%endif

%post -n nuvola-icon-theme
touch --no-create %{_kde4_iconsdir}/nuvola &> /dev/null || :

%posttrans -n nuvola-icon-theme
gtk-update-icon-cache %{_kde4_iconsdir}/nuvola-icon-theme &> /dev/null || :

%postun -n nuvola-icon-theme
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/nuvola &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/nuvola &> /dev/null || :
fi

%post -n mono-icon-theme
touch --no-create %{_kde4_iconsdir}/mono &> /dev/null || :

%posttrans -n mono-icon-theme
gtk-update-icon-cache %{_kde4_iconsdir}/mono-icon-theme &> /dev/null || :

%postun -n mono-icon-theme
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/mono &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/mono &> /dev/null || :
fi

%files common
%doc README
%license COPYING

%if ! 0%{?plasma5}
%files
%{_kde4_appsdir}/color-schemes/*.colors
%{_kde4_appsdir}/desktoptheme/Androbit
%{_kde4_appsdir}/desktoptheme/Aya
%{_kde4_appsdir}/desktoptheme/Produkt
%{_kde4_appsdir}/desktoptheme/slim-glow/
%{_kde4_appsdir}/desktoptheme/Tibanna
%{_kde4_appsdir}/kwin/
%{_kde4_libdir}/kde4/kwin*.so
%{_kde4_datadir}/emoticons/*

%if 0%{?xscreensaver}
%files kxs
%{_kde4_bindir}/kxsconfig
%{_kde4_bindir}/kxsrun
%endif

%files screensavers
%{_kde4_appsdir}/kfiresaver/
%{_kde4_appsdir}/kscreensaver/
%{_kde4_bindir}/*.kss
%{_kde4_datadir}/kde4/services/ScreenSavers/*
%endif

# split for multilib'ing
%files -n kde-style-phase
%{_kde4_appsdir}/kstyle/themes/phase.themerc
%{_kde4_libdir}/kde4/kstyle_phase_config.so
%{_kde4_libdir}/kde4/plugins/styles/phasestyle.so

%if 0%{?kdeclassic_icons}
%files -n kdeclassic-icon-theme
%{_kde4_iconsdir}/kdeclassic/
%endif

%files -n nuvola-icon-theme
%{_kde4_iconsdir}/nuvola/

%files -n mono-icon-theme
%{_kde4_iconsdir}/mono/

%files wallpapers
%{_kde4_datadir}/wallpapers/*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.08.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.08.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.08.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.08.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.08.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.08.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.08.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Rex Dieter <rdieter@fedoraproject.org> 15.08.3-1
- 15.08.3

* Thu Aug 20 2015 Than Ngo <than@redhat.com> - 15.08.0-1
- 15.08.0

* Wed Aug 05 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.3-1
- 15.04.3
- omit trademarked icons (#1005467)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.2-1
- 15.04.2

* Thu May 28 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.1-1
- 15.04.1

* Sat May 09 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.0-2
- copr conditional

* Fri Apr 17 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.0-1
- 15.04.0

* Thu Mar 05 2015 Rex Dieter <rdieter@fedoraproject.org> - 14.12.3-2
- drop Requires: kde-workspace
- omit main pkg (color-schemes, plasma theme, kwin style, emoticons), -screensavers on plasma5 (f22+)
- s/eigen2/eigen3/

* Sun Mar 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 14.12.3-1
- 14.12.3

* Tue Feb 24 2015 Than Ngo <than@redhat.com> - 14.12.2-1
- 14.12.2

* Sat Jan 17 2015 Rex Dieter <rdieter@fedoraproject.org> - 14.12.1-1
- 14.12.1

* Sun Nov 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1
- 4.14.3

* Sun Oct 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.2-1
- 4.14.2

* Tue Sep 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.1-1
- 4.14.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.0-1
- 4.14.0

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.97-1
- 4.13.97

* Mon Jul 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.2-1
- 4.13.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.1-1
- 4.13.1

* Sat Apr 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.0-1
- 4.13.0

* Fri Apr 04 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.97-1
- 4.12.97

* Sun Mar 23 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.95-1
- 4.12.95

* Wed Mar 19 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.90-1
- 4.12.90

* Sun Mar 02 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-1
- 4.12.2

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-1
- 4.12.1

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.97-1
- 4.11.97

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.95-1
- 4.11.95

* Tue Nov 19 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.90-3
- -kxs has kde-workspace dep too, make >= 4.11

* Sun Nov 17 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.90-2
- make kde-workspace dep unversioned

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.90-1
- 4.11.90
- introduce -common subpkg, Obsoletes: -sounds

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Wed Sep 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-1
- 4.11.1

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.95-1
- 4.10.95

* Fri Jun 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.90-1
- 4.10.90

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Mon Apr 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Tue Jan 22 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.90-1
- 4.9.90

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Thu Nov 22 2012 Than Ngo <than@redhat.com> - 1:4.9.3-2
- fix macro in changelog

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- 4.9.3

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 1:4.9.1-1
- 4.9.1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Tue May 01 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.1-1
- 4.8.1

* Tue Feb 28 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-2
- whitespace cosmetics
- s/kdebase-workspace/kde-workspace/

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.7.97-1
- 4.7.97

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.7.90-1
- 4.7.90

* Fri Nov 25 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.80-1
- 4.7.80 (beta 1)

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Tue Sep 06 2011 Than Ngo <than@redhat.com> - 4.7.1-1
- 4.7.1

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> - 4.7.0-1
- 4.7.0

* Fri Jul 08 2011 Jaroslav Reznik <jreznik@redhat.com> - 4.6.95-1
- 4.6.95 (rc2)

* Mon Jun 27 2011 Than Ngo <than@redhat.com> - 4.6.90-1
- 4.6.90 (rc1)

* Mon Jun 06 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.80-1
- 4.6.80 (beta1)
- add mono icon theme

* Fri Apr 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-1
- 4.6.3

* Wed Apr 06 2011 Than Ngo <than@redhat.com> - 4.6.2-1
- 4.6.2

* Sun Feb 27 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1
- 4.6.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.0-1
- 4.6.0

* Wed Jan 05 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-1
- 4.5.95 (4.6rc2)

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> 4.5.90-1
- 4.5.90 (4.6rc1)

* Sat Dec 04 2010 Thomas Janssen <thomasj@fedoraproject.org> 4.5.85-1
- 4.5.85 (4.6beta2)

* Sun Nov 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-1
- 4.5.80 (4.6beta1)

* Fri Oct 29 2010 Than Ngo <than@redhat.com> - 4.5.3-1
- 4.5.3

* Fri Oct 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-1
- 4.5.2

* Fri Aug 27 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.5.1-1
- 4.5.1

* Tue Aug 03 2010 Than Ngo <than@redhat.com> - 4.5.0-1
- 4.5.0

* Sun Jul 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.95-1
- 4.5 RC3 (4.4.95)

* Wed Jul 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.92-1
- 4.5 RC2 (4.4.92)

* Fri Jun 25 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.90-1
- 4.5 RC1 (4.4.90)

* Mon Jun 07 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.85-1
- 4.5 Beta 2 (4.4.85)

* Fri May 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.80-1
- 4.5 Beta 1 (4.4.80)

* Fri Apr 30 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.3-1
- 4.4.3

* Mon Mar 29 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.4.2-1
- 4.4.2

* Sat Feb 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.1-1
- 4.4.1

* Fri Feb 12 2010 Than Ngo <than@redhat.com> - 4.4.0-2
- fix build issue 

* Fri Feb 05 2010 Than Ngo <than@redhat.com> - 4.4.0-1
- 4.4.0

* Sun Jan 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.98-1
- KDE 4.3.98 (4.4rc3)

* Wed Jan 20 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.3.95-1
- KDE 4.3.95 (4.4rc2)

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-1
- kde-4.3.90 (4.4rc1)

* Fri Dec 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.85-1
- kde-4.3.85 (4.4beta2)

* Tue Dec  1 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.80-1
- KDE 4.4 beta1 (4.3.80)

* Sun Nov 22 2009 Ben Boeckel <MathStuf@gmail.com> - 4.3.75-0.1.svn1048496
- Update to 4.3.75 snapshot

* Fri Nov 13 2009 Than Ngo <than@redhat.com> - 4.3.3-2
- rhel cleanup, fix conditional for RHEL

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Oct 26 2009 Than Ngo <than@redhat.com> - 4.3.2-3
- rhel cleanup

* Tue Oct 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.2-2
- rebuild (eigen2)

* Sun Oct 04 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Mon Sep 28 2009 Than Ngo <than@redhat.com> - 4.3.1-2
- rhel cleanup

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1
- add missing screensavers bz#472886

* Thu Aug 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-2
- kde-style-phase subpkg (multilib'd)
- %%files: cleanup some dir ownership

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Tue Jul 21 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Thu Jul 09 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3.rc2

* Thu Jun 25 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Thu Jun 04 2009 Lorenzo Villani <lvillani@binaryhelix.net> - 4.2.90-1
- KDE 4.3 Beta 2

* Wed May 13 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.85-1
- KDE 4.3 beta 1

* Wed Apr 01 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-3
- optimize scriptlets
- omit (unused) noarch hacks, use f10+ support
- -extras -> -screensavers rename
- -icons -> kdeclassic-icon-theme rename
- main pkg, Requires: -wallpapers, -sounds (upgrade path)
- -wallpapers, -sounds: drop Req: kdebase-workspace
- BR: eigen2-devel

* Tue Mar 31 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.2.2-2
- split wallpapers and sounds
- noarch subpackages

* Mon Mar 30 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-1
- KDE 4.2.2

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 4.2.1-1
- 4.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Sat Jan 10 2009 Than Ngo <than@redhat.com> - 4.1.96-2
- fix file list

* Wed Jan 07 2009 Than Ngo <than@redhat.com> - 4.1.96-1
- 4.2rc1

* Thu Dec 11 2008 Than Ngo <than@redhat.com> -  4.1.85-1
- 4.2beta2

* Wed Nov 26 2008 Than Ngo <than@redhat.com> 4.1.80-3
- enable webcollage since xscreensaver has sane default setting

* Thu Nov 20 2008 Than Ngo <than@redhat.com> 4.1.80-2
- drop duplicated BRs

* Wed Nov 19 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-1
- 4.1.80
- BR cmake 2.6
- make install/fast

* Tue Nov 18 2008 Than Ngo <than@redhat.com> 4.1.3-2
- drop webcollage bz#461926

* Wed Nov 12 2008 Than Ngo <than@redhat.com> 4.1.3-1
- KDE 4.1.3

* Mon Sep 29 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-2
- make VERBOSE=1
- respin against new(er) kde-filesystem

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- 4.1.2

* Fri Aug 29 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Wed Jul 23 2008 Than Ngo <than@redhat.com> 4.1.0-1
- 4.1.0

* Fri Jul 18 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-1
- 4.0.99

* Fri Jul 11 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-1
- 4.0.98

* Sun Jul 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-1
- 4.0.85

* Fri Jun 27 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.84-1
- 4.0.84

* Thu Jun 19 2008 Than Ngo <than@redhat.com> 4.0.83-1
- 4.0.83 (beta2)

* Sun Jun 15 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.82-1
- 4.0.82

* Wed Jun 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.80-2
- omit crystalsvg icons for now

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta1

* Wed May 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.72-1
- update to 4.0.72

* Fri Apr 18 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.3-6
- revert icons noarch hack (wasn't working anyway, rel-eng veto)

* Thu Apr 17 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.3-5
- -icons: build noarch

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.3-3
- -kxs: move here: Requires: kdebase-workspace

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- rebuild for NDEBUG and _kde4_libexecdir

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3

* Mon Mar 24 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.2-3
- kdeartwork-icons-crystalsvg -> crystalsvg-icon-theme
- add scriptlet deps

* Thu Mar 20 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.2-2
- -icons: Provides: *-icon-theme (Locolor, ikons, kdeclassic, kids, slick)
- include noarch build hooks (not enabled)

* Thu Feb 28 2008 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2

* Mon Feb 25 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-3
- %%files: don't own %%_kde4_libdir/kde4/plugins (thanks wolfy!)

* Fri Feb 15 2008 Than Ngo <than@redhat.com> 4.0.1-2
- rebuilt against GCC 4.3

* Sat Feb 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-1
- update to 4.0.1

* Tue Jan 08 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.0-1
- update to 4.0.0

* Mon Dec 10 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.97.0-1
- kde-3.97.0
- touchup for cvs import
- rework subpkg names a bit

* Fri Nov 30 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.2-1
- kde-3.96.2

* Fri Nov 23 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.1-1
- kde-3.96.1

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-5
- put crystalsvg-icon-theme in it's own subpkg

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-4
- BR: kde-filesystem >= 4

* Sun Nov 18 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-3
- BR: libXtst-devel
- Require kdebase-workspace not kdebase-workspace-devel

* Sun Nov 18 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-2
- kdeartwork-icons: Provide: crystalsvg-icon-theme

* Sun Nov 18 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-1
- Initial version for Fedora

* Sat Oct 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.5.8-1
- kde-3.5.8

* Wed Aug 29 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.5.7-4
- License: GPLv2
- (Build)Requires: kdebase3(-devel)

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.5.7-3
- Rebuild for selinux ppc32 issue.

* Fri Jul 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.5.7-2
- webcollagerc: [directory] /usr/share/backgrounds/images/ (#227683)

* Mon Jun 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.5.7-1
- 3.5.7

* Thu May 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.5.6-5
- don't include %%_bindir/kxs* in main pkg
- --enable-final

* Fri May 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.5.6-4
- resurrect -kxs subpkg (see also #220704)

* Wed Mar 21 2007 Than Ngo <than@redhat.com> - 3.5.6-2.fc7
- cleanup specfile

* Wed Feb 07 2007 han Ngo <than@redhat.com> 3.5.6-1.fc7
- 3.5.6

* Thu Aug 10 2006 Than Ngo <than@redhat.com> 3.5.4-1
- rebuild

* Mon Jul 24 2006 Than Ngo <than@redhat.com> 3.5.4-0.pre1
- prerelease of 3.5.4 (from the first-cut tag)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.5.3-1.1
- rebuild

* Thu Jun 01 2006 Than Ngo <than@redhat.com> 3.5.3-1
- update to 3.5.3

* Wed Apr 05 2006 Than Ngo <than@redhat.com> 3.5.2-1
- update to 3.5.2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.5.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.5.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Than Ngo <than@redhat.com> 3.5.1-1
- 3.5.1

* Sat Dec 17 2005 Than Ngo <than@redhat.com> 3.5.0-2
- requires on xscreensaver-extras

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov 29 2005 Than Ngo <than@redhat.com> 3.5.0-1
- 3.5 final

* Tue Oct 25 2005 Than Ngo <than@redhat.com> 3.4.92-1
- update to 3.5 Beta 2

* Thu Oct 06 2005 Than Ngo <than@redhat.com> 3.4.91-1
- update to 3.5 Beta 1

* Tue Aug 09 2005 Than Ngo <than@redhat.com> 3.4.2-1
- update to 3.4.2

* Thu Jun 30 2005 Than Ngo <than@redhat.com> 3.4.1-2
- configure script does not look the right xscreensaver dirs
  apply patch to fix this problem, #161312, thanks to Rex Dieter

* Tue Jun 28 2005 Than Ngo <than@redhat.com> 3.4.1-1
- 3.4.1

* Fri Mar 18 2005 Than Ngo <than@redhat.com> 3.4.0-1
- 3.4.0

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 3.4.0-0.rc1.2
- rebuilt against gcc-4.0.0-0.31

* Mon Feb 28 2005 Than Ngo <than@redhat.com> 3.4.0-0.rc1.1
- 3.4.0 rc1

* Wed Feb 16 2005 Than Ngo <than@redhat.com> 3.3.92-0.1
- KDE-3.4 Beta2

* Wed Dec 15 2004 Than Ngo <than@redhat.com> 3.3.2-0.3
- fix buildreq on xscreensaver-base

* Mon Dec 06 2004 Than Ngo <than@redhat.com> 3.3.2-0.2
- add correct paths for xscreensaver, xscreensaver-4.18-14 stores the
  config files and graphic hacks in %%{_libdir}/xscreensaver/config/hacks
  and %%{_libexecdir}/xscreensaver/hacks/

* Fri Dec 03 2004 Than Ngo <than@redhat.com> 3.3.2-0.1
- update to 3.3.2
- remove kdeartwork-3.3.1-kaleidescope.patch, it's included in 3.3.2

* Tue Nov 02 2004 Than Ngo <than@redhat.com> 3.3.1-3
- fix typo in configuration command.

* Mon Oct 18 2004 Than Ngo <than@redhat.com> 3.3.1-2
- rebuilt

* Wed Oct 13 2004 Than Ngo <than@redhat.com> 3.3.1-1
- update to 3.3.1

* Mon Aug 23 2004 Than Ngo <than@redhat.com> 3.3.0-1
- update to 3.3.0 release
- fix file conflict

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 3.3.0-0.1.rc2
- update to 3.3.0 rc2

* Mon Jun 21 2004 Than Ngo <than@redhat.com> 3.2.3-1
- update to 3.2.3

* Mon May 24 2004 Than Ngo <than@redhat.com> 3.2.2-3
- fix file conflict with other kde packages

* Mon May 24 2004 Than Ngo <than@redhat.com> 3.2.2-2
- fix file conflict with other kde packages

* Tue Apr 13 2004 Than Ngo <than@redhat.com> 3.2.2-1
- 3.2.2 release

* Thu Apr 08 2004 Than Ngo <than@redhat.com> 3.2.1-3
- fix file conflict with kdeedu

* Thu Apr 08 2004 Than Ngo <than@redhat.com> 3.2.1-2
- fix icontheme name, bug #119015

* Sun Mar 07 2004 Than Ngo <than@redhat.com> 3.2.1-1
- 3.2.1 release

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 05 2004 Than Ngo <than@redhat.com> 3.2.0-0.3
- 3.2.0 release
- build against qt 3.3.0

* Mon Jan 19 2004 Than Ngo <than@redhat.com> 3.1.95-0.1
- KDE 3.2 RC1

* Mon Dec 15 2003 Than Ngo <than@redhat.com> 3.1.94-0.2
- subpackage for icon

* Mon Dec 01 2003 Than Ngo <than@redhat.com> 3.1.94-0.1
- KDE 3.2 Beta 2

* Thu Nov 27 2003 Than Ngo <than@redhat.com> 3.1.93-0.2
- get rid of rpath

* Wed Nov 12 2003 Than Ngo <than@redhat.com> 3.1.93-0.1
- KDE 3.2 Beta1
- cleanup

* Tue Sep 30 2003 Than Ngo <than@redhat.com> 3.1.4-1
- 3.1.4

* Mon Sep 01 2003 Than Ngo <than@redhat.com> 3.1.3-3
- add requires xscreensaver

* Tue Aug 12 2003 Than Ngo <than@redhat.com> 3.1.3-2
- rebuilt

* Mon Aug 04 2003 Than Ngo <than@redhat.com> 3.1.3-1
- 3.1.3

* Thu Jun 26 2003 Than Ngo <than@redhat.com> 3.1.2-5
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Than Ngo <than@redhat.com> 3.1.2-3
- get rid of buildrequires atomake15

* Mon May 19 2003 Than Ngo <than@redhat.com> 3.1.2-2
- 3.1.2

* Wed Mar 19 2003 Than Ngo <than@redhat.com> 3.1.1-1
- 3.1.1

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Fri Feb 21 2003 Than Ngo <than@redhat.com> 3.1-2
- get rid of gcc path from dependency_libs

* Tue Jan 28 2003 Than Ngo <than@redhat.com> 3.1-1
- 3.1 final

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 3.1-0.4
- rebuild

* Tue Jan 14 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.3
- removed size_t check
- excluded ia64

* Mon Jan 13 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.2
- rc6

* Wed Nov 27 2002 Than Ngo <than@redhat.com> 3.1-0.1
- update to 3.1 rc4
- get rid of sub packages

* Sun Nov 10 2002 Than Ngo <than@redhat.com> 3.0.5-1
- update to 3.0.5

* Thu Nov  7 2002 Than Ngo <than@redhat.com> 3.0.4-2
- fix some build problems

* Tue Oct 15 2002 Than Ngo <than@redhat.com> 3.0.4-1
- 3.0.4

* Fri Sep 13 2002 Than Ngo <than@redhat.com> 3.0.3-3.1
- Fixed to build on x86_64

* Mon Sep  2 2002 Than Ngo <than@redhat.com> 3.0.3-3
- Add BuildPrereq automake15

* Sun Aug 25 2002 Than Ngo <than@redhat.com> 3.0.3-2
- rebuild against new qt

* Mon Aug 12 2002 Than Ngo <than@redhat.com> 3.0.3-1
- 3.0.3

* Tue Jul 23 2002 Tim Powers <timp@redhat.com> 3.0.2-3
- build using gcc-3.2-0.1

* Fri Jul 19 2002 Than Ngo <than@redhat.com> 3.0.2-2
- Fixed screen saver issue

* Tue Jul 09 2002 Than Ngo <than@redhat.com> 3.0.2-1
- 3.0.2
- use desktop-file-install

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 14 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.1-1
- 3.0.1

* Tue Apr 16 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-4
- Rebuild

* Wed Mar 27 2002 Than Ngo <than@redhat.com> 3.0.0-3
- final

* Thu Jan 31 2002 Bernhard Rossenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020129.2
- Remove KBlankscreen, it's in kdebase

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jan  8 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020108.1
- Add missing files

* Mon Jan  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020107.1
- Update

* Mon Jul 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010723.1
- Update
