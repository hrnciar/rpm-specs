%{?nodejs_find_provides_and_requires}

Name:       nodejs-boom
Version:    2.10.1
Release:    10%{?dist}
Summary:    HTTP friendly error objects
License:    BSD

URL:        https://github.com/spumko/boom
Source0:    https://registry.npmjs.org/boom/-/boom-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
This library provides friendly JavaScript objects that represent HTTP errors.

%prep
%setup -q -n package
%nodejs_fixdep hoek 0.9
# fixdep does not work on nodejs engine
sed -i 's/"node": ">=0.10.40"/"node": ">=0.10.36"/' package.json

#fix perms
chmod 0644 README.md LICENSE images/* lib/* package.json

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/boom
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/boom

%nodejs_symlink_deps

#Yet Another Unpackaged Test Framework (lab)
#%%check
#make test

%files
%{nodejs_sitelib}/boom
%doc README.md CONTRIBUTING.md images
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 01 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.10.1-2
- Change fixdep on engine into sed

* Thu Nov 19 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.10.1-1
- Update to 2.10.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.2-2
- fix boom dep

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.2-1
- new upstream release 0.4.2

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-2
- add macro for EPEL6 dependency generation

* Mon Apr 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-1
- initial package
