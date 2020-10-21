%global _hardened_build 1

Name:		proxychains-ng
Version:	4.13
Release:	6%{?dist}
Summary:	Redirect connections through proxy servers

License:	GPLv2+
URL:		https://github.com/rofl0r/proxychains-ng
Source0:	http://ftp.barfooze.de/pub/sabotage/tarballs/proxychains-ng-%{version}.tar.xz

Provides:	proxychains = %{version}
Obsoletes:	proxychains < %{version}

BuildRequires:  gcc
%description
ProxyChains NG is based on ProxyChains.

ProxyChains NG hooks network-related (TCP only) libc functions in dynamically
linked programs via a preloaded DSO (dynamic shared object) and redirects the
connections through one or more SOCKS4a/5 or HTTP proxies.

Since Proxy Chains NG relies on the dynamic linker, statically linked binaries
are not supported.

%prep
%setup -q -n proxychains-ng-%{version}

%build
%configure --disable-static --libdir=%{_libdir}/%{name}
make %{?_smp_mflags}

%install
%make_install install-config
ln -s %{_bindir}/proxychains4 %{buildroot}%{_bindir}/proxychains
chmod +x %{buildroot}%{_libdir}/%{name}/libproxychains4.so

%files
%license COPYING
%doc AUTHORS README TODO
%config(noreplace) %{_sysconfdir}/proxychains.conf
%{_bindir}/proxychains4
%{_bindir}/proxychains
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libproxychains4.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 Pranav Kant <pranvk@fedoraproject.org> - 4.13-2
- Add symlink for /usr/bin/proxychains

* Sat Dec 22 2018 Pranav Kant <pranvk@fedoraproject.org> - 4.13-1
- Update to 4.13

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Pranav Kant <pranvk@fedoraproject.org> 4.12-1
- Update to 4.12

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 13 2016 Pranav Kant <pranvk@fedoraproject.org> 4.11-1
- Update to 4.11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Pranav Kant <pranvk@fedoraproject.org> 4.10-1
- Update to 4.10

* Sun Jun 14 2015 Pranav Kant <pranvk@fedoraproject.org> 4.8.1-9
- Fix source URL

* Thu May 21 2015 Pranav Kant <pranvk@fedoraproject.org> 4.8.1-8
- Fix CVE-2015-3887

* Fri May 8 2015 Pranav Kant <pranav913@gmail.com> 4.8.1-7
- Fixed fsf patch from upstream
- Added Obsoletes

* Tue Mar 17 2015 Pranav Kant <pranav913@gmail.com> 4.8.1-6
- Remove legacy script - proxyresolv4
- Move .so file to application-specific directory

* Mon Mar 16 2015 Pranav Kant <pranav913@gmail.com> 4.8.1-5
- Remove .so versioning

* Mon Mar 16 2015 Pranav Kant <pranav913@gmail.com> 4.8.1-4
- Install .so file with executable flags
- Replace old optflags patch with corrected patch

* Wed Mar 11 2015 Pranav Kant <pranav913@gmail.com> 4.8.1-3
- Dropped Obsoletes

* Mon Feb 2 2015 Pranav Kant <pranav913@gmail.com> 4.8.1-2
- Moved COPYING to %%license
- Downstream .so name versioning

* Fri Sep 26 2014 Pranav Kant <pranav913@gmail.com> 4.8.1-1
- Changed the URL from sourceforge to github
- Consistently used macros instead of variables
- Turn PIE on
- Fixed minor release numbering issue
- Added a patch for makefile to honour optflags
