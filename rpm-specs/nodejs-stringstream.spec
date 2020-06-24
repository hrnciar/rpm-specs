Name:           nodejs-stringstream
Version:        0.0.6
Release:        3%{?dist}
Summary:        Encode and decode streams into string streams

License:        MIT
URL:            https://github.com/mhart/StringStream
Source0:        https://github.com/mhart/stringstream/archive/v%{version}/stringstream-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
%{summary}.


%prep
%autosetup -n StringStream-%{version}
rm -rf node_modules


%build



%install
mkdir -p %{buildroot}%{nodejs_sitelib}/stringstream
cp -pr package.json stringstream.js %{buildroot}%{nodejs_sitelib}/stringstream
%nodejs_symlink_deps


%check
%{__nodejs} -e 'require("./")'


%files
%doc README.md example.js
%license LICENSE.txt
%{nodejs_sitelib}/stringstream


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Tom Hughes <tom@compton.nu> - 0.0.6-1
- Update to 0.0.6 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Piotr Popieluch <piotr1212@gmail.com> - 0.0.5-1
- Update to 0.0.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.0.4-1
- Initial package
