%global _hardened_build 1

Name:		pam-u2f
Version:	1.0.8
Release:	4%{?dist}
Summary:	Implements PAM authentication over U2F

License:	BSD
URL:		https://developers.yubico.com/pam-u2f/
Source0:	https://developers.yubico.com/pam-u2f/Releases/pam_u2f-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	pam-devel libu2f-host-devel libu2f-server-devel

# needed if applying patches
#BuildRequires:	autoconf
#BuildRequires:	automake

%description
The PAM U2F module provides an easy way to integrate the Yubikey (or
other U2F-compliant authenticators) into your existing user
authentication infrastructure.

%package -n pamu2fcfg
Summary:	Configures PAM authentication over U2F
Requires:	%{name}%{?_isa} = %{version}-%{release} json-c

%description -n pamu2fcfg
pamu2fcfg provides a command line tool for configuring PAM authentication
over U2F.

%prep
%autosetup -n pam_u2f-%{version}

%build
%configure --with-pam-dir=%{_libdir}/security
%make_build

%install
%make_install
#remove libtool files
find %{buildroot} -name '*.la' -delete

%check
make check

%files
%doc AUTHORS NEWS README
%license COPYING
%{_mandir}/man8/*
%{_libdir}/security/*

%files -n pamu2fcfg
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.0.8-4
- Rebuild (json-c)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Seth Jennings <spartacus06@gmail.com> - 1.0.8-1
- New upstream release
- Fixes Debug file descriptor leak CVE-2019-1221
- Fixes insecure debug file handling CVE-2019-1220
- resolves: #1717326

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Seth Jennings <spartacus06@gmail.com> - 1.0.7-1
- New upstream release

* Thu Apr 19 2018 Seth Jennings <spartacus06@gmail.com> - 1.0.6-1
- New upstream release
- resolves: #1568058

* Mon Apr 16 2018 Seth Jennings <spartacus06@gmail.com> - 1.0.5-2
- fix spec file

* Mon Apr 16 2018 Seth Jennings <spartacus06@gmail.com> - 1.0.5-1
- New upstream release
- resolves: #1568058

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-8
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Seth Jennings <spartacus06@gmail.com> - 1.0.4-6
- Resolves: #1528392

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Seth Jennings <spartacus06@gmail.com> - 1.0.4-2
- Remove Fedora-specific README

* Mon Sep 19 2016 Seth Jennings <spartacus06@gmail.com> - 1.0.4-1
- New upstream release
- resolves: #1377459

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.3-5
- Fix up descriptions
- Use %%autosetup macro

* Mon Dec 14 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.3-4
- Add upstream patches https://github.com/Yubico/pam-u2f/issues/28

* Mon Nov 30 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.3-3
- Use find -delete option
- Fixup description
- Remove explicit Requires pam

* Wed Nov 18 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.3-2
- Fix typo in pamu2fcfg description

* Wed Nov 18 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.3-1
- Initial package release
