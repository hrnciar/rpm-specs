%global srcname base64url


Name:      erlang-%{srcname}
Version:   1.0.1
Release:   4%{?dist}
BuildArch: noarch

License: MIT
Summary: URL safe base64-compatible codec
URL: https://github.com/dvv/base64url
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-rebar


%description
Standalone URL safe base64-compatible codec.


%prep
%autosetup -n %{srcname}-%{version}


%build
%{rebar_compile}


%check
%{rebar_eunit}


%install
%{erlang_install}


%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (#1720987).
- https://github.com/dvv/base64url/compare/v1.0...1.0.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0-3
- Convert to a noarch package.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0-1
- Initial release (#1534261).
