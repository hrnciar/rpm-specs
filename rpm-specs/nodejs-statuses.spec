%global enable_tests 0
%global module_name statuses

Name:           nodejs-%{module_name}
Version:        1.3.1
Release:        8%{?dist}
Summary:        HTTP status utility
License:        MIT
URL:            https://github.com/jshttp/statuses
Source0:        https://github.com/jshttp/statuses/archive/v%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
#BuildRequires:  npm(csv-parse)
BuildRequires:  npm(istanbul)
BuildRequires:  npm(mocha)
BuildRequires:  npm(stream-to-array)
# not packaged
#BuildRequires:  npm(eslint)
#BuildRequires:  npm(eslint-config-standard)
#BuildRequires:  npm(eslint-plugin-promise)
#BuildRequires:  npm(eslint-plugin-standard
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json codes.json lib src scripts index.js \
                                   %{buildroot}%{nodejs_sitelib}/%{module_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha --reporter spec --check-leaks --bail test/
/usr/bin/istanbul-js cover /usr/bin/mocha --report lcovonly -- --reporter spec --check-leaks test/
/usr/bin/istanbul-js cover /usr/bin/mocha -- --reporter dot --check-leaks test/
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Parag Nemade <pnemade AT redhat DOT com> - 1.3.1-7
- Disable tests as nodejs-istanbul is retired in F31+ (rh#1736298)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.3.1-1
- Update

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.2.1-2
- runtime needs codes.json

* Mon Feb 09 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.2.1-1
- Initial packaging

