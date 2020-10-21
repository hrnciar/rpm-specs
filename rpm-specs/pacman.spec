# We ship a .pc file but don't want to have a dep on pkg-config. We
# strip the automatically generated dep here and instead co-own the
# directory.
%global __requires_exclude pkg-config

%global libmajor 12
%global libminor 0

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

Name:           pacman
Version:        5.2.1
Release:        5%{?dist}
Source0:        https://projects.archlinux.org/%{name}.git/snapshot/%{name}-%{version}.tar.gz
Source1:        https://www.archlinux.org/mirrorlist/all
Url:            https://www.archlinux.org/pacman
License:        GPLv2+
Summary:        Package manager for the Arch distribution

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  m4
BuildRequires:  gettext-devel
BuildRequires:  asciidoc
BuildRequires:  doxygen
BuildRequires:  libarchive-devel
BuildRequires:  gpgme-devel
BuildRequires:  openssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  perl-generators
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       bsdtar
Recommends:     arch-install-scripts

%description
Pacman is the package manager used by the Arch distribution. It can
be used to install Arch into a container or to recover an Arch
installation from a Fedora system (see arch-install-scripts package
for instructions).

Pacman is a frontend for the ALPM (Arch Linux Package Management)
library Pacman does not strive to "do everything." It will add, remove
and upgrade packages in the system, and it will allow you to query the
package database for installed packages, files and owners. It also
attempts to handle dependencies automatically and can download
packages from a remote server. Arch packages are simple archives, with
.pkg.tar.gz extension for binary packages and .src.tar.gz for source
packages.


%package -n libalpm
Summary: Arch Linux Package Management library

%description -n libalpm
This library is the backend behind Pacman — the package manager used
by the Arch distribution. It uses simple compressed files as a package
format, and maintains a text-based package database.


%package -n libalpm-devel
Summary: Development headers for libalpm
Requires: libalpm%{_isa} = %{version}-%{release}

%description -n libalpm-devel
This package contains the public headers necessary to use libalpm.


%package filesystem
Summary: Pacman filesystem layout
License: Public Domain
BuildArch: noarch

%description filesystem
This package provides some directories used by pacman and related
packages.


%prep
%autosetup -p1

# Enable some servers by default. rackspace.com is in the "worldwide" section,
# and "kernel.org" seems to be a good default too.
sed -r 's+^#(Server = https://(mirrors.kernel.org|mirror.rackspace.com)/)+\1+' <%{SOURCE1} >mirrorlist

%build
CONFIGURE_OPTS=(
        -Ddoxygen=enabled
)

%meson "${CONFIGURE_OPTS[@]}"
%meson_build

%install
%meson_install

%find_lang pacman
%find_lang pacman-scripts
%find_lang libalpm
cat pacman-scripts.lang >>pacman.lang

install -Dm0644 mirrorlist %{buildroot}%{_sysconfdir}/pacman.d/mirrorlist

cat >>%{buildroot}%{_sysconfdir}/pacman.conf <<EOF
[core]
SigLevel = Required DatabaseOptional
Include = %{_sysconfdir}/pacman.d/mirrorlist

[extra]
SigLevel = Required DatabaseOptional
Include = %{_sysconfdir}/pacman.d/mirrorlist
EOF

%files -f pacman.lang
%{_bindir}/makepkg
%{_bindir}/makepkg-template
%{_bindir}/pacman
%{_bindir}/pacman-conf
%{_bindir}/pacman-db-upgrade
%{_bindir}/pacman-key
%{_bindir}/repo-add
%{_bindir}/repo-elephant
%{_bindir}/repo-remove
%{_bindir}/testpkg
%{_bindir}/vercmp
%config(noreplace) %{_sysconfdir}/makepkg.conf
%config(noreplace) %{_sysconfdir}/pacman.conf
%config(noreplace) %{_sysconfdir}/pacman.d/mirrorlist
%{_datarootdir}/makepkg/
%dir %{_sharedstatedir}/pacman
%dir %{_localstatedir}/cache/pacman
%dir %{_localstatedir}/cache/pacman/pkg
%{_datadir}/pacman/*
%{_datadir}/pkgconfig/libmakepkg.pc
# https://bugzilla.redhat.com/show_bug.cgi?id=1819867
%exclude %{_datadir}/bash-completion/completions/makepkg
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_pacman
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%license COPYING
%doc NEWS

%files -n libalpm -f libalpm.lang
%{_libdir}/libalpm.so.%{libmajor}.%{libminor}.*
%{_libdir}/libalpm.so.%{libmajor}
%license COPYING

%files -n libalpm-devel
%{_includedir}/alpm_list.h
%{_includedir}/alpm.h
%{_libdir}/pkgconfig/libalpm.pc
%{_libdir}/libalpm.so
%{_mandir}/man3/*
%license COPYING
%doc HACKING

%files filesystem
%dir %{_sysconfdir}/pacman.d
%dir %{_datadir}/pacman


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May  5 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2.1-4
- Also include [extra] section in the default configuration

* Tue May  5 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2.1-3
- Update server list and make sure at least one server is uncommented

* Wed Apr  1 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2.1-2
- Remove makepkg bash completion script to fix file conflict

* Tue Mar 31 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2.1-1
- Update to latest upstream version (#1582967)
- Fix arbitrary command injection in download URLs (#1809299, #1809301)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.2-5
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun  6 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.0.2-1
- Update to latest upstream version (#1458966)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 5.0.1-2
- Rebuild for gpgme 1.18

* Thu Mar 31 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.0.1-1
- Update to latest upstream version (#1311111)

* Wed Feb  3 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.0.0-1
- Update to latest upstream version
- libalpm is bumped to version 10.0
- Upstream is in the process of splitting out makepkg, it is now
  installed in /usr/share/makepkg.

* Sat Jun 20 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.1-1
- Update to version 4.2.1
- libalpm is bumped to version 9.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-5.20130626git28cb22e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 07 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.1.2-4.20130626git28cb22e
- Require bsdtar (#1176244)
- Use %%license and a single directory for documentation

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-3.20130626git28cb22e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-2.20130626git28cb22e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 22 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.1.2-1.20130626git28cb22e
- Build from git snapshot.
- Include /etc/pacman.d/mirrorlist.
- Add pacman-filesystem package.
- Add missing build dependencies and fix other packaging issues.
- Package accepted (#998127).

* Fri Aug 16 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.1.2-1
- Initial packaging.
