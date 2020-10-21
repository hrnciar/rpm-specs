%global srcname unicode_util_compat

Name:       erlang-%{srcname}
Version:    0.5.0
Release:    3%{?dist}
BuildArch:  noarch

License:    ASL 2.0
Summary:    A unicode_util compatibility library for Erlang < 20
URL:        https://github.com/benoitc/unicode_util_compat
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-rebar


%description
This allows the usage of unicode_util and string from Erlang R21 in
older erlang >= R18.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{rebar_compile}


%install
%{erlang_install}


%check
%{rebar_eunit}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.5.0-1
- Initial release.
