Name:           massdns
Version:        0.3
Release:        2%{?dist}
Summary:        High-performance DNS stub resolver for bulk lookups and reconnaissance

License:        GPLv3+
URL:            https://github.com/blechschmidt/massdns
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  gcc
BuildRequires:  ldns-devel

%description
MassDNS is a simple high-performance DNS stub resolver targetting those who
seek to resolve a massive amount of domain names in the order of millions or
even billions. Without special configuration, MassDNS is capable of resolving
over 350,000 names per second using publicly available resolvers.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install PREFIX=%{buildroot}/usr/

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-1
- Update to latest upstream release 0.3

* Fri Jan 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2-1
- Initial package for Fedora
