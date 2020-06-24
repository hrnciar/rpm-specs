
%global snap 20170217

Name:    sni-qt
Summary: Plugin for Qt4 that turns QSystemTrayIcons into status notifiers
Version: 0.2.7
Release: 0.4.%{snap}%{?dist}

License: LGPLv3
URL:     https://launchpad.net/sni-qt
#Source0: https://launchpad.net/sni-qt/trunk/%{version}/+download/sni-qt-%{version}.tar.bz2
Source0: https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/sni-qt/%{version}+16.04.%{snap}.1-0ubuntu1/sni-qt_%{version}+16.04.%{snap}.1.orig.tar.gz

# From Ubuntu packaging version 0.2.5-0ubuntu3
Source1: sni-qt.conf

BuildRequires: cmake
BuildRequires: pkgconfig(dbusmenu-qt)
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtGui) pkgconfig(QtTest)
# %%check
BuildRequires: dbus-x11 xorg-x11-server-Xvfb

%description
This package contains a Qt4 plugin which turns all QSystemTrayIcon into
StatusNotifierItems (appindicators).


%prep
%setup -q -c


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -m644 -D -p %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/sni-qt.conf


%check
xvfb-run -a dbus-launch --exit-with-session make check ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:


%files
%doc NEWS README
%license COPYING
%config(noreplace) %{_sysconfdir}/xdg/sni-qt.conf
%{_qt4_plugindir}/systemtrayicon/


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-0.4.20170217
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-0.3.20170217
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.2.7-0.2.
- rebuild

* Tue Feb 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.2.7-0.1.20170217
- 0.2.7-20170217 snapshot as used in ubuntu
- %%check: make non-fatal, advisory only
- use %%make_build %%license

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.6-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Rex Dieter <rdieter@fedoraproject.org> 0.2.6-3
- update summary

* Thu Mar 06 2014 Rex Dieter <rdieter@fedoraproject.org> 0.2.6-2
- minor cleanup for fedora

* Wed Jul 04 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.2.6-1
- Initial release
- Version 0.2.6

