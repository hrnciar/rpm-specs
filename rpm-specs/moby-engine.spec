%global with_debug 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

# binaries and unitfiles are currently called 'docker'
# to match with upstream supplied packages
%global origname docker
%global newname moby
%global service_name %{origname}

# moby / docker-ce / cli
%global git_moby https://github.com/%{service_name}/%{service_name}-ce
%global commit_moby 4484c46d9d1a2d10b8fc662923ad586daeedb04f
%global shortcommit_moby %(c=%{commit_moby}; echo ${c:0:7})

# docker-proxy / libnetwork
%global git_libnetwork https://github.com/%{newname}/libnetwork
%global commit_libnetwork 026aabaa659832804b01754aaadd2c0f420c68b6
%global shortcommit_libnetwork %(c=%{commit_libnetwork}; echo ${c:0:7})

# tini
%global git_tini https://github.com/krallin/tini
%global commit_tini fec3683b971d9c3ef73f284f176672c44b448662
%global shortcommit_tini %(c=%{commit_tini}; echo ${c:0:7})

Name: %{newname}-engine
Version: 19.03.13
Release: 1.ce.git%{shortcommit_moby}%{?dist}
Summary: The open-source application container engine
License: ASL 2.0
# no golang / go-md2man for ppc64
ExcludeArch: ppc64
Source0: %{git_moby}/archive/%{commit_moby}.tar.gz
Source1: %{git_libnetwork}/archive/%{commit_libnetwork}.tar.gz
Source2: %{git_tini}/archive/%{commit_tini}.tar.gz
Source3: %{service_name}.service
Source4: %{service_name}.sysconfig
Source5: %{service_name}-zone.xml
URL: https://www.%{origname}.com

BuildRequires: btrfs-progs-devel
BuildRequires: device-mapper-devel
BuildRequires: git
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang >= 1.6.2}
BuildRequires: go-md2man
BuildRequires: libseccomp-devel >= 2.3.0
BuildRequires: make
BuildRequires: pkgconfig(audit)
BuildRequires: pkgconfig(systemd)
BuildRequires: sed
BuildRequires: firewalld-filesystem

# Build dependencies for tini
BuildRequires: cmake
BuildRequires: glibc-static

# required packages on install
Requires: container-selinux
Requires: iptables
Requires: systemd
Requires: tar
Requires: xz
Requires: pigz
Requires: runc
Requires: containerd

Requires(post): firewalld-filesystem
Requires(postun): firewalld-filesystem

# Resolves: rhbz#1165615
Requires: device-mapper-libs >= 1.02.90-1

# Replace the old Docker packages
Obsoletes: %{origname} < 2:%{version}-%{release}
Obsoletes: %{origname}-latest < 2:%{version}-%{release}
Obsoletes: %{origname}-common < 2:%{version}-%{release}
Provides: %{origname} = %{version}-%{release}
Provides: %{origname}-latest = %{version}-%{release}

# conflicting packages
Conflicts: %{origname}
Conflicts: %{origname}-latest
Conflicts: %{origname}-common
Conflicts: %{origname}-io
Conflicts: %{origname}-engine-cs
Conflicts: %{origname}-ce
Conflicts: %{origname}-ce-cli
Conflicts: %{origname}-ee

%description
Docker is an open source project to build, ship and run any application as a
lightweight container.

Docker containers are both hardware-agnostic and platform-agnostic. This means
they can run anywhere, from your laptop to the largest EC2 compute instance and
everything in between - and they don't require you to use a particular
language, framework or packaging system. That makes them great building blocks
for deploying and scaling web apps, databases, and backend services without
depending on a particular stack or provider.

%package fish-completion
Summary: Fish completion files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: fish
Conflicts: %{service_name}-fish-completion
Obsoletes: %{service_name}-fish-completion < 2:%{version}-%{release}
Provides: %{service_name}-fish-completion = %{version}-%{release}

%description fish-completion
This package installs %{summary}.

%package vim
Summary: Vim syntax highlighting files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: vim
Conflicts: %{service_name}-vim
Obsoletes: %{service_name}-vim < 2:%{version}-%{release}
Provides: %{service_name}-vim = %{version}-%{release}

%description vim
This package installs %{summary}.

%package zsh-completion
Summary: Zsh completion files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: zsh
Conflicts: %{service_name}-zsh-completion
Obsoletes: %{service_name}-zsh-completion < 2:%{version}-%{release}
Provides: %{service_name}-zsh-completion = %{version}-%{release}

%description zsh-completion
This package installs %{summary}.

%package nano
Summary: GNU nano syntax highlighting files for Moby
Requires: %{name} = %{version}-%{release}
Requires: nano

%description nano
This package installs %{summary}.

%prep
%autosetup -N -Sgit -n %{service_name}-ce-%{commit_moby}

# untar libnetwork
tar zxf %{SOURCE1}

# untar tini
tar zxf %{SOURCE2}

# correct rpmlint errors for bash completion
sed -i '/env bash/d' components/cli/contrib/completion/bash/docker

%build
# build docker-proxy / libnetwork
(
        cd libnetwork-%{commit_libnetwork}
        mkdir -p src/github.com/%{service_name}
        ln -fns ../../.. src/github.com/%{service_name}/libnetwork
        export GOPATH="${PWD}"
        export LDFLAGS="-linkmode=external"
        %gobuild -o %{service_name}-proxy github.com/%{service_name}/libnetwork/cmd/proxy
)

# build tini
(
        cd tini-%{commit_tini}
        %cmake .
        make tini-static -C "%{__cmake_builddir}"
)

# build engine
(
        cd components/engine
        mkdir -p _build/src/github.com/%{service_name}
        ln -fns ../../../.. _build/src/github.com/%{service_name}/%{service_name}
        export DOCKER_BUILDTAGS="seccomp selinux"
        export DOCKER_DEBUG=1
        export DOCKER_GITCOMMIT=%{shortcommit_moby}
        export GOPATH="${PWD}/_build"
        export VERSION=%{version}
        bash -x hack/make.sh dynbinary
)

# build cli
(
        cd components/cli
        mkdir -p src/github.com/%{service_name}
        ln -fns ../../.. src/github.com/%{service_name}/cli
        export DISABLE_WARN_OUTSIDE_CONTAINER=1
        export GOPATH="${PWD}"
        make VERSION=%{version} GITCOMMIT=%{shortcommit_moby} dynbinary
        man/md2man-all.sh
)

%install
install -dp %{buildroot}%{_bindir}
install -dp %{buildroot}%{_libexecdir}/%{service_name}

# install binary
install -p -m 755 components/cli/build/%{service_name} %{buildroot}%{_bindir}/%{service_name}
install -p -m 755 components/engine/bundles/dynbinary-daemon/%{service_name}d %{buildroot}%{_bindir}/%{service_name}d

# install proxy
install -p -m 755 libnetwork-%{commit_libnetwork}/%{service_name}-proxy %{buildroot}%{_libexecdir}/%{service_name}/%{service_name}-proxy

# install tini
install -p -m 755 tini-%{commit_tini}/%{__cmake_builddir}/tini-static %{buildroot}%{_libexecdir}/%{service_name}/%{service_name}-init

# install udev rules
install -dp %{buildroot}%{_prefix}/lib/udev/rules.d
install -p -m 644 components/engine/contrib/udev/80-%{service_name}.rules %{buildroot}%{_usr}/lib/udev/rules.d/80-%{service_name}.rules

# add init scripts
install -dp %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}
install -p -m 644 components/engine/contrib/init/systemd/docker.socket %{buildroot}%{_unitdir}

# for additional args
install -dp %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/%{service_name}

# add firewalld zone (cf #1817022)
install -dp %{buildroot}%{_prefix}/lib/firewalld/zones
install -p -m 644 %{SOURCE5} %{buildroot}%{_prefix}/lib/firewalld/zones/docker.xml

# add bash, zsh, and fish completions
install -dp %{buildroot}%{_datadir}/bash-completion/completions
install -dp %{buildroot}%{_datadir}/zsh/vendor-completions
install -dp %{buildroot}%{_datadir}/fish/vendor_completions.d
install -p -m 644 components/cli/contrib/completion/bash/%{service_name} %{buildroot}%{_datadir}/bash-completion/completions/%{service_name}
install -p -m 644 components/cli/contrib/completion/zsh/_%{service_name} %{buildroot}%{_datadir}/zsh/vendor-completions/_%{service_name}
install -p -m 644 components/cli/contrib/completion/fish/%{service_name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{service_name}.fish

# install manpages
install -dp %{buildroot}%{_mandir}/man{1,5,8}
install -p -m 644 components/cli/man/man1/*.1 %{buildroot}%{_mandir}/man1
install -p -m 644 components/cli/man/man5/*.5 %{buildroot}%{_mandir}/man5
install -p -m 644 components/cli/man/man8/*.8 %{buildroot}%{_mandir}/man8

# add vimfiles
install -dp %{buildroot}%{_datadir}/vim/vimfiles/doc
install -dp %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
install -dp %{buildroot}%{_datadir}/vim/vimfiles/syntax
install -p -m 644 components/engine/contrib/syntax/vim/doc/%{service_name}file.txt %{buildroot}%{_datadir}/vim/vimfiles/doc/%{service_name}file.txt
install -p -m 644 components/engine/contrib/syntax/vim/ftdetect/%{service_name}file.vim %{buildroot}%{_datadir}/vim/vimfiles/ftdetect/%{service_name}file.vim
install -p -m 644 components/engine/contrib/syntax/vim/syntax/%{service_name}file.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/%{service_name}file.vim

# add nano files
install -dp %{buildroot}%{_datadir}/nano
install -p -m 644 components/engine/contrib/syntax/nano/Dockerfile.nanorc %{buildroot}%{_datadir}/nano/Dockerfile.nanorc

for cli_file in LICENSE MAINTAINERS NOTICE README.md; do
    cp "components/cli/$cli_file" "cli-$cli_file"
done

%pre
getent group %{service_name} >/dev/null || groupadd -r %{service_name} || :

%post
%systemd_post %{service_name}.service %{service_name}.socket
%firewalld_reload

%preun
%systemd_preun %{service_name}.service %{service_name}.socket

%postun
%systemd_postun_with_restart %{service_name}.service
%firewalld_reload

%files
%license cli-LICENSE components/engine/LICENSE
%doc components/engine/{AUTHORS,CHANGELOG.md,CONTRIBUTING.md,MAINTAINERS,NOTICE,README.md}
%doc cli-MAINTAINERS cli-NOTICE cli-README.md
%config(noreplace) %{_sysconfdir}/sysconfig/%{service_name}
%{_bindir}/%{service_name}
%{_bindir}/%{service_name}d
%dir %{_libexecdir}/%{service_name}/
%{_libexecdir}/%{service_name}/%{service_name}-proxy
%{_libexecdir}/%{service_name}/%{service_name}-init
%{_usr}/lib/udev/rules.d/80-%{service_name}.rules
%{_unitdir}/%{service_name}.service
%{_unitdir}/%{service_name}.socket
%{_prefix}/lib/firewalld/zones/docker.xml
%{_datadir}/bash-completion/completions/%{service_name}
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files vim
%dir %{_datadir}/vim/vimfiles/{doc,ftdetect,syntax}
%{_datadir}/vim/vimfiles/doc/%{service_name}file.txt
%{_datadir}/vim/vimfiles/ftdetect/%{service_name}file.vim
%{_datadir}/vim/vimfiles/syntax/%{service_name}file.vim

%files zsh-completion
%dir %{_datadir}/zsh/vendor-completions/
%{_datadir}/zsh/vendor-completions/_%{service_name}

%files fish-completion
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{service_name}.fish

%files nano
%dir %{_datadir}/nano
%{_datadir}/nano/Dockerfile.nanorc

%changelog
* Fri Oct 02 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.13-1.ce.git4484c46
- Update to upstream 19.03.13 (#1837641)

* Fri Oct 02 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.11-4.ce.git42e35e6
- Fix FTBFS: adapt to change to CMake builds (#1864160)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.11-3.ce.git42e35e6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.11-2.ce.git42e35e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.11-1.ce.git42e35e6
- Update to upstream 19.03.11 to prevent CVE-2020-13401

* Thu May 07 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.8-2.ce.gitafacb8b
- Configure storage-driver explicitely (fixes #1832301)
- Add firewalld zone: trust interface docker0, as firewalld now uses nftables
  by default and docker communicates with iptables (fixes #1817022)

* Mon Mar 16 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.8-1.ce.gitafacb8b
- Update to latest upstream release - Docker CE 19.03.8
- Prune unused BuildRequires

* Sun Mar 8 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.7-2.ce.git7141c19
- Add Conflicts with docker-ce-cli and Obsoletes docker-common

* Sat Mar 7 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.7-1.ce.git7141c19
- Update to latest upstream release - Docker CE 19.03.7
- Add Epoch: 2 to Obsoletes for docker and docker-latest

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.09.8-3.ce.git0dd43dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.09.8-2.ce.git0dd43dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.8-1.ce.git0dd43dd
- Update to latest upstream release - Docker CE 18.09.8

* Sat Jul 13 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-5.ce.git2d0083d
- Move docker-init and docker-proxy to /usr/libexec/docker
- Update moby-engine-nano summary to follow guidelines

* Sat Jul 13 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-4.ce.git2d0083d
- Add nofile ulimit to default docker daemon options (#1715254, #1708115)

* Fri Jul 12 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-3.ce.git2d0083d
- rebuilt

* Fri Jul 12 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-2.ce.git2d0083d
- Depend on packaged versions "runc" and "containerd" instead of building them.

* Thu Jun 27 2019 David Michael <dm0@redhat.com> - 18.09.7-1.ce.git2d0083d
- Update docker-ce to commit 2d0083d (version 18.09.7).
- Update runc to commit 425e105.
- Update containerd to commit 894b81a (1.2.6).
- Update docker-proxy to commit e7933d4.

* Tue May 14 2019 David Michael <dm0@redhat.com> - 18.09.6-1.ce.git481bc77
- Update docker-ce to commit 481bc77 (version 18.09.6).
- Update docker-proxy to commit 872f0a8.
- Obsolete and provide the docker and docker-latest packages. (#1700006)

* Thu Apr 11 2019 David Michael <dm0@redhat.com> - 18.09.5-1.ce.gite8ff056
- Update docker-ce to commit e8ff056 (version 18.09.5).
- Update docker-runc to commit 2b18fe1.
- Update docker-containerd to commit bb71b10 (version 1.2.5).
- Update docker-proxy to commit 4725f21.
- Report the correct engine version.
- Install symlinks to unprefixed runc/containerd program names.

* Thu Mar 28 2019 David Michael <dm0@redhat.com> - 18.06.3-2.ce.gitd7080c1
- Conflict with docker-common. (#1693397)

* Thu Feb 21 2019 David Michael <dm0@redhat.com> - 18.06.3-1.ce.gitd7080c1
- Update docker-ce to commit d7080c1 (version 18.06.3).

* Tue Feb 12 2019 David Michael <dm0@redhat.com> - 18.06.2-1.ce.git6d37f41
- Update docker-ce to commit 6d37f41 (version 18.06.2).
- Update docker-runc to commit a592beb.

* Mon Feb 11 2019 David Michael <dm0@redhat.com> - 18.06.1-3.ce.gite68fc7a
- Apply a runc patch for CVE-2019-5736.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.06.1-2.ce.gite68fc7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 David Michael <dm0@redhat.com> - 18.06.1-1.ce.gite68fc7a
- Update docker-ce to commit e68fc7a (version 18.06.1).
- Update docker-runc to commit 69663f0.
- Update docker-containerd to commit 468a545 (version 1.1.2).
- Update docker-proxy to commit 3ac297b.
- Backport a fix for mounting named volumes.
- Create a "docker" group for non-root Docker access.
- Support systemd socket-activation.
- Make runc and containerd commit IDs match their expected values.
- Preserve containerd debuginfo.

* Mon Nov 12 2018 Marcin Skarbek <rpm@skarbek.name> - 18.06.0-2.ce.git0ffa825
- add configuration file
- update service file

* Sat Aug 18 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 18.06.0-1.ce.git0ffa825
- Resolves: #1539161 - first upload to Fedora
- built docker-ce commit 0ffa825
- built docker-runc commit ad0f5255
- built docker-containerd commit a88b631
- built docker-proxy commit a79d368
- built docker-init commit fec3683

* Tue Mar 20 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-4.ce.gitf5ec1e2
- correct some rpmlint errors

* Wed Feb 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-3.ce
- docker-* symlinks to moby-* (RE: gh PR 34226)

* Wed Feb 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-2.ce
- rename binaries as per upstream gh PR 34226

* Fri Jan 26 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-1
- initial build
- built moby commit f5ec1e2
- built cli commit 4b61f56
- built docker-runc commit 2d41c047
- built docker-containerd commit 3addd84
- built docker-proxy commit 7b2b1fe
