%global commit0 fdab195ed5ec8e4aae31949703a5304712f11642

Name:           qotd
Version:        0.11.3
Release:        9%{?dist}
Summary:        A simple and lightweight Quote of the Day daemon

License:        GPLv2+
URL:            https://gitlab.com/ammongit/qotd
Source0:        https://gitlab.com/ammongit/%{name}/repository/archive.tar.gz?ref=v%{version}#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  git
BuildRequires:  groff
BuildRequires:  ghostscript

%{?systemd_requires}

%description
QOTD (quote of the day) is specified in RFC 865 as a way of broadcasting a
quote to users. On both TCP and UDP, port 17 is officially reserved for
this purpose. This program is meant to provide a simple QOTD daemon on
IPv4 and IPv6 over TCP/IP.

%prep
%autosetup -n %{name}-v%{version}-%{commit0}

%build
make %{?_smp_mflags} CFLAGS="%{optflags} %{__global_ldflags}"
make -C man

%install
make install ROOT=%{buildroot}

# Build script autoinstalls qotd.pdf, so copy README there.
cp -a README.md %{buildroot}/%{_pkgdocdir}/

# Installs systemd service file.
mkdir -p %{buildroot}%{_unitdir}
cp -a misc/qotd.service %{buildroot}%{_unitdir}/

%post
%systemd_post qotd.service

%preun
%systemd_preun qotd.service

%postun
%systemd_postun_with_restart qotd.service

%files
%license LICENSE
%doc %{_pkgdocdir}/
%{_bindir}/qotdd
%{_mandir}/man5/qotd.conf.5*
%{_mandir}/man8/qotdd.8*
%{_datadir}/qotd
%{_unitdir}/qotd.service
%config(noreplace) %{_sysconfdir}/qotd.conf

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Ben Rosser <rosser.bjr@gmail.com> 0.11.3-2
- Add missing systemd scriplets, this was missed in review.

* Fri Jul 07 2017 Ben Rosser <rosser.bjr@gmail.com> 0.11.3-1
- Update to latest upstream release.
- Enable parallel build.
- Change license tag to correct GPLv2+.
- Add buildrequires on make.

* Sat Jun 17 2017 Ben Rosser <rosser.bjr@gmail.com> 0.11.0-1
- Initial package.
