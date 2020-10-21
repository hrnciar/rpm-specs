Summary: Serial line sniffer including very simple terminal emulator
Name: jpnevulator
Version: 2.3.6
Release: 2%{?dist}
License: GPLv2+
URL: http://jpnevulator.snarl.nl/
Source: http://jpnevulator.snarl.nl/download/%{name}-%{version}.tgz
BuildRequires: gcc

%description
Jpnevulator is a handy serial sniffer. You can use it to send data on a serial
device too. You can read or write from/to one or more serial devices at the
same time.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" %{?__global_ldflags: LDFLAGS="%{__global_ldflags}"}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" install

%files
%doc AUTHORS BUGS COPYING Changelog FAQ README TODO

%{_bindir}/*
%{_mandir}/*/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.6-1
- New version
  Resolves: rhbz#1833539

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.4-7
- Fixed FTBFS by adding gcc requirement
  Resolves: rhbz#1604452

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.4-1
- New version
  Resolves: rhbz#1370757

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.1-1
- New version
  Resolves: rhbz#1291672

* Wed Sep 30 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.1-1
- New version
  Resolves: rhbz#1267413

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug  6 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.3-1
- New version
  Resolves: rhbz#1127145

* Tue Jun 24 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.2-3
- Used install -p to preserve timestamps

* Tue Jun 24 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.2-2
- Build with system CFLAGS and LDFLAGS

* Tue Jun 24 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.2-1
- Initial release
