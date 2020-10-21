# Git snapshot metadata
%global snapshot 20120822
%global commit 9732348ba992348fa87aca58f99b6f07203d7d9f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# httpd configuration redefined by httpd-devel macro files
%{!?_httpd_apxs:        %{expand: %%global _httpd_apxs %{_sbindir}/apxs}}
%{!?_httpd_confdir:     %{expand: %%global _httpd_confdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_mmn:         %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}
%{!?_httpd_modconfdir:  %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:      %{expand: %%global _httpd_moddir %%{_libdir}/httpd/modules}}

Name:       mod_psgi
Version:    0.0.1
Release:    0.8.%{snapshot}git%{shortcommit}%{?dist}
Summary:    Apache httpd plugin for handling PSGI applications
License:    ASL 2.0
URL:        https://github.com/spiritloose/%{name}
Source0:    %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:    psgi.conf
Source2:    psgi.module.conf
# Do not edit perl CFLAGS,
# <https://github.com/spiritloose/mod_psgi/pull/9>
Patch0:     mod_psgi-Revert-Removed-D_FILE_OFFSET_BITS-64.patch
# Adapt tests to Perl >= 5.26,
# <https://github.com/spiritloose/mod_psgi/pull/9>
Patch1:     mod_psgi-Fix-building-with-perl-without-.-in-INC.patch
# Adapt tests to httpd 2.4,
# <https://github.com/spiritloose/mod_psgi/pull/9>
Patch2:     mod_psgi-Adjust-httpd-configuriation-to-2.4.patch
# Stabilize hash key order in tests,
# <https://github.com/spiritloose/mod_psgi/pull/9>
Patch3:     mod_psgi-test-Sort-query-fields.patch
BuildRequires:  autoconf
# automake for aclocal executed by autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::Embed)
# Tests:
BuildRequires:  httpd
# For prove tool
BuildRequires:  perl-Test-Harness
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Plack::Middleware::Lint)
BuildRequires:  perl(Plack::Test::Suite)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(warnings)
Requires:       httpd-mmn = %{_httpd_mmn}

%description
This Apache httpd plugin allows you to start Perl Web Server Gateway Interface
(PSGI) applications directly from the httpd server.

%prep
%autosetup -n %{name}-%{commit} -p 1
autoreconf -fi

%build
%configure \
    --with-apachectl='%{_sbindir}/apachectl' \
    --with-apxs='%{_httpd_apxs}' \
    --disable-debug \
    --with-perl='%{_bindir}/perl' \
    --with-prove='%{_bindir}/prove'
make %{?_smp_mflags}

%install
%make_install
install -d -m 755 $RPM_BUILD_ROOT%{_httpd_confdir}
install -d -m 755 $RPM_BUILD_ROOT%{_httpd_modconfdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_confdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_httpd_modconfdir}/03-psgi.conf

%check
make test

%files
%license LICENSE
%doc README
# Directories are owned by httpd-mmn
%config(noreplace) %{_httpd_confdir}/psgi.conf
%config(noreplace) %{_httpd_modconfdir}/03-psgi.conf
%{_httpd_moddir}/%{name}.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.8.20120822git9732348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.1-0.7.20120822git9732348
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.6.20120822git9732348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.5.20120822git9732348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.1-0.4.20120822git9732348
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.3.20120822git9732348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.2.20120822git9732348
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Nov 08 2018 Petr Pisar <ppisar@redhat.com> - 0.0.1-0.1.20120822git9732348
- 0.0.1 version packaged

