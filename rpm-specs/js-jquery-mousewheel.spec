Name:       js-jquery-mousewheel
Version:    3.1.13
Release:    8%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    A jQuery plugin that adds cross-browser mouse wheel support
URL:        https://github.com/jquery/jquery-mousewheel
Source0:    %{url}/archive/%{version}.tar.gz

BuildRequires: uglify-js
BuildRequires: web-assets-devel

Requires:      js-jquery >= 1.2.2
Requires:      web-assets-filesystem


%description
A jQuery plugin that adds cross-browser mouse wheel support with delta
normalization.


%prep
%autosetup -n jquery-mousewheel-%{version}

# We must minify the JS ourselves.
find . -name "*.min.js" -delete

# https://github.com/jquery/jquery-mousewheel/pull/176
chmod a-x jquery.mousewheel.js


%build
uglifyjs -c -m --comments some jquery.mousewheel.js > jquery.mousewheel.min.js


%install
install -d -m 0755 %{buildroot}/%{_jsdir}

cp -a jquery.mousewheel*.js %{buildroot}/%{_jsdir}


%files
%license LICENSE.txt
%doc ChangeLog.md
%doc README.md
%{_jsdir}/jquery.mousewheel*.js


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jan 21 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.13-1
- Initial release.
