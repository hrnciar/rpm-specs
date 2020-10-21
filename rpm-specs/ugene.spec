Name:    ugene
Summary: Integrated bioinformatics toolkit
Version: 34.0
Release: 4%{?dist}
#The entire source code is GPLv2+ except:
#file src/libs_3rdparty/qtbindings_core/src/qtscriptconcurrent.h which is GPLv2
#files in src/plugins_3rdparty/script_debuger/src/qtscriptdebug/ which are GPLv2
License: GPLv2+ and GPLv2
URL:     http://ugene.net
Source0: https://github.com/ugeneunipro/ugene/archive/%{version}.tar.gz/#/%{name}-%{version}.tar.gz
#Patch0:  ugene-1.31.0.patch

Patch1:  ugene-fix-build-againt-qt-5.15.patch
Patch2:  %{name}-gcc11.patch

BuildRequires: desktop-file-utils
BuildRequires: mesa-libGLU-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-mysql
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtsensors-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtwebchannel-devel
BuildRequires: qt5-qtxmlpatterns-devel
BuildRequires: qt5-qtwebengine-devel
BuildRequires: qt5-qtwebsockets-devel
BuildRequires: qt5-qtwebchannel-devel
BuildRequires: zlib-devel

Provides: bundled(sqlite)
Provides: bundled(samtools)
ExclusiveArch: %{ix86} x86_64

%description
Unipro UGENE is a cross-platform visual environment for DNA and protein
sequence analysis. UGENE integrates the most important bioinformatics
computational algorithms and provides an easy-to-use GUI for performing
complex analysis of the genomic data. One of the main features of UGENE
is a designer for custom bioinformatics workflows.

%prep
%setup -q

%patch1 -p1 -b .fix-build-againt-qt-5.15
%patch2 -p1 -b .gcc11

%build
%{qmake_qt5} -r \
        INSTALL_BINDIR=%{_bindir} \
        INSTALL_LIBDIR=%{_libdir} \
        INSTALL_DATADIR=%{_datadir} \
        INSTALL_MANDIR=%{_mandir} \
%if 0%{?_ugene_with_non_free}
        UGENE_WITHOUT_NON_FREE=0 \
%else
        UGENE_WITHOUT_NON_FREE=1 \
%endif
        UGENE_EXCLUDE_LIST_ENABLED=1


make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt LICENSE.3rd_party.txt
%{_bindir}/*
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ugene.*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/%{name}/
%{_mandir}/man1/*

%changelog
* Sun Oct 18 2020 Jeff Law <law@redhat.com> - 34.0-4
- Fix missing #includes for gcc-11

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 34.0-3
- rebuild (qt5)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 34.0-1
- ugene-34.0
- update Source0 URL
- no longer uses qt5 private api (yay)
- use %%check

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 33.0-13
- rebuild (qt5)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 33.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 33.0-11
- rebuild (qt5)

* Sat Oct 05 2019 Yuliya Algaer <yalgaer@redhat.com> - 33.0-10
- New release

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1.31.1-7
- rebuild (qt5)
- workaround FTBFS using -fpermissive (#1736931)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.31.1-5
- rebuild (qt5)

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.31.1-4
- rebuild (qt5)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.31.1-2
- rebuild (qt5)

* Thu Oct 25 2018 Yuliya Algaer <yalgaer@fedoraproject.com> - 1.31.1-1
- New upstream release

* Fri Aug 24 2018 Yuliya Algaer <yalgaer@fedoraproject.org> - 1.31.0-6
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.30.0-24
- rebuild (qt5)

* Mon Jun 11 2018 Yuliya Algaer <yalgaer@fedoraproject.org> - 1.30.0-23
- New upstream release

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.29.0-7
- rebuild (qt5)

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 1.29.0-6
- rebuild (qt5)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.29.0-4
- Remove obsolete scriptlets

* Tue Jan 02 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.29.0-3
- Fix FTBFS with Qt 5.10

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.29.0-2
- rebuild (qt5)

* Sun Dec 31 2017 Yuliya Algaer <yalgaer@fedoraproject.org> - 1.29.0-1
- New upstream release.

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 1.28.1-3
- rebuild (qt5)

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.28.1-2
- rebuild (qt5)

* Tue Nov 21 2017 Yuliya Algaer <yalgaer@fedoraproject.org> - 1.28.1-1
- New upstream release.

* Tue Oct 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.27.0-8
- rebuild (qt5)

* Mon Aug 28 2017 Yuliya Algaer <yalgaer@fedoraproject.org> - 1.27.0-7
- New upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
