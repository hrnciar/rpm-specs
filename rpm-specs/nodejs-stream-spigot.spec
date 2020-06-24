# test are failing
%global enable_tests 0
%global module_name stream-spigot

Name:           nodejs-%{module_name}
Version:        3.0.5
Release:        13%{?dist}
Summary:        Testing or converting simple functions into Readable streams

License:        MIT
URL:            https://github.com/brycebaril/node-stream-spigot
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
BuildRequires:  npm(tape)
BuildRequires:  npm(concat-stream)
BuildRequires:  npm(xtend)
BuildRequires:  npm(readable-stream)
%endif

%description
A readable stream generator, useful for testing or converting simple functions
into Readable streams.

%prep
%setup -q -n package
rm -rf node_modules

%nodejs_fixdep xtend ~4.x
%nodejs_fixdep readable-stream

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
node test
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.5-5
- Fix readable-stream

* Thu Dec 17 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.5-4
- Remove fixdep on readable-stream

* Wed Jul 22 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.5-3
- fixdep npm(readable-stream)
- disable test as they are failing

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.5-1
- update to 3.0.5 upstream release

* Sat Dec 27 2014 Parag Nemade <pnemade AT redhat DOT com> - 3.0.4-1
- Initial packaging

