Name:           ipv6gen
Version:        1.0
Release:        8%{?dist}
Summary:        IPv6 prefix generator
License:        GPLv2
URL:            https://github.com/vladak/%{name}

Source0:        https://github.com/vladak/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators


%description
ipv6gen is a tool which generates lists of IPv6 prefixes using the
process described by RFC 3531.


%prep
%autosetup


%install
install -Dp -m 0755 check-overlap.pl $RPM_BUILD_ROOT/%{_bindir}/check-overlap
install -Dp -m 0755 ipv6gen.pl       $RPM_BUILD_ROOT/%{_bindir}/ipv6gen
install -Dp -m 0644 ipv6gen.1        $RPM_BUILD_ROOT/%{_mandir}/man1/ipv6gen.1


%files
%license LICENSE
%doc Changelog.txt
%{_bindir}/check-overlap
%{_bindir}/ipv6gen
%{_mandir}/man1/ipv6gen.1*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Garrett Holmstrom <gholms@fedoraproject.org> - 1.0-1
- Created
