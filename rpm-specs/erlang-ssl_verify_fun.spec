%global realname ssl_verify_fun
%global upstream deadtrickster
%global upstream_reponame %{realname}.erl

Name:     erlang-%{realname}
Version:  1.1.5
Release:  3%{?dist}
Summary:  Collection of ssl verification functions for Erlang
License:  MIT
URL:      https://github.com/%{upstream}/%{upstream_reponame}
Source0:  https://github.com/%{upstream}/%{upstream_reponame}/archive/%{version}/%{upstream_reponame}-%{version}.tar.gz
# Fix the path used in `load_cert/1` during tests
Patch0:   erlang-ssl_verify_fun-fix-tests-load_cert.patch
BuildArch:      noarch
BuildRequires:  erlang-rebar
Requires:       erlang-rebar

%description
%{summary}.

%prep
%setup -q -n %{upstream_reponame}-%{version}
%patch0

%build
%{erlang_compile}

%install
%{erlang_install}

%check
%{erlang_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Timothée Floure <fnux@fedoraproject.org> - 1.1.5-1
- New upstream release
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Timothée Floure <fnux@fedoraproject.org> - 1.1.4-1
- New upstream release

* Sun Jul 15 2018 Timothée Floure <fnux@fedoraproject.org> - 1.1.3-1
- Let there be package
