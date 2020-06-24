%global realname eunit_formatters
%global upstream seancribbs

# Technically we're noarch, but our install path is not.
%global debug_package %{nil}

Name:     erlang-%{realname}
Version:  0.5.0
Release:  4%{?dist}
Summary:  Better output format for eunit test suites
License:  ASL 2.0
URL:      https://github.com/%{upstream}/%{realname}
Source0:  https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-v%{version}.tar.gz
BuildRequires:  erlang-rebar
Requires:       erlang-rebar

%description
%{summary}.

%prep
%autosetup -n %{realname}-%{version}

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Timothée Floure <fnux@fedoraproject.org> - 0.5.0-1
- Let there be package
