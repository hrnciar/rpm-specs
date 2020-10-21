%global tftpboot_dir %{_sharedstatedir}/tftpboot/

%global commit0 c46abca11dca886411fc95802a2cbaa66fdb691b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           cobbler
Version:        3.1.2
Release:        4%{?dist}
Summary:        Boot server configurator
URL:            https://cobbler.github.io/
License:        GPLv2+
Source0:        https://github.com/cobbler/cobbler/archive/v%{version}/%{name}-%{version}.tar.gz
#Source0:        https://github.com/cobbler/cobbler/archive/%{commit0}/%{name}-%{commit0}.tar.gz
# Revert upstream's VirtualHost addition
# https://github.com/cobbler/cobbler/issues/2286
Patch0:         cobbler-httpd.patch
BuildArch:      noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-cheetah
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires: %{py3_dist coverage}
%else
BuildRequires: python%{python3_pkgversion}-coverage
%endif
BuildRequires: python%{python3_pkgversion}-distro
BuildRequires: python%{python3_pkgversion}-future
BuildRequires: python%{python3_pkgversion}-netaddr
BuildRequires: python%{python3_pkgversion}-PyYAML
BuildRequires: python%{python3_pkgversion}-requests
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-simplejson
# For docs
BuildRequires: python%{python3_pkgversion}-sphinx

Requires: httpd
Requires: tftp-server
Requires: createrepo_c
Requires: file
Requires: rsync
Requires: xorriso
Requires: python%{python3_pkgversion}-cheetah
Requires: python%{python3_pkgversion}-distro
Requires: python%{python3_pkgversion}-dns
Requires: python%{python3_pkgversion}-future
Requires: python%{python3_pkgversion}-mod_wsgi
Requires: python%{python3_pkgversion}-netaddr
Requires: python%{python3_pkgversion}-PyYAML
Requires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-simplejson
Requires: python%{python3_pkgversion}-tornado

Requires: genisoimage
%if 0%{?fedora} || 0%{?rhel} >= 8
# Not everyone wants bash-completion...?
Recommends: bash-completion
Requires: dnf-plugins-core
# syslinux is only available on x86
Requires: (syslinux if (filesystem.x86_64 or filesystem.i686))
# grub2 efi stuff is only available on x86
Recommends: grub2-efi-ia32
Recommends: grub2-efi-x64
Recommends: logrotate
%else
Requires: yum-utils
%endif
# https://github.com/cobbler/cobbler/issues/1685
Requires: /sbin/service

BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Cobbler is a network install server.  Cobbler supports PXE, ISO
virtualized installs, and re-installing existing Linux machines.
The last two modes use a helper tool, 'koan', that integrates with
cobbler.  There is also a web interface 'cobbler-web'.  Cobbler's
advanced features include importing distributions from DVDs and rsync
mirrors, kickstart templating, integrated yum mirroring, and built-in
DHCP/DNS Management.  Cobbler has a XML-RPC API for integration with
other applications.


%package -n cobbler-web
Summary:        Web interface for Cobbler
Requires:       cobbler = %{version}-%{release}
Requires:       python%{python3_pkgversion}-django
Requires:       python%{python3_pkgversion}-mod_wsgi
Requires:       mod_ssl
Requires(post): coreutils
Requires(post): sed

%description -n cobbler-web
Web interface for Cobbler that allows visiting
http://server/cobbler_web to configure the install server.


%prep
%autosetup -p1

%build
%py3_build

%install
# bypass install errors ( don't chown in install step)
%py3_install ||:

# cobbler
rm %{buildroot}%{_sysconfdir}/cobbler/cobbler.conf

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mv %{buildroot}%{_sysconfdir}/cobbler/cobblerd_rotate %{buildroot}%{_sysconfdir}/logrotate.d/cobblerd

# Create data directories in tftpboot_dir
mkdir -p %{buildroot}%{tftpboot_dir}/{boot,etc,grub/system{,_link},images{,2},ppc,pxelinux.cfg,s390x}

# systemd
mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_sysconfdir}/cobbler/cobblerd.service %{buildroot}%{_unitdir}

# cobbler-web
rm %{buildroot}%{_sysconfdir}/cobbler/cobbler_web.conf


%pre
if [ $1 -ge 2 ]; then
    # package upgrade: backup configuration
    DATE=$(date "+%%Y%%m%%d-%%H%%M%%S")
    if [ ! -d "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}" ]; then
        mkdir -p "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
    fi
    for i in "config" "snippets" "templates" "triggers" "scripts"; do
        if [ -d "%{_sharedstatedir}/cobbler/${i}" ]; then
            cp -r "%{_sharedstatedir}/cobbler/${i}" "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
        fi
    done
    if [ -d %{_sysconfdir}/cobbler ]; then
        cp -r %{_sysconfdir}/cobbler "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
    fi
fi

%post
%systemd_post cobblerd.service

%preun
%systemd_preun cobblerd.service

%postun
%systemd_postun_with_restart cobblerd.service

%post -n cobbler-web
# Change the SECRET_KEY option in the Django settings.py file
# required for security reasons, should be unique on all systems
# Choose from letters and numbers only, so no special chars like ampersand (&).
RAND_SECRET=$(head /dev/urandom | tr -dc 'A-Za-z0-9!' | head -c 50 ; echo '')
sed -i -e "s/SECRET_KEY = ''/SECRET_KEY = \'$RAND_SECRET\'/" %{_datadir}/cobbler/web/settings.py


%files
%license COPYING
%doc AUTHORS.in README.md
%doc docs/developer-guide.rst docs/quickstart-guide.rst docs/installation-guide.rst
%config(noreplace) %{_sysconfdir}/cobbler
%config(noreplace) %{_sysconfdir}/logrotate.d/cobblerd
%config(noreplace) /etc/httpd/conf.d/cobbler.conf
%{_bindir}/cobbler
%{_bindir}/cobbler-ext-nodes
%{_bindir}/cobblerd
%{_sbindir}/fence_ipmitool
%{_sbindir}/tftpd.py
%{_datadir}/bash-completion/
%dir %{_datadir}/cobbler
%{_datadir}/cobbler/bin
%{_mandir}/man1/cobbler.1*
%{_mandir}/man5/cobbler.conf.5*
%{_mandir}/man8/cobblerd.8*
%{python3_sitelib}/cobbler/
%{python3_sitelib}/cobbler*.egg-info
%{_unitdir}/cobblerd.service
%{tftpboot_dir}/*
/var/www/cobbler
%config(noreplace) %{_sharedstatedir}/cobbler
%exclude %{_sharedstatedir}/cobbler/webui_sessions
/var/log/cobbler

%files -n cobbler-web
%license COPYING
%doc AUTHORS.in README.md
%config(noreplace) /etc/httpd/conf.d/cobbler_web.conf
%attr(-,apache,apache) %{_datadir}/cobbler/web
%dir %attr(700,apache,root) %{_sharedstatedir}/cobbler/webui_sessions
%attr(-,apache,apache) /var/www/cobbler_webui_content/


%changelog
* Thu Sep 17 2020 Orion Poplawski <orion@nwra.com> - 3.1.2-4
- Add requires on python-distro and file

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Orion Poplawski <orion@nwra.com> - 3.1.2-2
- Fix apache configuration

* Fri May 29 2020 Orion Poplawski <orion@nwra.com> - 3.1.2-1
- Update to 3.1.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-4
- Rebuilt for Python 3.9

* Fri Feb 21 2020 Orion Poplawski <orion@nwra.com> - 3.1.1-3
- Add requires for python3-dns

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Orion Poplawski <orion@nwra.com> - 3.1.1-1
- Update to 3.1.1

* Tue Oct 22 2019 Orion Poplawski <orion@nwra.com> - 3.0.1-4
- Drop koan completely, including obsoletes.  It is a separate package now.

* Thu Oct 10 2019 Orion Poplawski <orion@nwra.com> - 3.0.1-3
- Require /sbin/service

* Tue Oct  8 2019 Orion Poplawski <orion@nwra.com> - 3.0.1-2
- Fix requires (requests instead of urlgrabber)
- Fix BR for EL8

* Mon Sep 09 2019 Nicolas Chauvet <kwizart@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Fri Aug 30 2019 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-1
- Update to 3.0.0

* Mon Aug 26 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.8.5-0.1
- Update to 2.8.5 - pre-release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Orion Poplawski <orion@nwra.com> - 2.8.4-5
- Fix empty man pages (BZ 1653415)

* Mon Nov 26 2018 Orion Poplawski <orion@nwra.com> - 2.8.4-4
- Revert bind_manage_ipmi feature that is broken on 2.8

* Sun Nov 25 2018 Orion Poplawski <orion@nwra.com> - 2.8.4-3
- Use pathfix.py to fix python shebangs

* Sun Nov 25 2018 Orion Poplawski <orion@nwra.com> - 2.8.4-2
- Make koan require python2-ethtool (BZ 1638933)

* Sat Nov 24 2018 Orion Poplawski <orion@nwra.com> - 2.8.4-1
- Update to 2.8.4 (Fixes BZ 1613292, 1643860, 1614433, CVE-2018-1000226, CVE-2018-10931)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Orion Poplawski <orion@nwra.com> - 2.8.3-3
- koan requires urlgrabber

* Mon May 28 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.8.3-2
- Restore mergeability with epel7

* Mon May 28 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.8.3-1
- Update to 2.8.3 - security bugfix

* Wed Feb 21 2018 Orion Poplawski <orion@nwra.com> - 2.8.2-6
- Really fix django requires for Fedora 28+

* Tue Feb 20 2018 Orion Poplawski <orion@nwra.com> - 2.8.2-5
- Fix django requires for Fedora 28+

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.2-4
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.8.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Sep 18 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.2-1
- Update to 2.8.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-3
- Suppress logrotate output

* Mon Jun 12 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-2
- Fix module loading

* Wed May 24 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-1
- Update to 2.8.1

* Fri Feb 17 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-6
- Add patch to fix handling of multiple bridge interfaces

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-4
- Fix named patch

* Tue Jan 24 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-3
- Restart named-chroot service if used

* Fri Jan 20 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-2
- Fix logrotate script for systemd (bug #1414617)

* Thu Dec 1 2016 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-1
- Update to 2.8.0
- Restructure spec file

* Thu Sep 1 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-11.gitf78af86
- Add patches to fix TEMPLATE_DIRS and use OrderedDict

* Thu Aug 11 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-10.gitf78af86
- Force IPv4 connections to cobblerd from web proxy

* Thu Jul 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-9.gitf78af86
- Suppress "virt-install --os-variant list" error messages

* Thu Jul 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-8.git5680bf8
- Fix handling unknown os variants with osinfo-query

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.11-7.git95749a6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-6.git95749a6
- Fix typo in koan/app.py

* Wed Jul 13 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-5.git13b035f
- Update to current git snapshot (bug #1276896)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 1 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-3
- Require dnf-plugins-core

* Sun Jan 24 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-2
- Require dnf-core-plugins instead of yum-utils for repoquery on Fedora 23+

* Sun Jan 24 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-1
- Update to 2.6.11
- Make cobbler arch specific to allow for arch specific requires

* Thu Oct 1 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.10-1
- Update to 2.6.10

* Mon Jun 22 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.9-1
- Update to 2.6.9

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.8-2
- Support django 1.8 in Fedora 22+

* Fri May 8 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.8-1
- Update to 2.6.8
- Backport upstream patch to fix centos version detection (bug #1201879)

* Tue Apr 28 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.7-3
- Add patch to fix virt-install support for F21+/EL7 (bug #1188424)

* Mon Apr 27 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.7-2
- Create and own directories in tftp_dir

* Wed Dec 31 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.7-1
- Update to 2.6.7

* Sun Oct 19 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.6-1
- Update to 2.6.6

* Fri Aug 15 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.5-1
- Update to 2.6.5

* Wed Aug 13 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.4-2
- Require Django >= 1.4

* Mon Aug 11 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.4-1
- Update to 2.6.4

* Fri Jul 18 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.3-1
- Update to 2.6.3

* Wed Jul 16 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.2-1
- Update to 2.6.2
- Spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-1
- Update to 2.6.1
- Drop koan patch applied upstream

* Tue Apr 22 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-2
- Only require syslinux on x86

* Mon Apr 21 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-1
- Update to 2.6.0
