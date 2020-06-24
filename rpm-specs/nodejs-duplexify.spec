%global enable_tests 1
%global module_name duplexify

Name:           nodejs-%{module_name}
Version:        3.5.1
Release:        6%{?dist}
Summary:        Turn a writeable and readable stream into a single streams2 duplex stream

License:        MIT
URL:            https://github.com/mafintosh/duplexify
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tape)
BuildRequires:  npm(tap)
BuildRequires:  npm(through2)
BuildRequires:  npm(concat-stream)
BuildRequires:  npm(end-of-stream)
BuildRequires:  npm(stream-shift)
BuildRequires:  npm(readable-stream)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

%nodejs_fixdep end-of-stream ~1.x

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
tap test.js
%endif

%files
%doc README.md 
%license LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.5.1-1
- Update to 3.5.1 version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.5.0-1
- Update to 3.5.0 release

* Fri Oct 21 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.6-1
- Update to 3.4.6 release

* Thu Oct 06 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.5-2
- Add BR: npm(stream-shift) and npm(readable-stream)

* Fri Jul 15 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.5-1
- Update to 3.4.5 release

* Wed Feb 24 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.3-1
- Update to 3.4.3 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Parag Nemade <pnemade AT fedoraproject DOT org> - 3.4.2-2
- Remove fixdep npm(readable-stream)

* Fri Aug 14 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.4.2-1
- Update to 3.4.2

* Fri Aug 14 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.4.0-1
- Update to 3.4.0

* Wed Jul 22 2015 Parag Nemade <pnemade AT fedoraproject DOT org> - 3.2.0-3
- fixdep npm(readable-stream)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 22 2014 Parag Nemade <pnemade AT redhat DOT com> - 3.2.0-1
- Initial packaging

