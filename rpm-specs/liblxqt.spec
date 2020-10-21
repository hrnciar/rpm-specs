%define rpm_macros_dir %{_sysconfdir}/rpm
%if 0%{?fedora}
%define rpm_macros_dir %{_rpmconfigdir}/macros.d
%endif

Name:		liblxqt
Version:	0.15.0
Release:	3%{?dist}
License:	LGPLv2
Summary:	Core shared library for LXQt desktop suite
Url:		http://lxqt.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	macros.lxqt

BuildRequires: %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires: libXScrnSaver-devel
BuildRequires: lxqt-build-tools
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Xdg)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: cmake(PolkitQt5-1)
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif
Requires: xdg-utils >= 1.1.0

%description
Core utility library for all LXQT components

%package devel
Summary:	Devel files for liblxqt
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:       lxqt-build-tools >= 0.6.0
%if 0%{?fedora}
Requires: cmake >= 3.3
%else
Requires: cmake3 >= 3.3
%endif

%description devel
LXQt libraries for development.

%package l10n
BuildArch:      noarch
Summary:        Translations for liblxqt
Requires:       liblxqt
Obsoletes:      lxqt-l10n < 0.14.0

%description l10n
This package provides translations for the liblxqt package.

%prep
%setup -q 

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif

%cmake3 -DPULL_TRANSLATIONS=NO

%cmake_build

%if 0%{?el7}
EOF
%endif

%install
%cmake_install

# RPM macros
install -p -m0644 -D %{SOURCE1} %{buildroot}%{rpm_macros_dir}/macros.lxqt
sed -i -e "s|@@CMAKE_VERSION@@|%{version}|" %{buildroot}%{rpm_macros_dir}/macros.lxqt
touch -r %{SOURCE1} %{buildroot}%{rpm_macros_dir}/macros.lxqt

%find_lang liblxqt --with-qt

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING
%{_libdir}/liblxqt.so.0*
%{_bindir}/lxqt-backlight_backend
%{_datadir}/lxqt/power.conf
%{_datadir}/polkit-1/actions/org.lxqt.backlight.pkexec.policy

%files devel
%{_libdir}/liblxqt.so
%{_includedir}/lxqt/
%{_datadir}/cmake/lxqt/
%{_libdir}/pkgconfig/lxqt.pc
%{rpm_macros_dir}/macros.lxqt

%files l10n -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/%{name}
%{_datadir}/lxqt/translations/%{name}/liblxqt_ast.qm
%{_datadir}/lxqt/translations/%{name}/liblxqt_arn.qm

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-5
- Improve compatibility with epel7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.14.1-3
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com>   - 0.14.1-2
- rebuild (qt5)

* Mon Feb 25 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.1-1
- Update to 0.14.1

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-2
- Add l10n sub package

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-4
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- devel subpackage should depend on lxqt-build-tools

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
-  New upstream release 0.11.0

* Tue Feb 09 2016 Rex Dieter <rdieter@fedoraproject.org> 0.10.0-9
- fix grep usage in fix LXQtTranslateDesktop.cmake to assume text input (#1305999)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-7
- Remove razorqt obsoletes. Solves bug #1244155
- RazortQt EOL code should be maintained by bug requesters

* Thu Jan 14 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-6
- Rebuilt to all distros as missing for some reason on bodhi

* Sun Dec 13 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-5
- Fix macros 

* Tue Dec 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-4
- Add macros and use same process as kf5 to compile. Makes things easier with different cmake

* Tue Dec 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-3
- Prepare to use cmake3 on epel

* Mon Dec 07 2015 Orion Poplawski <orion@cora.nwra.com> - 0.10.0-2
- Update URL and Source0

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New major upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Rebuild (gcc5)

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Obsoletes razorqt-libs and razorqt-libs-devel

* Sun Feb 08 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-1
- Official new upstream release

* Mon Feb 02 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Prepare for 0.9.0

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-10
- Rebuild against new Qt 5.4.0

* Fri Dec 19 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-9
- As discussed on irc channel, let's simplify to keep only lxqt share data dir

* Tue Dec 16 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-8
- requires xdg-utils.

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-7
- own /usr/share/lxqt-qt5, /usr/share/lxqt-qt5/translations

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-6
- (upstreamable) patch to move cmake files to libdir properly

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-5
- revert cmake hack, cmake files still reference the old dir (working on a better solution)

* Fri Nov 07 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-4
- fix build for older distros/rpm (where %%autostetup isn't available, like el6)

* Fri Nov 07 2014 Helio Chissini de Castro <hcastro@redhat.com> 0.8.0-3
- Merge qt5 datadir patch

* Fri Nov 07 2014 TI_Eugene <ti.eugene@gmail.com> 0.8.0-2
- License changed to LGPLv2
- Removed BR liblxqt-devel in -devel package
- RHEL6 workaround in %%install section
- Library soname tune

* Mon Oct 27 2014 TI_Eugene <ti.eugene@gmail.com> 0.8.0-1
- initial packaging
