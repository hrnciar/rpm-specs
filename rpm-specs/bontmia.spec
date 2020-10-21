Summary:   Backup over network to multiple incremental archives
Name:      bontmia
Version:   0.14
Release:   24%{?dist}
License:   GPLv2
URL:       http://folk.uio.no/johnen/bontmia/
Source0:   http://folk.uio.no/johnen/%{name}/%{name}-%{version}.tar.gz
Patch0:    bontmia-0.14-mktemp.patch
Patch1:    bontmia-0.14-cp-al.patch
Requires:  bind-utils
Requires:  coreutils
Requires:  findutils
Requires:  grep
Requires:  hostname
Requires:  openssh-clients
Requires:  perl-interpreter
Requires:  rsync
Requires:  sed
BuildArch: noarch
%description
A disk based backup system which provides a complete snapshot of
backed up directories. Using a clever hardlink and rsync trick,
the backup is fast and space efficient.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
#empty

%install
install -D -p -m 0755 bontmia %{buildroot}%{_bindir}/bontmia

%files
%doc COPYING README
%{_bindir}/bontmia

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.14-17
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.14-13
- Add patch to fix cp issue (#1152534)
- Clean up

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 05 2012 Terje Rosten <terjeros@phys.ntnu.no> - 0.14-8
- hostname moved from net-tools

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.14-3
- Fix patch macro

* Sun Aug 19 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.14-2
- Fix license tag

* Tue Jun 12 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.14-1 
- initial build
