%global srcname pkix

Name:       erlang-%{srcname}
Version:    1.0.4
Release:    2%{?dist}
BuildArch:  noarch

License:    ASL 2.0
Summary:    PKIX certificates management for Erlang
URL:        https://github.com/processone/pkix/
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-rebar

Requires: ca-certificates


%description
A library for managing TLS certificates in Erlang.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{rebar_compile}


%install
%{erlang_install}

# pkix includes a CA bundle in priv/cacert.pem. Let's use a symlink to Fedora's CA bundle instead.
install -d -m 0755 %{buildroot}/%{erlang_appdir}/priv
ln -s /etc/pki/tls/certs/ca-bundle.trust.crt %{buildroot}/%{erlang_appdir}/priv/cacert.pem


%check
%{rebar_eunit}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4 (#1742452).
- https://github.com/processone/pkix/compare/1.0.2...1.0.4

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (#1717537).
- https://github.com/processone/pkix/compare/1.0.1...1.0.2

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1.
- https://github.com/processone/pkix/compare/1.0.0...1.0.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.0-1
- Initial release.
