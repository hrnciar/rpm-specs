%global build_no ~134~ubuntu15.10.1

Summary:		Conky scripts manager
Name:			conky-manager
Version:		2.3.4
Release:		11%{?dist}
License:		GPLv3+
URL:			http://teejeetech.blogspot.in/p/conky-manager.html
Source0:		https://launchpad.net/~teejee2008/+archive/ppa/+files/%{name}_%{version}%{build_no}.tar.xz
Patch0:			conky-manager-desktopentry-fixer-and-arabizer.patch
Requires:		lm_sensors
Requires:		hddtemp
Requires:		p7zip
Requires:		p7zip-plugins
Requires:		conky
Requires:		ImageMagick
BuildRequires:	vala
BuildRequires:	glib2-devel
BuildRequires:	gtk3-devel
BuildRequires:	gettext
BuildRequires:	libgee-devel
BuildRequires:	json-glib-devel
BuildRequires:	desktop-file-utils

%description
A simple GUI for managing Conky configuration files. Options for changing
themes and running Conky at start up.

%prep
%setup -q -n %{name}-%{version}%{build_no}
%patch0 -p0
sed -i '3d' src/conky-manager.desktop
#Enable debugging:
sed -i 's/valac/valac -g/g' src/makefile

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm %{buildroot}/%{_bindir}/conky-manager-uninstall #Not needed
desktop-file-install \
     --dir=%{buildroot}%{_datadir}/applications \
       src/%{name}.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README TODO
%license COPYING
%{_bindir}/conky-manager
%{_datadir}/applications/conky-manager.desktop
%{_datadir}/appdata/conky-manager.appdata.xml
%{_datadir}/pixmaps/conky-manager.png
%{_datadir}/conky-manager

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.3.4-9
- Fix build requires

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 16 2015 Mosaab Alzoubi <moceap@hotmail.com> - 2.3.4-1
- Update to 2.3.4
- Fix #1239408
- Upstream uses xz instead gz
- Improve summary
- Use %%license
- Use gee 0.8 instead 0.6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Mosaab Alzoubi <moceap@hotmail.com> - 2.3.1-1
- Update to 2.3.1
- Add ImageMagick as a require.
- Static patch name.

* Fri Oct 24 2014 Mosaab Alzoubi <moceap@hotmail.com> - 2.2-3
- Fix typo in %%install.
- Enable debugging.

* Wed Oct 22 2014 Mosaab Alzoubi <moceap@hotmail.com> - 2.2-2
- General revision.

* Sat Sep 27 2014 Mosaab Alzoubi <moceap@hotmail.com> - 2.2-1
- Update to 2.2

* Fri Oct 18 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2.0.1-3
- To zero warnings by rpmlint.
- Some fixes to be compatible with Fedora rules.

* Wed Oct 9 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2.0.1-2
- Some fixes to be compatible with Fedora rules.

* Sun Oct 6 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2.0.1-1
- Initial build.
