%{?nodejs_find_provides_and_requires}

Name:           nodejs-slide
Version:        1.1.6
Release:        9%{?dist}
Summary:        A flow control library that fits in a slideshow
License:        ISC
URL:            https://github.com/isaacs/slide-flow-control
Source0:        https://registry.npmjs.org/slide/-/slide-%{version}.tgz
BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
Provides simple, easy callbacks for node.js.


%prep
%setup -q -n package
rm -rf node_modules


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/slide
cp -pr package.json index.js lib %{buildroot}%{nodejs_sitelib}/slide
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/slide


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Tom Hughes <tom@compton.nu> - 1.1.6-1
- Update to 1.1.6 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.5-1
- update to upstream release 1.1.5
- add ExclusiveArch logic

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-1
- new upstream release 1.1.4

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-7
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-6
- add macro for EPEL6 dependency generation

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-4
- add missing build section
- mention missing license

* Thu Apr 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-3
- missing package.json

* Thu Apr 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-2
- bring into conformance with newer library packaging standards
- guard Requires for F17 automatic dependency generation

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-1
- initial package
