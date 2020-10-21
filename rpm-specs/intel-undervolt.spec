# LTO
%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto

Name:           intel-undervolt
Version:        1.7
Release:        4%{?dist}
Summary:        Intel CPU undervolting and throttling configuration tool

License:        GPLv3+
URL:            https://github.com/kitsunyan/intel-undervolt
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  i386 x86_64

BuildRequires:  gcc
BuildRequires:  systemd
%{?systemd_requires}

%description
intel-undervolt is a tool for undervolting and throttling limits alteration for
Intel CPUs.

Undervolting works on Haswell and newer CPUs and based on the content of this
article https://github.com/mihic/linux-intel-undervolt


%prep
%autosetup

# Cant build with proper build flags on Fedora
# * https://github.com/kitsunyan/intel-undervolt/issues/31
sed -i 's|CFLAGS =|CFLAGS =%{build_cflags}|' \
    Makefile.in


%build
%set_build_flags
%configure --enable-systemd
%make_build


%install
%make_install

%post
%systemd_post %{name}.service
%systemd_post %{name}-loop.service

%preun
%systemd_preun %{name}.service
%systemd_preun %{name}-loop.service

%postun
%systemd_postun_with_restart %{name}.service
%systemd_postun_with_restart %{name}-loop.service


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/*.service
%config(noreplace) %{_sysconfdir}/%{name}.conf


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7-2
- Update to 1.7

* Mon Apr 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6-2
- Initial package
