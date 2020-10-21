# support for IP-to-country lookups
%bcond_without geoip

Name:           ncdc
Version:        1.20
Release:        10%{?dist}
Summary:        Modern and lightweight direct connect client
License:        MIT
URL:            http://dev.yorhel.nl/ncdc
Source0:        http://dev.yorhel.nl/download/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(sqlite3)
%if %{with geoip}
BuildRequires:  pkgconfig(geoip)
%endif

%description
Ncdc is a modern and lightweight direct connect client with a 
friendly ncurses interface.

%prep
%autosetup

%build
%configure --disable-silent-rules \
  %{?with_geoip:--with-geoip=yes}
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.20-1
- Update to 1.20

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.19.1-6
- Add conditional support for geoip
- Use pkgconfig() style dependencies
- use %%license macro

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Christopher Meng <rpm@cicku.me> - 1.19.1-1
- Update to 1.19.1

* Mon Oct 07 2013 Christopher Meng <rpm@cicku.me> - 1.18.1-1
- Initial Package(BZ#1016170).
