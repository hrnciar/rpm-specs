%global upstream hexpm
%global realname hex_core

Name:     erlang-%{realname}
Version:  0.4.0
Release:  4%{?dist}
Summary:  Reference implementation of Hex specifications
License:  ASL 2.0
URL:      https://github.com/%{upstream}/%{realname}
Source0:  https://repo.hex.pm/tarballs/%{realname}-%{version}.tar
BuildArch:     noarch
BuildRequires: erlang-rebar
BuildRequires: erlang-proper
Requires:      erlang-proper

%description
%{summary}.

%prep
%setup -c -q
tar xzf contents.tar.gz # contained in source0

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Timothée Floure <fnux@fedoraproject.org> - 0.4.0-1
- Let there be package
