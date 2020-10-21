Name:          toolbox
Version:       0.0.96

%global goipath github.com/containers/%{name}
%gometa

Release:       1%{?dist}
Summary:       Unprivileged development environment

License:       ASL 2.0
URL:           https://github.com/containers/%{name}
Source0:       https://github.com/containers/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

# Fedora specific
Patch100:      toolbox-Don-t-use-Go-s-semantic-import-versioning.patch
Patch101:      toolbox-Make-the-build-flags-match-Fedora-s-gobuild.patch
Patch102:      toolbox-Make-the-build-flags-match-Fedora-s-gobuild-for-PPC64.patch

BuildRequires: ShellCheck
BuildRequires: golang >= 1.13
BuildRequires: golang-github-cpuguy83-md2man
BuildRequires: golang(github.com/HarryMichal/go-version)
BuildRequires: golang(github.com/acobaugh/osrelease)
BuildRequires: golang(github.com/briandowns/spinner) >= 1.10.0
BuildRequires: golang(github.com/docker/go-units) >= 0.4.0
BuildRequires: golang(github.com/godbus/dbus) >= 5.0.3
BuildRequires: golang(github.com/mattn/go-isatty) >= 0.0.12
BuildRequires: golang(github.com/sirupsen/logrus) >= 1.4.2
BuildRequires: golang(github.com/spf13/cobra) >= 0.0.5
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: meson
BuildRequires: pkgconfig(bash-completion)
BuildRequires: systemd

Requires:      flatpak-session-helper
Requires:      podman >= 1.4.0


%description
Toolbox is offers a familiar RPM based environment for developing and
debugging software that runs fully unprivileged using Podman.

# The list of requires packages for -support and -experience should be in sync with:
# https://github.com/containers/toolbox/blob/master/images/fedora/f33/extra-packages
%package       support
Summary:       Required packages for the container image to support %{name}

# These are really required to make the image work with toolbox
Requires:      passwd
Requires:      shadow-utils
Requires:      krb5-libs
Requires:      vte-profile

%description   support
The %{name}-support package contains all the required packages that are needed
to be installed in the container image to make it work with the %{name}.

The %{name}-support package should be typically installed from the Dockerfile
if the image isn't based on the fedora-toolbox image.


%package       experience
Summary:       Set of packages to enhance the %{name} experience

Requires:      %{name}-support = %{version}-%{release}
Requires:      bash-completion
Requires:      bzip2
Requires:      diffutils
Requires:      dnf-plugins-core
Requires:      findutils
Requires:      flatpak-spawn
Requires:      fpaste
Requires:      git
Requires:      gnupg
Requires:      gnupg2-smime
Requires:      gvfs-client
Requires:      hostname
Requires:      iputils
Requires:      jwhois
Requires:      keyutils
Requires:      less
Requires:      lsof
Requires:      man-db
Requires:      man-pages
Requires:      mlocate
Requires:      mtr
Requires:      openssh-clients
Requires:      pigz
Requires:      procps-ng
Requires:      rsync
Requires:      sudo
Requires:      tcpdump
Requires:      time
Requires:      traceroute
Requires:      tree
Requires:      unzip
Requires:      wget
Requires:      which
Requires:      words
Requires:      xz
Requires:      zip

%description   experience
The %{name}-experience package contains all the packages that should be
installed in the container to provide the same default experience as working
on the host.

The %{name}-experience package should be typically installed from the
Dockerfile if the image isn't based on the fedora-toolbox image.


%package       tests
Summary:       Tests for %{name}

Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      bats

%description   tests
The %{name}-tests package contains system tests for %{name}.


%prep
%setup -q
%patch100 -p1

%ifnarch ppc64
%patch101 -p1
%else
%patch102 -p1
%endif

%gomkdir


%build
export GO111MODULE=off
export GOPATH=%{gobuilddir}:%{gopath}
ln -s src/cmd cmd
ln -s src/pkg pkg
%meson --buildtype=plain -Dprofile_dir=%{_sysconfdir}/profile.d
%meson_build


%check
%meson_test


%install
%meson_install


%files
%doc CODE-OF-CONDUCT.md NEWS README.md SECURITY.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/bash-completion
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-*.1*
%{_sysconfdir}/profile.d/%{name}.sh
%{_tmpfilesdir}/%{name}.conf

%files support

%files experience

%files tests
%{_datadir}/%{name}


%changelog
* Thu Oct 01 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.0.96-1
- Update to 0.0.96

* Sun Aug 30 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.0.95-1
- Update to 0.0.95

* Mon Aug 24 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.0.94-1
- Update to 0.0.94

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.0.93-1
- Update to 0.0.93

* Fri Jul 03 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.0.92-1
- Update to 0.0.92

* Fri Jul 03 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.0.91-2
- Fix the 'toolbox --version' output

* Tue Jun 30 2020 Harry Míchal <harrymichal@seznam.cz> - 0.0.91-1
- Update to 0.0.91

* Sat Jun 27 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.0.18-5
- Remove ExclusiveArch to match Podman

* Wed Jun 10 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.0.18-4
- Sync the "experience" packages with the current Dockerfile
- Make "experience" Require "support"

* Fri Apr 03 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.0.18-3
- Drop compatibility Obsoletes and Provides for fedora-toolbox

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.0.18-1
- Update to 0.0.18

* Wed Nov 20 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.17-1
- Update to 0.0.17

* Tue Oct 29 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.16-1
- Update to 0.0.16

* Mon Sep 30 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.15-1
- Update to 0.0.15

* Wed Sep 18 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.14-1
- Update to 0.0.14

* Thu Sep 05 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.13-1
- Update to 0.0.13

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.12-1
- Update to 0.0.12

* Tue Jun 25 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.11-2
- Require flatpak-session-helper

* Fri Jun 21 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.11-1
- Update to 0.0.11

* Tue May 21 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.10-1
- Update to 0.0.10

* Tue Apr 30 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.9-1
- Update to 0.0.9

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.0.8-2
- Rebuild with Meson fix for #1699099

* Fri Apr 12 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.8-1
- Update to 0.0.8

* Thu Mar 14 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.7-1
- Update to 0.0.7

* Fri Feb 22 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.6-1
- Initial build after rename from fedora-toolbox
