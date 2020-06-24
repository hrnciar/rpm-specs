%global enable_tests 1
%global module_name read-all-stream

Name:           nodejs-%{module_name}
Version:        3.1.0
Release:        9%{?dist}
Summary:        Read all stream content and pass it to callback

License:        MIT
URL:            https://github.com/floatdrop/read-all-stream
Source0:        https://github.com/floatdrop/%{module_name}/archive/v%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(readable-stream)
BuildRequires:  npm(pinkie-promise)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf node_modules

%nodejs_fixdep pinkie-promise "^2.0.0"

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
mocha
%endif

%files
%doc readme.md 
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.0-1
- Update to 3.1.0

* Fri Dec 18 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-4
- bump release for f23->f24

* Thu Nov 26 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-3
- fixdep npm(pinkie-promise)

* Fri Aug 07 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-2
- Update to 3.0.1

* Sat Jul 18 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.0-2
- Add missing BR:npm(readable-stream)

* Wed Jul 15 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0.0-1
- Update to 3.0.0

* Thu Jan 22 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-1
- Update to 1.0.1

* Sun Dec 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.1.2-2
- Add test.js from upstream and enable tests

* Thu Dec 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.1.2-1
- Initial packaging

