Summary:	Compact and feature-rich WordStar-compatible editor
Name:		jupp
Version:	38
Release:	5%{?dist}
License:	GPLv1
URL:		https://www.mirbsd.org/jupp.htm
Source0:	https://www.mirbsd.org/MirOS/dist/%{name}/joe-3.1%{name}%{version}.tgz
BuildRequires:	gcc
BuildRequires:	ncurses-devel
BuildRequires:	libselinux-devel

%description
Jupp is a compact and feature-rich WordStar-compatible editor and also the
MirOS fork of the JOE 3.x editor which provides easy conversion for former
PC users as well as powerfulness for programmers, while not doing annoying
things like word wrap "automagically". It can double as a hex editor and
comes with a character map plus Unicode support. Additionally it contains
an extension to visibly display tabs and spaces, has a cleaned up, extended
and beautified options menu, more CUA style key-bindings, an improved math
functionality and a bracketed paste mode automatically used with Xterm.

%prep
%setup -q -n %{name}

%build
chmod +x configure
%configure --disable-termidx --sysconfdir=%{_sysconfdir}/%{name}
%make_build sysconfjoesubdir=

%install
%make_install sysconfjoesubdir=

# Some cleanups to be done by upstream for future releases
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{jmacs,joe,jpico,jstar,rjoe}rc
rm -f $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}/{jmacs,jpico,jstar,jupp,rjoe}*
mv -f $RPM_BUILD_ROOT%{_bindir}/{joe,%{name}}
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/{joe,%{name}}.1

%files
%license COPYING
%doc HINTS INFO LIST NEWS README
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}rc
%dir %{_sysconfdir}/%{name}/charmaps/
%config(noreplace) %{_sysconfdir}/%{name}/charmaps/*
%dir %{_sysconfdir}/%{name}/syntax/
%config(noreplace) %{_sysconfdir}/%{name}/syntax/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert Scheck <robert@fedoraproject.org> 38-1
- Upgrade to 38

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 25 2017 Robert Scheck <robert@fedoraproject.org> 32-1
- Upgrade to 32

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 Robert Scheck <robert@fedoraproject.org> 30-1
- Upgrade to 30

* Tue Nov 01 2016 Robert Scheck <robert@fedoraproject.org> 29-1
- Upgrade to 29

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 23 2014 Robert Scheck <robert@fedoraproject.org> 28-1
- Upgrade to 28

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Robert Scheck <robert@fedoraproject.org> 27-1
- Upgrade to 27

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 27 2013 Robert Scheck <robert@fedoraproject.org> 26-1
- Upgrade to 26

* Tue Mar 19 2013 Robert Scheck <robert@fedoraproject.org> 24-1
- Upgrade to 24
- Initial spec file for Fedora and Red Hat Enterprise Linux
