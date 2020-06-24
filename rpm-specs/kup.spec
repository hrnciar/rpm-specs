Name:       kup
Version:    0.3.6
Release:    7%{?dist}
Summary:    Kernel.org Uploader

License:    GPLv2
URL:        https://git.kernel.org/pub/scm/utils/kup/kup.git
Source0:    https://www.kernel.org/pub/software/network/kup/kup-%{version}.tar.xz
BuildArch:  noarch
BuildRequires:  perl-generators

%description
Kup is a secure upload tool used by kernel developers to upload
cryptographically verified packages to kernel.org.

This package includes the client-side kup utility.


%package server
Summary:    Kernel.org Uploader - server utilities
Requires:   gnupg, xz, perl-Digest-SHA

%description server
Kup is a secure upload tool used by kernel developers to upload
cryptographically verified packages to kernel.org.

This package includes the server-side kup-server utility.


%package utils
Summary:    Kernel.org Uploader - extra utilities
Obsoletes:  kup-server-utils < 0.3.3-2
Provides:   kup-server-utils = %{version}-%{release}

%description utils
Kup is a secure upload tool used by kernel developers to upload
cryptographically verified packages to kernel.org.

This package includes additional tools that may come in useful with kup.


%prep
%setup -q


%build


%install
rm -rf %{buildroot}
mkdir -pm 0755 \
    %{buildroot}%{_bindir}        \
    %{buildroot}%{_mandir}/man1   \
    %{buildroot}%{_sysconfdir}/kup

install -pm 0755 kup gpg-sign-all genrings kup-server %{buildroot}%{_bindir}
install -pm 0644 kup.1 kup-server.1 %{buildroot}%{_mandir}/man1/
install -pm 0644 kup-server.cfg %{buildroot}/%{_sysconfdir}/kup/kup-server.cfg

# Runtime directories and files
mkdir -pm 0755 \
    %{buildroot}%{_sharedstatedir}/kup/{pub,tmp,pgp}

mkdir -p %{buildroot}%{_localstatedir}/run/kup
touch %{buildroot}%{_localstatedir}/run/kup/lock



%files
%doc COPYING ChangeLog README
%{_bindir}/kup
%{_mandir}/man1/kup.*

%files server
%doc COPYING test
%config %dir %{_sysconfdir}/kup
%config(noreplace) %{_sysconfdir}/kup/kup-server.cfg
%{_bindir}/kup-server
%{_mandir}/man1/kup-server.*
%dir %attr(1777,root,root) %{_sharedstatedir}/kup/tmp
%dir %{_sharedstatedir}/kup
%dir %{_sharedstatedir}/kup/pgp
%dir %{_sharedstatedir}/kup/pub
%dir %{_localstatedir}/run/kup
%{_localstatedir}/run/kup/lock


%files utils
%{_bindir}/gpg-sign-all
%{_bindir}/genrings


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.6-1
- Update to upstream 0.3.6 with support for subcmd and gitolite
  itegration in the client.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.3.4-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.4-1
- Upstream 0.3.4-1 with support for sha256 logging of uploads.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.3-2
- Rename -server-utils into -utils, as the tools aren't actually
  server-specific.

* Mon Feb 13 2012 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.3-1
- Upstream 0.3.3

* Tue Nov 29 2011 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.2-1
- Upstream 0.3.2

* Thu Nov 24 2011 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.1-1
- Upstream 0.3.1
- Upstream now releases tarballs, so remove the gen-tarball script.

* Fri Nov 18 2011 Konstantin Ryabitsev <mricon@kernel.org> - 0.3-2
- Require gnupg and xz for kup-server (gzip and bzip2 are in base)

* Wed Nov 16 2011 Konstantin Ryabitsev <mricon@kernel.org> - 0.3-1
- Use the git-checkout notation as per Fedora guidelines.
- Move "test" dir to be with the -server package.
- Make kup-client to just be the "kup" package.
- Provide the kup-generate-tarball.sh script to automate tarball generation.
- Create a -server-utils subpackage for gpg-sign-all and genrings tools.
- Create a tmpfiles entry for systemd (needed for F15 and above).

* Mon Nov 14 2011 Konstantin Ryabitsev <mricon@kernel.org>
- Match Fedora's spec format.
- Generate runtime directories.

* Mon Oct 17 2011 John 'Warthog9' Hawley <warthog9@kernel.org>
- created spec file
