Name:           certwatch
Version:        1.2
Release:        5%{?dist}
Summary:        SSL/TLS certificate expiry warning generator
License:        GPLv2+
URL:            https://github.com/notroj/certwatch
Source0:        https://github.com/notroj/certwatch/archive/v%{version}.tar.gz#/certwatch-%{version}.tar.gz
BuildRequires:  gcc, openssl-devel, xmlto, autoconf, automake
BuildRequires:  perl(Test), perl(Test::Harness), perl(Test::Output), /usr/bin/openssl
Obsoletes:      crypto-utils < 2.5-7

%description
This package provides a utility for generating warnings when SSL/TLS
certificates are soon to expire. 

%package mod_ssl
Summary: SSL/TLS certificate expiry warnings for mod_ssl
Requires: crontabs, mod_ssl, certwatch = %{version}-%{release}, /usr/sbin/sendmail

%description mod_ssl
The certwatch-mod_ssl package contains a cron script which runs a
daily check for any expired or soon-to-expire certificates listed in
the mod_ssl configuration.

%prep
%setup -q
autoreconf -i

%build
%configure
%make_build

%install
%make_install
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -m 755 -p certwatch.cron $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/certwatch

%check
export TZ=UTC
make check

%files
%{_bindir}/certwatch
%license LICENSE
%{_mandir}/man1/*

%files -n certwatch-mod_ssl
%ghost %{_sysconfdir}/sysconfig/certwatch
%config(noreplace) %{_sysconfdir}/cron.daily/certwatch
%{_mandir}/man5/*

%changelog
* Tue Aug  4 2020 Joe Orton <jorton@redhat.com> - 1.2-5
- re-enable LTO (#1863318)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 1.2-3
- Disable LTO on s390x for now

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Joe Orton <jorton@redhat.com> - 1.2-1
- Initial revision

