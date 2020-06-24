%global srcname idna

Name:       erlang-%{srcname}
Version:    6.0.0
Release:    2%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    Erlang IDNA lib
URL:        https://github.com/benoitc/erlang-idna
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-rebar
BuildRequires: erlang-unicode_util_compat

Requires: erlang-unicode_util_compat


%description
A pure Erlang IDNA implementation that folllows RFC5891.


%prep
%setup -q -n %{name}-%{version}


%build
%{rebar_compile}


%install
%{erlang_install}


%check
%{rebar_eunit}


%files
%license LICENSE
%doc CHANGELOG
%doc README.md
%{erlang_appdir}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 6.0.0-1
- Initial release.
