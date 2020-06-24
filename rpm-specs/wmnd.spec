Name:		wmnd
Version:	0.4.17
Release:	18%{?dist}
Summary:	Dockapp for monitoring network interfaces

License:	GPLv2+
URL:		http://www.thregr.org/~wavexx/software/wmnd/

Source:		%{url}/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	autoconf automake git libXext-devel libXpm-devel

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
WMND is a dockapp for monitoring network interfaces under WindowMaker
and other compatible window managers. WMND currently works on Linux,
FreeBSD, NetBSD, Solaris, OpenSolaris, Darwin and IRIX.

WMND can monitor multiple interfaces at the same time, sports several
display modes and can also monitor remote interfaces through SNMP.

%prep
%setup -q

%build
autoreconf -fis
%configure \
	--docdir=%{_pkgdocdir} \
	--enable-drivers=linux_proc
make %{?_smp_mflags}

%install
%{make_install}
cp -p AUTHORS COPYING NEWS README THANKS TODO %{buildroot}%{_pkgdocdir}

%files
%doc %{_pkgdocdir}
%{_bindir}/wmnd
%{_mandir}/man1/wmnd.1*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 08 2016 Alexey I. Froloff <raorn@raorn.name> - 0.4.17-10
- Fix documentation packaging.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Alexey I. Froloff <raorn@raorn.name> - 0.4.17-5
- Use %%_pkgdocdir for documentation path

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Alexey I. Froloff <raorn@raorn.name> - 0.4.17-1
- New version (0.4.17)

* Wed Jun 06 2012 Alexey I. Froloff <raorn@raorn.name> - 0.4.16-2
- Updated to wmnd-0.4.16-4-gc96f86d

* Tue Jun 05 2012 Alexey I. Froloff <raorn@raorn.name> - 0.4.16-1
- Initial build for Fedora
