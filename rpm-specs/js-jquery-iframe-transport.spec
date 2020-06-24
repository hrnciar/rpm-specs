Name:       js-jquery-iframe-transport
Version:    1.0.1
Release:    7%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    A jQuery Ajax transport plugin for iframe-based file uploads
URL:        https://github.com/cmlenz/jquery-iframe-transport
Source0:    %{url}/archive/v%{version}.tar.gz

BuildRequires: closure-compiler
BuildRequires: web-assets-devel

Requires:      js-jquery >= 1.6.0
Requires:      web-assets-filesystem


%description
jQuery Ajax transport plugin that supports file uploads through a hidden iframe.


%prep
%setup -q -n jquery-iframe-transport-%{version}


%build
closure-compiler --compilation_level=SIMPLE_OPTIMIZATIONS \
    jquery.iframe-transport.js > jquery.iframe-transport.min.js


%install
install -d -m 0755 %{buildroot}/%{_jsdir}
install -d -m 0755 %{buildroot}/%{_jsdir}/jquery-iframe-transport

install -D -p -m 0644 jquery.iframe-transport.js %{buildroot}/%{_jsdir}/jquery-iframe-transport/
install -D -p -m 0644 jquery.iframe-transport.min.js %{buildroot}/%{_jsdir}/jquery-iframe-transport/


%files
%license LICENSE
%doc README.md
%doc demo
%doc Gruntfile.js
%{_jsdir}/jquery-iframe-transport


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jan 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.1-1
- Initial release.
