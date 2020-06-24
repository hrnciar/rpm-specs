Name:           nodejs-closure-compiler
Version:        0.2.10
Release:        9%{?dist}
Summary:        Bindings to Google's Closure Compiler for Node.js

License:        MIT
URL:            https://github.com/tim-smart/node-closure
Source0:        http://registry.npmjs.org/closure-compiler/-/closure-compiler-%{version}.tgz
# Use the Fedora wrapper script to invoke the compiler
Patch0:         nodejs-closure-compiler-invoke.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:       closure-compiler

BuildRequires:  nodejs-packaging
BuildRequires:  coffee-script

%description
A wrapper to the Google Closure compiler tool. It runs the jar file
in a child process and returns the results in a callback.


%prep
%setup -q -n package
%patch0 -p1
%nodejs_fixdep -r google-closure-compiler
rm -rf node_modules lib/*


%build
cake build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/closure-compiler
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/closure-compiler
%nodejs_symlink_deps


%files
%doc LICENSE.txt README.md
%{nodejs_sitelib}/closure-compiler


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 31 2015 Tom Hughes <tom@compton.nu> - 0.2.10-1
- Update to 0.2.10 upstream release

* Sat Sep 12 2015 Tom Hughes <tom@compton.nu> - 0.2.9-1
- Update to 0.2.9 upstream release

* Fri Jul 31 2015 Tom Hughes <tom@compton.nu> - 0.2.7-1
- Update to 0.2.7 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Tom Hughes <tom@compton.nu> - 0.2.6-2
- Use the Fedora wrapper script to invoke the compiler

* Wed Apr 23 2014 Tom Hughes <tom@compton.nu> - 0.2.6-1
- Update to 0.2.6 upstream release

* Tue Apr 22 2014 Tom Hughes <tom@compton.nu> - 0.2.5-1
- Initial build of 0.2.5
