Name:           office-runner
Version:        1.0.2
Release:        16%{?dist}
Summary:        Office game for laptop owners

License:        GPLv3
URL:            http://www.hadess.net/2011/09/omg-i-haz-designed-bug-fix.html
Source0:        http://ftp.gnome.org/pub/GNOME/sources/office-runner/1.0/office-runner-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  gtk3-devel
BuildRequires:  gnome-settings-daemon-devel
BuildRequires:  desktop-file-utils

%description
This program is dedicated to office workers who want not to suspend their laptop
when moving between rooms meeting. office-runner inhibits suspend for 10 minutes 
when closing the lid and record their time when moving between meeting rooms.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/office-runner.desktop
%find_lang %{name}

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
<!-- Copyright 2014 William Moreno Reyes <williamjmorenor@gmail.com> -->
<!--
EmailAddress: hadess@hadess.net
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">office-runner.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Close your laptop lid and start running</summary>
  <description>
    <p>
      Office runner let you close your laptop lid and go quickly to a meeting or
      other place without having to wait until the computer turns off and then wake up.
    </p>
  </description>
  <url type="homepage">http://www.hadess.net/2011/09/omg-i-haz-designed-bug-fix.html</url>
  <screenshots>
    <screenshot type="default">http://2.bp.blogspot.com/-aJ2QmlyCCQ8/TnNgJniDNaI/AAAAAAAAAa8/jUiYw74gbjk/s1600/office-runner.png</screenshot>
  </screenshots>
</application>
EOF

%files -f %{name}.lang
%doc COPYING NEWS
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/office-runner.desktop
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-12
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-10
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.0.2-4
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 6 2013 Baptiste Mille-Mathias <baptistemm@fedoraproject.org> - 1.0.2-1
- New upstream release
  - More efficient drawing of the timer label
  - Fix conflicting desktop file categories
  - Fix "time to better time" calculation
  - Added French translation

* Sat Aug 24 2013 Baptiste Mille-Mathias <baptistem@gnome.org> - 1.0.1-2
- Update call to update icon cache to match the one provided in 
  http://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Icon_Cache
- Remove useless call to update-mime-database
- Use macro %%{buildroot} consistently

* Sun Aug 18 2013 Baptiste Mille-Mathias <baptistem@gnome.org> - 1.0.1-1
- Initial version
