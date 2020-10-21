%global srcname jose


Name:      erlang-%{srcname}
Version:   1.10.1
Release:   4%{?dist}
BuildArch: noarch

License: MIT
Summary: JSON Object Signing and Encryption (JOSE) for Erlang and Elixir
URL:     https://github.com/potatosalad/erlang-jose
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/potatosalad/erlang-jose/pull/93
# https://github.com/potatosalad/erlang-jose/issues/87
Patch0: 0000-Add-crypto-compat-wrapper-for-OTP-23-deprecations.patch

BuildRequires: erlang-base64url
BuildRequires: erlang-proper
BuildRequires: erlang-rebar
BuildRequires: erlang-triq


%description
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%{rebar_compile}


%check
%{rebar_eunit}


%install
%{erlang_install}


%files
%license LICENSE.md
%doc ALGORITHMS.md
%doc CHANGELOG.md
%doc examples
%doc README.md
%{erlang_appdir}


%changelog
* Mon Oct 05 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.10.1-4
- Fix FTBFS (#1863505).

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1 (#1787846).
- https://github.com/potatosalad/erlang-jose/blob/1.10.1/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.8.4-7
- Rebuild for https://bugzilla.redhat.com/show_bug.cgi?id=1748545

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
