# The latest version of Citrix Hypervisor
%global upstream_major 8
%global upstream_minor 0
%global upstream_micro 0
%global buildnum 3
%global upstream_name xe-guest-utilities
%global service_name xe-linux-distribution
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0


Summary: XAPI Virtual Machine Monitoring Scripts
Name:    %{upstream_name}-latest
Version: 7.17.0
Release: 3%{?dist}
License: BSD
URL:     https://github.com/xenserver/%{upstream_name}
Source0: %{url}/archive/v%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
# Follow upstream to enable net.ipv4.conf.all.arp_notify
Patch0:  enable_net.ipv4.conf.all.arp_notify.patch
# XAPI project only supports ix86 and x86_64 virtual machine
ExclusiveArch: %{ix86} x86_64
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: systemd
# the only version that has been built in Fedora
Obsoletes:     %{upstream_name} = 7.12.0
%{?systemd_requires}

%description
Scripts for monitoring XAPI project virtual machine.

Writes distribution version information and IP address to XenStore.

This package follows the latest version of %{upstream_name} upstream.

%prep
%setup -q -n %{upstream_name}-%{version}
%patch0 -p1
sed -i -e 's:/usr/share/oem/xs:%{_sbindir}:' mk/%{service_name}.service
# move xenstore utilities provided by this package to a private directory
# to prevent conflict with xen-runtime
sed -i -e 's:/usr/bin/xenstore-exists:%{_libexecdir}/%{upstream_name}/xenstore-exists:' mk/xen-vcpu-hotplug.rules

%build
# Mimic the latest Citrix Hypervisor
export GOPATH="%{gopath}"
make PRODUCT_MAJOR_VERSION=%{upstream_major} \
     PRODUCT_MINOR_VERSION=%{upstream_minor} \
     PRODUCT_MICRO_VERSION=%{upstream_micro} \
     RELEASE=%{buildnum} \
     GO_FLAGS='-a -ldflags "${LDFLAGS:-}%{?currentgoldflags} -B 0x$$(head -c20 /dev/urandom|od -An -tx1|tr -d '"'"' \n'"'"') -extldflags '"'"'%__global_ldflags %{?__golang_extldflags}'"'"' -compressdwarf=false" -v -x'

%install
mkdir -p %{buildroot}%{_sbindir}
mv -v build/stage/usr/sbin/* %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libexecdir}/%{upstream_name}
mv -v build/stage/usr/bin/* %{buildroot}%{_libexecdir}/%{upstream_name}

mkdir -p %{buildroot}%{_unitdir}
cp -p mk/%{service_name}.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}
cp -p mk/xen-vcpu-hotplug.rules %{buildroot}%{_udevrulesdir}/z10-xen-vcpu-hotplug.rules

mkdir -p %{buildroot}%{_localstatedir}/cache
touch %{buildroot}%{_localstatedir}/cache/%{service_name}

%post
%systemd_post %{service_name}.service

%preun
%systemd_preun %{service_name}.service

%postun
%systemd_postun_with_restart %{service_name}.service

%triggerun -- %{upstream_name}
if /bin/ls /etc/rc3.d/S*%{service_name} >/dev/null 2>&1; then
    # Re-enable the service if it was enabled in sysv mode
    /usr/bin/systemctl enable %{service_name} >dev/null 2>&1||:
    /bin/rm /etc/rc3.d/S*%{service_name} >/dev/null 2>&1||:
    /usr/bin/systemctl try-restart %{service_name} >dev/null 2>&1||:
fi


%files
%license LICENSE
%{_sbindir}/%{service_name}
%{_sbindir}/xe-daemon
%{_unitdir}/%{service_name}.service
%{_udevrulesdir}/z10-xen-vcpu-hotplug.rules
%{_libexecdir}/%{upstream_name}
%ghost %{_localstatedir}/cache/%{service_name}

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Robin Lee <cheeselee@fedoraproject.org> - 7.17.0-2
- Fix debugsource generation on EL7/EL8

* Wed Dec 11 2019 Robin Lee <cheeselee@fedoraproject.org> - 7.17.0-1
- Release 7.17.0
- Update GO_FLAGS

* Mon Dec  9 2019 Robin Lee <cheeselee@fedoraproject.org> - 7.16.0-1
- Rename to xe-guest-utilities-latest to not conflict with the xe-guest-utilities package
  provided in Citrix Hypervisor
- Release 7.16.0
- Separate %%{buildnum} and %%{release}

* Wed Aug 14 2019 Robin Lee <cheeselee@fedoraproject.org> - 7.12.0-2
- Re-enable the service if it was enabled in sysv mode
- Follow upstream to enable net.ipv4.conf.all.arp_notify

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.12.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun  6 2019 Robin Lee <cheeselee@fedoraproject.org> - 7.12.0-1
- Update to 7.12.0
- Remove upstreamed patches
- Don't require removed subpackage
- use %%{_localstatedir} instead of %%{_var}

* Wed May  8 2019 Robin Lee <cheeselee@fedoraproject.org> - 7.11.0-1
- Massively modified for Fedora review based on mk/xe-guest-utilities.spec.in
