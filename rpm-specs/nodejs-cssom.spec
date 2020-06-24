%{?nodejs_find_provides_and_requires}

Name:       nodejs-cssom
Version:    0.3.0
Release:    11%{?dist}
Summary:    CSS Object Model implementation and CSS parser for Node.js
License:    MIT
URL:        https://github.com/NV/CSSOM
Source0:    http://registry.npmjs.org/cssom/-/cssom-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
%{summary}.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cssom
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/cssom

%nodejs_symlink_deps


%files
%doc README.mdown MIT-LICENSE.txt
%{nodejs_sitelib}/cssom


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.0-1
- update to upstream release 0.3.0
- MIT-LICENSE.txt is now included upstream

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.5-6
- fix compatible arches for f18/el6

* Fri Jul 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.5-5
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.5-4
- rebuild for missing npm(cssom) provides on EL6

* Thu Feb 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.5-3
- add copy of MIT-LICENSE.txt from upstream that contains license text

* Mon Feb 18 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.5-2
- add comment about License availability

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.5-1
- initial package
