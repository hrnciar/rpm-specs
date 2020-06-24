Name:		icfg 
Version:	0.9	
Release:	19%{?dist}
Summary:	Command line utility to edit network configuration (icfg-*) files
License:	GPLv2
URL:		https://fedorahosted.org/icfg
Source0:	https://fedorahosted.org/releases/i/c/icfg/%{name}-%{version}.tbz2
Requires:	python3 
BuildArch:	noarch

Patch0: icfg-python.patch
Patch1: icfg-python3.patch

%description
This is a utility for manipulating SysV network interface configuration files
(the files matching the glob /etc/sysconfig/network-scripts/icfg-*).  These are
text based files, that are normally easily edited by hand, but in many
environments hand editing is not desirable (for instance, during kickstart
installations).  Icfg creates a scriptable interface to allow an admin to
provision a systems network interfaces during install, without having to fall
back to using a series of sed and awk commands

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1

install -m755 -p src/icfg $RPM_BUILD_ROOT/usr/bin/icfg
install -m644 -p doc/icfg.1 $RPM_BUILD_ROOT/usr/share/man/man1/icfg.1

%files
%doc COPYING 
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Neil Horman <nhorman@redhat.com> - 0.9-15
- update for python3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-11
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 17 2015 Neil Horman <nhorman@redhat.com> - 0.9-9
- Remove python2 dep.

* Fri Jul 10 2015 Neil Horman <nhorman@redhat.com> - 0.9-8
- Update to require python3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Neil Horman <nhorman@redhat.com> - 0.9-1
- Initial build

