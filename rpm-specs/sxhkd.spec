%global _legacy_common_support 1
Name:		sxhkd
Version:	0.6.1
Release:	5%{?dist}
Summary:	Simple X hotkey daemon

License:	BSD
URL:		https://github.com/baskerville/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
%{?systemd_requires}
BuildRequires:	systemd
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-keysyms-devel


%description
sxhkd is an X daemon that reacts to input events by executing commands.

Its configuration file is a series of bindings that define the associations
between the input events and the commands.

The format of the configuration file supports a simple notation for mapping
multiple shortcuts to multiple commands in parallel.


%prep
%setup -q


%build
%make_build VERBOSE=1 %{?_smp_mflags} CFLAGS="%{optflags}" \
	LDFLAGS="%{?__global_ldflags}"


%install
%make_install PREFIX="%{_prefix}"
install -p -D -m 0644 contrib/systemd/%{name}.service \
	%{buildroot}/%{_unitdir}/%{name}.service


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_docdir}/%{name}/examples
%{_mandir}/man*/%{name}.1.gz
%{_unitdir}/%{name}.service


%changelog
* Thu Aug 06 2020 Jeff Law <law@redhat.com> - 0.6.1-5
- Enable _legacy_common_support

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 5 2019 Oles Pidgornyy <pidgornyy@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Oles Pidgornyy <pidgornyy@fedoraproject.org> - 0.5.8-1
- Update to 0.5.8 (#1471313)

* Sun Jun 18 2017 Oles Pidgornyy <pidgornyy@fedoraproject.org> - 0.5.7-1
- Initial release
