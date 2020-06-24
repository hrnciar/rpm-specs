Name:           nodejs-chrono
Version:        1.0.5
Release:        11%{?dist}
Summary:        Format dates in JavaScript

License:        MIT
URL:            https://github.com/kkaefer/chrono.js
Source0:        http://registry.npmjs.org/chrono/-/chrono-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(expresso)

%description
Allows formatting of time in a `strftime` style, but with syntax taken
from PHP's date function. It implements pretty much all of the tokens
from PHP's date function, except for B (Swatch internet time) and
e (Content/City timezone identifier). You can escape characters with
a `\` (remember to encode the `\` in a string as well). All other
characters will be printed as they appear in the format string.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/chrono
cp -pr package.json index.js lib %{buildroot}/%{nodejs_sitelib}/chrono
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/expresso/bin/expresso


%files
%doc LICENSE README.markdown
%{nodejs_sitelib}/chrono


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 14 2014 Tom Hughes <tom@compton.nu> - 1.0.5-1
- Update to 1.0.5 upstream release
- Update to latest nodejs packaging standards

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 1.0.4-1
- Initial build of 1.0.4
