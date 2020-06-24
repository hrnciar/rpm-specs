%{?nodejs_find_provides_and_requires}

Name:           nodejs-opener
Version:        1.4.1
Release:        9%{?dist}
Summary:        Opens stuff, like webpages and files and executables

License:        WTFPL
URL:            https://github.com/domenic/opener
Source0:        http://registry.npmjs.org/opener/-/opener-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
Opens stuff, like webpages and files and executables, cross-platform.


%prep
%setup -q -n package

#get rid of DOS EOLs
sed -i "s|\r||g" LICENSE.txt README.md


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/opener
cp -pr package.json opener.js %{buildroot}%{nodejs_sitelib}/opener

chmod 0755 %{buildroot}%{nodejs_sitelib}/opener/opener.js

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/opener/opener.js %{buildroot}%{_bindir}/opener


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"


%files
%doc README.md
%license LICENSE.txt
%{nodejs_sitelib}/opener
%{_bindir}/opener


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 1.4.1-1
- Update to 1.4.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.0-7
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.0-6
- add macro for EPEL6 dependency generation

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.0-4
- fix EOLs on README.md also

* Fri Jan 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.0-3
- rename from opener to nodejs-opener
- add exec permission on opener (executable and lib are same file)
- remove DOS EOLs from LICENSE.txt

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.0-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.0-1
- initial package generated by npm2rpm
