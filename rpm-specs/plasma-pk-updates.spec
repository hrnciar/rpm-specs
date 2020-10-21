%undefine __cmake_in_source_build

#global commit0 73b70b3834a8fafdc4d6e93ee448b263cb0f9060
#global gittag0 GIT-TAG
#global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global snap 20170102

Name:           plasma-pk-updates
Version:        0.3.2
Release:        7%{?dist}
Summary:        Plasma applet for system updates using PackageKit

License:        GPLv2+
URL:            https://cgit.kde.org/plasma-pk-updates.git
# Git snapshot
# git clone git://anongit.kde.org/plasma-pk-updates.git; cd plasma-pk-updates
# git archive --prefix=plasma-pk-updates-%{version}/ %{commit0} | xz -9 > ../plasma-pk-updates-%{version}-%{shortcommit0}.tar.xz
Source0:        plasma-pk-updates-%{version}.tar.xz

# Upstream patches

# Downstream patches
Patch100: plasma-pk-updates-0.3.2-notif.patch

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  PackageKit-Qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

BuildRequires:  libappstream-glib

Requires:       PackageKit

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.plasma.pkupdates.appdata.xml ||:


%files -f %{name}.lang
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.pkupdates.desktop
%{_kf5_qmldir}/org/kde/plasma/PackageKit/
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.pkupdates/
%{_kf5_metainfodir}/org.kde.plasma.pkupdates.appdata.xml


%changelog
* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.3.2-7
- drop persistent notifications (#1316705,#1358146)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Jan Grulich <jgrulich@redhat.com> - 0.3.2-1
- 0.3.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-8
- rebuild

* Sun Jan 21 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.1-7
- PackageKit-Qt 1.0.x build fix upstreamed, use patch from upstream git

* Sun Jan 21 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.1-6
- fix FTBFS with PackageKit-Qt 1.0.x: remove unused obsolete PkStrings::message

* Tue Jan 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-5
- pull in upstream fixes

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-2
- .spec cosmetics: fix URL for real, use %%autosetup

* Wed May 31 2017 Jan Grulich <jgrulich@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Thu Apr 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.2-12.20170102git73b70b3
- update URL, fix %%snap

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11.20160307git73b70b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Jan Grulich <jgrulich@redhat.com> - 0.2-10-20170102git73b70b3
- Fresh snapshot
  Resolves: kdebz#374429

* Mon Mar 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.2-9.20160307git7b484b0
- update URL, fresh snapshot

* Mon Mar 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.2-8.20160216git
- omit plasma update script (no longer needed)

* Tue Feb 16 2016 Jan Grulich <jgrulich@redhat.com> - 0.2-7.20160216git
- Update to latest git snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Rex Dieter <rdieter@fedoraproject.org> 0.2-5
- rebuild (PackageKit-Qt)

* Thu Oct 29 2015 Rex Dieter <rdieter@fedoraproject.org> 0.2-4
- .spec cosmetics, (explicit) Requires: PackageKit

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Apr 07 2015 Jan Grulich <jgrulich@redhat.com> 0.2-1
- update to 0.2

* Mon Mar 30 2015 Rex Dieter <rdieter@fedoraproject.org> 0.1-4
- enable org.kde.plasma.pkupdates by default, except not liveimage (#1206760)

* Mon Mar 23 2015 Jan Grulich <jgrulich@redhat.com> - 0.1-3
- backport minor fixes from upstream

* Mon Mar 23 2015 Jan Grulich <jgrulich@redhat.com> - 0.1-2
- fix URL

* Wed Mar 18 2015 Jan Grulich <jgrulich@redhat.com> - 0.1-1
- Initial relase
