Name:       makepasswd
Version:    0.5.3
Release:    19%{?dist}
Summary:    Generates (pseudo-)random passwords of a desired length

License:    GPLv3
URL:        http://people.defora.org/~khorben/projects/makepasswd/
Source0:    http://ftp.defora.org/pub/projects/makepasswd/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
BuildRequires:  openssl-devel

#Patch BZ 1048269
Patch0: makepasswd-0.5.3-fix-duplicate-text-in-man-page.patch

#Patch BZ 1126076
Patch1: makepasswd-0.5.3-Avoid-a-crash-on-invalid-input-values.patch

#BZ 1771883
Patch2: makepasswd-0.5.3-default-pwdlength.patch

%description
Makepasswd generates (pseudo-)random passwords of a desired length. 

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1

%build
make %{?_smp_mflags} CFLAGSF= CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags} -lcrypt -lcrypto"

%install
install -D -p -m 755 src/makepasswd %{buildroot}%{_bindir}/makepasswd
install -D -p -m 644 doc/makepasswd.1 %{buildroot}%{_mandir}/man1/makepasswd.1

%files
%doc COPYING
%{_mandir}/man1/makepasswd.1*
%{_bindir}/makepasswd


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Johan Swensson <kupo@kupo.se> - 0.5.3-18
- Fixes bugzilla 1126076

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.5.3-15
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.5.3-12
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Johan Swensson <kupo@kupo.se> - 0.5.3-6
- Fix for BZ#1126076

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Johan Swensson <kupo@kupo.se> - 0.5.3-3
- Fix duplicate text in man page (#1048269)

* Thu Jan 02 2014 Johan Swensson <kupo@kupo.se> - 0.5.3-2
- Removed unnecessary build step

* Fri Dec 20 2013 Johan Swensson <kupo@kupo.se> - 0.5.3-1
- New upstream release
- openssl is now used instead of bundled md5 implementation

* Mon Oct 21 2013 Johan Swensson <kupo@kupo.se> - 0.5.2-5
- Use correct LDFLAGS
- Use optflags macro instead of RPM_OPT_FLAGS

* Sun Oct 20 2013 Johan Swensson <kupo@kupo.se> - 0.5.2-4
- Make changelog timestamp/version string consistent

* Fri Sep 27 2013 Johan Swensson <kupo@kupo.se> - 0.5.2-3
- use plain make instead of make macro
- remove unnecessary slashes in install phase
- use doc macro for license file

* Fri Sep 27 2013 Johan Swensson <kupo@kupo.se> - 0.5.2-2
- removed Makefile patch, passing arguments directly to make instead
- changed source mirror by request from upstream
- fixed incorrect timestamps in chagelog

* Fri Sep 27 2013 Johan Swensson <kupo@kupo.se> - 0.5.2-1
- update to new upstream release 0.5.2
- adds license file
- minor changes getting rid of unnecessary steps in the install phase

* Thu Sep 26 2013 Johan Swensson <kupo@kupo.se> - 0.5.1-3
- additional package fixes
- patch Makefile

* Thu Sep 26 2013 Johan Swensson <kupo@kupo.se> - 0.5.1-2
- package fixes with input from informal review

* Thu Sep 26 2013 Johan Swensson <kupo@kupo.se> - 0.5.1-1
- initial build

