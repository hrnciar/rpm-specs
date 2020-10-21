Summary:        GUI for editing keybindings in Enlightenment, DR16
Name:           e16-keyedit
Version:        0.8
Release:        9%{?dist}
License:        MIT with advertising
URL:            http://www.enlightenment.org/
Source0:        http://downloads.sourceforge.net/enlightenment/e16-keyedit-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
Requires:       e16 >= 1.0.1
%description
The e16-keyedit package provides a graphical interface for managing
keybindings in Enlightenment, DR16.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}
cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=e16keyedit
Comment=Manage keybindings for e16
Exec=e16keyedit
Terminal=false
Type=Application
Icon=/usr/share/e16/misc/e16
Categories=Settings;DesktopSettings;
EOF

%install
%{make_install}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop

%files
%license COPYING
%doc README AUTHORS ChangeLog
%{_bindir}/e16keyedit
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.8-1
- 0.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7-8
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- fix desktop file to follow specification

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.7-4
- Rebuilt for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 16 2010 Terje Rosten <terjeros@phys.ntnu.no> - 0.7-2
- Add patch now upstream
- Require newer e16

* Fri Apr 16 2010 Terje Rosten <terjeros@phys.ntnu.no> - 0.7-1
- 0.7

* Sun Feb 14 2010 Terje Rosten <terjeros@phys.ntnu.no> - 0.6-1
- 0.6
- Add DSO patch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 18 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.5-3
- Add desktop file

* Thu Mar 27 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.5-2
- Fix license

* Mon Aug 20 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.5-1
- Initial build (based on upstream spec, thanks!)
