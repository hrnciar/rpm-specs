%global enable_tests 0
%global commit ac60cad509a124e36ea55f6a3c3720a17d82a7bc

Name:           nodejs-get
Version:        1.4.0
Release:        10%{?dist}
Summary:        A slightly higher-level HTTP client for node

License:        BSD
URL:            http://github.com/mapbox/node-get
Source0:        https://github.com/mapbox/node-get/archive/%{commit}/node-get-%{commit}.tar.gz
BuildArch:      noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
%endif

%description
%summary


%prep
%setup -q -n node-get-%{commit}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/get
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/get
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha -R spec
%endif


%files
%doc LICENSE README.md CHANGELOG.md
%{nodejs_sitelib}/get


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec  5 2014 Tom Hughes <tom@compton.nu> - 1.4.0-1
- Update to 1.4.0 upstream release
- Switch to source from github to get tests more easily

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 18 2013 Tom Hughes <tom@compton.nu> - 1.3.0-1
- Update to 1.3.0 upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun  7 2013 Tom Hughes <tom@compton.nu> - 1.2.1-3
- Replace local patch with one from upstream

* Tue Apr 30 2013 Tom Hughes <tom@compton.nu> - 1.2.1-2
- Add comments to document patches
- Increase timeout on tests

* Mon Feb 25 2013 Tom Hughes <tom@compton.nu> - 1.2.1-1
- Initial build of 1.2.1
