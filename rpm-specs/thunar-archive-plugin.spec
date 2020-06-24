# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=215241

%global minor_version 0.4
%global thunar_version 1.8.0
%global xfceversion 4.13

Name:           thunar-archive-plugin
Version:        0.4.0
Release:        23%{?dist}
Summary:        Archive plugin for the Thunar file manager

License:        LGPLv2+
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/thunar-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2
#VCS:           git:git://git.xfce.org/thunar-plugins/thunar-archive-plugin

BuildRequires:  gcc-c++
BuildRequires:  exo >= 0.12.0
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  Thunar-devel >= %{thunar_version}
BuildRequires:  libxml2-devel
BuildRequires:  intltool
BuildRequires:  gettext
Requires:       Thunar >= %{thunar_version}

%description
The Thunar Archive Plugin allows you to create and extract archive files using 
the file context menus in the Thunar file manager. Starting with version 0.2.0, 
the plugin provides a generic scripting interface for archive managers. 


%prep
%setup -q


%build
%configure

%make_build


%install
%make_install

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}

%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
# On Fedora < 19 we need to install file-roller.tap as gnome-file-roller.tap,
# because the name # has to match the basename of the desktop-file in
# %%{_datadir}/applications.
mv %{buildroot}%{_libexecdir}/thunar-archive-plugin/file-roller.tap \
    %{buildroot}%{_libexecdir}/thunar-archive-plugin/gnome-file-roller.tap
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README THANKS NEWS
%doc scripts/template.tap
%{_libdir}/thunarx-*/thunar-archive-plugin.so
%{_libexecdir}/thunar-archive-plugin/
%{_datadir}/icons/hicolor/*/*/*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.0-20
- Update to 0.4.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.3.1-5
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 11 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1
- Remove aarch64 patch, no longer necessary

* Fri May 10 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-6
- Make the plugin find file-roller again (#961626)
- Add aarch64 support (#926629)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
- Remove upstreamed extract-here.patch
- Omit dependency on xarchiver and let users install their favorite archiver
- Update icon-cache scriptlets

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 19 2008 Christoph Wickert <fedora christoph-wickert de> - 0.2.4-5
- When used with file roller "Extract here" now always creates folder

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.4-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Christoph Wickert <fedora christoph-wickert de> - 0.2.4-3
- Rebuild for BuildID feature

* Mon Jan 22 2007 Christoph Wickert <fedora christoph-wickert de> - 0.2.4-2
- Rebuild for Thunar 0.8.0.

* Sat Jan 20 2007 Christoph Wickert <fedora christoph-wickert de> - 0.2.4-1
- Update to 0.2.4.

* Sun Nov 12 2006 Christoph Wickert <fedora christoph-wickert de> - 0.2.2-2
- Require xarchiver.
- Shorten %%description.
- Use thunarver macro.
- Include template.tap to %%doc.

* Sat Nov 11 2006 Christoph Wickert <fedora christoph-wickert de> - 0.2.2-1
- Update to 0.2.2.

* Wed Sep 13 2006 Christoph Wickert <fedora christoph-wickert de> - 0.2.0-1
- Initial Fedora Extras Version.
