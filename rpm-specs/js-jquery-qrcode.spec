Name:       js-jquery-qrcode
Version:    1.0
Release:    6%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    A JavaScript library for standalone qrcode generation
URL:        https://github.com/jeromeetienne/jquery-qrcode
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: closure-compiler
BuildRequires: web-assets-devel

Requires:      js-jquery >= 1.9.0
Requires:      js-qrcode-generator
Requires:      web-assets-filesystem


%description
jquery.qrcode.js is jquery plugin for a pure browser qrcode generation.
It allows you to easily add qrcode to your web pages. It is standalone,
and less than 4 kB after minify+gzip. It doesn't rely on external
services which go on and off, or add latency while loading. It is based
on qrcode-generator which builds qrcodes in various language.
jquery.qrcode.js wraps that library to make it easy to include in your
website.

Note: The upstream version of this library bundles qrcode-generator into
this package, but Fedora has chosen to unbundle it. Thus, you will need
to include qrcode.js from js-qrcode-generator in a script tag before
including this script if you wish to use this library.


%prep
%autosetup -n jquery-qrcode-%{version}

# We must minify the JS ourselves.
find . -name "*.min.js" -delete

# This is a different project:
# https://github.com/kazuhikoarase/qrcode-generator
rm src/qrcode.js


%build
closure-compiler --compilation_level=SIMPLE_OPTIMIZATIONS src/jquery.qrcode.js > \
    jquery.qrcode.min.js


%install
install -d -m 0755 %{buildroot}/%{_jsdir}
install -d -m 0755 %{buildroot}/%{_jsdir}/jquery-qrcode
install -d -m 0755 %{buildroot}/%{_jsdir}/jquery-qrcode/js

install -D -p -m 0644 jquery.qrcode.min.js %{buildroot}/%{_jsdir}/jquery-qrcode/js


%files
%license MIT-LICENSE.txt
%doc README.md
%doc examples
%doc index.html
%{_jsdir}/jquery-qrcode


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 13 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0-1
- Initial release.
