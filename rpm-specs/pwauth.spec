%global _hardened_build 1

Name:           pwauth
Version:        2.3.10
Release:        21%{?dist}
Summary:        External plugin for mod_authnz_external authenticator

License:        BSD
URL:            https://github.com/phokz/pwauth/
Source0:        https://github.com/phokz/pwauth/archive/%{name}-%{version}.tar.gz
Source1:        pwauth.pam
Patch1:         pwauth-make.patch
Patch2:         pwauth-strchr.patch
Patch3:         pwauth-cleanup.patch

BuildRequires:  gcc
BuildRequires:  pam-devel

Requires:       httpd

%description
Pwauth is an authenticator designed to be used with mod_auth_external
or mod_authnz_external and the Apache HTTP daemon to support reasonably
secure web authentication out of the system password database on most
versions of Unix.


%prep
%setup -q

%patch1 -p1 -b .make
%patch2 -p1 -b .strchr
%patch3 -p1 -b .cleanup

%build
export CFLAGS="${RPM_OPT_FLAGS}"
export LDFLAGS="${RPM_LD_FLAGS}"

%make_build CFLAGS="${CFLAGS} -Wno-comment" LDFLAGS="${LDFLAGS}"


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}/pam.d

install -p -m 4750 -t %{buildroot}%{_bindir} pwauth
install -p -m 0750 -t %{buildroot}%{_bindir} unixgroup
install -p -T %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/pwauth


%files
%attr(4750,-,apache) %{_bindir}/pwauth
%attr(0750,-,apache) %{_bindir}/unixgroup
%attr(644,-,-) %{_sysconfdir}/pam.d/pwauth
%doc CHANGES INSTALL README


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Philip Prindeville <philipp@fedoraproject.org> - 2.3.10-18
- Update spec to reflect rehoming of project

* Mon Jul 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.3.10-17
- BR: gcc (#1605529)
- use %%make_build

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.3.10-11
- Requires: httpd (#1319087)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-5
- Fix for bz#965461
- Get rid of some of the more worrisome compiler warnings.
- Use patch instead of sed to modify Makefile.

* Fri Mar 22 2013 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-4
- Fix for bz#924881

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-1
- Initial checkin after Fedora packaging review.

* Tue Apr 17 2012 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-0
- Initial RPM packaging.
