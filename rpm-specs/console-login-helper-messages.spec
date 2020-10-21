%global github_owner    coreos
%global github_project  console-login-helper-messages

Name:           console-login-helper-messages
Version:        0.2
Release:        1%{?dist}
Summary:        Combines motd, issue, profile features to show system information to the user before/on login
License:        BSD
URL:            https://github.com/%{github_owner}/%{github_project}
Source0:        https://github.com/%{github_owner}/%{github_project}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  systemd make
%{?systemd_requires}
Requires:       bash systemd

%description
%{summary}.

%package motdgen
Summary:        Message of the day generator script showing system information
Requires:       console-login-helper-messages
# sshd reads /run/motd.d, where the generated MOTD message is written.
Recommends:     openssh
# bash: bash scripts are included in this package
# systemd: systemd service and path units, and querying for failed units
# (the above applies to the issuegen and profile subpackages too)
Requires:       bash systemd
# setup: filesystem paths need setting up.
#   * https://pagure.io/setup/pull-request/14
#   * https://pagure.io/setup/pull-request/15
#   * https://pagure.io/setup/pull-request/16
# Make exception for fc29 - soft requires as we will create /run/motd.d
# ourselves if it doesn't already exist.
%if 0%{?fc29}
Requires:       setup
%else
Requires:       setup >= 2.12.7-1
%endif
# pam: to display motds in /run/motd.d.
#   * https://github.com/linux-pam/linux-pam/issues/47
#   * https://github.com/linux-pam/linux-pam/pull/69
#   * https://github.com/linux-pam/linux-pam/pull/76
Requires:       ((pam >= 1.3.1-15) if openssh)
# selinux-policy: to apply pam_var_run_t contexts:
#   * https://github.com/fedora-selinux/selinux-policy/pull/244
# Make exception for fc29, as PAM will create the tmpfiles. (In Fedora 30 and
# above, setup is responsible for this).
%if 0%{?fc29}
Requires:       ((selinux-policy >= 3.14.2-50) if openssh)
%else
Requires:       ((selinux-policy >= 3.14.3-23) if openssh)
%endif

%description motdgen
%{summary}.

%package issuegen
Summary:        Issue generator script showing SSH keys and IP address
Requires:       console-login-helper-messages
Requires:       bash systemd setup
# systemd-udev: for displaying IP info using udev
# NetworkManager: for displaying IP info using NetworkManager dispatcher script
# NetworkManager is recommended as it supports complex/custom networking devices
Requires:       (NetworkManager or systemd-udev)
# fedora-release: for /etc/issue.d path
#   * https://src.fedoraproject.org/rpms/fedora-release/pull-request/64#
Requires:       fedora-release
# agetty is included in util-linux, which searches /etc/issue.d.
# Needed to display issues symlinked from /etc/issue.d.
#   * https://github.com/karelzak/util-linux/commit/37ae6191f7c5686f1f9a2c3984e2cd9a62764029#diff-15eca7082c3cb16e5ac467f4acceb9d0R54
#   * https://github.com/karelzak/util-linux/commit/1fc82a1360305f696dc1be6105c9c56a9ea03f52#diff-d7efd2b3dbb10e54185f001dc21d43db
Requires:       util-linux >= 2.32-1

%description issuegen
%{summary}.

%package profile
Summary:        Profile script showing systemd failed units
Requires:       console-login-helper-messages
Requires:       bash systemd setup

%description profile
%{summary}.

%prep
%setup -q

%build

%install
make install DESTDIR=%{buildroot}

%post
%systemd_post %{name}-issuegen.service
%systemd_post %{name}-motdgen.service
%systemd_post %{name}-issuegen.path
%systemd_post %{name}-motdgen.path
%systemd_post %{name}-gensnippet-os-release.service
%systemd_post %{name}-gensnippet-ssh-keys.service

%preun
%systemd_preun %{name}-issuegen.service
%systemd_preun %{name}-motdgen.service
%systemd_preun %{name}-issuegen.path
%systemd_preun %{name}-motdgen.path
%systemd_preun %{name}-gensnippet-os-release.service
%systemd_preun %{name}-gensnippet-ssh-keys.service

%postun
%systemd_postun_with_restart %{name}-issuegen.service
%systemd_postun_with_restart %{name}-motdgen.service
%systemd_postun_with_restart %{name}-issuegen.path
%systemd_postun_with_restart %{name}-motdgen.path
%systemd_postun_with_restart %{name}-gensnippet-os-release.service
%systemd_postun_with_restart %{name}-gensnippet-ssh-keys.service

# TODO: %check

%files
%doc README.md
%doc doc/manual.md
%license LICENSE
%dir %{_libexecdir}/%{name}
%dir %{_prefix}/lib/%{name}
%dir %{_prefix}/share/%{name}
%dir %{_sysconfdir}/%{name}
%{_tmpfilesdir}/%{name}.conf
%{_prefix}/lib/%{name}/libutil.sh

%files issuegen
%{_unitdir}/%{name}-issuegen.service
%{_unitdir}/%{name}-issuegen.path
%{_unitdir}/%{name}-gensnippet-ssh-keys.service
%{_tmpfilesdir}/%{name}-issuegen.conf
%{_sysconfdir}/NetworkManager/dispatcher.d/90-%{name}-gensnippet_if
%{_prefix}/lib/%{name}/issuegen.defs
%{_libexecdir}/%{name}/issuegen
%{_libexecdir}/%{name}/gensnippet_ssh_keys
%{_libexecdir}/%{name}/gensnippet_if
%{_libexecdir}/%{name}/gensnippet_if_udev
%ghost %{_sysconfdir}/issue.d/40_%{name}.issue
%dir %{_prefix}/lib/%{name}/issue.d
%dir %{_sysconfdir}/%{name}/issue.d

%files motdgen
%{_unitdir}/%{name}-motdgen.service
%{_unitdir}/%{name}-motdgen.path
%{_unitdir}/%{name}-gensnippet-os-release.service
%{_tmpfilesdir}/%{name}-motdgen.conf
%{_prefix}/lib/%{name}/motdgen.defs
%{_libexecdir}/%{name}/motdgen
%{_libexecdir}/%{name}/gensnippet_os_release
%dir %{_prefix}/lib/%{name}/motd.d
%dir %{_sysconfdir}/%{name}/motd.d

%files profile
%{_prefix}/share/%{name}/profile.sh
%{_tmpfilesdir}/%{name}-profile.conf
%ghost %{_sysconfdir}/profile.d/%{name}-profile.sh

%changelog
* Fri Sep 25 2020 Kelvin Fan <kfan@redhat.com> - 0.2-1
- Update to 0.2
- Add presets for `.service` units
- %ghost symlinks defined in tmpfiles.d directory

* Fri Sep 18 2020 Kelvin Fan <kfan@redhat.com> - 0.19-2
- BuildRequire `make`
- Remove preinstall scripts

* Tue Sep 08 2020 Kelvin Fan <kfan@redhat.com> - 0.19-1
- Update to 0.19
- Invoke make install
- Remove -motdgen.service, -issuegen.service presets
- Require NetworkManager or systemd-udev

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Robert Fairley <rfairley@redhat.com> - 0.18.2-1
- Update to 0.18.2

* Thu Apr 30 2020 Robert Fairley <rfairley@redhat.com> - 0.18.1-1
- Update to 0.18.1

* Tue Apr 28 2020 Robert Fairley <rfairley@redhat.com> - 0.18-1
- Update to 0.18
- Change github_owner to coreos

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Robert Fairley <rfairley@redhat.com> - 0.17-1
- Update to 0.17
- Add manual.md to package docs
- Use tmpfiles_create_pkg macro

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Robert Fairley <rfairley@redhat.com> - 0.16-3
- Specfile tidyups (comments, formatting), and remove fc28 conditionals

* Fri Mar 22 2019 Robert Fairley <rfairley@redhat.com> - 0.16-2
- Add condition for f28 setup Requires

* Thu Mar 21 2019 Robert Fairley <rfairley@redhat.com> - 0.16-1
- relax setup dependency for f29
- general upstream source/tidiness improvements
- house executable scripts in /usr/libexec
- change Source0 to use GitHub-generated archive link
- drop .path units for motdgen and issuegen

* Fri Mar 15 2019 Robert Fairley <rfairley@redhat.com> - 0.15-1
- make motdgen generate motd in /run with no symlink

* Fri Mar 15 2019 Robert Fairley <rfairley@redhat.com> - 0.14-1
- issuegen.service: rely on sshd-keygen.target
- issuegen: don't show kernel version

* Thu Jan 24 2019 Robert Fairley <rfairley@redhat.com> - 0.13-4
- update reviewers.md and manual.md with correct paths

* Wed Jan 23 2019 Robert Fairley <rfairley@redhat.com> - 0.13-3
- change generated issue to be scoped in private directory

* Wed Jan 23 2019 Robert Fairley <rfairley@redhat.com> - 0.13-2
- change generated motd to be scoped in private directory

* Wed Jan 23 2019 Robert Fairley <rfairley@redhat.com> - 0.13-1
- add a symlink for motdgen (quick solution until upstream pam_motd.so changes propagate)

* Fri Jan 18 2019 Robert Fairley <rfairley@redhat.com> - 0.12-2
- fix Requires for selinux-policy, add missing Requires for systemd-udev and fedora-release

* Wed Jan 16 2019 Robert Fairley <rfairley@redhat.com> - 0.12-1
- fix specfile Source0 to correct github URL

* Wed Jan 16 2019 Robert Fairley <rfairley@redhat.com> - 0.11-1
- add reviewers.md, specfile fixes

* Wed Jan 16 2019 Robert Fairley <rfairley@redhat.com> - 0.1-12
- add move README.md sections out into a manual, update specfile

* Wed Jan 09 2019 Robert Fairley <rfairley@redhat.com> - 0.1-11
- specfile cleanup, go through git commit history to write changelog

* Wed Jan 09 2019 Robert Fairley <rfairley@redhat.com> - 0.1-10
- Add license, tidyups

* Mon Dec 10 2018 Robert Fairley <rfairley@redhat.com> - 0.1-9
- Add tmpfiles_create_package usage to reproduce coredump

* Mon Dec 10 2018 Robert Fairley <rfairley@redhat.com> - 0.1-8
- Remove tmpfiles_create_package usage

* Mon Dec 10 2018 Robert Fairley <rfairley@redhat.com> - 0.1-7
- Fix usage of tmpfiles_create_package macro in specfile

* Fri Dec 07 2018 Robert Fairley <rfairley@redhat.com> - 0.1-6
- Fix tmpfile symlink paths

* Fri Dec 07 2018 Robert Fairley <rfairley@redhat.com> - 0.1-5
- Add [systemd] label to failed units message in profile script

* Tue Dec 04 2018 Robert Fairley <rfairley@redhat.com> - 0.1-4
- Minor formatting edits to generated issue and motd

* Tue Dec 04 2018 Robert Fairley <rfairley@redhat.com> - 0.1-3
- Remove printing package manager info (rpm-ostree, dnf)

* Tue Dec 04 2018 Robert Fairley <rfairley@redhat.com> - 0.1-2
- Add CI with copr
- Drop requirement on specifc SELinux version
- Various tidyups including filenames

* Tue Sep 25 2018 Robert Fairley <rfairley@redhat.com> - 0.1-1
- Initial Package
