Name:       js-jquery-datetimepicker
Version:    2.5.20
Release:    5%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    jQuery Plugin Date and Time Picker
URL:        https://github.com/xdan/datetimepicker
Source0:    %{url}/archive/%{version}/datetimepicker-%{version}.tar.gz

BuildRequires: uglify-js
BuildRequires: web-assets-devel

Requires:      js-jquery >= 1.7.2
Requires:      js-jquery-mousewheel >= 3.1.13
Requires:      js-php-date-formatter >= 1.3.4
Requires:      web-assets-filesystem


%description
A jQuery date and time picking plugin.


%prep
%setup -q -n datetimepicker-%{version}

# We must minify the JS ourselves.
rm -rf build
rm -f *.min.js


%build
uglifyjs jquery.datetimepicker.js -c -m -o jquery.datetimepicker.min.js


%install
install -d -m 0755 %{buildroot}/%{_webassetdir}
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-datetimepicker
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-datetimepicker/css
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-datetimepicker/js

install -D -p -m 0644 *.css %{buildroot}/%{_webassetdir}/jquery-datetimepicker/css
install -D -p -m 0644 *.js %{buildroot}/%{_webassetdir}/jquery-datetimepicker/js


%files
%license MIT-LICENSE.txt
%doc README.md
%{_webassetdir}/jquery-datetimepicker


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.5.20-1
- Update to 2.5.20 (#1559194).
- https://github.com/xdan/datetimepicker/compare/2.5.18...2.5.20

* Sun Feb 18 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.5.18-1
- Update to 2.5.18 (#1546511).
- https://github.com/xdan/datetimepicker/compare/2.5.17...2.5.18

* Tue Feb 06 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.5.17-1
- Update to 2.5.17 (#1504318).

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
