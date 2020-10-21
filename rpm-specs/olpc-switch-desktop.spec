Name:		olpc-switch-desktop
Version:	0.9.2
Release:	5%{?dist}
Summary:	OLPC desktop switching utilities

License:	GPLv2+
URL:		http://wiki.laptop.org/go/Olpc-switch-desktop
Source0:	http://dev.laptop.org/pub/source/olpc-switch-desktop/%{name}-%{version}.tar.bz2
Patch1:		olpc-switch-desktop-python3.patch
BuildArch:	noarch

BuildRequires:  gcc
BuildRequires:	gettext, desktop-file-utils, intltool
Requires:	python3, sugar, gtk3, python3-gobject, desktop-file-utils, dbus


%description
This package contains a Sugar control panel extension for switching to GNOME,
and a GNOME program for switching back to Sugar.


%prep
%autosetup -p1
sed -i 's#env python#env python3#' gnome/olpc-switch-to-sugar

%build
%configure
%make_build


%install
%make_install
%find_lang %{name}
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/olpc-switch-to-sugar.desktop


%files -f %{name}.lang
%license COPYING
%doc README
%{_bindir}/olpc-switch-to-sugar
%{_datadir}/icons/hicolor/scalable/apps/olpc-switch-to-sugar.svg
%{_datadir}/applications/olpc-switch-to-sugar.desktop
%{_datadir}/sugar/data/icons/module-switch-desktop.svg
%{_datadir}/sugar/extensions/cpsection/switchdesktop


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.2-3
- Initial move to python3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Peter Robinson <pbrobinson@fedoraproject.org>  0.9.2-1
- Update to 0.9.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9-10
- Remove obsolete scriptlets

* Fri Jan 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 14 2012 Daniel Drake <dsd@laptop.org> - 0.9-1
- New release, ported to GTK3

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 04 2011 Daniel Drake <dsd@laptop.org> - 0.8-1
- New version; fixes widget layout and adds translations

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.7-3
- recompiling .py files against Python 2.7 (rhbz#623340)

* Wed Dec  9 2009 Daniel Drake <dsd@laptop.org> - 0.7-2
- build requires intltool

* Wed Dec  9 2009 Daniel Drake <dsd@laptop.org> - 0.7-1
- Updated translations

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Daniel Drake <dsd@laptop.org> - 0.6-1
- Initial import

