%global srcname fast_tls

%global p1_utils_ver 1.0.20

Name: erlang-%{srcname}
Version: 1.1.8
Release: 1%{?dist}

License: ASL 2.0
Summary: TLS / SSL native driver for Erlang / Elixir
URL: https://github.com/processone/%{srcname}/
Source0: https://github.com/processone/%{srcname}/archive/%{version}/fast_tls-%{version}.tar.gz
# Set the default cipher list to PROFILE=SYSTEM.
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
Patch0: 0000-Use-the-system-ciphers-by-default.patch

Provides:  erlang-p1_tls = %{version}-%{release}
Obsoletes: erlang-p1_tls < 1.0.1

BuildRequires: gcc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar
BuildRequires: openssl-devel

Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
TLS / SSL native driver for Erlang / Elixir. This is used by ejabberd.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%{rebar_compile}


%check
%{rebar_eunit}


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.8-1
- Update to 1.1.8 (#1807288).
- https://github.com/processone/fast_tls/blob/1.1.8/CHANGELOG.md

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.3-1
- Update to 1.1.13 (#1789166).
- https://github.com/processone/fast_tls/blob/1.1.3/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.2-2
- Bring fast_tls back to s390x (#1772967).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2 (#1742457).
- https://github.com/processone/fast_tls/blob/1.1.2/CHANGELOG.md
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (#1713299).
- https://github.com/processone/fast_tls/blob/1.1.1/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 (#1683114).
- https://github.com/processone/fast_tls/blob/1.1.0/CHANGELOG.md

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.26-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
