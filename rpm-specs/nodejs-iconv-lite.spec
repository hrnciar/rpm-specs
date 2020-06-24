Name:           nodejs-iconv-lite
Version:        0.4.18
Release:        7%{?dist}
Summary:        Convert character encodings in pure JavaScript

License:        MIT
URL:            https://github.com/ashtuchkin/iconv-lite/archive/
Source0:        https://github.com/ashtuchkin/iconv-lite/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/ashtuchkin/iconv-lite/commit/be3c9e5728352bf8924c8d340423b99812e27472
Patch0:         nodejs-iconv-lite-node10.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(iconv)
BuildRequires:  npm(mocha)
BuildRequires:  npm(semver)
#BuildRequires:  npm(unorm)

%description
%{summary}.


%prep
%autosetup -p1 -n iconv-lite-%{version}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/iconv-lite
cp -pr package.json encodings/ lib/ \
    %{buildroot}%{nodejs_sitelib}/iconv-lite
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
# Remove tests failing due to glibc based iconv
rm test/dbcs-test.js
# Remove tests that require unorm
rm test/sbcs-test.js
mocha --reporter spec --grep .


%files
%doc README.md Changelog.md
%license LICENSE
%{nodejs_sitelib}/iconv-lite


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Tom Hughes <tom@compton.nu> - 0.4.18-1
- Update to 0.4.18 upstream release

* Fri Jun 09 2017 Troy Dawson <tdawson@redhat.com> - 0.4.17-1
- Update to 0.4.17 upstream release

* Fri Feb 17 2017 Tom Hughes <tom@compton.nu> - 0.4.15-1
- Update to 0.4.15 upstream release
- Enable as many tests as possible

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 Piotr Popieluch <piotr1212@gmail.com> - - 0.4.13-1
- Update to new version
- Cleanup specfile
- Switch Source0 to github to include test

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.11-1
- update to upstream release 0.2.11

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.10-3
- fix ExclusiveArch usage

* Wed Jul 10 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.10-2
- do not package generation/ directory

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.10-1
- initial package
