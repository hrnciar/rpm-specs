%{?nodejs_find_provides_and_requires}

Name:           nodejs-yamlish
Version:        0.0.5
Release:        16%{?dist}
Summary:        Parser/encoder for the yamlish format
BuildArch:      noarch

#no license file included; "MIT" indicated in package.json
License:        MIT
URL:            https://github.com/isaacs/yamlish
Source0:        https://registry.npmjs.org/yamlish/-/yamlish-%{version}.tgz

BuildRequires:  nodejs-packaging


%description
This is a module to parse the "yamlish" format used to serialize
objects in the TAP format.

It's like yaml, but just a tiny little bit smaller.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/yamlish
cp -pr package.json yamlish.js %{buildroot}%{nodejs_sitelib}/yamlish

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/yamlish
%doc README.md
%license LICENSE

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.0.5-8
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-3
- add macro to enable dependency generation on EPEL6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-1
- initial package generated by npm2rpm
