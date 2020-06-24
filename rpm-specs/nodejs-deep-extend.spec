%global enable_tests 1
%global module_name deep-extend

Name:           nodejs-%{module_name}
Version:        0.6.0
Release:        4%{?dist}
Summary:        Recursive object extending

License:        MIT
URL:            https://github.com/unclechu/node-deep-extend
Source0:        https://github.com/unclechu/node-%{module_name}/archive/v%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
%endif

%description
%{summary}.

%prep
%autosetup -n node-%{module_name}-%{version}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js lib %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
mocha
%endif

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 0.6.0-1
- Update to 0.6.0 version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.5.1-1
- Update to 0.5.1 version (#1578248)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.5.0-1
- Update to 0.5.0 version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.4.1-1
- Update to 0.4.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.3.2-1
- Initial packaging

