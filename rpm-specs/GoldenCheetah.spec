%global __cmake_in_source_build 1

#For git snapshots, set to 0 to use release instead:
%global usesnapshot 1
%if 0%{?usesnapshot}
%global commit0 6164dd963f154ce9a05661167b23c6c06b2649dd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%global commitdate 20200905
%endif

Name:           GoldenCheetah
%if 0%{?usesnapshot}
Version:        3.6
Release:        0.3.%{commitdate}git%{shortcommit0}%{?dist}
%else
Version:        3.5
Release:        3%{?dist}
%endif
Summary:        Cycling Performance Software
Epoch:          1
License:        GPLv3
URL:            http://www.goldencheetah.org/
%if 0%{?usesnapshot}
Source0:        https://github.com/GoldenCheetah/GoldenCheetah/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%else
Source0:        https://github.com/GoldenCheetah/GoldenCheetah/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif
Source1:        %{name}.desktop
# https://github.com/GoldenCheetah/GoldenCheetah/issues/2690
Source2:        %{name}.appdata.xml
# Use Qwt Widget Library
Patch0:         %{name}_20200614git5c84f7f.patch
Patch1:         %{name}_bison-3.7.patch
Patch2:         %{name}-gcc11.patch

BuildRequires:  gcc-c++
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  ImageMagick
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Bluetooth)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5Location)
#BuildRequires:  pkgconfig(QxtCore-qt5)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  lmfit-devel
BuildRequires:  libkml-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qttranslations
BuildRequires:  R-core-devel
BuildRequires:  R-Rcpp-devel
BuildRequires:  R-RInside-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sip-devel
BuildRequires:  gsl-devel
Requires:       hicolor-icon-theme

# qt5-qtwebengine-devel is missing on ppc64, ppc64le, s390x CPU architectures.
ExclusiveArch:  %{qt5_qtwebengine_arches}

%description
#Golden Cheetah is a program for cyclists: 
- download and import activities from most popular bike computers from CycleOps,
  SRM, Polar, Garmin and others;
- analyze, track and review performance data and metrics;
- train indoors with real-time monitoring supporting trainers from Racermate,
  Tacx and any ANT+ device; 
- Golden Cheetah is free software and distributed under the GPL.

%package data
Summary:       Icons and translation files for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description data
This package contains icons and translation files.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep
%if 0%{?usesnapshot}
%setup -qn %{name}-%{commit0}
%else
%setup -qn %{name}-%{version}
%endif
%patch0 -p1
%patch1 -p1
%patch2 -p1

# fixes W: spurious-executable-perm
find . -type f  \( -name "*.cpp" -o -name "*.h" \) -exec chmod a-x {} \;

%build
# Create translation files.
lrelease-qt5 src/Resources/translations/*.ts
%{_qt5_qmake} %{_qt5_qmake_flags}
%make_build

%install
mkdir -p %{buildroot}%{_bindir}/
cp -p %{_builddir}/%{buildsubdir}/src/GoldenCheetah %{buildroot}%{_bindir}/

desktop-file-install                        \
--dir=%{buildroot}%{_datadir}/applications  \
%{SOURCE1}

install -Dm644 %{SOURCE2} %{buildroot}/%{_metainfodir}/%{name}.appdata.xml

install -d -m 0755 %{buildroot}%{_datadir}/%{name}/translations
install -m 0644 src/Resources/translations/gc_{es,nl,zh-tw,pt-br,pt,ru,it,cs,ja,de,sv,fr,zh-cn}.qm \
        %{buildroot}%{_datadir}/%{name}/translations

#icons
for size in 256 48 32 16; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
  convert doc/web/logo.jpg -resize ${size} %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

%find_lang %{name} --all-name --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files data
%{_datadir}/%{name}

%files doc
%doc doc/user/*.pdf

%changelog
* Mon Oct 12 2020 Jeff Law <law@redhat.com> - 3.6-0.3.20200908git6164dd9
- Add missing #include for gcc-11

* Fri Sep 18 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.6-0.2.20200908git6164dd9
- Update to 3.6-0.2.20200905git6164dd9
- Add GoldenCheetah_bison-3.7.patch
- Rebuilt for new qt5-qtcharts

* Sun Aug 09 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.6-0.1.20200908git7c90abf
- Revert version 4.0 and use master git
- Add epoch to allow install older version

* Sun Jul 26 2020 Martin Gansser <martinkg@fedoraproject.org> - 4.0-0.1.20200614git5c84f7f
- Update to 4.0-0.1.20200614git5c84f7f
- fixes (BZ#1842192) and (BZ#1859481)
- Add BR gsl-devel
- Cleanup spec file

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.5-1
- Update to 3.5-1

* Mon Dec 09 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.14.rc2git5df46ee
- Update to 3.5-0.14.rc2git5df46ee
- Add BR srmio-devel

* Mon Oct 14 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.13.rc1gitd01fdf5
- Update to 3.5-0.13.rc1gitd01fdf5

* Wed Aug 21 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.12.20190821git1d6d66f
- Update to 3.5-0.12.20190821git1d6d66f
- Remove BR qwtplot3d-qt5-devel

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-0.11.20190225gitd93404f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.10.20190225gitd93404f
- Update to 3.5-0.10.20190225gitd93404f

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-0.9.20190127git9138a28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.8.20190128git9138a28
- Rebuilt for lmfit-8.2

* Mon Jan 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.7.20190128git9138a28
- Update to 3.5-0.7.20190128git9138a28

* Thu Dec 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.6.20181211gitf7d2431
- Update to 3.5-0.6.20181211gitf7d2431
- qwtplot3d is deprecated removed from sys-path.patch

* Wed Nov 28 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.5.20181125gitea5c07d
- Merge qxt-sys.patch qwt3d-sys.patch and lmfit-levmar.patch to sys-path.patch
- Update to 3.5-0.5.20181125gitea5c07d

* Mon Nov 26 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.4.20181125git0c668c0
- Add %%{name}-lmfit-levmar.patch
- Update to git0c668c0 

* Fri Nov 23 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.3.20181120gitaae6243
- Add BR gcc-c++
- Add comments explaining what the patches do
- Correct version to 3.5 dev branch
- Remove obsolete scriptlets
- use %%find_lang macro for translation files
- Remove owned directories in the data subpackage

* Thu Nov 22 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.2.20181120gitaae6243
- Add %%{name}-qxt-sys.patch
- Add %%{name}-qwt3d-sys.patch

* Tue Nov 20 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.5-0.1.20181120gitaae6243
- initial build
