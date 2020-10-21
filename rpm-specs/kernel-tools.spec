# Much of this is borrowed from the original kernel.spec
# It needs a bunch of the macros for rawhide vs. not-rawhide builds.

# this should go away soon
%define _legacy_common_support 1

# For a stable, released kernel, released_kernel should be 1. For rawhide
# and/or a kernel built from an rc or git snapshot, released_kernel should
# be 0.
%global released_kernel 1
%global baserelease 1
%global fedora_build %{baserelease}

# base_sublevel is the kernel version we're starting with and patching
# on top of -- for example, 3.1-rc7-git1 starts with a 3.0 base,
# which yields a base_sublevel of 0.
%global base_sublevel 9

## If this is a released kernel ##
%if 0%{?released_kernel}

# Do we have a -stable update to apply?
%global stable_update 0
# Set rpm version accordingly
%if 0%{?stable_update}
%global stablerev %{stable_update}
%global stable_base %{stable_update}
%endif
%global rpmversion 5.%{base_sublevel}.%{stable_update}

## The not-released-kernel case ##
%else
# The next upstream release sublevel (base_sublevel+1)
%global upstream_sublevel %(echo $((%{base_sublevel} + 1)))

# The rc snapshot level
%global rcrev 0
# Set rpm version accordingly
%global rpmversion 5.%{upstream_sublevel}.0
%endif
# Nb: The above rcrev values automagically define Patch00 and Patch01 below.

# pkg_release is what we'll fill in for the rpm Release: field
%if 0%{?released_kernel}

%global pkg_release %{fedora_build}%{?buildid}%{?dist}

%else

# non-released_kernel
%if 0%{?rcrev}
%global rctag .rc%rcrev
%else
%global rctag .rc0
%endif
%global gittag .git0
%global pkg_release 0%{?rctag}%{?gittag}.%{fedora_build}%{?buildid}%{?dist}

%endif

# The kernel tarball/base version
%global kversion 5.%{base_sublevel}
%global KVERREL %{version}-%{release}.%{_target_cpu}

# perf needs this
%undefine _strict_symbol_defs_build

BuildRequires: kmod, patch, bash, tar, git-core
BuildRequires: bzip2, xz, findutils, gzip, m4, perl-interpreter, perl(Carp), perl-devel, perl-generators, make, diffutils, gawk
BuildRequires: gcc, binutils, redhat-rpm-config, hmaccalc
BuildRequires: net-tools, hostname, bc, elfutils-devel
BuildRequires: zlib-devel binutils-devel newt-devel python3-docutils perl(ExtUtils::Embed) bison flex xz-devel
BuildRequires: audit-libs-devel glibc-devel glibc-headers glibc-static python3-devel java-devel
BuildRequires: asciidoc xmlto libcap-devel
BuildRequires: opencsd-devel
# Used to mangle unversioned shebangs to be Python 3
BuildRequires: /usr/bin/pathfix.py
%ifnarch s390x %{arm}
BuildRequires: numactl-devel
%endif
BuildRequires: pciutils-devel gettext ncurses-devel
BuildConflicts: rhbuildsys(DiskFree) < 500Mb
BuildRequires: rpm-build, elfutils
%{?systemd_requires}
BuildRequires: systemd

Source0: https://www.kernel.org/pub/linux/kernel/v5.x/linux-%{kversion}.tar.xz

# Sources for kernel-tools
Source2000: cpupower.service
Source2001: cpupower.config

# Here should be only the patches up to the upstream canonical Linus tree.

# For a stable release kernel
%if 0%{?stable_base}
Source5000: patch-5.%{base_sublevel}.%{stable_base}.xz
%else
# non-released_kernel case
# These are automagically defined by the rcrev value set up
# near the top of this spec file.
%if 0%{?rcrev}
Source5000: patch-5.%{upstream_sublevel}-rc%{rcrev}.xz
%endif
%endif

# ongoing complaint, full discussion delayed until ksummit/plumbers
Patch0: 0001-iio-Use-event-header-from-kernel-tree.patch
Patch1: 0001-Filter-lto-options-from-the-perl-ccopts.patch

#Revert this
Patch2: 0001-tools-libbpf-Avoid-counting-local-symbols-in-ABI-che.patch

# rpmlint cleanup
Patch6: 0002-perf-Don-t-make-sourced-script-executable.patch

Name: kernel-tools
Summary: Assortment of tools for the Linux kernel
License: GPLv2
URL: http://www.kernel.org/
Version: %{rpmversion}
Release: %{pkg_release}
Provides:  cpupowerutils = 1:009-0.6.p1
Obsoletes: cpupowerutils < 1:009-0.6.p1
Provides:  cpufreq-utils = 1:009-0.6.p1
Provides:  cpufrequtils = 1:009-0.6.p1
Obsoletes: cpufreq-utils < 1:009-0.6.p1
Obsoletes: cpufrequtils < 1:009-0.6.p1
Obsoletes: cpuspeed < 1:1.5-16
Requires: kernel-tools-libs = %{version}-%{release}
%description -n kernel-tools
This package contains the tools/ directory from the kernel source
and the supporting documentation.


%package -n perf
Summary: Performance monitoring for the Linux kernel
Requires: bzip2
License: GPLv2
%description -n perf
This package contains the perf tool, which enables performance monitoring
of the Linux kernel.

%global pythonperfsum Python bindings for apps which will manipulate perf events
%global pythonperfdesc A Python module that permits applications \
written in the Python programming language to use the interface \
to manipulate perf events.

%package -n python3-perf
Summary: %{pythonperfsum}
%{?python_provide:%python_provide python3-perf}
%description -n python3-perf
%{pythonperfdesc}

%package -n kernel-tools-libs
Summary: Libraries for the kernels-tools
License: GPLv2
%description -n kernel-tools-libs
This package contains the libraries built from the tools/ directory
from the kernel source.

%package -n kernel-tools-libs-devel
Summary: Assortment of tools for the Linux kernel
License: GPLv2
Requires: kernel-tools = %{version}-%{release}
Provides:  cpupowerutils-devel = 1:009-0.6.p1
Obsoletes: cpupowerutils-devel < 1:009-0.6.p1
Requires: kernel-tools-libs = %{version}-%{release}
Provides: kernel-tools-devel
%description -n kernel-tools-libs-devel
This package contains the development files for the tools/ directory from
the kernel source.

%package -n bpftool
Summary: Inspection and simple manipulation of eBPF programs and maps
License: GPLv2
%description -n bpftool
This package contains the bpftool, which allows inspection and simple
manipulation of eBPF programs and maps.

%package -n libbpf
Summary: The bpf library from kernel source
License: GPLv2
%description -n libbpf
This package contains the kernel source bpf library.

%package -n libbpf-devel
Summary: Developement files for the bpf library from kernel source
License: GPLv2
%description -n libbpf-devel
This package includes libraries and header files needed for development
of applications which use bpf library from kernel source.

%package -n libperf
Summary: The perf library from kernel source
License: GPLv2
%description -n libperf
This package contains the kernel source perf library.

%package -n libperf-devel
Summary: Developement files for the perf library from kernel source
License: GPLv2
%description -n libperf-devel
This package includes libraries and header files needed for development
of applications which use perf library from kernel source.

%prep
%setup -q -n kernel-%{kversion}%{?dist} -c

cd linux-%{kversion}

# This is for patching either an -rc or stable
%if 0%{?rcrev}
    xzcat %{SOURCE5000} | patch -p1 -F1 -s
%endif

%if 0%{?stable_base}
    xzcat %{SOURCE5000} | patch -p1 -F1 -s
%endif

%patch0 -p1
%patch1 -p1
%patch2 -p1 -R
%patch6 -p1

# END OF PATCH APPLICATIONS

# Mangle /usr/bin/python shebangs to /usr/bin/python3
# -p preserves timestamps
# -n prevents creating ~backup files
# -i specifies the interpreter for the shebang
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" tools/ tools/perf/scripts/python/*.py scripts/gen_compile_commands.py

###
### build
###
%build
# The kernel tools build with -ggdb3 which seems to interact badly with LTO
# causing various errors with references to discarded sections and symbol
# type errors from the LTO plugin.  Until those issues are addressed
# disable LTO
%define _lto_cflags %{nil}

cd linux-%{kversion}

%global perf_make \
  make EXTRA_CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" %{?cross_opts} V=1 NO_PERF_READ_VDSO32=1 NO_PERF_READ_VDSOX32=1 WERROR=0 NO_LIBUNWIND=1 HAVE_CPLUS_DEMANGLE=1 NO_GTK2=1 NO_STRLCPY=1 NO_BIONIC=1 CORESIGHT=1 prefix=%{_prefix}
%global perf_python3 -C tools/perf PYTHON=%{__python3}
# perf
# make sure check-headers.sh is executable
chmod +x tools/perf/check-headers.sh
%{perf_make} %{perf_python3} all

%global tools_make \
  make CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" HOSTCFLAGS="%{?build_hostcflags}" HOSTLDFLAGS="%{?build_hostldflags}" V=1

# cpupower
# make sure version-gen.sh is executable.
chmod +x tools/power/cpupower/utils/version-gen.sh
%{tools_make} %{?_smp_mflags} -C tools/power/cpupower CPUFREQ_BENCH=false
%ifarch %{ix86}
    pushd tools/power/cpupower/debug/i386
    %{tools_make} %{?_smp_mflags} centrino-decode powernow-k8-decode
    popd
%endif
%ifarch x86_64
    pushd tools/power/cpupower/debug/x86_64
    %{tools_make} %{?_smp_mflags} centrino-decode powernow-k8-decode
    popd
%endif
%ifarch %{ix86} x86_64
   pushd tools/power/x86/x86_energy_perf_policy/
   %{tools_make}
   popd
   pushd tools/power/x86/turbostat
   %{tools_make}
   popd
%endif #turbostat/x86_energy_perf_policy
pushd tools/thermal/tmon/
%{tools_make}
popd
pushd tools/iio/
%{tools_make}
popd
pushd tools/gpio/
%{tools_make}
popd

%global bpftool_make \
  make EXTRA_CFLAGS="${RPM_OPT_FLAGS}" EXTRA_LDFLAGS="%{__global_ldflags}" DESTDIR=$RPM_BUILD_ROOT V=1

pushd tools/bpf/bpftool
%{bpftool_make}
popd
pushd tools/lib/bpf
%{tools_make} V=1
popd
pushd tools/lib/perf
make V=1
popd

# Build the docs
pushd tools/kvm/kvm_stat/
%make_build man
popd
pushd tools/perf/Documentation/
%make_build man
popd

###
### install
###

%install

cd linux-%{kversion}

# perf tool binary and supporting scripts/binaries
%{perf_make} %{perf_python3} DESTDIR=%{buildroot} lib=%{_lib} install-bin install-traceevent-plugins
# remove the 'trace' symlink.
rm -f %{buildroot}%{_bindir}/trace

# For both of the below, yes, this should be using a macro but right now
# it's hard coded and we don't actually want it anyway right now.
# Whoever wants examples can fix it up!

# remove examples
rm -rf %{buildroot}/usr/lib/perf/examples
# remove the stray header file that somehow got packaged in examples
rm -rf %{buildroot}/usr/lib/perf/include/bpf/

# python-perf extension
%{perf_make} %{perf_python3} DESTDIR=%{buildroot} install-python_ext

# perf man pages (note: implicit rpm magic compresses them later)
install -d %{buildroot}/%{_mandir}/man1
install -pm0644 tools/kvm/kvm_stat/kvm_stat.1 %{buildroot}/%{_mandir}/man1/
install -pm0644 tools/perf/Documentation/*.1 %{buildroot}/%{_mandir}/man1/

make -C tools/power/cpupower DESTDIR=%{buildroot} libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false install
rm -f %{buildroot}%{_libdir}/*.{a,la}
%find_lang cpupower
mv cpupower.lang ../
%ifarch %{ix86}
    pushd tools/power/cpupower/debug/i386
    install -m755 centrino-decode %{buildroot}%{_bindir}/centrino-decode
    install -m755 powernow-k8-decode %{buildroot}%{_bindir}/powernow-k8-decode
    popd
%endif
%ifarch x86_64
    pushd tools/power/cpupower/debug/x86_64
    install -m755 centrino-decode %{buildroot}%{_bindir}/centrino-decode
    install -m755 powernow-k8-decode %{buildroot}%{_bindir}/powernow-k8-decode
    popd
%endif
chmod 0755 %{buildroot}%{_libdir}/libcpupower.so*
mkdir -p %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sysconfig
install -m644 %{SOURCE2000} %{buildroot}%{_unitdir}/cpupower.service
install -m644 %{SOURCE2001} %{buildroot}%{_sysconfdir}/sysconfig/cpupower
%ifarch %{ix86} x86_64
   mkdir -p %{buildroot}%{_mandir}/man8
   pushd tools/power/x86/x86_energy_perf_policy
   %{tools_make} DESTDIR=%{buildroot} install
   popd
   pushd tools/power/x86/turbostat
   %{tools_make} DESTDIR=%{buildroot} install
   popd
%endif #turbostat/x86_energy_perf_policy
pushd tools/thermal/tmon
%{tools_make} INSTALL_ROOT=%{buildroot} install
popd
pushd tools/iio
%{tools_make} DESTDIR=%{buildroot} install
popd
pushd tools/gpio
%{tools_make} DESTDIR=%{buildroot} install
popd
pushd tools/kvm/kvm_stat
%{tools_make} INSTALL_ROOT=%{buildroot} install-tools
popd
pushd tools/bpf/bpftool
%{bpftool_make} prefix=%{_prefix} bash_compdir=%{_sysconfdir}/bash_completion.d/ mandir=%{_mandir} install doc-install
# man-pages packages this (rhbz #1686954)
rm %{buildroot}%{_mandir}/man7/bpf-helpers.7
popd
pushd tools/lib/bpf
%{tools_make} DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} V=1 install install_headers
popd
pushd tools/lib/perf
make DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} V=1 install install_headers
popd

###
### scripts
###

%ldconfig_scriptlets -n kernel-tools-libs

%post -n kernel-tools
%systemd_post cpupower.service

%preun -n kernel-tools
%systemd_preun cpupower.service

%postun
%systemd_postun cpupower.service

%files -n perf
%{_bindir}/perf
%dir %{_libdir}/traceevent
%{_libdir}/traceevent/plugins/
%{_libdir}/libperf-jvmti.so
%{_libexecdir}/perf-core
%{_datadir}/perf-core/
%{_mandir}/man[1-8]/perf*
%{_sysconfdir}/bash_completion.d/perf
%doc linux-%{kversion}/tools/perf/Documentation/examples.txt
%license linux-%{kversion}/COPYING
%{_docdir}/perf-tip/tips.txt

%files -n python3-perf
%license linux-%{kversion}/COPYING
%{python3_sitearch}/*

%files -n kernel-tools -f cpupower.lang
%{_bindir}/cpupower
%{_datadir}/bash-completion/completions/cpupower
%ifarch %{ix86} x86_64
%{_bindir}/centrino-decode
%{_bindir}/powernow-k8-decode
%endif
%{_unitdir}/cpupower.service
%{_mandir}/man[1-8]/cpupower*
%config(noreplace) %{_sysconfdir}/sysconfig/cpupower
%ifarch %{ix86} x86_64
%{_bindir}/x86_energy_perf_policy
%{_mandir}/man8/x86_energy_perf_policy*
%{_bindir}/turbostat
%{_mandir}/man8/turbostat*
%endif
%{_bindir}/tmon
%{_bindir}/iio_event_monitor
%{_bindir}/iio_generic_buffer
%{_bindir}/lsiio
%{_bindir}/lsgpio
%{_bindir}/gpio-hammer
%{_bindir}/gpio-event-mon
%{_bindir}/gpio-watch
%{_mandir}/man1/kvm_stat*
%{_bindir}/kvm_stat
%license linux-%{kversion}/COPYING

%files -n kernel-tools-libs
%{_libdir}/libcpupower.so.0
%{_libdir}/libcpupower.so.0.0.1
%license linux-%{kversion}/COPYING

%files -n kernel-tools-libs-devel
%{_libdir}/libcpupower.so
%{_includedir}/cpufreq.h
%{_includedir}/cpuidle.h

%files -n bpftool
%{_sbindir}/bpftool
%{_sysconfdir}/bash_completion.d/bpftool
%{_mandir}/man8/bpftool-btf.8.gz
%{_mandir}/man8/bpftool-cgroup.8.gz
%{_mandir}/man8/bpftool-gen.8.gz
%{_mandir}/man8/bpftool-iter.8.gz
%{_mandir}/man8/bpftool-link.8.gz
%{_mandir}/man8/bpftool-map.8.gz
%{_mandir}/man8/bpftool-net.8.gz
%{_mandir}/man8/bpftool-prog.8.gz
%{_mandir}/man8/bpftool-perf.8.gz
%{_mandir}/man8/bpftool-struct_ops.8.gz
%{_mandir}/man8/bpftool-feature.8.gz
%{_mandir}/man8/bpftool.8.gz
%license linux-%{kversion}/COPYING

%files -n libbpf
%{_libdir}/libbpf.so.0
%{_libdir}/libbpf.so.0.1.0
%license linux-%{kversion}/COPYING

%files -n libbpf-devel
%{_libdir}/libbpf.a
%{_libdir}/libbpf.so
%{_libdir}/pkgconfig/libbpf.pc
%{_includedir}/bpf/bpf.h
%{_includedir}/bpf/bpf_core_read.h
%{_includedir}/bpf/bpf_endian.h
%{_includedir}/bpf/bpf_helper_defs.h
%{_includedir}/bpf/bpf_helpers.h
%{_includedir}/bpf/bpf_tracing.h
%{_includedir}/bpf/btf.h
%{_includedir}/bpf/libbpf.h
%{_includedir}/bpf/libbpf_common.h
%{_includedir}/bpf/libbpf_util.h
%{_includedir}/bpf/xsk.h
%license linux-%{kversion}/COPYING

%files -n libperf
%{_libdir}/libperf.so.0
%{_libdir}/libperf.so.0.0.1
%license linux-%{kversion}/COPYING

%files -n libperf-devel
%{_libdir}/libperf.a
%{_libdir}/libperf.so
%{_libdir}/pkgconfig/libperf.pc
%{_includedir}/perf/core.h
%{_includedir}/perf/cpumap.h
%{_includedir}/perf/event.h
%{_includedir}/perf/evlist.h
%{_includedir}/perf/evsel.h
%{_includedir}/perf/mmap.h
%{_includedir}/perf/threadmap.h
%{_mandir}/man3/libperf.3.gz
%{_mandir}/man7/libperf-counting.7.gz
%{_mandir}/man7/libperf-sampling.7.gz
%{_docdir}/libperf/examples/sampling.c
%{_docdir}/libperf/examples/counting.c
%{_docdir}/libperf/html/libperf.html
%{_docdir}/libperf/html/libperf-counting.html
%{_docdir}/libperf/html/libperf-sampling.html
%license linux-%{kversion}/COPYING

%changelog
* Mon Oct 12 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-1
- Linux v5.9.0

* Mon Oct  5 14:55:47 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc8.git0.1
- Linux v5.9-rc8

* Mon Sep 28 16:49:41 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc7.git0.1
- Linux v5.9-rc7

* Mon Sep 21 10:05:53 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc6.git0.1
- Linux v5.9-rc6

* Tue Sep 15 08:33:45 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc5.git0.1
- Linux v5.9-rc5

* Thu Sep 10 11:29:45 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc4.git0.1
- Linux v5.9-rc4

* Mon Aug 31 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc3.git0.1
- Linux v5.9-rc3

* Tue Aug 25 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc2.git0.1
- Linux v5.9-rc2

* Mon Aug 17 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc1.git0.1
- Linux v5.9-rc1

* Mon Aug 03 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-1
- Linux v5.8.0

* Mon Jul 27 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc7.git0.1
- Linux v5.8-rc7

* Tue Jul 21 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc6.git0.1
- Linux v5.8-rc6

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 5.8.0-0.rc5.git0.2
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Mon Jul 13 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc5.git0.1
- Linux v5.8-rc5

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 5.8.0-0.rc4.git0.3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jul 08 2020 Jeff Law <law@redhat.com> - 5.8.0-0.rc4.git0.2
- Disable LTO

* Mon Jul 06 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc4.git0.1
- Linux v5.8-rc4

* Mon Jun 29 2020 Luis Claudio R. Goncalves <lclaudio@uudg.org> - 5.8.0-0.rc3.git0.1
- Linux v5.8-rc3

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.8.0-0.rc2.git0.2
- Perl 5.32 rebuild

* Mon Jun 22 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc2.git0.1
- Linux v5.8-rc2

* Sun Jun 14 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc1.git0.1
- Linux v5.8-rc1

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 5.7.0-0.rc7.git0.2
- Rebuilt for Python 3.9

* Mon May 25 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.7.0-0.rc7.git0.1
- Linux v5.7-rc7

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 5.7.0-0.rc5.git0.2
- Rebuilt for Python 3.9

* Mon May 11 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.7.0-0.rc5.git0.1
- Linux v5.7-rc5

* Wed May 06 2020  Justin M. Forbes <jforbes@fedoraproject.org> - 5.7.0-rc4
- Linux v5.7-rc4

* Sun Apr 26 2020 Justin Forbes <jforbes@fedoraproject.org> - 5.7.0-0.rc3.git0.1
- Linux v5.7-rc3

* Tue Apr 14 2020 Michael Petlan <mpetlan@redhat.com> - 5.6.0-0.rc7.git0.2
- Add libperf, libperf-devel and libperf-debuginfo packages

* Wed Apr 08 2020 Justin Forbes <jforbes@fedoraproject.org>
- Remove manual perf-debuginfo left from kernel (rhbz 1822110)

* Mon Mar 30 2020 Justin Forbes <jforbes@fedoraproject.org>
- Add BuildRequires of libcap-devel for turbostat changes
- Linux v5.6

* Mon Mar 23 2020 Peter Robinson <pbrobinson@fedoraproject.org> 5.6.0-0.rc7.git0.1
- Linux v5.6-rc7

* Tue Mar 17 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc6.git0.1
- Linux v5.6-rc6

* Thu Mar 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> 5.6.0-0.rc5.git0.1
- Linux v5.6-rc5

* Mon Mar 02 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc4.git0.1
- Linux v5.6-rc4

* Wed Feb 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> 5.6.0-0.rc3.git0.1
- Linux v5.6-rc3

* Mon Feb 17 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc2.git0.1
- Linux v5.6-rc2

* Fri Feb 14 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc1.git0.1
- Linux v5.6-rc1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-1
- Linux v5.5

* Mon Jan 20 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-0.rc7.git0.1
- Linux v5.5-rc7

* Mon Jan 13 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-0.rc6.git0.1
- Linux v5.5-rc6

* Mon Jan 06 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-0.rc5.git0.1
- Linux v5.5-rc5

* Mon Dec 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> - 5.5.0-0.rc4.git0.1
- Linux v5.5-rc4

* Mon Dec 23 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-0.rc3.git0.1
- Linux v5.5-rc3

* Mon Dec 16 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-0.rc2.git0.1
- Linux v5.5-rc2

* Thu Dec 05 2019 Laura Abbott <labbott@redhat.com> - 5.4.0-2
- Bump and build for small fixes

* Wed Dec 04 2019 Jeremy Cline <jcline@redhat.com> - 5.4.0-1
- Linux v5.4

* Mon Nov 04 2019 Jeremy Cline <jcline@redhat.com> - 5.4.0-0.rc6.git0.1
- Linux v5.4-rc6

* Mon Oct 28 2019 Jeremy Cline <jcline@redhat.com> - 5.4.0-0.rc5.git0.1
- Linux v5.4-rc5

* Thu Oct 03 2019 Jeremy Cline <jcline@redhat.com> - 5.4.0-0.rc1.git0.1
- Linux v5.4-rc1

* Mon Sep 16 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-1
- Linux v5.3.0

* Tue Sep 10 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc8.git0.1
- Linux v5.3-rc8.git0

* Tue Sep 03 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc7.git0.1
- Linux v5.3-rc7.git0

* Mon Aug 26 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc6.git0.1
- Linux v5.3-rc6.git0

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 5.3.0-0.rc5.git0.2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc5.git0.1
- Linux v5.3-rc5.git0

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 5.3.0-0.rc4.git0.2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc4.git0.1
- Linux v5.3-rc4.git0

* Mon Aug 05 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc3.git0.1
- Linux v5.3-rc3.git0

* Mon Jul 29 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc2.git0.1
- Linux v5.3-rc2.git0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-0.rc1.git0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc1.git0.1
- Linux v5.3-rc1.git0

* Mon Jul 08 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-1
- Linux v5.2.0

* Mon Jul 01 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc7.git0.1
- Linux v5.2-rc7.git0

* Mon Jun 24 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc6.git0.1
- Linux v5.2-rc6.git0

* Mon Jun 17 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc5.git0.1
- Linux v5.2-rc5.git0

* Mon Jun 10 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc4.git0.1
- Linux v5.2-rc4.git0

* Tue Jun 04 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.2.0-0.rc3.git0.3
- Perl 5.30 re-rebuild updated packages

* Mon Jun 03 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc3.git0.1
- Linux v5.2-rc3.git0

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.2.0-0.rc2.git0.2
- Perl 5.30 rebuild

* Mon May 27 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-rc2.git0.1
- Linux v5.2-rc2.git0

* Mon May 20 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-rc1.git0.1
- Linux v5.2-rc1.git0

* Mon May 06 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-1
- Linux v5.1

* Mon Apr 29 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc7.git0.1
- Linux v5.1-rc7

* Mon Apr 22 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc6.git0.1
- Linux v5.1-rc6

* Tue Apr 16 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc5.git0.1
- Linux v5.1-rc5

* Mon Apr 08 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc4.git0.1
- Linux v5.1-rc4

* Tue Apr 02 2019 Jiri Olsa <jolsa@redhat.com> - 5.1.0-0.rc3.git0.2
- Add libbpf, libbpf-devel and libbpf-debuginfo packages

* Mon Apr 01 2019 Jeremy Cline <jeremy@jcline.org> - 5.1.0-0.rc3.git0.1
- Linux v5.1-rc3

* Mon Mar 18 2019 Jeremy Cline <jeremy@jcline.org> - 5.1.0-0.rc2.git0.1
- Linux v5.1-rc2

* Mon Mar 18 2019 Jeremy Cline <jeremy@jcline.org> - 5.1.0-0.rc1.git0.1
- Linux v5.1-rc1

* Mon Mar 04 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-1
- Linux v5.0.0

* Mon Feb 25 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc8.git0.1
- Linux v5.0-rc8

* Sun Feb 17 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc7.git0.1
- Linux v5.0-rc7

* Mon Feb 11 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc6.git0.1
- Linux v5.0-rc6

* Mon Feb 04 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc5.git0.1
- Linux v5.0-rc5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.rc4.git0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc4.git0.1
- Linux v5.0-rc4

* Fri Jan 25 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc3.git0.2
- Rebuild for gcc9

* Mon Jan 14 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc3.git0.1
- Linux v5.0-rc3

* Mon Jan 14 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc2.git0.1
- Linux v5.0-rc2

* Thu Jan 10 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-0.rc1.git0.2
- Remove Python 2 subpackage

* Mon Jan 07 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc1.git0.1
- Linux v5.0-rc1

* Mon Dec 24 2018 Justin M. Forbes <jforbes@fedoraproject.org> - 4.20.0-1
- Linux v4.20.0

* Mon Dec 17 2018 Justin M. Forbes <jforbes@fedoraproject.org> - 4.20.0-0.rc7.git0.1
- Linux v4.20-rc7

* Mon Dec 10 2018 Justin M. Forbes <jforbes@fedoraproject.org> - 4.20.0-0.rc6.git0.1
- Linux v4.20-rc6

* Mon Dec 03 2018 Justin M. Forbes <jforbes@fedoraproject.org> - 4.20.0-0.rc5.git0.1
- Linux v4.20-rc5

* Mon Nov 26 2018 Justin M. Forbes <jforbes@fedoraproject.org> - 4.20.0-0.rc4.git0.1
- Linux v4.20-rc4

* Mon Nov 19 2018 Jeremy Cline <jeremy@jcline.org> - 4.20.0-0.rc3.git0.1
- Linux v4.20-rc3

* Sun Nov 11 2018 Justin M. Forbes <jforbes@fedoraproject.org> - 4.20.0-0.rc2.git0.1
- Linux v4.20-rc2

* Mon Nov 05 2018 Justin M. Forbes <jforbes@fedoraproject.org> - 4.20.0-0.rc1.git0.1
- Linux v4.20-rc1
