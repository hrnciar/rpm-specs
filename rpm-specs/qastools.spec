Name:           qastools
Version:        0.21.0
Release:        9%{?dist}
Summary:        Collection of desktop applications for ALSA
License:        GPLv3

URL:            http://xwmw.org/qastools
Source0:        http://downloads.sourceforge.net/%{name}/%{version}/%{name}_%{version}.tar.xz

BuildRequires:  cmake gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel qt5-qtsvg-devel qt5-linguist
BuildRequires:  pkgconfig(alsa)
# For libudev.h
BuildRequires:  systemd-devel

Requires:       qasconfig%{?_isa} = %{version}-%{release}
Requires:       qashctl%{?_isa} = %{version}-%{release}
Requires:       qasmixer%{?_isa} = %{version}-%{release}


%description
QasTools is a collection of desktop applications for the ALSA sound system.


%package        -n qascommon
Summary:        Common part of QasTools

%description	-n qascommon
Common part of QasTools.


%package	-n qasconfig
Summary:	ALSA configuration browser
Requires:	qascommon%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description	-n qasconfig
Browser for the ALSA configuration tree.


%package	-n qashctl
Summary:	ALSA complex mixer
Requires:	qascommon%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description	-n qashctl
Mixer for ALSA's more complex "High level Control Interface".


%package	-n qasmixer
Summary:	ALSA simple mixer
Requires:	qascommon%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description	-n qasmixer
Desktop mixer for ALSA's "Simple Mixer Interface" (alsamixer).


%prep
%setup -q -n %{name}_%{version}


%build
%cmake -DSKIP_LICENSE_INSTALL:BOOL=ON
make %{?_smp_mflags}


%install
%make_install
for file in %{buildroot}/%{_datadir}/applications/*.desktop; do
    desktop-file-validate $file
done
%find_lang %{name} --with-qt --without-mo
# hack
rm -f %{buildroot}/%{_datadir}/%{name}/l10n/qastools_default.qm

%files
# meta package

%files -n qascommon -f %{name}.lang
%license COPYING
%doc CHANGELOG README TODO
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/widgets/

%files -n qasconfig
%{_bindir}/qasconfig
%{_datadir}/applications/qasconfig.desktop
%{_datadir}/icons/hicolor/*/apps/qasconfig.*
%{_mandir}/man1/qasconfig.1.*

%files -n qashctl
%{_bindir}/qashctl
%{_datadir}/applications/qashctl.desktop
%{_datadir}/icons/hicolor/*/apps/qashctl.*
%{_mandir}/man1/qashctl.1.*

%files -n qasmixer
%{_bindir}/qasmixer
%{_datadir}/%{name}/icons/
%{_datadir}/applications/qasmixer.desktop
%{_datadir}/icons/hicolor/*/apps/qasmixer.*
%{_mandir}/man1/qasmixer.1.*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.21.0-4
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Richard Shaw <hobbes1069@gmail.com> - 0.21.0-1
- Update to latest upstream release.

* Tue Apr 26 2016 Richard Shaw <hobbes1069@gmail.com> - 0.20.0-1
- Update to latest upstream release.

* Sun Feb  7 2016 Richard Shaw <hobbes1069@gmail.com> - 0.18.1-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.17.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 26 2013 TI_Eugene <ti.eugene@gmail.com> - 0.17.2-1
- Vesion bump
- Splitting into separate subpackages
- Spec cleanups

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Richard Shaw <hobbes1069@gmail.com> - 0.17.1-3
- Fix FTBFS for rawhide/GCC 4.7.

* Tue Apr 17 2012 Richard Shaw <hobbes1069@gmail.com> - 0.17.1-2
- Inital release.
- Updated spec file per reviewer comments.
