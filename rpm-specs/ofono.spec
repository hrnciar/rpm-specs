
Name:    ofono
Summary: Open Source Telephony
Version: 1.23
Release: 2%{?dist}

License: GPLv2
URL:     http://ofono.org/
Source0: https://git.kernel.org/pub/scm/network/ofono/ofono.git/snapshot/ofono-%{version}.tar.gz

BuildRequires: automake libtool
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libudev) >= 145
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(mobile-broadband-provider-info)

BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
oFono.org is a place to bring developers together around designing an
infrastructure for building mobile telephony (GSM/UMTS) applications.
oFono includes a high-level D-Bus API for use by telephony applications.
oFono also includes a low-level plug-in API for integrating with telephony
stacks, cellular modems and storage back-ends.

%package devel
Summary: Development files for oFono
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q


%build
if [ ! -f configure ]; then
./bootstrap
fi

%configure \
  --enable-bluetooth \
  --enable-pie \
  --disable-silent-rules

%make_build


%install
%make_install

# create/own this
mkdir -p %{buildroot}%{_libdir}/ofono/plugins


%check
make check


%post
%systemd_post ofono.service

%preun
%systemd_preun ofono.service

%postun
%systemd_postun_with_restart ofono.service

%files
%doc ChangeLog AUTHORS README
%license COPYING
%{_sysconfdir}/dbus-1/system.d/ofono.conf
%dir %{_sysconfdir}/ofono/
%config(noreplace) %{_sysconfdir}/ofono/phonesim.conf
%{_sbindir}/ofonod
%{_unitdir}/ofono.service
%{_mandir}/man8/ofonod.8*
%dir %{_libdir}/ofono/
%dir %{_libdir}/ofono/plugins/

%files devel
%{_includedir}/ofono/
%{_libdir}/pkgconfig/ofono.pc


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.23-1
- 1.23
- use %%license %%make_build
- -devel: make base dep unarched, no point in making base multilib too

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.22-1
- 1.22

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 04 2014 Rex Dieter <rdieter@fedoraproject.org> 1.14-1
- first try (borrowed from obs)

