Name: kstart
Version: 4.2
Release: 13%{?dist}
Summary: Daemon version of kinit for Kerberos v5
License: MIT
URL: http://www.eyrie.org/~eagle/software/kstart/
Source0: http://archives.eyrie.org/software/kerberos/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: krb5-devel

%description
k5start is a modified version of kinit which can use keytabs to authenticate, 
can run as a daemon and wake up periodically to refresh a ticket, and can run 
single commands with its own authentication credentials and refresh those 
credentials until the command exits. 

%prep
%setup -q

%build
%configure --enable-setpag --enable-reduced-depends --with-aklog=%{_bindir}/aklog

%make_build

%install
%make_install

%files
%license LICENSE
%doc NEWS README
%{_bindir}/k5start
%{_bindir}/krenew
%{_mandir}/man1/k5start.1.gz
%{_mandir}/man1/krenew.1.gz

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 4.2-12
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 4.2-3
- Drop EL5 compatibility
- Package LICENSE file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 4.2-1
- Upgrade to 4.2

* Tue Dec 01 2015 Ken Dreyer <ktdreyer@ktdreyer.com> 4.1-8
- Remove obsolete --disable-k4start configure option (thanks shawn@eth0.net)
  (rhbz#1287213)
- Add --with-aklog=/usr/bin/aklog configure option (thanks shawn@eth0.net)
  (rhbz#1287210)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 08 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 4.1
- Upgrade to 4.1

* Fri Dec 30 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 4.0
- Upgrade to 4.0

* Tue Feb 08 2011 Simon Wilkinson <simon@sxw.org.uk> - 3.16
- Upgrade to 3.16
- Enable support for setpag

* Sun Apr 13 2008 Simon Wilkinson <simon@sxw.org.uk> 3.11-1
- Update to 3.11
- Fix license tag, as per approval requirement

* Sat Jan 27 2007 Simon Wilkinson <simon@sxw.org.uk> 3.10-1
- Initial revision for Fedora

