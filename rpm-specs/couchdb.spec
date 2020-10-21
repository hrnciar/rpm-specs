Name:           couchdb
Version:        3.1.1
Release:        1%{?dist}
Summary:        A document database server, accessible via a RESTful JSON API
License:        ASL 2.0
URL:            https://couchdb.apache.org/
Source0:        https://downloads.apache.org/%{name}/source/%{version}/apache-%{name}-%{version}.tar.gz
Source1:        https://downloads.apache.org/%{name}/source/%{version}/apache-%{name}-%{version}.tar.gz.asc
Source3:        %{name}.service
Source4:        %{name}.tmpfiles.conf
Source5:        %{name}.temporary.sh
Patch1:         couchdb-0001-Build-with-SpiderMonkey-60-on-ARM-64.patch
Patch2:		couchdb-0002-Build-with-Erlang-23.patch
BuildRequires: curl-devel >= 7.18.0
BuildRequires: erlang-bear
BuildRequires: erlang-erts
BuildRequires: erlang-eunit
BuildRequires: erlang-folsom
BuildRequires: erlang-hyper
BuildRequires: erlang-ibrowse >= 4.0.1
BuildRequires: erlang-jiffy
BuildRequires: erlang-meck
BuildRequires: erlang-mochiweb
BuildRequires: erlang-os_mon
BuildRequires: erlang-rebar
BuildRequires: erlang-rpm-macros
BuildRequires: erlang-sd_notify
BuildRequires: erlang-setup
BuildRequires: erlang-snappy
BuildRequires: erlang-triq
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: mozjs60-devel
BuildRequires: libicu-devel
BuildRequires: libtool
BuildRequires: systemd

Requires(pre): systemd
Requires(post): systemd
Requires(preun): systemd

# Users and groups
Requires(pre): shadow-utils

%description
Apache CouchDB is a distributed, fault-tolerant and schema-free
document-oriented database accessible via a RESTful HTTP/JSON API.
Among other features, it provides robust, incremental replication
with bi-directional conflict detection and resolution, and is
queryable and indexable using a table-oriented view engine with
JavaScript acting as the default view definition language.


%prep
%autosetup -p 1 -n apache-%{name}-%{version}

#gzip -d -k ./share/doc/build/latex/CouchDB.pdf.gz

# FIXME FIXME FIXME
# Remove bundled libraries
#b64url/
#chttpd/
#config/
#ddoc_cache/
#docs/
#ets_lru/
#fabric/
#fauxton/
#global_changes/
#ioq/
#khash/
#mango/
#mem3/
#rexi/
#rm -f bin/rebar
#rm -rf src/bear/
#rm -rf src/folsom/
#rm -rf src/hyper/
#rm -rf src/ibrowse/
#rm -rf src/jiffy/
#rm -rf src/meck/
#rm -rf src/mochiweb
#rm -rf src/rebar/
#rm -rf src/setup/
#rm -rf src/snappy
#rm -rf src/triq/


%build
./configure --user=couchdb --with-curl --erlang-md5 --spidermonkey-version 60 --skip-deps --rebar /usr/bin/rebar
REBAR=/usr/bin/rebar make %{?_smp_mflags} VERBOSE=1 release


%install
# Install systemd-service
install -D -p -m 0644 %{SOURCE4} %{buildroot}/usr/lib/tmpfiles.d/%{name}.conf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
# Temporary systemd + selinux wrapper
# This makes the service run in couchdb_t
install -D -p -m 0755 %{SOURCE5} %{buildroot}%{_libexecdir}/%{name}

# Install runtime apps and scripts
install -D -p -m 0755 rel/%{name}/bin/%{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0755 rel/%{name}/bin/couchjs %{buildroot}%{_bindir}/couchjs
install -D -p -m 0755 rel/%{name}/bin/remsh %{buildroot}%{_bindir}/remsh

# Install Erlang VM and application config files
install -D -p -m 0644 rel/%{name}/etc/default.d/README %{buildroot}%{_sysconfdir}/%{name}/default.d/README
install -D -p -m 0644 rel/%{name}/etc/local.d/README %{buildroot}%{_sysconfdir}/%{name}/local.d/README
install -D -p -m 0644 rel/%{name}/etc/default.ini %{buildroot}%{_sysconfdir}/%{name}/default.ini
install -D -p -m 0644 rel/%{name}/etc/local.ini %{buildroot}%{_sysconfdir}/%{name}/local.ini
install -D -p -m 0644 rel/%{name}/etc/vm.args %{buildroot}%{_sysconfdir}/%{name}/vm.args

# Install Erlang runtime libs
mkdir -p %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/b64url-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/chttpd-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/config-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/couch-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/couch_epi-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/couch_event-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/couch_index-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/couch_log-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/couch_mrview-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/couch_peruser-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/couch_plugins-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/couch_replicator-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/couch_stats-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/ddoc_cache-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/dreyfus-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/ets_lru-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/fabric-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/global_changes-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/ioq-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/ken-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/khash-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/mango-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/mem3-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/recon-2.5.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/rexi-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/
cp -arv rel/%{name}/lib/smoosh-3.0.0/ %{buildroot}%{_libdir}/erlang/lib/

# We do not install release (yet)
# FIXME

# Install man-pages
install -D -p -m 0644 rel/%{name}/share/docs/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Copy required data files
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -arv rel/%{name}/share/server %{buildroot}%{_datadir}/%{name}
cp -arv rel/%{name}/share/www %{buildroot}%{_datadir}/%{name}


# Create room for executable
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}

# Create room for logs
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

%check
#make check
#make check-eunit


%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /bin/bash \
-c "Couchdb Database Server" %{name}
exit 0


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%doc BUGS.md COMMITTERS.md CONTRIBUTING.md CONTRIBUTORS NOTICE README.rst
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/local.d/
%dir %{_sysconfdir}/%{name}/default.d/
%{_sysconfdir}/%{name}/local.d/README
%{_sysconfdir}/%{name}/default.d/README
%config %attr(0644, %{name}, %{name}) %{_sysconfdir}/%{name}/default.ini
%config(noreplace) %attr(0644, %{name}, %{name}) %{_sysconfdir}/%{name}/local.ini
%config(noreplace) %attr(0644, %{name}, %{name}) %{_sysconfdir}/%{name}/vm.args
#%%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_bindir}/%{name}
%{_bindir}/couchjs
%{_bindir}/remsh
%{_libdir}/erlang/lib/b64url-%{version}/
%{_libdir}/erlang/lib/chttpd-%{version}/
%{_libdir}/erlang/lib/config-%{version}/
%{_libdir}/erlang/lib/couch-%{version}/
%{_libdir}/erlang/lib/couch_epi-%{version}/
%{_libdir}/erlang/lib/couch_event-%{version}/
%{_libdir}/erlang/lib/couch_index-%{version}/
%{_libdir}/erlang/lib/couch_log-%{version}/
%{_libdir}/erlang/lib/couch_mrview-%{version}/
%{_libdir}/erlang/lib/couch_peruser-%{version}/
%{_libdir}/erlang/lib/couch_plugins-%{version}/
%{_libdir}/erlang/lib/couch_replicator-%{version}/
%{_libdir}/erlang/lib/couch_stats-%{version}/
%{_libdir}/erlang/lib/ddoc_cache-%{version}/
%{_libdir}/erlang/lib/dreyfus-%{version}/
%{_libdir}/erlang/lib/ets_lru-%{version}/
%{_libdir}/erlang/lib/fabric-%{version}/
%{_libdir}/erlang/lib/global_changes-%{version}/
%{_libdir}/erlang/lib/ioq-%{version}/
%{_libdir}/erlang/lib/ken-%{version}/
%{_libdir}/erlang/lib/khash-%{version}/
%{_libdir}/erlang/lib/mango-%{version}/
%{_libdir}/erlang/lib/mem3-%{version}/
%{_libdir}/erlang/lib/recon-2.5.0/
%{_libdir}/erlang/lib/rexi-%{version}/
%{_libdir}/erlang/lib/smoosh-%{version}/
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%dir %attr(0755, %{name}, %{name}) %{_localstatedir}/log/%{name}
%dir %attr(0755, %{name}, %{name}) %{_localstatedir}/run/%{name}


%changelog
* Sun Oct  4 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.1.1-1
- Ver. 3.1.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 5 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.3.1-1
- Ver. 2.3.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.7.1-16
- Rebuild with noarch deps

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 1.7.1-14
- Rebuild for ICU 63

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.7.1-13
- Rebuilt for libcrypt.so.2 (#1666033)

* Wed Nov 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.7.1-12
* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.7.1-10
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.7.1-9
- Rebuild for ICU 61.1

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.7.1-8
- Rebuild for Erlang 20 (with proper builddeps)

* Tue Mar 06 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.7.1-7
- Rebuild for Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.7.1-5
- Rebuilt for switch to libxcrypt

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.7.1-4
- Rebuild for ICU 60.1

* Mon Nov 20 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.7.1-3
- Backport more timeout fixes to resolve armv7hl failures

* Thu Nov 16 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.7.1-2
- Fix test failures on armv7hl

* Wed Nov 15 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.7.1-1
- Ver. 1.7.1 (last-minute fix release)

* Wed Nov 15 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.7.0-1
- Ver. 1.7.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 1.6.1-22
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-20
- Rebuilt to pick up a new JS185 VA-48 API

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-18
- Fix FTBFS with Erlang 19

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.6.1-17
- Rebuild for Erlang 19

* Tue Jun  7 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-16
- Missing BuildRequires added

* Tue Jun  7 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-15
- Spec-file cleanups

* Mon Apr 18 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-14
- Use erlang-jiffy as an underlying JSON-library instead of outdated ejson

* Sat Apr 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-13
- Remove faulty macros

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 1.6.1-12
- rebuild for ICU 57.1

* Wed Mar 30 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-11
- Rebuild with Erlang 18.3
- Fix for recent erlang-mochiweb

* Wed Feb 10 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-10
- Fix FTBFS with Erlang 18.x.y

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-8
- Rebuild for Erlang 18.2.2

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1.6.1-7
- rebuild for ICU 56.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 1.6.1-5
- rebuild for ICU 54.1

* Thu Nov 27 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-4
- Fix CVE-2010-5312 couchdb: jquery-ui: XSS vulnerability in jQuery.ui.dialog
  title option (rhbz #1166767)

* Fri Nov 14 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-3
- Fix systemd unit file permissions (755 -> 644)
- Remove EL5,EL6 support

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-2
- Rebuild for Erlang 17.3.3

* Sun Sep 07 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-1
- Ver. 1.6.1

* Fri Aug 29 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-13
- Kill fragile etap tests in favor of eunit-based test-suite

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-12
- Rebuild with Erlang 17.2.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 1.6.0-11
- rebuild for ICU 53.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 09 2014 Warren Togami <warren@slickage.com> - 1.6.0-9
- Add systemd notify support

* Sun Jul 06 2014 Warren Togami <warren@slickage.com> - 1.6.0-8
- SELinux: Use /usr/libexec/couchdb wrapper for systemd ExecStart, executes as couchdb_t
  Additional fixes to selinux-policy are required,
  see latest status http://wtogami.fedorapeople.org/a/2014/couchdb.txt
- Remove -heart from ExecStart, systemd handles service runtime
- default.ini contains default configuration from upstream.
  It has previously warned users to not modify it as it will be overwritten on package upgrade.
  Now package upgrades really will overwrite default.ini.
- Configuration is read during CouchDB startup in this order:
  default.ini -> default.d/*.ini -> local.d/*.ini -> local.ini
  Other packages are meant to drop configuration into default.d/
  Users can modify local.ini or add new files in local.d/
- CouchDB runtime config changes are written to local.ini

* Thu Jul 03 2014 Warren Togami <warren@slickage.com> - 1.6.0-6
- silence stdout/stderr to prevent redundant flooding of /var/log/messages
  CouchDB already logs these messages to /var/log/couchdb/couch.log
  Instead print the log filename to stdout, in case a user who ran it
  from the CLI is confused about where the messages went.
- -couch_ini accepts .ini or a .d/ directory.  For directories it reads
  any *.ini file.  Fixes #1002277.

* Mon Jun 23 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-2
- Fix building with sligntly older gcc/glibc

* Sun Jun 22 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-1
- Ver. 1.6.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 David Tardon <dtardon@redhat.com> - 1.5.0-2
- rebuild for new ICU

* Fri Jan 10 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.5.0-1
- Ver. 1.5.0

* Fri Oct 25 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-3
- Rebuild with new requires - __erlang_nif_version, __erlang_drv_version

* Fri Sep 06 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-2
- Moved tmpfiles entry to /usr

* Sun Aug 25 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-1
- Ver. 1.3.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.2-3
- Fix for R16B01 ( https://issues.apache.org/jira/browse/COUCHDB-1833 )

* Fri May 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.2-2
- Fix for R16B and latest mochiweb

* Mon Apr 15 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.2-1
- Ver. 1.2.2 (bugfix release)

* Fri Mar 15 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-4
- Fix FTBFS in Rawhide (F-19)

* Fri Feb 08 2013 Jon Ciesla <limburgher@gmail.com> - 1.2.1-3
- libicu rebuild.

* Tue Jan 22 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-2
- Revert systemd-macros

* Mon Jan 21 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-1
- Ver. 1.2.1 (security bugfix release)
- Introduce handy systemd-related macros (see rhbz #850069)

* Tue Oct 30 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-3
- Unbundle snappy (see rhbz #871149)
- Add _isa to the Requires

* Mon Sep 24 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-2
- Build fixes
- Temporarily disable verbosity

* Mon Sep 24 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0

* Mon Sep 24 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-4.1
- Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-3
- Improve systemd support

* Wed May 16 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-2
- Updated systemd files (added EnvironmentFile option)

* Sun Mar 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-1
- Ver. 1.1.1

* Sun Mar 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.0.3-6
- Fix building on f18

* Wed Feb 15 2012 Jon Ciesla <limburgher@gmail.com> - 1.0.3-5
- Migrate to systemd, BZ 771434.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.3-3
- Rebuilt with new libicu

* Mon Aug 15 2011 Kalev Lember <kalevlember@gmail.com> - 1.0.3-2
- Rebuilt for rpm bug #728707

* Thu Jul 21 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.3-1
- Ver. 1.0.3

* Tue Jul 12 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-8
- Build for EL-5 (see patch99 - quite ugly, I know)

* Sat Jun 18 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-7
- Requires ibrowse >= 2.2.0 for building
- Fixes for /var/run mounted as tmpfs (see rhbz #656565, #712681)

* Mon May 30 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-6
- Patched patch for new js-1.8.5

* Fri May 20 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-5
- Fixed issue with ibrowse-2.2.0

* Thu May 19 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.2-4
- Fixed issue with R14B02

* Thu May  5 2011 Jan Horak <jhorak@redhat.com> - 1.0.2-3
- Added Spidermonkey 1.8.5 patch

* Mon Mar 07 2011 Caolán McNamara <caolanm@redhat.com> 1.0.2-2
- rebuild for icu 4.6

* Thu Nov 25 2010 Peter Lemenkov <lemenkov@gmail.com> 1.0.2-1
- Ver. 1.0.2
- Patches were rebased

* Tue Oct 12 2010 Peter Lemenkov <lemenkov@gmail.com> 1.0.1-4
- Added patches for compatibility with R12B5

* Mon Oct 11 2010 Peter Lemenkov <lemenkov@gmail.com> 1.0.1-3
- Narrowed list of BuildRequires

* Thu Aug 26 2010 Peter Lemenkov <lemenkov@gmail.com> 1.0.1-2
- Cleaned up spec-file a bit

* Fri Aug  6 2010 Peter Lemenkov <lemenkov@gmail.com> 1.0.1-1
- Ver. 1.0.1

* Thu Jul 15 2010 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-1
- Ver. 1.0.0

* Wed Jul 14 2010 Peter Lemenkov <lemenkov@gmail.com> 0.11.1-1
- Ver. 0.11.1
- Removed patch for compatibility with Erlang/OTP R14A (merged upstream)

* Sun Jul 11 2010 Peter Lemenkov <lemenkov@gmail.com> 0.11.0-3
- Compatibility with Erlang R14A (see patch9)

* Tue Jun 22 2010 Peter Lemenkov <lemenkov@gmail.com> 0.11.0-2
- Massive spec cleanup

* Tue Jun 22 2010 Peter Lemenkov <lemenkov@gmail.com> 0.11.0-1
- Ver. 0.11.0 (a feature-freeze release candidate)

* Fri Jun 18 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-13
- Remove ldconfig invocation (no system-wide shared libraries)
- Removed icu-config requires

* Tue Jun 15 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-12
- Narrow explicit requires

* Tue Jun  8 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-11
- Remove bundled ibrowse library (see rhbz #581282).

* Mon Jun  7 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-10
- Use system-wide erlang-mochiweb instead of bundled copy (rhbz #581284)
- Added %%check target and necessary BuildRequires - etap, oauth, mochiweb

* Wed Jun  2 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-9
- Remove pid-file after stopping CouchDB

* Tue Jun  1 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-8
- Suppress unneeded message while stopping CouchDB via init-script

* Mon May 31 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-7
- Do not manually remove pid-file while stopping CouchDB

* Mon May 31 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-6
- Fix 'stop' and 'status' targets in the init-script (see rhbz #591026)

* Thu May 27 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-5
- Use system-wide erlang-etap instead of bundled copy (rhbz #581281)

* Fri May 14 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-4
- Use system-wide erlang-oauth instead of bundled copy (rhbz #581283)

* Thu May 13 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-3
- Fixed init-script to use /etc/sysconfig/couchdb values (see rhbz #583004)
- Fixed installation location of beam-files (moved to erlang directory)

* Fri May  7 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-2
- Remove useless BuildRequires

* Fri May  7 2010 Peter Lemenkov <lemenkov@gmail.com> 0.10.2-1
- Update to 0.10.2 (resolves rhbz #578580 and #572176)
- Fixed chkconfig priority (see rhbz #579568)

* Fri Apr 02 2010 Caolán McNamara <caolanm@redhat.com> 0.10.0-3
- rebuild for icu 4.4

* Thu Oct 15 2009 Allisson Azevedo <allisson@gmail.com> 0.10.0-2
- Added patch to force init_enabled=true in configure.ac.

* Thu Oct 15 2009 Allisson Azevedo <allisson@gmail.com> 0.10.0-1
- Update to 0.10.0.

* Sun Oct 04 2009 Rahul Sundaram <sundaram@fedoraproject.org> 0.9.1-2
- Change url. Fixes rhbz#525949

* Thu Jul 30 2009 Allisson Azevedo <allisson@gmail.com> 0.9.1-1
- Update to 0.9.1.
- Drop couchdb-0.9.0-pid.patch.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Allisson Azevedo <allisson@gmail.com> 0.9.0-2
- Fix permission for ini files.
- Fix couchdb.init start process.

* Tue Apr 21 2009 Allisson Azevedo <allisson@gmail.com> 0.9.0-1
- Update to 0.9.0.

* Tue Nov 25 2008 Allisson Azevedo <allisson@gmail.com> 0.8.1-4
- Use /etc/sysconfig for settings.

* Tue Nov 25 2008 Allisson Azevedo <allisson@gmail.com> 0.8.1-3
- Fix couchdb_home.
- Added libicu-devel for requires.

* Tue Nov 25 2008 Allisson Azevedo <allisson@gmail.com> 0.8.1-2
- Fix spec issues.

* Tue Nov 25 2008 Allisson Azevedo <allisson@gmail.com> 0.8.1-1
- Initial RPM release
