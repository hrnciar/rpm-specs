Name:       js-tag-it
Version:    2.0
Release:    7%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    A jQuery UI plugin handling multi-tag fields and suggestions/autocomplete
URL:        https://github.com/aehlke/tag-it
Source0:    %{url}/archive/v%{version}.tar.gz

BuildRequires: closure-compiler
BuildRequires: web-assets-devel

Requires:      js-jquery
Requires:      web-assets-filesystem


%description
Tag-it is a simple and configurable tag editing widget with autocomplete
support.


%prep
%setup -q -n tag-it-%{version}

# We must minify the JS ourselves.
rm -f js/*.min.js


%build
closure-compiler --compilation_level=SIMPLE_OPTIMIZATIONS js/tag-it.js > js/tag-it.min.js


%install
install -d -m 0755 %{buildroot}/%{_webassetdir}
install -d -m 0755 %{buildroot}/%{_webassetdir}/tag-it
install -d -m 0755 %{buildroot}/%{_webassetdir}/tag-it/css
install -d -m 0755 %{buildroot}/%{_webassetdir}/tag-it/js

install -D -p -m 0644 css/*.css %{buildroot}/%{_webassetdir}/tag-it/css
install -D -p -m 0644 js/*.js %{buildroot}/%{_webassetdir}/tag-it/js


%files
%license LICENSE
%doc README.markdown
%doc examples.html
%{_webassetdir}/tag-it


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jan 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.0-1
- Initial release.
