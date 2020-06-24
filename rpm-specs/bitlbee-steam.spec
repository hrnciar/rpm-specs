Name:           bitlbee-steam
Version:        1.4.2
Release:        8%{?dist}
Summary:        Steam protocol plugin for BitlBee

License:        GPLv2+
URL:            https://github.com/bitlbee/bitlbee-steam
Source0:        https://github.com/bitlbee/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  bitlbee-devel
BuildRequires:  glib2-devel
BuildRequires:  libgcrypt-devel

Requires:       bitlbee%{?_isa}

%global __provides_exclude_from ^%{_libdir}/bitlbee/.*


%description
The Steam protocol plugin for BitlBee.  This plugin uses the Steam Mobile
API allowing it to run alongside the main Steam client.  It is worth
noting that the Steam Mobile API is HTTP based, which does lead to mild
latency.


%prep
%autosetup


%build
%configure --disable-static
%make_build


%install
%make_install
rm $RPM_BUILD_ROOT/%{_libdir}/bitlbee/steam.la


%files
%license COPYING
%doc AUTHORS README
%{_libdir}/bitlbee/steam.so


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

