%global _hardened_build 1

Name:           xfce4-hardware-monitor-plugin
Version:        1.6.0
Release:        10%{?dist}
Summary:        Xfce4 panel plugin to monitor various hardware

License:        GPL+ and LGPLv2+
URL:            https://goodies.xfce.org/projects/panel-plugins/xfce4-hardware-monitor-plugin
Source0:        http://git.xfce.org/panel-plugins/%{name}/snapshot/%{name}-%{version}.tar.bz2

BuildRequires:  xfce4-dev-tools
BuildRequires:  xfce4-panel-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  libgnomecanvasmm26-devel
BuildRequires:  libglademm24-devel
BuildRequires:  libgtop2-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  libtool
BuildRequires:  gcc-c++

%description
A Xfce4 panel plugin that can display various system stats
(CPU, filesystem and network usage among others) in graphs, 
visualisations or with text

%prep
%autosetup

%build
xdt-autogen
%configure
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/xfce4/panel/plugins/libhardwaremonitor.la
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/xfce4-hardware-monitor-plugin

%changelog
* Wed Aug 26 2020 Jeff Law <law@redhat.wcom> - 1.6.0-10
- Do not force C++11 mode

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.0-5
- Add gcc-c++ as BR

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.6.0-3
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Update to 1.6.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 1.5.0-4
- Rebuilt for libgtop2 soname bump

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 17 2015 Kevin Fenzi <kevin@scrye.com> 1.4.7-3
- Build with c++11 due to gtkmm30 doing so.

* Sat Oct 10 2015 Kevin Fenzi <kevin@scrye.com> 1.4.7-2
- Updates from review: remove la files. 
- Updates from review: use http url for source.
- Updates from review: Update license. 
- Fixed directory ownership

* Sat Sep 12 2015 Kevin Fenzi <kevin@scrye.com> 1.4.7-1
- Initial version for review
