%global debug_package   %{nil}

# container-selinux
%global git0 https://github.com/containers/container-selinux
%global commit0 9b3b66f400ed2f2bee76559fb200cf1c1f92d29c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# container-selinux stuff (prefix with ds_ for version/release etc.)
# Some bits borrowed from the openstack-selinux package
%global selinuxtype targeted
%global moduletype services
%global modulenames container

# Usage: _format var format
# Expand 'modulenames' into various formats as needed
# Format must contain '$x' somewhere to do anything useful
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %1+=" "; done;

# Hooked up to autobuilder, please check with @lsm5 before updating
Name: container-selinux
%if 0%{?fedora}
Epoch: 2
%endif
Version: 2.148.0
Release: 3.dev.git%{shortcommit0}%{?dist}
License: GPLv2
URL: %{git0}
Summary: SELinux policies for container runtimes
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildArch: noarch
BuildRequires: git
BuildRequires: pkgconfig(systemd)
BuildRequires: selinux-policy >= %_selinux_policy_version
BuildRequires: selinux-policy-devel >= %_selinux_policy_version
# RE: rhbz#1195804 - ensure min NVR for selinux-policy
Requires: selinux-policy >= %_selinux_policy_version
Requires(post): selinux-policy-base >= %_selinux_policy_version
Requires(post): selinux-policy-targeted >= %_selinux_policy_version
Requires(post): policycoreutils
Requires(post): libselinux-utils
Requires(post): sed
Obsoletes: %{name} <= 2:1.12.5-13
Obsoletes: docker-selinux <= 2:1.12.4-28
Provides: docker-selinux = %{?epoch:%{epoch}:}%{version}-%{release}

%description
SELinux policy modules for use with container runtimes.

%prep
%autosetup -Sgit -n %{name}-%{commit0}

%build
make

%install
# install policy modules
%_format MODULES $x.pp.bz2
install -d %{buildroot}%{_datadir}/selinux/packages
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/services
install -p -m 644 container.if %{buildroot}%{_datadir}/selinux/devel/include/services
install -m 0644 $MODULES %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}/%{_datadir}/containers/selinux
install -m 644 container_contexts %{buildroot}/%{_datadir}/containers/selinux/contexts

%check

%pre
%selinux_relabel_pre -s %{selinuxtype}

%post
# Install all modules in a single transaction
if [ $1 -eq 1 ]; then
   %{_sbindir}/setsebool -P -N virt_use_nfs=1 virt_sandbox_use_all_caps=1
fi
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
%{_sbindir}/semodule -n -s %{selinuxtype} -r container 2> /dev/null
%{_sbindir}/semodule -n -s %{selinuxtype} -d docker 2> /dev/null
%{_sbindir}/semodule -n -s %{selinuxtype} -d gear 2> /dev/null
%selinux_modules_install -s %{selinuxtype} $MODULES
. %{_sysconfdir}/selinux/config
sed -e "\|container_file_t|h; \${x;s|container_file_t||;{g;t};a\\" -e "container_file_t" -e "}" -i /etc/selinux/${SELINUXTYPE}/contexts/customizable_types 
matchpathcon -qV %{_sharedstatedir}/containers || restorecon -R %{_sharedstatedir}/containers &> /dev/null || :

%postun
if [ $1 -eq 0 ]; then
   %selinux_modules_uninstall -s %{selinuxtype} %{modulenames} docker
fi

%posttrans
%selinux_relabel_post -s %{selinuxtype}

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%doc README.md
%{_datadir}/selinux/*
%dir %{_datadir}/containers/selinux
%{_datadir}/containers/selinux/contexts
# Currently shipped in selinux-policy-doc
#%%{_datadir}/man/man8/container_selinux.8.gz

# Hooked up to autobuilder, please check with @lsm5 before updating
%changelog
* Thu Oct 15 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.148.0-3.dev.git9b3b66f
- autobuilt 9b3b66f

* Wed Oct 14 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.148.0-2.dev.git3c361a2
- bump to 2.148.0
- autobuilt 3c361a2

* Mon Oct 12 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.147.0-2.dev.git9fb1698
- bump to 2.147.0
- autobuilt 9fb1698

* Thu Oct  8 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.146.0-2.dev.git2908536
- bump to 2.146.0
- autobuilt 2908536

* Thu Sep 10 18:12:36 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.145.0-2.dev.git464e922
- bump to 2.145.0
- autobuilt 464e922

* Mon Aug 31 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.144.0-5.dev.git5d929d4
- Resolves: #1797554 - use _selinux_policy_version macro

* Fri Aug 28 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.144.0-4.dev.git5d929d4
- Resolves: #1780129 - bump min selinux-policy

* Thu Aug 13 14:10:45 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.144.0-3.dev.git5d929d4
- autobuilt 5d929d4

* Wed Aug 12 15:10:04 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.144.0-2.dev.git746ea7a
- bump to 2.144.0
- autobuilt 746ea7a

* Wed Aug 05 22:10:34 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.143.0-2.dev.gite2d5a9e
- bump to 2.143.0
- autobuilt e2d5a9e

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.142.0-3.dev.gitfe6a25c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 11:09:45 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.142.0-2.dev.gitfe6a25c
- bump to 2.142.0
- autobuilt fe6a25c

* Fri Jul 24 10:09:44 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.141.0-2.dev.git2750e78
- bump to 2.141.0
- autobuilt 2750e78

* Thu Jul 23 2020 Merlin Mathesius <mmathesi@redhat.com> - 2:2.140.0-2.dev.git965c7fb
- Cleanup usage of %%{epoch} macro to allow building for ELN

* Thu Jul 23 19:10:26 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.140.0-2.dev.git965c7fb
- bump to 2.140.0
- autobuilt 965c7fb

* Sat Jul 18 11:10:04 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.139.0-2.dev.git8c26927
- bump to 2.139.0
- autobuilt 8c26927

* Thu Jul 09 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.138.0-2.dev.git9884317
- bump to 2.138.0
- autobuilt 9884317

* Thu Jun 11 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.137.0-2.dev.git6b721da
- bump to 2.137.0
- autobuilt 6b721da

* Thu Jun 11 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.136.0-2.dev.git441172a
- bump to 2.136.0
- autobuilt 441172a

* Fri May 29 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.135.0-2.dev.git0d99e89
- bump to 2.135.0
- autobuilt 0d99e89

* Thu May 28 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.134.0-2.dev.gitff26015
- bump to 2.134.0
- autobuilt ff26015

* Mon May 11 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.132.0-3.dev.git0a878bd
- autobuilt 0a878bd

* Wed Apr 15 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.132.0-2.dev.git448dfbf
- bump to 2.132.0
- autobuilt 448dfbf

* Thu Apr 09 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.131.0-2.dev.git9ce0dac
- bump to 2.131.0
- autobuilt 9ce0dac

* Mon Apr 06 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.130.0-2.dev.gitfd55ae0
- bump to 2.130.0
- autobuilt fd55ae0

* Sun Mar 29 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.129.0-2.dev.gitf00d1f4
- bump to 2.129.0
- autobuilt f00d1f4

* Sun Mar 29 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.128.0-2.dev.git363646f
- bump to 2.128.0
- autobuilt 363646f

* Fri Mar 27 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.127.0-2.dev.git6caf15d
- bump to 2.127.0
- autobuilt 6caf15d

* Thu Mar 26 2020 Dan Walsh <dwalsh@fedoraproject.org> - 2:2.126.0-2.dev.git867a377
- Install selinux contexts file into /usr/share/containers/selinux/contexts

* Thu Mar 26 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.126.0-2.dev.git867a377
- bump to 2.126.0
- autobuilt 867a377

* Mon Mar 23 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.125.2-2.dev.gitae0720d
- bump release tag

* Mon Mar 23 2020 Dan Walsh <dwalsh@fedoraproject.org> - 2:2.125.2-1.dev.gitae0720d
- Install container_contexts file

* Mon Mar 23 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.125.0-3.1.dev.gitfde876b
- autobuilt fde876b

* Mon Mar 23 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.125.0-2.1.dev.gitb321ea4
- bump release tag for smooth upgrade path

* Fri Mar 20 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.125.0-0.1.dev.gitb321ea4
- bump to 2.125.0
- autobuilt b321ea4

* Tue Feb 11 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.124.0-4.dev.git5624558
- keep functional upgrade path from f31

* Tue Feb 11 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.124.0-0.4.dev.git5624558
- autobuilt 5624558

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.124.0-0.3.dev.gitf958d0c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.124.0-0.2.dev.gitf958d0c
- use more current selinux policy version

* Wed Dec 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.124.0-0.1.dev.gitf958d0c
- bump to 2.124.0
- autobuilt f958d0c

* Mon Dec 09 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.123.0-0.4.dev.git0b25a4a
- run selinux_relabel_pre

* Fri Nov 29 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.123.0-0.3.dev.git0b25a4a
- autobuilt 0b25a4a

* Fri Nov 29 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2:2.123.0-0.2.dev.git661a904
- Use selinux macros in post install scripts

* Mon Nov 25 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.123.0-0.1.dev.git661a904
- bump to 2.123.0
- autobuilt 661a904

* Fri Nov 22 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.122.0-0.1.dev.git4560dd4
- bump to 2.122.0
- autobuilt 4560dd4

* Tue Nov 19 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.120.1-0.2.dev.gita233788
- autobuilt a233788

* Wed Nov 06 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.120.1-0.1.dev.git6fb6dcf
- bump to 2.120.1
- autobuilt 6fb6dcf

* Sun Oct 27 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.119.1-0.1.dev.git2ecb2a8
- bump to 2.119.1
- autobuilt 2ecb2a8

* Thu Oct 24 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.119.0-0.1.dev.gitb383f07
- bump to 2.119.0
- autobuilt b383f07

* Fri Oct 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.118.0-0.1.dev.git79bdcb5
- bump to 2.118.0
- autobuilt 79bdcb5

* Fri Sep 20 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.117.0-0.1.dev.gitbfde70a
- bump to 2.117.0
- autobuilt bfde70a

* Thu Sep 05 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.116.0-0.1.dev.gitc5ef5ac
- bump to 2.116.0
- autobuilt c5ef5ac

* Wed Aug 21 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.115.0-0.1.dev.gitfddfbbb
- bump to 2.115.0
- autobuilt fddfbbb

* Mon Aug 19 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.114.0-0.1.dev.git028ab00
- bump to 2.114.0
- autobuilt 028ab00

* Fri Aug 9 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.113-1
- Allow containers to name_bind to rawip_sockets.

* Thu Aug 8 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.112-1
- Allow containers to use fusefs_t entrypoint
- Dontaudit attempts to setattr on devicenodes.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.111.0-3.1.dev.git9a75deb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.111.0-2.1.dev.git9a75deb
- bump to 2.111.0
- autobuilt 9a75deb

* Wed Jul 10 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2.110.0-1.1.dev.git544d71f
- bump to v2.110.0
- hook up to autobuild

* Mon Jul 8 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.109-1
- Allow containers to accept connections on all socket types
- Allow containers to connect to gssproxy stream sockets if added to container

* Fri Jun 14 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.107-1
- Allow containers to manipulate Onload files.

* Tue Jun 11 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.106-1
- Allow all unconfined domains to manage unlabeled keyrings
- Add labeling for kubernetes pods

* Mon Jun 3 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.104-1
- Set proper labeling for container volumes in SilverBlue

* Fri May 17 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.103-1
- Set proper labeling for container volumes

* Sun May 12 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.102-1
- Allow all container domains to be entered from container_file_t

* Fri May 3 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.101-1
- Allow containers to read rpm cache and rpm databse

* Tue Apr 23 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.100-1
- Allow containers running as spc_t to create unlabeled_t kernel keyrings

* Mon Apr 22 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.99-1
- Fix labeling on /var/lib/containers/storage/overlay-layers,images to be sharable.

* Mon Apr 15 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.98-1
- Allow iptables to append to container_file_t

* Fri Apr 12 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.97-1
- Allow containers to read/write sysctl_kernel_ns_last_pid_t
- Allow containers to manage fusefs sockets and named pipes

* Thu Apr 4 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.96-1
- Allow containers to read/write sysctl_kernel_ns_last_pid_t

* Mon Apr 1 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.95-1
- Allow containers to create fusefs sockets and named pipes

* Thu Mar 28 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.94-1
- Allow init_t to manage container content
- Allow container domains to create fifo_files on fusefs file systems
- Add boolean to allow containers to use ceph file systems

* Tue Mar 26 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.91-1
- Allow container runtimes to create unlabeled keyrings

* Wed Mar 20 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.90-1
- Allow containers to mount and umount fuse file systems.  This will allow us
- to use buidlah within a user namespace separated container.

* Sat Mar 9 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.89-1
- Allow all container domains to have container file types entrypoint
- Add new release to fix issues with udica
- Allow container_runtime_t to dyntransition to container domains

* Sat Mar 09 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.89-5.git2521d0d
- bump to 2.89
- autobuilt 2521d0d

* Thu Mar 07 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.88-4.git5c98b56
- bump to 2.88
- autobuilt 5c98b56

* Wed Mar 06 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.87-3.git2c1a2ab
- autobuilt 2c1a2ab

* Sat Mar 02 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.87-2.git891a85f
- bump to 2.87
- autobuilt 891a85f

* Fri Mar 1 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.86-1
- Allow unconfined user and services to dyntrans to container domains, needed for CRIU
- Allow containers exectue hugetlb files.

* Thu Feb 28 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.85-1
- More allow rules to allow containers to run within containers

* Thu Feb 28 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.84-1
- More allow rules to allow containers to run within containers

* Tue Feb 26 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.82-2.git5e1f62f
- bump to 2.82
- autobuilt 5e1f62f

* Mon Feb 25 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.83-1
- Allow containers to mounton cgroup and container_file_t

* Sun Feb 10 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.82-1.nightly.git5e1f62f
- Allow confined users to use containers

* Fri Feb 08 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.80-3.git21c2be6
- bump to 2.80
- autobuilt 21c2be6

* Thu Feb 7 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.81-1
- Add new labels for paths for containerd

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.80-2.git1b655d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.80-1.nightly.git21c2be6
- Don't allow containers to talk to contianer runtime sockets

* Fri Jan 11 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.79-1
- Fix labeling on /var/lib/registries

* Thu Jan 10 2019 Dan Walsh <dwalsh@fedoraproject.org> - 2.78-1
- Fix labeling for images in docker daemon user namespace

* Mon Dec 17 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.77-1
- Allow container-runtime to setattr on fifo_file handed into container runtime.

* Tue Nov 13 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.752.75-1.dev.git99e2cfd1
- bump to 2.75
- autobuilt 99e2cfd

* Mon Nov 12 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.76-1
- Allow containers to sendto dgram socket of container runtimes
- Needed to run container runtimes in notify socket unit files.

* Tue Oct 30 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.75-1.dev.git99e2cfd
- Allow containers to use fuse file systems by default

* Fri Oct 19 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.74-1
- Allow containers to setexec themselves

* Sat Sep 22 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.73-2
- Remove requires for policycoreutils-python-utils we don't need it.

* Wed Sep 12 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.73-1
- Define spc_t as a container_domain, so that container_runtime will transition
to spc_t even when setup with nosuid.

* Wed Sep 12 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.72-1
- Allow container_runtimes to setattr on callers fifo_files
github.com/opencontainers/selinux
* Mon Aug 27 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.71-2
- Fix restorecon to not error on missing directory

* Wed Aug 22 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.71-1
- Allow unconfined_r to transition to system_r over container_runtime_exec_t

* Wed Aug 22 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.70-1
- Allow unconfined_t to transition to container_runtime_t over container_runtime_exec_t

* Wed Jul 25 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.69-1
- dontaudit attempts to write to sysctl_kernel_t

* Wed Jul 18 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.68-2.gitc139a3d
- autobuilt c139a3d

* Mon Jul 16 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.67-1
- Add label for /var/lib/origin
- Add customizable_file_t to customizable_types

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.67-3.dev.git042f7cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.67-2.git042f7cf
- autobuilt 042f7cf

* Sat Jul 07 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.67-1.git0407867
- bump to 2.67
- autobuilt 0407867

* Sat Jun 30 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.66-1
- Allow container runtimes to dbus chat with systemd-resolved

* Tue Jun 12 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.64-1.gitdfaf8fd
- bump to 2.64
- autobuilt dfaf8fd

* Mon Jun 11 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.65-1
- Add new type to handle containers running with a non priv user in a userns
- allow containers to map all sockets

* Sun Jun 3 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.64-1.gitdfaf8fd
- Allow containers to create all socket classes

* Wed May 30 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.63-1
- Allow containers to create icmp packets

* Fri May 25 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.62-1.git1ecf953
- bump to 2.62
- autobuilt 1ecf953

* Mon May 21 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.61-1
- Allow spc_t to load kernel modules from inside of container 

* Mon May 21 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.60-1
- Allow containers to list cgroup directories

* Mon May 21 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.59-1
- Transition for unconfined_service_t to container_runtime_t when executing container_runtime_exec_t.

* Mon May 21 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.58-2
- Run restorecon /usr/bin/podman in postinstall

* Fri May 18 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.58-1
- Add labels to allow podman to be run from a systemd unit file

* Tue Apr 17 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.55-12.gitd248f91
- autobuilt commit d248f91

* Tue Apr 17 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.55-11.gitd248f91
- autobuilt commit d248f91

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.55-10.gitd248f91
- autobuilt commit d248f91

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.55-9.gitd248f91
- autobuilt commit d248f91

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.55-8
- autobuilt commit d248f91

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.55-7
- autobuilt commit d248f91

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.55-6
- autobuilt commit d248f91

* Mon Apr 09 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.55-5
- autobuilt commit d248f91

* Mon Apr 09 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:2.55-4
- autobuilt commit d248f91

* Mon Apr 09 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.55-3
- autobuilt commit d248f91

* Mon Apr 09 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.55-2
- autobuilt commit d248f91

* Thu Mar 15 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.55-1
- Dontaudit attempts by containers to write to /proc/self

* Wed Mar 14 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.54-1
-  Add rules for container domains to make writing custom policy easier
-  Allow shell_exec_t as a container_runtime_t entrypoint

* Thu Mar 8 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.52-1
- Add rules for container domains to make writing custom policy easier

* Thu Mar 8 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.51-1
- Allow shell_exec_t as a container_runtime_t entrypoint

* Wed Mar 7 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.50-1
- Allow bin_t as a container_runtime_t entrypoint
- Add rules for running container runtimes on mls

* Thu Feb 15 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.48-1
- Allow container domains to map container_file_t directories

* Sat Feb 10 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.47-1
- Change default label of /exports to container_var_lib_t

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2:2.46-3
- Escape macros in %%CHANGELOG

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.46-1
- Add support for nosuid_transition flags for container_runtime and unconfined domains
* Fri Feb 02 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.45-1
- Allow containers to sendto their own stream sockets

* Mon Jan 29 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.44-1
- Allow container domains to read kernel ipc info

* Mon Jan 22 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.43-1
- Allow containers to memory map the fifo_files leaked into container from
container runtimes.

* Tue Jan 16 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.42-1
- Allow unconfined domains to transition to container types, when no-new-privs is set.

* Tue Jan 9 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.41-1
- Add support to nnp_transition for container domains
- Eliminates need for typebounds.

* Tue Jan 9 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.40-1
- Allow container_runtime_t to use user ttys
- Fixes bounds check for container_t

* Mon Jan 8 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.39-1
- Allow container runtimes to use interited terminals.  This helps
satisfy the bounds check of container_t versus container_runtime_t.

* Sat Jan 6 2018 Dan Walsh <dwalsh@fedoraproject.org> - 2.38-1
- Allow container runtimes to mmap container_file_t devices
- Add labeling for rhel push plugin

* Tue Dec 12 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.37-1
- Allow containers to use inherited ttys
- Allow ostree to handle labels under /var/lib/containers/ostree

* Mon Nov 27 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.36-1
- Allow containers to relabelto/from all file types to container_file_t

* Mon Nov 27 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.35-1
- Allow container to map chr_files labeled container_file_t

* Wed Nov 22 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.34-1
- Dontaudit container processes getattr on kernel file systems

* Sun Nov 19 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.33-1
- Allow containers to read /etc/resolv.conf and /etc/hosts if volume
- mounted into container.

* Wed Nov 8 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.32-1
- Make sure users creating content in /var/lib with right labels

* Thu Oct 26 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.31-1
- Allow the container runtime to dbus chat with dnsmasq
- add dontaudit rules for container trying to write to /proc

* Tue Oct 10 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.29-1
- Add support for lxcd
- Add support for labeling of tmpfs storage created within a container.

* Mon Oct 9 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.28-1
- Allow a container to umount a container_file_t filesystem

* Fri Sep 22 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.27-1
-  Allow container runtimes to work with the netfilter sockets
-  Allow container_file_t to be an entrypoint for VM's
-  Allow spc_t domains to transition to svirt_t

* Fri Sep 22 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.24-1
-     Make sure container_runtime_t has all access of container_t

* Thu Sep 7 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.23-1
- Allow container runtimes to create sockets in tmp dirs

* Tue Sep 5 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.22-1
- Add additonal support for crio labeling.

* Mon Aug 14 2017 Troy Dawson <tdawson@redhat.com> - 2.21-3
- Fixup spec file conditionals

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 6 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.21-1
- Allow containers to execmod on container_share_t files.

* Thu Jul 6 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.20-2
- Relabel runc and crio executables

* Fri Jun 30 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.20-1
- Allow container processes to getsession

* Mon Jun 12 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.19-1
- Allow containers to create tun sockets

* Tue Jun 6 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.18-1
- Fix labeling for CRI-O files in overlay subdirs

* Mon Jun 5 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.17-1
- Revert change to run the container_runtime as ranged

* Thu Jun 1 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.16-1
- Add default labeling for cri-o in /etc/crio directories

* Wed May 31 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.15-1
- Allow container types to read/write container_runtime fifo files
- Allow a container runtime to mount on top of its own /proc

* Fri May 19 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.14-1
- Add labels for crio rename
- Break container_t rules out to use a separate container_domain
- Allow containers to be able to set namespaced SYCTLS
- Allow sandbox containers manage fuse files.
- Fixes to make container_runtimes work on MLS machines
- Bump version to allow handling of container_file_t filesystems
- Allow containers to mount, remount and umount container_file_t file systems
- Fixes to handle cap_userns
- Give container_t access to XFRM sockets
- Allow spc_t to dbus chat with init system
- Allow spc_t to dbus chat with init system
- Add rules to allow container runtimes to run with unconfined disabled
- Add rules to support cgroup file systems mounted into container.
- Fix typebounds entrypoint problems
- Fix typebounds problems
- Add typebounds statement for container_t from container_runtime_t
- We should only label runc not runc*

* Tue Feb 28 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.10-1
- Add rules to allow container runtimes to run with unconfined disabled
- Add rules to support cgroup file systems mounted into container.

* Mon Feb 13 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2.9-1
- Add rules to allow container_runtimes to run with unconfined disabled

* Thu Feb 9 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2:8.1-1
- Allow container_file_t to be stored on cgroup_t file systems

* Tue Feb 7 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2:7.1-1
- Fix type in container interface file

* Mon Feb 6 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2:6.1-1
- Fix typebounds entrypoint problems

* Fri Jan 27 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2:5.1-1
- Fix typebounds problems

* Thu Jan 19 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2:4.1-1
- Add typebounds statement for container_t from container_runtime_t
- We should only label runc not runc*

* Tue Jan 17 2017 Dan Walsh <dwalsh@fedoraproject.org> - 2:3.1-1
- Fix labeling on /usr/bin/runc.*
- Add sandbox_net_domain access to container.te
- Remove containers ability to look at /etc content

* Wed Jan 11 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.2-4
- use upstream's RHEL-1.12 branch, commit 56c32da for CentOS 7

* Tue Jan 10 2017 Jonathan Lebon <jlebon@redhat.com> - 2:2.2-3
- properly disable docker module in %%post

* Sat Jan 07 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.2-2
- depend on selinux-policy-targeted
- relabel docker-latest* files as well

* Fri Jan 06 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.2-1
- bump to v2.2
- additional labeling for ocid

* Fri Jan 06 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0-2
- install policy at level 200
- From: Dan Walsh <dwalsh@redhat.com>

* Fri Jan 06 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0-1
- Resolves: #1406517 - bump to v2.0 (first upload to Fedora as a
standalone package)
- include projectatomic/RHEL-1.12 branch commit for building on centos/rhel

* Mon Dec 19 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.12.4-29
- new package (separated from docker)
