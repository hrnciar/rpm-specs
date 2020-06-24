Name:       js-responsive-elements
Version:    1.0.2
Release:    6%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    A library that helps element to adapt and respond to the area they occupy
URL:        https://github.com/kumailht/responsive-elements
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: web-assets-devel

Requires:      js-jquery
Requires:      web-assets-filesystem


%description
Responsive elements makes it possible for any element to adapt and
respond to the area they occupy. It's a tiny javascript library that you
can drop into your projects today.


%prep
%autosetup -n responsive-elements-%{version}


%install
install -d -m 0755 %{buildroot}/%{_jsdir}
install -d -m 0755 %{buildroot}/%{_jsdir}/responsive-elements

install -D -p -m 0644 *.js %{buildroot}/%{_jsdir}/responsive-elements/


%files
%license LICENSE
%doc README.md
%{_jsdir}/responsive-elements


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 13 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.2-1
- Initial release.
