Summary: UROnode addon - an SMTP mailbox
Name: axmail
Version: 2.9
Release: 2%{?dist}
License: GPLv2+
URL: http://axmail.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: axmail-README.fedora
Patch0: axmail-2.9-install-fix.patch
Patch1: axmail-2.8-gcc-10-fix.patch
BuildRequires: gcc
# http://fedorahosted.org/fpc/ticket/447
Provides: bundled(mailx) = 5.3b

%description
axMail is an add-on to URONode or LinuxNode that provides you and your
users with the ability to send and receive SMTP-based email. It can also
be used with a HylaFax server, making it possible to send and receive faxes
using just a dumb terminal. Setup is easy and many options are available
for the SysOp.

%prep
%setup -q
%patch0 -p1 -b .install-fix
%patch1 -p1 -b .gcc-10-fix

# Copy Fedora readme into place
cp -p %{SOURCE1} README.fedora

# Removing old license file, this was permitted by upstream N1URO and
# will be fixed in next upstream release. The package is now licensed
# under GPLv2+ as stated in the copying.
rm -f .COPYING

# Rename welcome.txt to axmail-welcome.txt to prevent possible future conflicts
mv -f etc/welcome.txt etc/axmail-welcome.txt

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}"

%install
make %{?_smp_mflags} DESTDIR="%{buildroot}" MAN_DIR="%{buildroot}%{_mandir}" install

# Ghosts
mkdir -p %{buildroot}%{_var}/lock
touch %{buildroot}%{_var}/lock/axmail

%files
%doc README.fedora README FAQ copying

%{_sbindir}/*
%config(noreplace) %{_sysconfdir}/ax25/axmail.conf
%config(noreplace) %{_sysconfdir}/ax25/axmail-welcome.txt
%{_mandir}/*/*
%{_datadir}/axmail
%ghost %{_var}/lock/axmail

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.9-1
- New version

* Mon Feb 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8-10
- Fixed FTBFS with gcc-10
  Resolves: rhbz#1799184

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.8-6
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8-5
- Fixed FTBFS by adding gcc requirement

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.8-2
- Rebuilt for switch to libxcrypt

* Tue Jan  9 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8-1
- New version
- Dropped build-fix patch (not needed)
- Integrated welcome-rename patch to install-fix patch

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.1-3
- Pointed URLs to sourceforge.net

* Mon Feb 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.1-2
- Removed setgroups patch from dist-git

* Mon Feb 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.1-1
- New version
- Rebased install-fix and build-fix patches
- Dropped setgroups patch (upstreamed)

* Fri Jul 18 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0-1
- Initial release
