Name:           akmods
Version:        0.5.6
Release:        26%{?dist}
Summary:        Automatic kmods build and install tool 

License:        MIT
URL:            http://rpmfusion.org/Packaging/KernelModules/Akmods

# We are upstream, these files are maintained directly in pkg-git
Source0:        95-akmods.preset
Source1:        akmods
Source2:        akmodsbuild
Source3:        akmods.h2m
Source4:        akmodsinit
Source5:        akmodsposttrans
Source6:        akmods.service.in
Source7:        akmods-shutdown
Source8:        akmods-shutdown.service
Source9:        README
Source10:       LICENSE
Source11:       akmods@.service
Source12:       akmods-ostree-post
Source13:       95-akmodsposttrans.install

BuildArch:      noarch

BuildRequires:  help2man

# not picked up automatically
%if 0%{?rhel} == 6
Requires:       %{_bindir}/nohup
%endif
Requires:       %{_bindir}/flock
Requires:       %{_bindir}/time

# needed for actually building kmods:
Requires:       %{_bindir}/rpmdev-vercmp
Requires:       kmodtool >= 1-9

# this should track in all stuff that is normally needed to compile modules:
Requires:       bzip2 coreutils diffutils file findutils gawk gcc grep
Requires:       gzip make sed tar unzip util-linux which rpm-build

%if 0%{?rhel}
Requires:       kernel-abi-whitelists
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
# We use a virtual provide that would match either
# kernel-devel or kernel-PAE-devel
Requires:       kernel-devel-uname-r
Suggests:       (kernel-debug-devel if kernel-debug)
Suggests:       (kernel-devel if kernel)
Suggests:       (kernel-lpae-devel if kernel-lpae)
Suggests:       (kernel-PAE-devel if kernel-PAE)
Suggests:       (kernel-PAEdebug-devel if kernel-PAEdebug)
# Theses are from planetccrma-core or rhel-7-server-rt-rpms
Suggests:       (kernel-rt-devel if kernel-rt)
Suggests:       (kernel-rtPAE-devel if kernel-rtPAE)
%else
# There is no much variant there, so using a sane default
Requires:       kernel-devel
%endif

# we create a special user that used by akmods to build kmod packages
Requires(pre):  shadow-utils

%if 0%{?fedora} || 0%{?rhel} > 6
# systemd unit requirements.
BuildRequires:  systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# Optional but good to have on recent kernel
Requires: elfutils-libelf-devel
%endif


%description
Akmods startup script will rebuild akmod packages during system
boot while its background daemon will build them for kernels right
after they were installed.


%prep
%setup -q -c -T
cp -p %{SOURCE9} %{SOURCE10} .


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_usrsrc}/akmods \
         %{buildroot}%{_sbindir} \
         %{buildroot}%{_sysconfdir}/kernel/postinst.d \
         %{buildroot}%{_localstatedir}/cache/akmods

install -pm 0755 %{SOURCE1} %{buildroot}%{_sbindir}/
install -pm 0755 %{SOURCE2} %{buildroot}%{_sbindir}/
install -pm 0755 %{SOURCE12} %{buildroot}%{_sbindir}/
install -pm 0755 %{SOURCE5} %{buildroot}%{_sysconfdir}/kernel/postinst.d/

%if 0%{?fedora} || 0%{?rhel} > 6
mkdir -p %{buildroot}%{_prefix}/lib/kernel/install.d
install -pm 0755 %{SOURCE13} %{buildroot}%{_prefix}/lib/kernel/install.d/
mkdir -p \
         %{buildroot}%{_unitdir} \
         %{buildroot}%{_presetdir}
sed "s|@SERVICE@|display-manager.service|" %{SOURCE6} >\
    %{buildroot}%{_unitdir}/akmods.service
install -pm 0644 %{SOURCE0} %{buildroot}%{_presetdir}/
install -pm 0755 %{SOURCE7} %{buildroot}%{_sbindir}/
install -pm 0644 %{SOURCE8} %{buildroot}%{_unitdir}/
install -pm 0644 %{SOURCE11} %{buildroot}%{_unitdir}/
%else
mkdir -p %{buildroot}%{_initddir}/
install -pm 0755 %{SOURCE4} %{buildroot}%{_initddir}/akmods
%endif

# Generate and install man pages.
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -i %{SOURCE3} -s 1 \
    -o %{buildroot}%{_mandir}/man1/akmods.1 \
       %{buildroot}%{_sbindir}/akmods
help2man -N -i %{SOURCE3} -s 1 \
    -o %{buildroot}%{_mandir}/man1/akmodsbuild.1 \
       %{buildroot}%{_sbindir}/akmodsbuild


%pre
# create group and user
getent group akmods >/dev/null || groupadd -r akmods
getent passwd akmods >/dev/null || \
useradd -r -g akmods -d /var/cache/akmods/ -s /sbin/nologin \
    -c "User is used by akmods to build akmod packages" akmods

%if 0%{?fedora} || 0%{?rhel} > 6
%post
%systemd_post akmods.service
%systemd_post akmods@.service
%systemd_post akmods-shutdown.service

%preun
%systemd_preun akmods.service
%systemd_preun akmods@.service
%systemd_preun akmods-shutdown.service

%postun
%systemd_postun akmods.service
%systemd_postun akmods@.service
%systemd_postun akmods-shutdown.service
%else
%post
if [ $1 -eq 1 ] ; then
  /sbin/chkconfig --add akmods ||:
fi

%preun
if [ $1 -eq 0 ] ; then
  /sbin/chkconfig --del akmods || :
fi
%endif


%files
%doc README
%if 0%{?rhel} > 6 || 0%{?fedora} > 20
%license LICENSE
%else
%doc LICENSE
%endif
%{_sbindir}/akmodsbuild
%{_sbindir}/akmods
%{_sbindir}/akmods-ostree-post
%{_sysconfdir}/kernel/postinst.d/akmodsposttrans
%if 0%{?fedora} || 0%{?rhel} > 6
%{_unitdir}/akmods.service
%{_unitdir}/akmods@.service
%{_sbindir}/akmods-shutdown
%{_unitdir}/akmods-shutdown.service
%{_prefix}/lib/kernel/install.d/95-akmodsposttrans.install
# akmods was enabled in the default preset by f28
%if 0%{?fedora} && 0%{?fedora} >= 28
%exclude %{_presetdir}/95-akmods.preset
%else
%{_presetdir}/95-akmods.preset
%endif
%else
%{_initddir}/akmods
%endif
%{_usrsrc}/akmods
%attr(-,akmods,akmods) %{_localstatedir}/cache/akmods
%{_mandir}/man1/*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 0.5.6-24
- Check kernel presence differently for systemd-boot machines - rhbz#1769144

* Wed Oct 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.5.6-23
- Add requires kernel-abi-whitelists for RHEL

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.5.6-21
- Add check for rhel8

* Wed May 15 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 0.5.6-20
- Fix akmodsposttrans after kernel update/install on Fedora >= 28 and 
  RHEL >= 7 - rhbz#1709055

* Thu Feb 28 2019 Alexander Larsson <alexl@redhat.com> - 0.5.6-19
- Support ostree/silverblue builds - rhbz#1667014

* Thu Feb 28 2019 Hans de Goede <hdegoede@redhat.com>
- Do not fail when the old initscripts pkg is not installed - rhbz#1680121

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.5.6-17
- Don't enforce target arch - rhbz#1644430
- Rework log file path
- Avoid using /usr/lib/modules for el6 compat

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.5.6-15
- Add inihibitor for akmods@.service
- Use restart on akmodsposttrans

* Mon Mar 26 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.5.6-14
- Switch to always retry by default
- Drop akmods preset by f28
- Don't enable service on ah
- Test a rw directory

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.5.6-12
- Update kernel posttrans method - rhbz#1518401

* Thu Aug 03 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.5.6-11
- Rework kernel-devel requires on el

* Thu Aug 03 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.5.6-10
- Enable suggests on fedora
- Add back el6 support in spec
- Add Requires elfutils-libelf-devel

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.5.6-8
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Thu May  4 2017 Hans de Goede <hdegoede@redhat.com> - 0.5.6-7
- "udevadm trigger" may have bad side-effects (rhbz#454407) instead
  look for modalias files under /sys/devices and call modprobe directly
- Fix exit status when no akmod packages are installed, so that systemd
  does not consider the akmods.service as having failed to start

* Wed May  3 2017 Hans de Goede <hdegoede@redhat.com> - 0.5.6-6
- Run "udevadm trigger" and "systemctl restart systemd-modules-load.service"
  when new kmod packages have been build and installed so that the new
  modules may be used immediately without requiring a reboot

* Mon Mar  6 2017 Hans de Goede <hdegoede@redhat.com> - 0.5.6-5
- Add LICENSE file (rhbz#1422918)

* Fri Feb 24 2017 Hans de Goede <hdegoede@redhat.com> - 0.5.6-4
- Replace %%{_prefix}/lib/systemd/system-preset with %%{_presetdir}

* Thu Feb 16 2017 Hans de Goede <hdegoede@redhat.com> - 0.5.6-3
- Submit to Fedora for package review

* Mon Nov 28 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.5.6-2
- Use Suggests kernel-devel weak-dependency - see rfbz#3386

* Fri Oct 14 2016 Richard Shaw <hobbes1069@gmail.com> - 0.5.6-1
- Disable shutdown systemd service file by default.
- Remove modprobe line from main service file.

* Wed Aug 17 2016 Sérgio Basto <sergio@serjux.com> - 0.5.4-3
- New release

* Sun Jan 03 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.5.4-2
- Revert conflicts kernel-debug-devel

* Thu Jul 23 2015 Richard Shaw <hobbes1069@gmail.com> - 0.5.4-1
- Do not mark a build as failed when only installing the RPM fails.
- Run akmods-shutdown script instead of akmods on shutdown.
- Add systemd preset file to enable services by default.

* Wed Jul 15 2015 Richard Shaw <hobbes1069@gmail.com> - 0.5.3-2
- Add package conflicts to stop pulling in kernel-debug-devel, fixes BZ#3386.
- Add description for the formatting of the <kernel> parameter, BZ#3580.
- Update static man pages and clean them up.
- Fixed another instance of TMPDIR causing issues.
- Added detection of dnf vs yum to akmods, fixed BZ#3481.

* Wed Apr  1 2015 Richard Shaw <hobbes1069@gmail.com> - 0.5.2-1
- Fix temporary directory creation when TMPDIR environment variable is set,
  fixes BZ#2596.
- Update systemd scripts to use macros.
- Fix akmods run on shutdown systemd unit file, fixes BZ#3503.

* Sun Nov 16 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-4
- Fix akmods on armhfp - rfbz#3117
- Use yum instead of rpm to install packages - rfbz#3350
  Switch to a better date format

* Fri Jan 11 2013 Richard Shaw <hobbes1069@gmail.com> - 0.5.1-3
- Really fix akmods.service.in.

* Fri Jun 01 2012 Richard Shaw <hobbes1069@gmail.com> - 0.5.1-2
- Add service file to run again on shutdown.
- Add conditional for Fedora 18 to specify correct systemd graphical service.

* Thu Apr 12 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.4.0-4
- Rebuilt

* Tue Mar 20 2012 Richard Shaw <hobbes1069@gmail.com> - 0.4.0-3
- Add additional error output if the needed kernel development files are not
  installed. (Fixes #561)

* Mon Mar 05 2012 Richard Shaw <hobbes1069@gmail.com> - 0.4.0-2
- Remove remaining references to previous Fedora releases
- Remove legacy SysV init script from CVS.
- Added man page for akmods and cleaned up man page for akmodsbuild.

* Tue Feb 07 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.4.0-1
- Update for UsrMove support
- Remove unused references to older fedora
- Change Requires from kernel-devel to kernel-devel-uname-r
