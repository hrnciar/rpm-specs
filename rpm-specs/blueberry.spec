Name:		blueberry
Version:	1.3.7
Release:	2%{?dist}
Summary:	Bluetooth configuration tool

License:	GPLv3+
URL:		https://github.com/linuxmint/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	python3-devel

Requires:	bluez-obexd
Requires:	bluez-tools
Requires:	filesystem
Requires:	gnome-bluetooth
Requires:	hicolor-icon-theme
Requires:	rfkill
Requires:	xapps >= 1.6.1
Requires:	wmctrl

%if (0%{?rhel} && 0%{?rhel} <= 7)
Requires:	dbus-python
Requires:	pygobject3
Requires:	python-setproctitle
%else
Requires:	python3-dbus
Requires:	python3-gobject
Requires:	python3-setproctitle
%endif

%description
%{summary} depending on gnome-bluetooth.


%package -n cinnamon-applet-%{name}
Summary:	Cinnamon applet for %{name}

Requires:	%{name}	== %{version}-%{release}
Requires:	cinnamon

%description -n cinnamon-applet-%{name}
Cinnamon applet for %{name}.


%prep
%autosetup -p 1


%build
%make_build


%install
%{__mkdir} -p %{buildroot}
%{__cp} -a .%{_prefix} .%{_sysconfdir} %{buildroot}
%{__grep} -RZl '#!%{__python3}' %{buildroot}%{_prefix}/lib/%{name}/* |	\
	%{_bindir}/xargs -0 %{__chmod} -c 0755
for file in $(%{_bindir}/find %{buildroot} -name '*.desktop' -type f)
do
	%{_bindir}/desktop-file-validate ${file}
done
%find_lang %{name}


%if (0%{?rhel} && 0%{?rhel} <= 7)
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
	/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
	%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor	\
		&>/dev/null || :
	%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas	\
		&> /dev/null || :
fi


%posttrans
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor		\
	&>/dev/null || :
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas		\
	&> /dev/null || :
%endif


%files -f %{name}.lang
%license debian/copyright COPYING
%doc debian/changelog
# Desktop-file for xdg/autostart.
%config %{_sysconfdir}/xdg/autostart/*%{name}*.desktop
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/status/%{name}*.png
%{_datadir}/icons/hicolor/*/status/%{name}*.svg
%{_prefix}/lib/%{name}


%files -n cinnamon-applet-%{name}
%{_datadir}/cinnamon/applets/%{name}*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.7-1
- Update to 1.3.7

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Leigh Scott <leigh123linux@gmail.com> - 1.3.3-2
- Add version to xapps requires (rhbz#1791184)

* Wed Dec 11 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.3-1
- Update to 1.3.3

* Tue Dec 10 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.3.2-1
- update to 1.3.2 (#1777008)
- add missing xapps dependency for blueberry tray

* Tue Nov 26 2019 Leigh Scott <leigh123linux@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Fri Nov 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.0-1
- Update to 1.3.0

* Thu Aug 22 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.9-1
- Update to 1.2.9

* Thu Aug 22 2019 Kevin Fenzi <kevin@scrye.com> - 1.2.8-1
- Update to 1.2.8. Fixes bug #1742148

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Kevin Fenzi <kevin@scrye.com> - 1.2.6-1
- Update to 1.2.6, drop upstreamed python3 patches and workarounds.

* Sat Mar 23 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.5-2
- Add path to build with python3

* Tue Feb 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.3-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-1
- New upstream release

* Tue May 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-1
- New upstream release

* Thu Feb 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.20-6
- Do it better

* Thu Feb 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.20-5
- Add some upstream fixes
- Remove the python3 dep

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.20-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.20-2
- Remove obsolete scriptlets

* Mon Dec 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.20-1
- New upstream release

* Sun Dec 10 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.19-1
- New upstream release

* Tue Nov 14 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.18-1
- New upstream release
  Add upstream fix for double icons (rhbz#1478751)

* Mon Nov 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.17-1
- New upstream release (rhbz#1509725)

* Fri Oct 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.16-1
- New upstream release

* Tue Oct 24 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.15-6
- Patch for util-linux rfkill change in f28

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.15-5
- Preserve mode of files when changing hashbang

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.15-4
- Fix regex for EPEL

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.15-3
- Use Python2 on EPEL <= 7

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.15-1
- New upstream release (rhbz#1465880)

* Mon Jun 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.13-1
- New upstream release

* Wed May 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.12-1
- New upstream release (rhbz#1454974)

* Sat May 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.11-1
- New upstream release

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.10-3
- Add requires for bluez-tools

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.10-2
- Fix dependencies
- Update patches from upstream

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.10-1
- New upstream release
- Add sub-pkg for new Cinnamon applet

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.9-2
- Fix %%files for el <= 7

* Thu Jan 05 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.9-1
- Initial rpm-release (rhbz#1409404)

* Sun Jan 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.9-0.3
- Added scriptlets for Fedora <= 23 and RHEL <= 7

* Sun Jan 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.9-0.2
- Updated Patch0

* Sun Jan 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.9-0.1
- Initial package (rhbz#1409404)
