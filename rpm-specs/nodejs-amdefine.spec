%{?nodejs_find_provides_and_requires}

Name:           nodejs-amdefine
Version:        0.0.4
Release:        14%{?dist}
Summary:        Provide AMD's define() API for declaring modules in the AMD format
BuildArch:      noarch

# "amdefine is released under two licenses: new BSD, and MIT. You may pick the
#  license that best suits your development needs."
License:        BSD or MIT
URL:            https://github.com/jrburke/amdefine
Source0:        http://registry.npmjs.org/amdefine/-/amdefine-%{version}.tgz

BuildRequires:  nodejs-devel

%description
A module that can be used to implement the Asynchronous Module Definition's
define() in Node. This allows you to code to the AMD API and have the module
work in node programs without requiring those other programs to use AMD.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/amdefine
cp -pr package.json amdefine.js %{buildroot}%{nodejs_sitelib}/amdefine

%files
%{nodejs_sitelib}/amdefine
%doc LICENSE README.md

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-2
- add macro to enable dependency generation on EPEL6

* Fri Jan 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- initial package generated by npm2rpm
