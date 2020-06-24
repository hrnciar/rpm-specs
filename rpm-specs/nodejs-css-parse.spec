%{?nodejs_find_provides_and_requires}

%global commit 212d7d4b5f049e31d30907ee73ac767329db92e1

%global enable_tests 1

Name:       nodejs-css-parse
Version:    1.7.0
Release:    12%{?dist}
Summary:    A JavaScript CSS parser for Node.js and the browser
License:    MIT
URL:        https://github.com/reworkcss/css-parse
# Use GitHub as the NPM tarball is missing test/, examples/, History.md.
Source0:    https://github.com/reworkcss/css-parse/archive/%{commit}/%{name}-%{version}.tar.gz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
%endif

%description
%{summary}.


%prep
%setup -q -n css-parse-%{commit}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/css-parse
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/css-parse

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha --require should --reporter spec --bail
%endif


%files
%doc examples/ History.md LICENSE Readme.md
%{nodejs_sitelib}/css-parse


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.7.0-2
- update URL tag

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.7.0-1
- initial package

