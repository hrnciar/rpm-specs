%global srcname luerl


Name:       erlang-%{srcname}
Version:    0.3
Release:    5%{?dist}
BuildArch:  noarch

License:    ASL 2.0
Summary:    Lua in Erlang
URL:        https://github.com/rvirding/luerl
Source0:    %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: dos2unix
BuildRequires: erlang-rebar


%description
An experimental implementation of Lua 5.2 written solely in pure Erlang.


%prep
%autosetup -n %{srcname}-%{version}

dos2unix examples/hello/hello2-3.lua


%build
%{rebar_compile}


%check
%{rebar_eunit}


%install
%{erlang_install}


%files
%license LICENSE
%doc examples
%doc README.md
%doc src/NOTES
%{erlang_appdir}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3-1
- Update to 0.3 (#1560805).

* Sun Mar 25 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.2-6
- Convert into a noarch package.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
