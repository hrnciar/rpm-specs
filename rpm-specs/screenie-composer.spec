%global snapshot 49c2630

Name:           screenie-composer
Version:        1.0.0
Release:        0.23.20110805git%{snapshot}%{?dist}
Summary:        Fancy screenshot composer

License:        GPLv2+
URL:            https://github.com/ariya/screenie
# Tarballs are only available via github. The current snapshot can be downloaded at
# https://github.com/ariya/screenie/tarball/49c2630c393b003a473263001a18e27144744178
Source0:        ariya-screenie-%{snapshot}.tar.gz
Source1:        %{name}.desktop

# Link program libraries statically as they are not intended to
# be used by third-party developers. Their names are way too generic as well.
Patch0:         %{name}-%{version}-static.patch
# Fix segfault occured due to call of uninitialized class variables.
Patch1:         %{name}-%{version}-mime.patch
# remove rpath definition
Patch2:         %{name}-%{version}-rpath.patch
# undefine g++ macros major/minor expanded to gnu_dev_major/minor
Patch3:         %{name}-%{version}-gnu.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt4-devel

%description
Screenie is an easy to use screenshot composer tool that lets you create fancy
and stylish screenshots from a given set of images. 


%prep
%setup -q -n ariya-screenie-%{snapshot}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

find -type f -exec chmod 644 {} \;

%build
%{qmake_qt4}
make %{?_smp_mflags}


%install
install -D bin/release/Screenie %{buildroot}%{_bindir}/%{name}
install -D -p -m 644 src/Resources/img/application-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
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
BugReportURL: https://code.google.com/p/screenie/issues/detail?id=9
SentUpstream: 2014-07-08
-->
<application>
  <id type="desktop">screenie-composer.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Create stylish screenshots</summary>
  <description>
    <p>
      Screenie is a simple to use screenshot composition tool, with the abilty
      to add perspective and reflections to screenshots.
      To use screenie, the user simply imports a screenshot, then tweaks a few
      variables that control the angle of the perspective effect, the amount of
      reflection, and the background colour.
    </p>
  </description>
  <url type="homepage">https://code.google.com/p/screenie/</url>
  <screenshots>
    <screenshot type="default">http://lh6.ggpht.com/ariya.hidayat/SEW_gDTc7ZI/AAAAAAAAAdI/2jmyFxAuRYo/s400/2545790007_43dfcd4326_o.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files
%doc LICENSE.GPL2 README.txt
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.23.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.22.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.21.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.20.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.19.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Martin Gieseking <martin.gieseking@uos.de> - 1.0.0-0.18.20110805git
- Added BR: gcc-c++ according to new packaging guidelines.
- Updated project URL.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.17.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.16.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.15.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.14.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.13.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-0.12.20110805git49c2630
- use %%qmake_qt4 macro to ensure proper build flags

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.11.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-0.10.20110805git49c2630
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.0.0-0.9.20110805git49c2630
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.8.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.7.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.6.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.5.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.4.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.3.20110805git49c2630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 17 2011 Martin Gieseking <martin.gieseking@uos.de> 1.0.0-0.2.20110805git49c2630
- added patch to undefine g++ macros major/minor

* Fri Aug 05 2011 Martin Gieseking <martin.gieseking@uos.de> 1.0.0-0.1.20110805git49c2630
- initial package

