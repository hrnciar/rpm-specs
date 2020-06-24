%global _hardened_build 1

%if 0%{?fedora} || 0%{?rhel} >= 7
    %global with_systemd 1
%endif # 0%{?fedora} || 0%{?rhel} >= 7

Name:			ratools
Version:		0.6.2
Release:		12%{?dist}
Summary:		Framework for IPv6 Router Advertisements
License:		ASL 2.0
URL:			https://www.nonattached.net/ratools
Source0:		https://github.com/danrl/ratools/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?with_systemd}
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd
%endif # with_systemd

BuildRequires:		gcc

%description
Ratools is a fast, dynamic, multi-threading framework for creating, modifying
and sending IPv6 Router Advertisements (RA).

%prep
%setup -q

%build
CFLAGS="%{?optflags}"				\
LDFLAGS="%{?__global_ldflags}"		\
make %{?_smp_mflags} -C src/

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/rad %{buildroot}%{_bindir}/rad
install -pm 0755 bin/ractl %{buildroot}%{_bindir}/ractl

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/*
install -pm 0644 bash-completion.d/ractl.sh %{buildroot}%{_sysconfdir}/bash_completion.d/ractl

mkdir -p %{buildroot}%{_mandir}/man8
install -pm 0644 man/*.8 %{buildroot}%{_mandir}/man8

%if 0%{?with_systemd}
mkdir -p %{buildroot}%{_unitdir}
install -pm 0644 systemd/ratools-rad.service %{buildroot}%{_unitdir}/ratools-rad.service
install -pm 0644 systemd/ratools-rad.socket %{buildroot}%{_unitdir}/ratools-rad.socket

%post
%systemd_post ratools-rad.service

%preun
%systemd_preun ratools-rad.service

%postun
%systemd_postun_with_restart ratools-rad.service
%endif # with_systemd

%files
%doc README.md example.conf
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/rad
%{_bindir}/ractl
# Setting (noreplace) for the bash-completion is a bad idea,
# since this file is NOT config as meant to be customized by the user.
# https://bugzilla.redhat.com/show_bug.cgi?id=1100899#c6
%config %{_sysconfdir}/bash_completion.d/ractl
%{_mandir}/man8/*.8*
%if 0%{?with_systemd}
%{_unitdir}/ratools-rad.service
%{_unitdir}/ratools-rad.socket
%endif # with_systemd

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Florian Lehner <dev@der-flo.net> - 0.6.2-9
- Add gcc as BuildRequire

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct  6 2015 Florian Lehner <dev@der-flo.net - 0.6.2-1
- Update to Version 0.6.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Florian Lehner <dev@der-flo.net> - 0.6.1-1
- Update to Version 0.6.1
- Use license-Macro

* Mon Dec 29 2014 Florian Lehner <dev@der-flo.net> - 0.6.0-1
- Update to Version 0.6.0

* Sun Aug 24 2014 Florian Lehner <dev@der-flo.net> - 0.5.4-1
- Update version to 0.5.4

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Florian Lehner <dev@der-flo.net> - 0.5.3-4
- Use systemd only on supported platforms

* Sun Jul 20 2014 Florian Lehner <dev@der-flo.net> - 0.5.3-3
- Replace mkdir and install with its macro

* Wed Jun 18 2014 Florian Lehner <dev@der-flo.net> - 0.5.3-2
- Use macroized scriptlets for systemd

* Mon Jun 16 2014 Florian Lehner <dev@der-flo.net> - 0.5.3-1
- Move ractl.8-manpage from section 1 to section 8
- Add rad.8-manpage
- Add Systemd files
- Move config.example to example.conf

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Florian Lehner <dev@der-flo.net> 0.5.2-3
- add manpage

* Sat May 31 2014 Florian Lehner <dev@der-flo.net> 0.5.2-2
- Add comment about not using noreplace
- Rename Source0 after downloading

* Fri May 30 2014 Florian Lehner <dev@der-flo.net> 0.5.2-1
- Update to new version
- Use smp_mflags while make

* Mon May 26 2014 Florian Lehner <dev@der-flo.net> 0.5-3
- Set permissions on files properly
- Correct misspelling of the license
- Don't let the package own a directory of another package
- Add missing 'config.example' to docs-section
- Rename Source to Source0
- Use macro in Source0-URL
- Remove index.html from URL
- Remove Group-tag
- Add information about Patch0
- Add _hardend_build
- Fix issue on installing bash_completion.d
- Add CFLAGS and LDFLAGS options in front of make
- Use noreplace

* Fri May 23 2014 Florian Lehner <dev@der-flo.net> 0.5-2
- Add Patch for arm7hl

* Fri May 23 2014 Florian Lehner <dev@der-flo.net> 0.5-1
- Initial packaging (#1100899)
