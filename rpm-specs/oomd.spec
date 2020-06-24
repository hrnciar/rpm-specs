Name:		oomd
Summary:	Userspace Out-Of-Memory (OOM) killer
Version:	0.4.0
Release:	1%{dist}
License:	GPLv2
URL:		https://github.com/facebookincubator/oomd/
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExcludeArch:	i686 armv7hl

BuildRequires:	gcc-c++
BuildRequires:	meson >= 0.45
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(gtest_main)
BuildRequires:	pkgconfig(gmock)
BuildRequires:	systemd-rpm-macros
%{?systemd_requires}

%description
Out of memory killing has historically happened inside kernel space. On a
memory overcommitted linux system, malloc(2) and friends usually never fail.
However, if an application dereferences the returned pointer and the system has
run out of physical memory, the linux kernel is forced take extreme measures,
up to and including killing processes. This is sometimes a slow and painful
process because the kernel can spend an unbounded amount of time swapping in
and out pages and evicting the page cache. Furthermore, configuring policy is
not very flexible while being somewhat complicated.

oomd aims to solve this problem in userspace. oomd leverages PSI and cgroupv2
to monitor a system holistically. oomd then takes corrective action in
userspace before an OOM occurs in kernel space. Corrective action is configured
via a flexible plugin system, in which custom code can be written. By default,
this involves killing offending processes. This enables an unparalleled level
of flexibility where each workload can have custom protection rules.
Furthermore, time spent livedlocked in kernelspace is minimized.

%prep
%autosetup

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md docs/
%{_bindir}/oomd
%{_unitdir}/oomd.service
%{_mandir}/man1/oomd.*
%config(noreplace) %{_sysconfdir}/oomd/

%post
%systemd_post oomd.service

%preun
%systemd_preun oomd.service

%postun
%systemd_postun_with_restart oomd.service

%changelog
* Thu Jun  4 2020 Filipe Brandenburger <filbranden@gmail.com> - 0.4.0-1
- Upgrade to v0.4.0

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.3.2-2
- Rebuild (jsoncpp)

* Wed Feb 19 2020 Filipe Brandenburger <filbranden@gmail.com> - 0.3.2-1
- Update to v0.3.2

* Tue Feb 18 2020 Filipe Brandenburger <filbranden@gmail.com> - 0.3.1-1
- Update to v0.3.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.2.0-5
- Rebuild (jsoncpp)

* Thu Sep 12 2019 Filipe Brandenburger <filbranden@gmail.com> - 0.2.0-4
- First official build for Fedora
- Exclude 32-bit architectures, which fail to build.

* Tue Sep 10 2019 Filipe Brandenburger <filbranden@gmail.com> - 0.2.0-3
- Initial release of oomd RPM package
