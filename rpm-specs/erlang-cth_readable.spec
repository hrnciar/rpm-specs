%global realname cth_readable
%global upstream ferd

Name:     erlang-%{realname}
Version:  1.4.4
Release:  3%{?dist}
Summary:  Common test hooks for more readable erlang logs
License:  BSD
URL:      https://github.com/%{upstream}/%{realname}
Source0:  https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  erlang-rebar
BuildRequires:  erlang-lager
Requires:       erlang-rebar

%description
%{summary}.

%prep
%autosetup -n %{realname}-%{version}
# Fails since kernel/include/logger.hrl is not shipped witch Fedora's erlang
# installation
rm test/show_logs_SUITE.erl

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Timothée Floure <fnux@fedoraproject.org> - 1.4.4-1
- Switch to noarch
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.2-1
- Let there be package
