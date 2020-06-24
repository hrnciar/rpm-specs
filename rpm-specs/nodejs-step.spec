Name:           nodejs-step
Version:        1.0.0
Release:        8%{?dist}
Summary:        A simple control-flow library for Node.js

License:        MIT
URL:            https://github.com/creationix/step
Source0:        http://registry.npmjs.org/step/-/step-%{version}.tgz
BuildArch:      noarch

BuildRequires:  nodejs-devel

%description
A simple control-flow library for Node.js that makes parallel
execution, serial execution, and error handling painless.


%prep
%setup -q -n package
rm -rf node_modules


%build


%check
for test in test/*Test.js
do
  %{__nodejs} ${test}
done


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/step
cp -pr package.json %{buildroot}/%{nodejs_sitelib}/step
install -p -D -m0644 lib/step.js %{buildroot}/%{nodejs_sitelib}/step/lib/step.js
%nodejs_symlink_deps


%files
%doc README.markdown
%license license.txt
%{nodejs_sitelib}/step


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan  7 2017 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul  1 2015 Tom Hughes <tom@compton.nu> - 0.0.6-2
- Add license file

* Wed Jul  1 2015 Tom Hughes <tom@compton.nu> - 0.0.6-1
- Update to 0.0.6 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.0.5-1
- Initial build of 0.0.5
