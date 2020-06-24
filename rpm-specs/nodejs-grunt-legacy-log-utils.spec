%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global srcname grunt-legacy-log-utils
%global commit 94e472a37f5e129d119765685aacd94b310be998

Name:           nodejs-grunt-legacy-log-utils
Version:        2.0.1
Release:        2%{?dist}
Summary:        Static methods for the Grunt 0.4.x logger

License:        MIT
URL:            https://github.com/gruntjs/grunt-legacy-log-utils
Source0:        https://github.com/gruntjs/%{srcname}/archive/%{commit}/%{srcname}-%{version}.tar.gz


BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(grunt-contrib-nodeunit)
BuildRequires:  npm(lodash)
BuildRequires:  npm(chalk)
BuildRequires:  npm(grunt-cli)
%endif


%description
%{summary}.


%prep
%setup -q -n %{srcname}-%{commit}
%nodejs_fixdep chalk "^1.1.3"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-legacy-log-utils
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/grunt-legacy-log-utils
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/grunt nodeunit
%endif


%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE-MIT
%{nodejs_sitelib}/grunt-legacy-log-utils


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Tom Hughes <tom@compton.nu> - 2.0.1-1
- Update to 2.0.1 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.0.0-2
- Enable tests

* Mon Aug 15 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.0.0-1
- Update to 1.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Tom Hughes <tom@compton.nu> - 0.1.1-3
- Update npm(lodash) dependency

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.1.1-2
- Update npm(colors) dependency

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.1.1-1
- Initial build of 0.1.1
