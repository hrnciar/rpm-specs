%global with_debug 1
%global with_check 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global provider github
%global provider_tld com
%global project containers
%global repo conmon
# https://github.com/containers/conmon
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit0 e5e2b93f68a1d06ab322c72584a31eee3ce00c70
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global git0 https://%{import_path}

# Used for comparing with latest upstream tag
# to decide whether to autobuild (non-rawhide only)
%global built_tag v2.0.20

Name: %{repo}
Epoch: 2
Version: 2.0.22
Release: 0.7.dev.git%{shortcommit0}%{?dist}
Summary: OCI container runtime monitor
License: ASL 2.0
URL: %{git0}
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildRequires: gcc
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: systemd-devel
BuildRequires: systemd-libs
Requires: glib2
Requires: systemd-libs

%description
%{summary}.

%prep
%autosetup -Sgit -n %{name}-%{commit0}

%build
%{__make} DEBUGTAG="enable_debug" all

%install
%{__make} PREFIX=%{buildroot}%{_prefix} install install.crio

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/crio/%{name}

%changelog
* Sat Oct 10 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.22-0.7.dev.gite5e2b93
- autobuilt e5e2b93

* Tue Oct  6 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.22-0.6.dev.git162c363
- autobuilt 162c363

* Fri Sep 18 09:34:35 EDT 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.22-0.5.dev.git59c2817
- build with journald support

* Wed Sep 16 16:12:47 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.22-0.4.dev.git59c2817
- autobuilt 59c2817

* Tue Sep 15 13:12:54 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.22-0.3.dev.gitd213bfa
- autobuilt d213bfa

* Mon Sep 14 14:12:03 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.22-0.2.dev.giteb93261
- autobuilt eb93261

* Tue Sep  8 22:12:10 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.22-0.1.dev.gitdd4fc17
- bump to 2.0.22
- autobuilt dd4fc17

* Tue Sep  8 21:12:42 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.21-0.11.dev.gitbc88ac5
- autobuilt bc88ac5

* Thu Sep  3 14:13:45 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.21-0.10.dev.git668b748
- autobuilt 668b748

* Wed Sep 02 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.21-0.9.dev.git1d7b3a5
- Resolves: #1786090 - build with -g for debuginfo

* Thu Aug 27 14:14:25 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.21-0.8.dev.git1d7b3a5
- autobuilt 1d7b3a5

* Wed Aug 26 13:11:37 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.21-0.7.dev.git6eb222d
- autobuilt 6eb222d

* Tue Aug 25 15:11:33 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.21-0.6.dev.git9d61f0f
- autobuilt 9d61f0f

* Mon Aug 24 14:11:36 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.21-0.5.dev.git76548e1
- autobuilt 76548e1

* Fri Aug 21 15:10:39 UTC 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.21-0.4.dev.git7ab6aa1
- autobuilt 7ab6aa1

* Wed Aug 05 16:10:09 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.21-0.3.dev.git5a6b2ac
- autobuilt 5a6b2ac

* Tue Aug 04 2020 Peter Hunt <pehunt@redhat.com> - 2:2.0.21-0.2.dev.gitfe1563c
- rebuild

* Tue Jul 28 14:09:38 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.21-0.1.dev.gitfe1563c
- bump to 2.0.21
- autobuilt fe1563c

* Mon Jul 27 21:09:33 GMT 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.20-0.3.dev.git5bc12e0
- autobuilt 5bc12e0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.20-0.2.dev.git3c396d4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.20-0.1.dev.git3c396d4
- bump to 2.0.20
- autobuilt 3c396d4

* Wed Jul 15 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.19-0.6.dev.git4fea27e
- autobuilt 4fea27e

* Wed Jul 08 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.19-0.5.dev.giteff699e
- autobuilt eff699e

* Mon Jun 29 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.19-0.4.dev.git9a1d403
- autobuilt 9a1d403

* Mon Jun 22 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.19-0.3.dev.git42414b8
- autobuilt 42414b8

* Wed Jun 17 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.19-0.2.dev.gitab8f5e5
- autobuilt ab8f5e5

* Mon Jun 15 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.19-0.1.dev.git96ea3a2
- bump to 2.0.19
- autobuilt 96ea3a2

* Wed Jun 10 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.18-0.8.dev.git2c32b99
- autobuilt 2c32b99

* Mon Jun 08 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.18-0.7.dev.gitf951578
- autobuilt f951578

* Wed Jun 03 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.18-0.6.dev.git50aeae4
- autobuilt 50aeae4

* Wed Jun 03 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.18-0.5.dev.gitf12e90b
- autobuilt f12e90b

* Tue Jun 02 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.18-0.4.dev.gitd951a5a
- autobuilt d951a5a

* Mon Jun 01 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.18-0.3.dev.git63d0e3d
- autobuilt 63d0e3d

* Wed May 27 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.18-0.2.dev.gitd0f367d
- autobuilt d0f367d

* Tue May 26 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.18-0.1.dev.git27bb67e
- bump to 2.0.18
- autobuilt 27bb67e

* Tue May 26 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.17-0.3.dev.git27eb304
- autobuilt 27eb304

* Mon May 25 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.17-0.2.dev.git82e9358
- depend on glib2

* Tue May 12 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.17-0.1.dev.git82e9358
- bump to 2.0.17
- autobuilt 82e9358

* Tue May 12 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.16-0.4.dev.gitedd4aaa
- autobuilt edd4aaa

* Tue May 12 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.16-0.3.dev.git6fa9c2a
- autobuilt 6fa9c2a

* Mon May 11 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.16-0.2.dev.git42cb289
- autobuilt 42cb289

* Thu Apr 02 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.16-0.1.dev.gite34c6d6
- bump to 2.0.16
- autobuilt e34c6d6

* Wed Apr 01 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.15-0.6.dev.gitb763fdd
- autobuilt b763fdd

* Tue Mar 31 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.15-0.5.dev.git9c9b3e7
- autobuilt 9c9b3e7

* Mon Mar 30 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.15-0.4.dev.git3ea6c68
- autobuilt 3ea6c68

* Wed Mar 25 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.15-0.3.dev.git89b2478
- autobuilt 89b2478

* Mon Mar 23 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.15-0.2.dev.gitff29dd6
- autobuilt ff29dd6

* Fri Mar 20 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.15-0.1.dev.gitb97c274
- bump to 2.0.15
- autobuilt b97c274

* Fri Mar 20 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.14-0.2.dev.git1b53637
- autobuilt 1b53637

* Tue Mar 17 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.14-0.1.dev.git849ab62
- bump to 2.0.14
- autobuilt 849ab62

* Mon Mar 16 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.12-0.1.dev.git51c0e7b
- bump to 2.0.12
- autobuilt 51c0e7b

* Tue Feb 11 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.11-0.6.dev.git86aa80b
- autobuilt 86aa80b

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.11-0.5.dev.git77f4a51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.11-0.4.dev.git77f4a51
- autobuilt 77f4a51

* Tue Jan 14 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.11-0.3.dev.gitccfdbb6
- autobuilt ccfdbb6

* Sat Jan 11 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.11-0.2.dev.git5039b44
- autobuilt 5039b44

* Wed Jan 08 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.11-0.1.dev.gitad05887
- bump to 2.0.11
- autobuilt ad05887

* Tue Jan 07 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.10-0.3.dev.git26f6817
- autobuilt 26f6817

* Tue Jan 07 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.10-0.2.dev.git6e39a83
- autobuilt 6e39a83

* Mon Jan 06 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.10-0.1.dev.gitb7bfc7b
- bump to 2.0.10
- autobuilt b7bfc7b

* Mon Jan 06 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.9-0.3.dev.git1560392
- autobuilt 1560392

* Fri Dec 20 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.9-0.2.dev.gitb17d81b
- autobuilt b17d81b

* Fri Dec 13 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.9-0.1.dev.gitc2e2e67
- bump to 2.0.9
- autobuilt c2e2e67

* Fri Dec 13 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.8-0.2.dev.gitc8f7443
- autobuilt c8f7443

* Thu Dec 12 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.8-0.1.dev.git036ff29
- bump to 2.0.8
- autobuilt 036ff29

* Thu Dec 12 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.7-0.3.dev.git4100fb2
- autobuilt 4100fb2

* Thu Dec 12 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.7-0.2.dev.git95ed45a
- autobuilt 95ed45a

* Wed Dec 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.7-0.1.dev.git8ba9575
- bump to 2.0.7
- autobuilt 8ba9575

* Wed Dec 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.6-0.2.dev.gitba14d9c
- autobuilt ba14d9c

* Tue Dec 10 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.6-0.1.dev.gitbc9e976
- bump to 2.0.6
- autobuilt bc9e976

* Tue Dec 10 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.5-0.2.dev.gitc792503
- autobuilt c792503

* Mon Dec 09 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.5-0.1.dev.gitfd5ac47
- bump to 2.0.5
- autobuilt fd5ac47

* Mon Dec 02 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.4-0.3.dev.gitdf8c6aa
- autobuilt df8c6aa

* Fri Nov 29 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.4-0.2.dev.git42bce45
- autobuilt 42bce45

* Mon Nov 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.4-0.1.dev.gitf6d23b5
- bump to 2.0.4
- autobuilt f6d23b5

* Mon Nov 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.3-0.3.dev.git098fcce
- autobuilt 098fcce

* Thu Nov 07 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.3-0.2.dev.git002da25
- autobuilt 002da25

* Mon Oct 21 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.3-0.1.dev.gitbc758d8
- built commit bc758d8

* Wed Sep 25 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.2-0.1.dev.git422ce21
- build latest upstream master

* Tue Sep 10 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.0-2
- remove BR: go-md2man since no manpages yet

* Tue Sep 10 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.0-1
- bump to v2.0.0

* Fri May 31 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:0.2.0-1
- initial package
