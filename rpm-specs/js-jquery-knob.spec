Name:       js-jquery-knob
Version:    1.2.13
Release:    8%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    Nice, downward compatible, touchable, jQuery dial
URL:        http://anthonyterrien.com/knob/
Source0:    https://github.com/aterrien/jQuery-Knob/archive/%{version}.tar.gz

BuildRequires: closure-compiler
BuildRequires: web-assets-devel

Requires:      js-jquery >= 1.7.0
Requires:      web-assets-filesystem


%description
Nice, downward compatible, touchable, jQuery dial


%prep
%setup -q -n jQuery-Knob-%{version}

# We must minify the JS ourselves.
find . -name "*.min.js" -delete
# Some files have an unneeded execute bit set
find . -type f | xargs chmod a-x


%build
closure-compiler --compilation_level=SIMPLE_OPTIMIZATIONS js/jquery.knob.js > js/jquery.knob.min.js


%install
install -d -m 0755 %{buildroot}/%{_webassetdir}
install -d -m 0755 %{buildroot}/%{_webassetdir}/jQuery-Knob
install -d -m 0755 %{buildroot}/%{_webassetdir}/jQuery-Knob/js

install -D -p -m 0644 js/*.js %{buildroot}/%{_webassetdir}/jQuery-Knob/js


%files
%license LICENSE
%doc README.md
%doc excanvas.js
%doc index.html
%doc secretplan.jpg
%{_webassetdir}/jQuery-Knob


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.2.13-2
- Remove execute bit on all files, not just ones with extensions.

* Sun Jan 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.2.13-1
- Initial release.
