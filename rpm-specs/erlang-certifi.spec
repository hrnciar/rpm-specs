%global realname certifi
%global upstream certifi
%global upstream_reponame erlang-certifi

# Technically we're noarch, but our install path is not.
%global debug_package %{nil}

Name:     erlang-%{realname}
Version:  2.3.1
Release:  4%{?dist}
Summary:  Dummy certifi (certificate bundle) package for erlang
License:  BSD
URL:      https://github.com/%{upstream}/%{upstream_reponame}
Source0:  https://github.com/%{upstream}/%{upstream_reponame}/archive/%{version}/%{upstream_reponame}-%{version}.tar.gz
Patch0:   erlang-certifi-enforce_fedora_ca_bundle.patch
BuildRequires:  erlang-rebar sed erlang-parse_trans
Requires:       erlang-rebar

%description
Upstream certifi provides a custom CA bundle to erlang. Since custom CA bundles
cannot be packaged in Fedora, this 'dummy' package patches certifi to point to
the default Fedora CA bundle.

%prep
%setup -q -n %{upstream_reponame}-%{version}
%patch0

# Fix dependency version issue
sed -i 's/{parse_trans, "3.2.0"}/{parse_trans, "3.3.0"}/' rebar.config

%build
%{erlang_compile}

%install
%{erlang_install}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Timothée Floure <fnux@fedoraproject.org> - 2.3.1-1
- Let there be package
