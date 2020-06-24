%global debug_package %{nil}

Summary:       An additive synthesizer using JACK
Name:          Add64
Version:       3.9.3
Release:       1%{?dist}
URL:           http://sourceforge.net/projects/add64
Source0:       http://downloads.sourceforge.net/project/add64/%{name}-%{version}.tar.bz2
Source1:       %{name}.desktop
# icon taken from screenshot
Source2:       add64.png
Source3:       Makefile
License:       GPLv3

BuildRequires: jack-audio-connection-kit-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: desktop-file-utils

%description
Add64 is an additive synthesizer using Qt and the JACK audio connection kit

%prep
%setup -q -n %{name}-%{version}

%build
%{_qt5_libdir}/qt5/bin/qmake -makefile
make %{?_smp_mflags}

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/applications
install -d -m 755 %{buildroot}%{_datadir}/pixmaps

install -m 755 -p %{name} %{buildroot}%{_bindir}
install -m 644 -p %{SOURCE2} %{buildroot}%{_datadir}/pixmaps
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
    %{SOURCE1}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/add64/discussion/general/thread/6ff4fec1/
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">Add64.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Additive software sound synthesizer</summary>
  <description>
    <p>
      Add64 is an additive modular software synthesizer for generating sounds.
      Unlike other software synthesizers -- that use a skeuomorphic interface of
      knobs, sliders and buttons, Add64 displays a spectral graph and allows the
      user to modify the oscillators and related parameters.
    </p>
  </description>
  <url type="homepage">http://www.amsynth.com/add64.html</url>
  <screenshots>
    <screenshot type="default">http://www.amsynth.com/images/Add64-Harmonics.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files 
%doc LICENSE 
%{_bindir}/%{name}
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/add64.png

%changelog
* Sun May 24 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 3.9.3-1
- New version 3.9.3

* Tue May 05 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 3.9.2-1
- New version 3.9.2

* Sun Apr 26 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 3.9.0-1
- New version 3.9.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2.2-12
- gcc7 fix

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.2-8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.2.2-7
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 26 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.2.2-2
- Add missing BR

* Mon Jun 11 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.2.2-1
- Initial build
