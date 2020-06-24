Name:       qrcode-generator
Version:    20170724
Release:    6%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    QR code generator implementation in several languages
URL:        https://github.com/kazuhikoarase/qrcode-generator
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: closure-compiler
BuildRequires: web-assets-devel


%description
QR Code Generator implementation in ActionScript3, Java, JavaScript and
more.


%package -n js-qrcode-generator
Summary:       QR code generator implementation in JavaScript

Requires:      js-jquery
Requires:      web-assets-filesystem


%description -n js-qrcode-generator
A QR code generator implementation in JavaScript.


%prep
%autosetup -n qrcode-generator-%{version}


%install
install -d -m 0755 %{buildroot}/%{_jsdir}
install -d -m 0755 %{buildroot}/%{_jsdir}/%{name}

install -D -p -m 0644 js/qrcode.d.ts %{buildroot}/%{_jsdir}/%{name}/
install -D -p -m 0644 js/qrcode.js %{buildroot}/%{_jsdir}/%{name}/
install -D -p -m 0644 js/qrcode_SJIS.js %{buildroot}/%{_jsdir}/%{name}/
install -D -p -m 0644 js/qrcode_UTF8.js %{buildroot}/%{_jsdir}/%{name}/


%files -n js-qrcode-generator
%license LICENSE
%doc js/README.md
%doc js/sample.html
%doc js/sample.js
%{_jsdir}/%{name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20170724-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170724-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170724-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170724-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170724-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 20170724-1
- Initial release (#1422344).
