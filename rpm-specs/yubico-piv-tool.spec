%global __cmake_in_source_build 1

Name:		yubico-piv-tool
Version:	2.1.1
Release:	1%{?dist}
Summary:	Tool for interacting with the PIV applet on a YubiKey

License:	GPLv3+
URL:		https://developers.yubico.com/yubico-piv-tool/
Source0:	https://developers.yubico.com/yubico-piv-tool/Releases/yubico-piv-tool-%{version}.tar.gz
Source1:	https://developers.yubico.com/yubico-piv-tool/Releases/yubico-piv-tool-%{version}.tar.gz.sig
Source2:	gpgkey-C4686BFE.gpg

BuildRequires:	pcsc-lite-devel openssl-devel chrpath
BuildRequires:	gnupg2 gengetopt help2man
BuildRequires:	check-devel
BuildRequires:	gcc gcc-c++
BuildRequires:	cmake3
Requires:		pcsc-lite-ccid

%description
The Yubico PIV tool is used for interacting with the
Privilege and Identification Card (PIV) applet on a YubiKey.

With it you may generate keys on the device, importing keys and certificates,
and create certificate requests, and other operations. A shared library and
a command-line tool is included.

%package devel
Summary: Tool for interacting with the PIV applet on a YubiKey
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The Yubico PIV tool is used for interacting with the
Privilege and Identification Card (PIV) applet on a YubiKey.
This package includes development files.


%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

%build
%cmake3 . -DYKPIV_INSTALL_PKGCONFIG_DIR=%{_libdir}/pkgconfig/
%make_build VERBOSE=1

%check
make test

%install
%make_install
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/yubico-piv-tool
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libykcs11.so.*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libykpiv.so.*
rm -f $RPM_BUILD_ROOT%{_libdir}/libykpiv.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/libykcs11.{la,a}


%ldconfig_scriptlets


%files
%license COPYING
%{_bindir}/yubico-piv-tool
%{_libdir}/libykpiv.so.1*
%{_libdir}/libykpiv.so.2*
%{_libdir}/libykcs11.so.1*
%{_libdir}/libykcs11.so.2*


%doc
%{_mandir}/man1/yubico-piv-tool.1.gz

%files devel
%{_libdir}/libykpiv.so
%{_libdir}/libykcs11.so
%attr(0644,root,root) %{_libdir}/pkgconfig/ykpiv.pc
%attr(0644,root,root) %{_libdir}/pkgconfig/ykcs11.pc
%dir %{_includedir}/ykpiv
%attr(0644,root,root) %{_includedir}/ykpiv/ykpiv.h
%attr(0644,root,root) %{_includedir}/ykpiv/ykpiv-config.h


%changelog
* Thu Jul 30 2020 Jakub Jelen <jjelen@redhat.com> - 2.1.1-1
- New upstream release (#1859119)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Jakub Jelen <jjelen@redhat.com> - 2.1.0-1
- New upstream release (#1855024)

* Fri Feb  7 2020 Orion Poplawski <orion@nwra.com> - 2.0.0-1
- Update to 2.0.0 (#1796170)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Jakub Jelen <jjelen@redhat.com> - 1.7.0-1
- New upstream release (#1695650)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Jakub Jelen <jjelen@redhat.com> - 1.6.2-1
- New upstream release

* Tue Aug 21 2018 Jakub Jelen <jjelen@redhat.com> - 1.6.1-1
- New upstream bugfix release

* Wed Aug 08 2018 Jakub Jelen <jjelen@redhat.com> - 1.6.0-1
- New upstream release fixing YSA-2018-03 (#1613863)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Jakub Jelen <jjelen@redhat.com> - 1.5.0-1
- New upstream release (#1543947)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.4-2
- Escape macros in %%changelog

* Fri Oct 20 2017 Jakub Jelen <jjelen@redhat.com> - 1.4.4-1
- New upstream release (#1504462)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Jakub Jelen <jjelen@redhat.com> - 1.4.3-1
- New upstream release (#1443074)

* Thu Feb 23 2017 Jakub Jelen <jjelen@redhat.com> - 1.4.2-3
- Rebuild against OpenSSL 1.0.2 (#1424566)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 Jakub Jelen <jjelen@redhat.com> - 1.4.2-1
- New upstream release (#1370850)

* Fri Aug 12 2016 Jakub Jelen <jjelen@redhat.com> - 1.4.1-1
- New upstream release (#1366435)

* Tue May 03 2016 Jakub Jelen <jjelen@redhat.com> - 1.4.0-1
- New upstream release
- Source tarball verification

* Fri Apr 29 2016 Jakub Jelen <jjelen@redhat.com> - 1.3.1-1
- New upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Jakub Jelen <jjelen@redhat.com> 1.2.2-1
- Update to 1.2.2

* Tue Dec 08 2015 Jakub Jelen <jjelen@redhat.com> 1.2.1-1
- Update to 1.2.1 (#1289091)

* Mon Nov 16 2015 Jakub Jelen <jjelen@redhat.com> 1.1.2-1
- Update to 1.1.2 (#1281987)

* Thu Nov 12 2015 Jakub Jelen <jjelen@redhat.com> 1.1.1-1
- Update to 1.1.1 (#1280522)

* Sun Nov 08 2015 Jessica Frazelle <jess@docker.com> 1.1.0-1
- Rebase to 1.1.0

* Fri Oct 02 2015 Jakub Jelen <jjelen@redhat.com> 1.0.3-1
- Rebase to 1.0.3

* Thu Jul 16 2015 Jakub Jelen <jjelen@redhat.com> 1.0.1-1
- Rebase to 1.0.1

* Mon Jul 13 2015 Jakub Jelen <jjelen@redhat.com> 1.0.0-3
- License is GPLv3+
- owner for %%{_includedir}/ykpiv
- remove hard-coded paths from ./configure
- make check is run unconditionally
- change RPATH handling to make check pass

* Thu Jul 09 2015 Jakub Jelen <jjelen@redhat.com> 1.0.0-2
- Fixed problems for Fedora Review

* Thu Jul 09 2015 Jakub Jelen <jjelen@redhat.com> 1.0.0-1
- Initial release

